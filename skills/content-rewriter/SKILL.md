---
name: content-rewriter
description: Rewrite content you are given into a proven straight-talking, insider-to-insider voice and humanise it so it reads as written by a person and not as AI, while keeping every fact exactly as supplied. Use whenever existing or drafted website content needs adjusting, rewriting, restyling, re-voicing, humanising, de-AI-ing, tightening or "making it sound like us": articles, blog posts, guides, news pieces, case studies, landing and service pages, on any subject and for any site. Use it for a single piece or a batch, and whenever a content agent passes copy through for a voice pass before publishing. This skill changes how content is written, never what it says; it does not research or write new content from a topic.
---

# Content Rewriter

You are given a piece of content. You hand back the same content, saying the same things, rewritten in the
voice and reading as written by a person who knows the subject.

The skill supplies **how it is written**. The content you were given supplies **everything that is true**.
You do not need to know the subject, the organisation or the audience beyond what the piece itself tells
you, which is what lets this work on any topic.

Read both of these before rewriting anything:

- `references/voice.md`: who is speaking, tone, rhythm, headlines, structure, calls to action and the
  banned phrases.
- `references/humaniser.md`: what makes copy read as machine-written and how to fix it.

## The rule that outranks the rest: same facts in, same facts out

The original is your only source of facts. A rewrite that reads beautifully but has gained a statistic,
sharpened a claim or lost a condition has failed, because whoever supplied the content will publish it
trusting that it still says what they wrote.

**Carry across unchanged:**
- Every figure, date, price, name, place and product detail.
- Every quotation and testimonial, word for word, with its attribution.
- Every link, with its destination. Anchor text may change; the target may not.
- The call to action: what the reader is asked to do, and the phone number, address or link for doing it.
  The sentence around it is yours to rewrite.
- Blocks of legal, disclaimer or terms wording, and technical specifications, word for word. A single
  sentence in the prose that describes a legal duty may be reworded into plain English, as long as every
  number, threshold, deadline and condition in it stays exactly as it was.
- The strength of each claim. "May reduce" stays "may reduce"; "most" does not become "all"; a condition
  ("for orders over £50") stays attached to its promise.

**Add nothing:** no new statistic, example, customer, anecdote, quotation, source, benefit or promise, and
no first-person experience the original does not contain. The voice likes a real example and a result in
numbers; if the original has none, the rewrite has none. Linking lines that carry no information of their
own ("So if your system is due a service…") are fine; that is writing, not adding.

**You are free to change:** the headline, the order, the paragraphing, the sentences, the words, the tone,
the subheadings, and the length. You may cut padding, repetition and empty sentences. If you cut anything
that carried information, list it when you hand back.

Do not use your own knowledge to correct or update the original. If something looks wrong or out of date,
keep it and flag it.

## Workflow

### 1. Read the original and take stock

Before changing a word, note:

- **Its job**: who it is for and what it wants the reader to do. Take this from the piece.
- **Its facts**: list every figure, name, quotation, link and claim. This list is what you check against
  at the end.
- **Its format**: Markdown, HTML, plain text; any shortcodes, image tags, embeds or tracking parameters.
  Format in is format out, and markup you do not understand is left exactly as it is.
- **Its spelling**: British or American. Keep whichever it uses.
- **Its key phrase**: if the title and opening are plainly built around a search phrase, keep that phrase
  in the new title and somewhere in the first hundred words. It does not have to be the first sentence;
  do not bend the opening out of shape to fit it.
- **Who is speaking**: the voice is an insider talking to their own kind. Use "we" as fellow members of
  the audience only if the original shows the organisation is made up of them. Otherwise write as an
  expert who is plainly on the reader's side.

### 2. Decide how far the voice applies

| Content | What to do |
|---|---|
| Articles, blog posts, news pieces, guides, case studies | Full rewrite in the voice |
| Landing, service, about and product pages | Voice, honesty and call-to-action rules apply; the article structure in `voice.md` §5 does not. Keep the page's sections and their order unless asked to restructure |
| Legal pages, terms, privacy and cookie policies, technical documentation, specifications | Do not apply the voice. Say so and hand back unchanged, or tidy for clarity only if asked |
| A piece that mixes the two | Rewrite the prose; leave the legal or technical blocks word for word |

If the request names a lighter touch ("just humanise it", "keep the structure", "don't change the
headline"), do exactly that much and no more.

### 3. Rewrite in the voice

Work from your list of facts, not sentence by sentence through the original. Paraphrasing each sentence in
turn keeps the original's shape, and the shape is usually the problem.

- **Lead with what the reader came for.** Find the most useful or most striking fact in the piece, often
  buried halfway down, and open on it.
- **Rebuild the order** around the voice's structure where the facts allow: the squeeze, the example, the
  obstacles and how each was solved, the result. Use only the parts the original has material for.
- **Write a headline** in one of the `voice.md` §4 shapes, using facts from the piece.
- **Short paragraphs, contractions, two to four question-then-answer beats**, a few idioms the audience
  would use.
- **Be plain about any downside the original mentions**, and do not soften it. Do not add one it does not
  mention.
- **Bold the sentences that carry the piece**, four to eight in an article.
- **Scale the voice to the length.** The counts in `voice.md` describe 450–900 word articles. In a piece
  of 300 words, one or two bold sentences and one question-then-answer beat is plenty; more reads as a tic.
- **Close and stop**: a short line to the reader, a reassurance if the original supports one, the
  original's call to action. No summary.

Expect the rewrite to be shorter than the original. Padding has gone and nothing has replaced it. Never
write to match the original's word count.

### 4. Humanise

Do the full pass in `references/humaniser.md`: find the paragraphs that say nothing specific, and either
rebuild them around a fact from elsewhere in the original or cut them; break up even rhythm; remove the
surface patterns. Where the humaniser says "take a position", take only the position the original takes,
stated more plainly. Humanising never means adding colour that is not in the source.

### 5. Check

Save the original and the rewrite as files and run the script that sits in this skill's folder:

```
python3 <this skill's folder>/scripts/content_check.py <rewrite file> --source=<original file>      # add --us for American English
```

- **BLOCKER**: a figure or quotation in the rewrite that is not in the original, or an unsupported
  superlative. Fix every one. A superlative that the original itself makes is not yours to remove: keep
  the claim and list it under flags.
- **FIX** and **AI-TELL**: deal with each, or be able to say why it stands.
- **NOTE**: guides drawn from articles in this voice, not pass marks. Page copy will not hit them.
- **Against the source**: every figure, quotation or link reported as gone must be a cut you chose. Put it
  back, or list it under LEFT OUT.

The script compares numbers, quotations and links, and it goes quiet on short pieces where its averages
mean little. It cannot see a changed meaning, a swapped name or a place that moved, so finish by reading
the original and the rewrite side by side against your fact list, looking for a claim that got stronger, a
condition that fell off, or a name that changed. Then run the checklist in `voice.md` §10.

### 6. Hand back

```
REWRITTEN COPY
[the piece, in the same format as the original]

WHAT CHANGED
- [three to six lines: new headline, what now leads, what was restructured, what kind of thing was cut]

LEFT OUT
- [anything from the original that carried information and is not in the rewrite]   (or "Nothing")

FLAGS
- [claims in the original a human may want to check or evidence; anything that looked wrong or dated;
  parts left untouched and why; what the voice wanted that the original could not supply]   (or "None")
```

If the original had a page title or meta description, rewrite those too and put them above the copy,
within 60 and 155 characters. Keep notes and markers out of the copy itself; they get published by
accident. You hand back copy. You do not publish or change a live page.

## When the original is thin

Some content has almost no facts in it: a few hundred words of general statements. Rewriting cannot add
what is not there. Rewrite it honestly, which will make it short, and say under FLAGS what it would need
(a real example, a number, a named source) to work in this voice. A short true piece is the right output;
a padded one is not.

## Working through a batch

- Each piece keeps its own facts. Never carry a figure or example from one piece into another, even when
  they are from the same site.
- Vary the results. Rotate headline shapes, openings and closers across the batch, because a set of pages
  that all open and close the same way reads as generated even when each is fine alone.
- If two pieces contradict each other on a fact, flag it on both and change neither.
