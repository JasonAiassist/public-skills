#!/usr/bin/env python3
"""Mechanical check for rewritten website copy: voice rules, AI-tell patterns, and fidelity to the source.

Usage: python3 content_check.py <rewrite.md|.html|.txt> [--source=<original file>] [--us]

  --source=FILE  compare against the original: any figure or quotation in the rewrite that is not in
                 the original is a BLOCKER (a rewrite adds no facts); figures, quotations and links
                 that were in the original but are gone are listed so the cut is a decision, not a slip.
  --us           skip the British-spelling check for copy written in American English.

It cannot judge voice or meaning: a clean report means "no mechanical faults", not "faithful and good".
Exit code 1 if any BLOCKER is found, else 0.
"""
import re
import statistics
import sys

BANNED = [
    "delve", "tapestry", "navigate the landscape", "in today's fast-paced world", "ever-evolving",
    "when it comes to", "it's important to note", "it's worth noting", "unlock", "unleash", "elevate",
    "empower", "seamless", "robust", "leverage", "game-changer", "game changer", "dive in", "embark",
    "realm", "testament to", "picture this", "picture your", "now picture", "imagine this", "here's the thing", "rest assured", "look no further",
    "in conclusion", "furthermore", "moreover", "additionally", "firstly", "secondly", "lastly",
    "the fact of the matter is",
]
SUPERLATIVES = [
    r"\bthe best\b", r"\buk'?s (top|best|leading|number one|no\.? ?1)\b", r"\bnumber one\b",
    r"(?<!uk's )(?<!uks )\bleading\b", r"\bthan anyone else\b", r"\bunbeatable\b", r"\bguarantee[ds]?\b",
]
AMERICAN = [r"\b\w+iz(e|ed|es|ing|ation)\b", r"\bcolor\b", r"\bfavor\b", r"\bcenter\b", r"\bneighbor", r"\bcheck (?=for £)"]
IZE_OK = {"size", "sized", "sizes", "sizing", "prize", "prized", "prizes", "seize", "seized", "seizes", "seizing", "citizen"}


NUMWORD = r"(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|twenty|thirty|forty|fifty|hundred|thousand|half|dozen)"
UNITS = r"(?:days?|weeks?|months?|years?|hours?|minutes?|people|customers|clients|users|members|orders|staff)"
FIG = re.compile(r"\b" + NUMWORD + r"(?:[ -]" + NUMWORD + r")*\s(?:" + UNITS + r"|per ?cent|in " + NUMWORD + r")\b|[£$€]\s?[\d,.]+\s?(?:k|m|bn|million|billion)?\b|\b\d[\d,.]*\s?(?:%|per ?cent)|\b\d[\d,.]*\+?\s" + UNITS + r"\b|\b\d+ in \d+\b|\b\d{1,2} (?:January|February|March|April|May|June|July|August|September|October|November|December)(?: \d{4})?\b|\b(?:19|20)\d{2}\b", re.I)
WORDNUM = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
           "ten": "10", "eleven": "11", "twelve": "12", "fifteen": "15", "twenty": "20", "thirty": "30", "forty": "40", "fifty": "50"}


def clean(raw):
    text = re.sub(r"<(script|style)\b.*?</\1>", " ", raw, flags=re.S | re.I)
    text = re.sub(r"</(p|h[1-6]|li|div|br)\s*>|<br\s*/?>", "\n\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\]\(https?://[^)]*\)", "]", text)
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"\*\*|__|^#+\s*|^[-*]\s+", "", text, flags=re.M)
    return text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')


def norm_fig(s):
    s = re.sub(r"per ?cent", "%", s.lower().replace("-", " "))
    s = " ".join(WORDNUM.get(w, w) for w in s.split())
    s = re.sub(r"(?<=\d)s\b|(?<=[a-z])s$", "", s)          # plurals: "4 months" == "4 month"
    return re.sub(r"[\s,]|\.$|\.0+\b", "", s)


def figures(text):
    return {norm_fig(m.group(0)): m for m in FIG.finditer(text)}


def numbers(text):
    """Every number in the text, however it is written: digits -> {'145', '18'}, small number words -> digits."""
    digits = {re.sub(r"[,\s]|\.$|\.0+$", "", n) for n in re.findall(r"\d[\d,. ]*\d|\d", text)}
    wordy = {WORDNUM[w] for w in re.findall(r"[a-z]+", text.lower()) if w in WORDNUM and w != "one"}
    return digits, wordy


def quotes(text):
    return {" ".join(q.lower().split()).strip(" .,!?") for q in re.findall(r'"([^"\n]{8,400})"', text) if len(q.split()) >= 3}


def links(raw):
    return {u.rstrip(".,)") for u in re.findall(r"https?://[^\s\"'<>)\]]+", raw)}


def strip_wrapper(raw):
    """A hand-back wraps the piece in header lines above and CHANGES/LEFT OUT/FLAGS below. Check the piece only."""
    m = re.search(r"^REWRITTEN COPY\s*$", raw, flags=re.M)
    if m:
        raw = raw[m.end():]
    return re.split(r"^(WHAT CHANGED|LEFT OUT|FLAGS|NOTES)\s*$", raw, flags=re.M)[0]


US = "--us" in sys.argv
SRC = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--source=")), None)
path = [a for a in sys.argv[1:] if not a.startswith("--")][0]
raw = strip_wrapper(open(path, encoding="utf-8").read())
bold = len(re.findall(r"\*\*[^*]+\*\*|<(strong|b)\b", raw, flags=re.I))
text = clean(raw)
low = text.lower()


paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
plen = [len(p.split()) for p in paras]
sents = [s for s in re.split(r"(?<=[.!?])\s+", " ".join(paras)) if s.strip()]
slen = [len(s.split()) for s in sents]
words = len(text.split())
count = lambda pat: len(re.findall(pat, low))

blockers, fixes, notes = [], [], []
for phrase in BANNED:
    n = low.count(phrase)
    if n:
        fixes.append(f'banned phrase "{phrase}" x{n}')
for pat in SUPERLATIVES:
    for m in re.finditer(pat, low):
        blockers.append(f'possible unsupported claim: "...{low[max(0, m.start()-30):m.end()+20].strip()}..."')
excl = text.count("!")
if excl > 1:
    fixes.append(f"{excl} exclamation marks (at most 1)")
dashes = text.count("—") + len(re.findall(r"(?<!\d)–|–(?!\d)", text))  # number ranges like 85–90% are fine
if dashes > 2:
    fixes.append(f"{dashes} em/en dashes (use sparingly)")
for pat in ([] if US else AMERICAN):
    hits = {m.group(0) for m in re.finditer(pat, low)} - IZE_OK
    if hits:
        fixes.append(f"possible American spelling: {sorted(hits)}")
if re.search(r"[\U0001F300-\U0001FAFF]|#\w+", text):
    fixes.append("emoji or hashtag present")
if count(r"it's not just|isn't just|not only") > 1:
    fixes.append('"not just X, it\'s Y" construction used more than once')

we, you = count(r"\b(we|our|us|we're|we've|we'll)\b"), count(r"\b(you|your|you're|you've|you'll)\b")
contractions = count(r"\b\w+'(re|ve|ll|d|s|t)\b")
qa = len(re.findall(r"\?\s+[A-Z]", text))
med_p = statistics.median(plen) if plen else 0
short_share = sum(1 for n in plen if n <= 25) / len(plen) if plen else 0
if med_p > 30:
    notes.append(f"median paragraph {med_p:.0f} words (this voice runs ~17)")
if we == 0 or you == 0 or max(we, you) > 3 * max(1, min(we, you)):
    notes.append(f"we/you out of balance ({we} vs {you})")
if contractions < 5 and words > 300:
    notes.append(f"only {contractions} contractions; may read stiff")
if qa == 0 and words > 300:
    notes.append("no question-then-answer beats")
if not 4 <= bold <= 8 and words > 400:
    notes.append(f"{bold} bold phrases (articles carry 4-8, on results and reassurance)")

# ---- humaniser checks: patterns that make copy read as machine-written ----
AI_WORDS = [
    "crucial", "vital", "comprehensive", "streamline", "landscape", "navigate", "navigating", "hassle-free",
    "tailored", "boasts", "plays a key role", "plays a crucial role", "stands as", "a wide range of",
    "in the world of", "let's take a look", "let's explore", "here's why", "the bottom line", "ultimately",
    "that said", "in summary", "to sum up", "overall,", "peace of mind", "stress-free", "daunting",
    "it's no secret", "at the end of the day", "now more than ever", "the good news is",
]
tells = []
for phrase in AI_WORDS:
    n = low.count(phrase)
    if n:
        tells.append(f'stock phrase "{phrase}" x{n}')
if len(slen) >= 12:
    cv = statistics.pstdev(slen) / (statistics.mean(slen) or 1)
    if cv < 0.45:
        tells.append(f"sentence lengths too even (variation {cv:.2f}; human copy here runs 0.55+): mix 4-word punches with 30-word runs")
if len(plen) >= 8:
    pcv = statistics.pstdev(plen) / (statistics.mean(plen) or 1)
    if pcv < 0.4:
        tells.append(f"paragraphs all about the same size (variation {pcv:.2f}): add one-liners, let one run long")
triplets = len(re.findall(r"\b[\w'-]+, [\w'-]+(?: [\w'-]+)?,? and [\w'-]+", low))
if triplets > max(2, words // 250):
    tells.append(f"{triplets} lists of three: break the habit, use two items or four, or name one thing")
trailing = len(re.findall(r", (ensuring|making|allowing|giving|helping|leaving|providing|offering|meaning|highlighting|reflecting|showing)\b", low))
if trailing > 2:
    tells.append(f'{trailing} sentences end on a ", ...ing" clause: split into two sentences')
openers = [s.split()[0].lower().strip("\"'(") for s in sents if s.split()]
if len(openers) >= 12:
    top = max(set(openers), key=openers.count)
    if openers.count(top) / len(openers) > 0.2 and top not in ("we", "the"):
        tells.append(f'{openers.count(top)} of {len(openers)} sentences start with "{top}"')
    this_abstract = len(re.findall(r"(?:^|[.!?]\s+)(this|these|that) (means|shows|highlights|underscores|approach|shift|change|trend)\b", low))
    if this_abstract > 2:
        tells.append(f'{this_abstract} sentences open "This means/shows/highlights...": say the thing directly')
if qa > 4:
    tells.append(f"{qa} question-then-answer beats: over 4 becomes a tic")
heads = re.findall(r"^#{2,6}\s+(.+)$", raw, flags=re.M) or re.findall(r"^#\s+(.+)$", raw, flags=re.M)[1:]
tc = [h for h in heads if len(h.split()) > 3 and sum(w[:1].isupper() for w in h.split()) / len(h.split()) > 0.8]
if tc:
    tells.append(f"{len(tc)} subheadings in Title Case: use sentence case")
if len(heads) >= 3 and all(h.strip().endswith("?") for h in heads):
    tells.append("every subheading is a question: vary them")
if re.search(r"^\s*[-*]\s+\*\*[^*\n]+(:\*\*|\*\*:)", raw, flags=re.M):
    tells.append("bullets with bold lead-ins and colons: write them as plain short items or as prose")
if re.search(r"^#{1,6}\s*(conclusion|final thoughts|summary|in summary|key takeaways|faqs?)\s*$", raw, flags=re.M | re.I):
    tells.append("has a Conclusion / Final thoughts / Key takeaways / FAQ heading: land and stop")

print(f"FILE {path}")
print(f"words {words} | paragraphs {len(paras)} (median {med_p:.0f} words, {short_share:.0%} are 25 or under)"
      f" | sentences median {statistics.median(slen) if slen else 0:.0f} words")
print(f"we/our/us {we} | you/your {you} | contractions {contractions} | question-answer beats {qa}"
      f" | bold {bold} | exclamation marks {excl} | dashes {dashes}")
figs = figures(text)
if SRC:
    sraw = open(SRC, encoding="utf-8").read()
    stext = clean(sraw)
    sfigs, squotes, slinks = figures(stext), quotes(stext), links(sraw)
    for k in figs.keys() - sfigs.keys():
        m = figs[k]
        blockers.append(f'figure not in the source: "{m.group(0)}"  ...{" ".join(text[max(0, m.start()-40):m.end()+30].split())}...')
    rd, rw = numbers(text)
    sd, sw = numbers(stext)
    known = {norm_fig(m.group(0)) for m in figs.values()}
    for n in sorted(rd - sd - sw):
        if not any(n in k for k in (figs.keys() - sfigs.keys())):
            blockers.append(f'number not in the source: "{n}"')
    for n in sorted(rw - sw - sd):
        notes.append(f'the number {n} is written as a word in the rewrite but is nowhere in the source: check it is not a new fact')
    for q in quotes(text) - squotes:
        if q not in " ".join(stext.lower().split()):
            blockers.append(f'quotation not found word for word in the source: "{q[:90]}"')
for label, items in (("BLOCKER", blockers), ("FIX", fixes), ("AI-TELL", tells), ("NOTE", notes)):
    for item in items:
        print(f"{label}: {item}")
if SRC:
    print(f"\nAGAINST THE SOURCE ({SRC}): source {len(stext.split())} words, rewrite {words} words")
    gone = [sfigs[k].group(0) for k in sfigs.keys() - figs.keys()]
    print("figures in the source that are not in the rewrite (each should be a deliberate cut, listed under LEFT OUT):")
    print("  " + (", ".join(sorted(set(gone))) if gone else "(none)"))
    gn = sorted((sd | sw) - rd - rw, key=lambda x: (len(x), x))
    print("other numbers in the source that are not in the rewrite: " + (", ".join(gn) if gn else "(none)"))
    gq = [q for q in squotes if q not in " ".join(low.split())]
    print("quotations dropped or altered: " + ("; ".join(f'"{q[:60]}..."' for q in gq) if gq else "(none)"))
    gl = sorted(slinks - links(raw))
    print("links dropped: " + (", ".join(gl) if gl else "(none)"))
else:
    print("\nFIGURES IN THE PIECE (no --source given, so check each against the original by hand):")
    for m in figs.values():
        print(f"  - {m.group(0)}  ...{' '.join(text[max(0, m.start()-50):m.end()+40].split())}...")
    if not figs:
        print("  (none found)")
sys.exit(1 if blockers else 0)
