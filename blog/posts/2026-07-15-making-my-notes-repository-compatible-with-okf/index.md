---
title: "Making my notes repository compatible with OKF"
date: 2026-07-15
description: "How I adapted my Markdown notes repository to Google's Open Knowledge Format without replacing the way it already worked."
tags: ["knowledge-management", "open-knowledge-format", "markdown", "ai-agents"]
---

In June 2026, Google proposed the [Open Knowledge Format](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing), or OKF. I had already been keeping my notes as Markdown files in Git, so the proposal caught my attention. My setup already shared many of the same parts, but it did not follow the OKF rules. I wanted to know what I would have to change.

The adaptation required less work than I expected. I kept my notes system and defined which part of the repository is portable. I also added a clear entry point, made a few file rules explicit, and taught the existing notes skill to follow them.

<!-- more -->

## What Google proposed

OKF is a small specification for packaging knowledge that humans and AI agents can both read. An OKF bundle is a directory of Markdown files. Each file describes one concept and can start with YAML frontmatter for structured fields such as `type`, `title`, `resource`, `tags`, and `timestamp`.

The path of a file identifies the concept. A file at `metrics/weekly_active_users.md`, for example, has `metrics/weekly_active_users` as its concept ID. Normal Markdown links connect one concept to another. Optional `index.md` files guide readers through the directory, while optional `log.md` files record changes.

The [OKF 0.1 specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) requires only a nonempty `type` for an ordinary concept file. A producer can choose its own types, extra metadata, directory structure, and body sections. The format does not require a server, database, software development kit, or Google service.

The limited scope is the main difference between OKF and many current knowledge bases. A wiki such as Confluence or Notion stores pages inside an application. The application controls page identity, links, search, access, and export. With OKF, files and the tools that read them handle those jobs. A concept is identified by its path, and a relationship is a normal file reference in a Markdown link.

Some tools, including Obsidian, already store Markdown files and therefore look much closer to OKF. The difference is that OKF defines a small exchange format. Two people can use different editors, search tools, or agents and still produce bundles that other tools can read. Google describes OKF as a format rather than a service, and that distinction is the reason I adopted it.

## Why OKF should help in the future

I first noticed OKF because Google introduced it, but I do not need Google to get the long term benefits. With OKF, my notes are separate from any notes application. I can replace my editor, search tool, or AI agent while keeping the same files and links.

OKF should also reduce how much unrelated text an agent reads. An agent can begin with a small topic index and open only the concepts related to its task. The agent spends fewer tokens on unrelated notes, and I can inspect the path it followed when an answer is incomplete.

People and agents can maintain the same knowledge through Git. Every change has a diff and a history. I can review an agent's edits before merging them, find when a claim changed, and restore an earlier version when an edit is wrong.

When I add a new search tool, exporter, or agent, it can rely on the small OKF contract. The tool does not need to learn every convention in my repository before it can start. It can identify concepts by path, read their types, follow their links, and ignore the private material outside the bundle.

I also get benefits if no wider OKF ecosystem appears. I must keep one concept per file, choose meaningful types, curate the indexes, and check the links. With a clear structure, I can find gaps and duplicate notes before the repository becomes harder to maintain.

## Drawing a boundary around portable knowledge

My notes repository contains more than durable knowledge. It also contains an inbox, meeting notes, reference lists, weekly summaries, scripts, agent instructions, and private memory. Making the whole repository an OKF bundle would mix knowledge with the machinery used to collect and maintain it.

I made only [`topics/`](https://github.com/cast42/notes/tree/main/topics) the OKF bundle. Everything outside that directory remains supporting material. The boundary lets me share or process the durable notes without also shipping private context or repository automation.

I added the bundle structure in the commit [Adopt OKF knowledge bundle structure](https://github.com/cast42/notes/commit/5f14a65b78ac729516342ee1c63cb9d018b17e60). The bundle now starts at `topics/index.md`. Its frontmatter contains only the format version:

```yaml
---
okf_version: "0.1"
---
```

The rest of the file is a short map of the main topics. A person or an agent can start there, choose a topic, open its own `index.md`, and then load only the concepts needed for a task. I call this progressive disclosure. It reduces how much an agent must read before it can find a useful note.

I renamed existing topic `README.md` files to `index.md` where needed and added missing topic indexes. I also added `topics/log.md` to record structural changes to the bundle. Both names are reserved by OKF, so nested index and log files do not have concept frontmatter.

## Making each concept valid

Every other Markdown file under `topics/` now needs valid YAML frontmatter and a nonempty `type`. The rule also applies to raw source captures because they live inside the bundle.

The repository already used fields such as `source_url`, `topics`, and `created_at`. I kept those fields. Rewriting every historical note would have created a large migration with little benefit. New or edited notes can add the matching OKF fields when they are useful:

| Existing field | OKF field |
| --- | --- |
| `source`, `source_url`, or `canonical_url` | `resource` |
| `topics` | `tags` |
| `date` or `created_at` | `timestamp` |
| `title` | `title` |

I also changed how the repository chooses `type`. Older notes often used the broad value `note`. The updated rules prefer a more useful type such as `article`, `book`, `paper`, `tweet`, `video`, `concept`, `investigation`, or `procedure`. OKF does not prescribe those values. They are local choices that give readers more information without creating a rigid taxonomy.

Links use ordinary relative Markdown paths. A concept links to `../knowledge_management/index.md`, for example, rather than using a wiki link or an application ID. If you clone or archive the bundle, the relationship remains in the files.

## Teaching the notes skill the new rules

I also had to update the repository's [notes skill](https://github.com/cast42/notes/tree/main/.agents/skills/cast42bot-notes). The skill helps agents capture sources, create notes, choose folders, and maintain topic indexes. If agents kept following the old instructions, new files could break the OKF rules.

In [Adapt notes skill for OKF](https://github.com/cast42/notes/commit/0eeb5bb32ff4a76fe7fc2f9ca7d25b8d0b26fc90), I changed how agents maintain the repository. An agent now starts at `topics/index.md` and reads the nearest topic index before opening many concept files. The agent classifies a file before writing it, preserves the special rules for `index.md` and `log.md`, chooses a meaningful type, and adds relative links when a relationship will help future searches.

The skill also keeps the distinction between capture and durable knowledge. New material can still start in `inbox/`. A source becomes part of the OKF bundle only after it is placed under `topics/` as a useful, self contained concept. OKF compatibility did not remove the fast capture path.

I updated the frontmatter normalizer too. It now skips the reserved index and log files, assigns more specific types from filenames and locations, and uses the current date instead of 1970 when a new file has no Git history.

## Adding checks without demanding a perfect archive

A written convention is easy to forget, so I added `scripts/validate_okf.py`. The validator checks the parts that tools must agree on:

- The bundle root declares OKF version 0.1 and no other root metadata.
- Reserved index and log files have no frontmatter.
- Every concept has valid YAML frontmatter with a nonempty `type`.
- Relative Markdown links point to files that exist.

Invalid structure or metadata fails validation. Broken links are warnings for now. The repository contains years of notes, and repairing every old link was not required to adopt the format. New work should not add warnings, while older links can be repaired over time.

GitHub Actions runs the same validator when a pull request or a push changes the bundle. The local command and the automated check enforce the same contract.

## What changed in practice

The final change was small because the repository already used Markdown, YAML frontmatter, Git, topic folders, and links. The work was mostly about turning habits into a clear contract:

- `topics/` became the portable OKF bundle.
- `topics/index.md` became its versioned entry point.
- Topic maps now use reserved `index.md` files.
- Concept files require a meaningful `type`.
- Existing metadata stays valid, with optional OKF aliases.
- Relative Markdown links form the knowledge graph.
- The notes skill maintains the rules during future work.
- A validator and GitHub Actions check catch structural errors.

The first benefit is portability. I can give the `topics/` directory to another agent or tool without explaining the entire repository. The second benefit is discipline. The same rules that make the notes portable also make them easier to navigate, validate, and maintain.

Google's proposal gave me a small shared contract for the files I already had. I can now use the repository outside the tools that created it, without moving the notes into a new application.
