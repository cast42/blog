---
title: "Updating my cognitive patterns with clearer evidence checks"
date:
  created: 2026-09-07
  updated: 2026-09-07
description: "How public sources informed three new reasoning procedures, refinements to existing patterns, and more careful guidance for human and AI collaboration."
tags: ["human-ai-collaboration", "cognitive-patterns", "reasoning", "evidence", "knowledge-management"]
---

# Updating my cognitive patterns with clearer evidence checks

In July, I [introduced the cognitive patterns in my notes repository](../2026-07-20-documenting-cognitive-patterns-for-human-ai-collaboration/index.md). Each pattern describes a reusable reasoning procedure, including when to use it, how to apply it, and where it can fail.

The collection now has 18 patterns. This update adds three patterns and makes focused changes to five existing ones. The new patterns cover evidence quality, decisions under uncertain future conditions, and causal claims. I also clarified when an AI should contribute during shared work.

The revisions make several checks explicit that were previously implicit. The checks do not show that an AI using the patterns produces more accurate answers.

<!-- more -->

## The foundations remain useful

[Sanjoy Mahajan's *The Art of Insight in Science and Engineering*](https://ocw.mit.edu/courses/res-6-011-the-art-of-insight-in-science-and-engineering-mastering-complexity-fall-2014/) remains an important source. Mahajan's methods informed the patterns for decomposition, approximation, and verification through independent routes. I kept those procedures and connected independent verification to a more explicit way to investigate disagreement.

The other foundation is [Claude Code Thinking Skills](https://github.com/tjboudreaux/cc-thinking-skills). Its [version 1.0 release](https://github.com/tjboudreaux/cc-thinking-skills/releases/tag/v1.0.0) reduced the catalog from the 39 skills in my earlier snapshot to 28, partly by combining overlapping procedures. My [version 1 review](https://github.com/cast42/notes/blob/main/topics/cognitive_patterns/2026-09-07_investigation_cc-thinking-skills-v1-review.md) had already updated seven local patterns before this broader source review began.

The review produced two useful refinements. First, routine work may need no pattern. Second, conflicting results need a resolution plan before they are combined. An upstream packaging change does not require the same merger in my notes. Explaining feedback loops and selecting an intervention remain separate tasks even when another collection packages them together.

The upstream evaluation also calls for restraint. Under its version 1 policy, no skill qualifies for automatic invocation. Its reported experiments do not establish an accuracy gain for my local adaptations.

## Three questions needed their own procedures

The three additions answer different questions.

| Question | New pattern | Intended output |
| --- | --- | --- |
| What can the available evidence support? | [Check evidence quality](https://github.com/cast42/notes/blob/main/topics/cognitive_patterns/check_evidence_quality.md) | A claim with a defensible scope and named limitations. |
| Which option remains useful if external conditions change? | [Test a plan across plausible futures](https://github.com/cast42/notes/blob/main/topics/cognitive_patterns/test_a_plan_across_plausible_futures.md) | A comparison of options and conditions for adapting them. |
| Can an observed difference be attributed to an intervention? | [Examine a causal claim](https://github.com/cast42/notes/blob/main/topics/cognitive_patterns/examine_a_causal_claim.md) | A defined comparison and an assessment of its assumptions. |

[The CIA's *Tradecraft Primer*](https://www.cia.gov/resources/csi/static/Tradecraft-Primer-apr09.pdf) informed the evidence checks. The relevant sections concern information quality and key assumptions. I adapted them into a procedure for tracing important claims to their observations and preserving the limits of the evidence. Several articles that repeat one report do not provide several independent observations.

The UK Government Office for Science's [*Futures Toolkit*](https://www.gov.uk/government/publications/futures-toolkit-for-policy-makers-and-analysts/the-futures-toolkit-html) informed the scenario pattern. Comparing every option across the same external conditions can show when a plan needs to change. A scenario is not a forecast, and a table with four scenarios does not imply four equally likely futures.

[Miguel Hernan and James Robins' *Causal Inference: What If*](https://miguelhernan.org/whatifbook) informed the causal review. I used the August 19, 2026 revision. The local procedure asks for a defined intervention and an alternative, then examines whether the available data support that comparison. It is a screening method. It does not replace the book's statistical methods or a suitable study design.

## An example of the difference

Consider a hypothetical report claiming that new route software reduced energy use by 12 percent. Depots volunteered to adopt the software, and their routes and the season changed during the same period. The report contains no comparable measurements from non-adopters.

The existing hypothesis pattern can compare explanations such as software effects and seasonal changes. The causal pattern adds a required step: define the intervention and the alternative before interpreting the percentage as an effect.

| Part of the review | What the revised guidance requires |
| --- | --- |
| Define the question. | Specify the eligible depots, software intervention, alternative routing method, and common measurement period. |
| Inspect the comparison. | Examine volunteer selection and concurrent changes before attributing the decline to software. |
| State what is supported. | Report the observed decline while withholding a causal percentage until a defensible comparison is available. |

A careful analyst can reach the same conclusion without a named pattern. The purpose of the new pattern is to make the comparison explicit and reusable. The example does not show that the pattern improves accuracy.

## Existing patterns needed smaller changes

[NIST's experimental-design guidance](https://www.itl.nist.gov/div898/handbook/pri/section3/pri3.htm) informed a separate experiment branch within hypothesis testing. Inspecting a record may be enough for diagnosis. When an experiment is needed, define the comparison and outcome before running it, and account for randomization and changing conditions.

[Duncan Sabien's explanation of Double Crux](https://www.lesswrong.com/posts/exa5kmvopeRyfJgCy/double-crux-a-strategy-for-mutual-understanding) suggested a more precise way to investigate disagreement. First, record the separate estimates. Then identify a disputed assumption whose resolution would change the recommendation. Investigate a factual disagreement about expected demand separately from a preference for spare capacity. Agreement after discussion is not new independent evidence.

[Donella Meadows' *Leverage Points*](https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/) helped clarify the intervention pattern. I made the local grouping explicit and added the missing feedback category. Meadows' hierarchy also needs a caution about generalization. A small adjustment near a threshold may be more useful than a goal change that nobody can implement.

## What the writing-assistant paper contributed

[Chao Zhang, Abe Davis, Chih-Wei Chen, and Chin-Chia Hsu](https://arxiv.org/html/2609.01588v1) studied writing assistants in *Designing Proactive Thought Partners for Writing*. Sixteen participants used the research system during one week of writing. They could configure the partner's role, the events that prompted a relevance check, and the context in which support would be useful.

The paper distinguishes an opportunity to intervene from a reason to intervene. I used that distinction in the selection guidance. An assistant should connect its contribution to a current need, such as an unsupported claim. Optional ideas should be easy to ignore. Already authorized work should proceed without another approval loop.

Applying that distinction beyond writing is my local adaptation. The study explored how people configured and experienced the system. The authors explicitly state that it does not establish causal effects on writing quality, productivity, learning, or long-term agency. I added guidance for collaboration. I did not add background monitoring.

## What I checked

I recorded five synthetic cases before editing the patterns. I then compared the current and revised guidance against the same facts. The cases included a routine correction where no pattern should be used. A later library example checked whether the guidance transferred beyond its worked examples.

The review found a stopping-rule inconsistency in the existing hypothesis pattern. The output allowed uncertainty, but the stopping step required one supported explanation. The revision now allows the analyst to stop with unresolved alternatives when further discrimination is unavailable at a justified cost.

Several direct answers already reached the same conclusions as the revised guidance. The same agent that wrote the changes also performed the review and had read the sources. The review was an editorial check. It was not a controlled model experiment and did not measure the verification effort required from a human.

All 18 patterns remain experimental. The [source review and worked checks](https://github.com/cast42/notes/blob/main/topics/cognitive_patterns/2026-09-07_investigation_public-source-pattern-update.md) record the changes and their limits. The [evaluation procedure](https://github.com/cast42/notes/blob/main/topics/cognitive_patterns/evaluate_pattern_changes.md) describes what a later outcome comparison would require. The [pattern index](https://github.com/cast42/notes/blob/main/topics/cognitive_patterns/index.md) is the starting point for using the collection.
