---
title: "Documenting cognitive patterns for better human and AI collaboration"
date: 2026-07-20
description: "How reusable reasoning procedures help humans and AI inspect their work, and how two external sources improved the procedures in my notes repository."
tags: ["human-ai-collaboration", "cognitive-patterns", "reasoning", "knowledge-management"]
---

# Documenting cognitive patterns for better human and AI collaboration

My notes repository stores sources, concepts, and investigations. Sources preserve what another author said. Concepts combine knowledge about one idea. Investigations record how I examined a specific question. I recently added a fourth kind of note that records how to reason about many different questions.

I call these notes cognitive patterns. A cognitive pattern is a reusable reasoning procedure. It contains questions, steps, failure modes, checks, and an example of how the same procedure can work in another field.

The goal is to make the reasoning between a question and an answer easier for a human and an AI to inspect together. A pattern can help them choose a suitable procedure, notice missing checks, and improve the procedure after using it. It does not make the answer true. Evidence still has to support every claim.

<!-- more -->

## Why document a way of thinking

Knowledge notes tell an AI what information is available, but they do not always tell it how to examine a new problem. A source may describe a failed project. A concept may explain feedback loops. Neither note tells the AI when to run a pre-mortem, how to compare several explanations, or how to check whether two estimates are independent.

A documented cognitive pattern fills that gap. It turns a useful reasoning habit into a procedure that a person or an AI can find and apply again. The procedure is also open to review. A reader can see which steps were followed, which assumptions were made, and where the procedure could fail.

Documentation also gives human and AI collaborators a shared vocabulary. A person can ask an AI to test competing hypotheses instead of asking it to "think harder." The AI can name the pattern it used and show the observations that separate one explanation from another. The person can then challenge a specific step instead of reviewing an unexplained answer from the beginning.

The repository keeps patterns separate from evidence for an important reason. A well written checklist can make an argument look orderly even when its facts are weak. Patterns guide the process. Sources, measurements, tests, and direct observations support the conclusion.

## How the patterns are used

The [cognitive pattern index](https://github.com/cast42/notes/blob/main/topics/cognitive_patterns/index.md) organizes patterns by the kind of reasoning they support. A human or an AI first retrieves the relevant knowledge and evidence. It then names the problem and chooses the smallest useful set of patterns.

Each selected pattern must have a separate job. One pattern may divide a large question into smaller parts. Another may test the proposed answer in an easy case. Adding more patterns without a clear job only creates a longer checklist.

After applying a pattern, the human and AI check its failure modes and evaluation criteria. They record whether it helped, where it failed, and what limited its use. A pattern should change through repeated use. It can gain a missing check, become narrower, or be removed when it adds effort without improving the work.

## What Claude Code Thinking Skills added

The [Claude Code Thinking Skills](https://github.com/tjboudreaux/cc-thinking-skills) repository packages 39 reasoning frameworks as skills. The collection covers decisions, uncertainty, diagnosis, systems, risk, and strategy. Its patterns usually explain when to use a procedure, when to skip it, which steps to follow, what mistakes to avoid, and how to inspect the output.

I did not copy the collection into my notes. Many skills overlap with patterns that were already present, and some are tied to specific coding tasks. Instead, I used the collection to find gaps and improve the local pattern structure. The [source note about the review](https://github.com/cast42/notes/blob/main/topics/cognitive_patterns/2026-07-20_github_tjboudreaux_cc-thinking-skills.md) records the choices in detail.

The review led to five additions:

- **Select cognitive patterns** starts from the problem and chooses the smallest set that covers it.
- **Combine cognitive patterns** gives every pattern a distinct role and explains how to handle conflicting results.
- **Update beliefs with evidence** begins with a prior belief, compares explanations, and changes confidence when new evidence arrives.
- **Run a pre-mortem** assumes that a plan failed, finds plausible causes, and turns them into changes and checkpoints.
- **Test competing hypotheses** states several explanations that can be disproved and looks for an observation that separates them.

The review also changed how patterns are evaluated. The Claude Code Thinking Skills project reports that none of its skills has yet shown a reliable and repeated improvement in accuracy. One scientific method skill produced promising results, but the main test did not meet the project's stated threshold.

The honest lesson is useful. A reasoning framework can improve the structure of an analysis without improving its conclusion. My notes therefore treat patterns as procedures to test, not as proof that an AI answer is better. Claims about accuracy require comparisons with direct reasoning, suitable tasks, and repeated results.

## What The Art of Insight added

Sanjoy Mahajan's [*The Art of Insight in Science and Engineering*](https://github.com/cast42/notes/blob/main/topics/cognitive_patterns/2014-01-01_book_sanjoy-mahajan_the-art-of-insight-in-science-and-engineering.md) approaches difficult problems by organizing complexity or carefully removing it. The book informed three more patterns and strengthened the rules for combining patterns.

The first addition is **decompose and abstract**. Decomposition divides a difficult question into smaller parts that are easier to understand or estimate. Abstraction then asks which operation made the solution work and whether the same operation transfers to another field. A useful pattern should capture that reusable operation instead of preserving every detail of the first example.

The second addition is **approximate and check easy cases**. An approximation should state what it keeps, what it discards, why the discarded detail is probably secondary, and when the omission could change the conclusion. The answer is then checked in simple cases such as zero, one, a boundary, or an extreme value. A polished calculation that fails an obvious case is still wrong.

The third addition is **verify with independent estimates**. Repeating the same prompt or calculation is weak verification because both attempts can make the same mistake. Stronger verification uses different evidence, assumptions, or representations. Agreement between different routes gives more useful support. Disagreement shows where the human and AI should investigate.

Mahajan's idea of independent routes also changes the interaction between a human and an AI. On a suitable task, the human can record a rough expectation before seeing the AI answer. The AI can then use a different method. They compare the results and explain any difference before accepting either answer. The process preserves the human's independent knowledge and reduces the risk that the first answer anchors both participants.

## What improved in the complete set

The first set of patterns was strongest on systems, incentives, feedback, and capability. The two reviews added procedures for choosing a pattern, handling uncertainty, checking plans before execution, testing explanations, simplifying difficult questions, and verifying answers through independent routes.

The complete workflow is now clearer:

1. Retrieve the relevant sources and concepts.
2. Name the kind of problem.
3. Choose the smallest useful set of patterns.
4. Give each pattern a distinct job.
5. Apply the procedures to the evidence.
6. Check easy cases, failure modes, and independent routes where they help.
7. State which patterns were used and what they added.
8. Revise or remove patterns when repeated use shows that they do not help.

The repository now documents both knowledge and reusable reasoning procedures. The separation lets a human and an AI inspect their work at two levels. They can ask whether the evidence supports the answer, and they can ask whether the chosen procedure was suitable and followed well.

Cognitive patterns do not remove judgment, uncertainty, or error. They make parts of the reasoning visible enough to discuss, test, and improve. That is their main contribution to human and AI collaboration.
