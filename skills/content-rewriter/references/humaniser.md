# Humaniser: making copy read as written by a person

Read this before the humanise pass on every piece.

## What actually makes copy read as machine-written

Readers do not spot AI by individual words. They spot it by **sameness and emptiness**: every paragraph the
same size, every point balanced, nothing said that could not have been said about any organisation in any
year. Swapping "leverage" for "use" does not fix that. Two things do:

1. **Specifics.** A place, a number, a date, a named source, a detail of how something actually went. A
   sentence that could appear unchanged on a competitor's site is the tell.
2. **A point of view.** The writer in this voice is on the reader's side and says what they think.
   Neutral, both-sides, "it depends on your circumstances" copy reads as generated.

So the humanise pass is mostly rewriting the emptiest paragraphs from scratch, and only then cleaning up
surface patterns. No pass can promise a piece will get past AI-detection software; those tools are
unreliable in both directions. The aim is copy a reader takes as written by someone who knows the subject.

## Honest, not disguised

Humanising never means faking. Do not invent a personal anecdote, a customer, a conversation, a quote or a
"last week one of our team…" story to add colour. Do not add deliberate typos or errors. If a paragraph is
empty and there is no real specific to put in it, cut it.

## The pass, in order

1. **Mark the empty paragraphs.** For each one ask: what in here is specific to this topic, this month,
   this organisation? If the answer is nothing, mark it.
2. **Rewrite the marked paragraphs from a blank line**, starting from a fact in the source content.
   Do not edit the old wording; it drags its shape with it. If there is no fact to build on, delete the
   paragraph.
3. **Take a position** wherever the draft sits on the fence. Say what the reader should make of it, not
   that "opinions differ". Statements of law, safety, health or money are the exception: keep any hedge
   that is true.
4. **Break the rhythm.** Put a four-word sentence next to a thirty-word one. Let one paragraph be a single
   line and another run to four sentences. Start the odd sentence with And or But.
5. **Sweep the patterns below.**
6. **Run `scripts/content_check.py`** and deal with every AI-TELL line. Then read the piece once more
   straight through, as a busy reader on a phone would.

## Patterns to remove

### Structure
- Introduction, three matching sections, conclusion. Real articles are lopsided: the interesting part gets
  the room.
- A closing summary, "Final thoughts", "Key takeaways", or an FAQ bolted on the end. Land and stop.
- Every subheading in the same form (all questions, all "The X of Y", all Title Case).
- An opening that restates the headline or announces what the article will cover.
- Signposting: "Let's take a look", "Here's why", "In this article", "Read on to find out".

### Sentences
- **Lists of three**, especially adjectives ("fast, simple and stress-free"). Use one strong word, or two,
  or a real list of four.
- **"It's not just X, it's Y"** and its cousins ("more than just", "not only… but also"). Once at most.
- **The trailing "-ing" clause**: "…, ensuring a smooth process", "…, giving you peace of mind". Stop the
  sentence, or state the result as a fact with a number.
- **The colon reveal** and the staged question ("The result? …", "The best part? …"). This voice does use
  question-then-answer, two to four times an article. More than that is a tic.
- **Balanced hedges**: "While X, it's also true that Y." Pick the one that matters.
- **Stacked hedging**: "may potentially", "can often help to". Say it or do not.
- Sentences opening "This means…", "This shows…", "This highlights…". Name the thing and say what it does.
- Em dashes used as the default pause. Use a full stop or a comma.
- Every sentence between 15 and 25 words.

### Words
The banned list in `voice.md` §9, plus: crucial, vital, comprehensive, streamline, landscape, navigate,
tailored, boasts, hassle-free, stress-free, peace of mind, daunting, plays a key role, a wide range of,
ultimately, that said, overall, the good news is, it's no secret, now more than ever, at the end of the
day. Most of these are padding around a missing fact. When you remove one, check whether the whole
sentence should go with it.

### Formatting
- Bullets with a bold lead-in and a colon. Write short plain items, or prose.
- Bold scattered on keywords. Bold only the sentences that carry the piece.
- Title Case subheadings; emoji; more than one exclamation mark.
- Bullets where the points depend on each other. Reasoning belongs in sentences.

## What a human writer does that a draft often lacks

- States the uncomfortable thing plainly, including the downside of their own offer.
- Names the source and the date, with the link.
- Uses a figure of speech the audience would use, once, where it fits.
- Leaves things out. Not every objection needs answering in every piece.
- Lets irritation show, at a decision or a practice, never at a person.
- Ends when the point is made.

## Before and after

The details below are made up to show the shape. In real copy they come from the content you were given.

**Before** (empty, even, balanced):

> Choosing the right accounting software can be a daunting process for many small businesses. With
> changing regulations and rising costs, it's more important than ever to understand your options. Whether
> you're a sole trader or a growing team, the right solution can ensure a smooth, fast and stress-free
> year end.

Nothing in that paragraph is specific. It holds a list of three, a "whether you're X or Y" and a trailing
promise, and it could sit on any vendor's site. It cannot be fixed by swapping words.

**After** (rewritten from facts found further down the same original):

> The filing deadline is 31 January. Most of us start thinking about it on the 20th.
>
> So here's the question we get every December: is it too late to switch?
>
> It isn't. Moving a year of records over takes about two days, and you can keep the old system running
> until you're sure.

Same job, but it opens on a date, takes a position, varies its sentence lengths and makes one promise it
can keep.
