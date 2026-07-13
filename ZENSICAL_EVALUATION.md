# Zensical evaluation

Date: 2026-07-13

Tested version: Zensical 0.0.50

Decision: **Keep MkDocs for now. Revisit when Zensical's blog and RSS compatibility are complete.**

## What matters for this blog

The goal is not maximum build speed or a newer stack. The goal is a static blog that remains simple, maintainable, and low-effort:

- Markdown posts automatically appear on the home page and in the archive.
- Existing dated URLs remain stable.
- Tags, search, RSS, images, and Giscus comments continue to work.
- A push to `main` reliably publishes to GitHub Pages.
- Adding a post should remain the only routine operation.

## Current MkDocs setup

The current stack uses:

- Material for MkDocs' `blog`, `search`, and `tags` plugins;
- `mkdocs-rss-plugin`;
- `mkdocs-glightbox`;
- a small Giscus template override; and
- `mkdocs gh-deploy` in GitHub Actions.

This is several packages, but it is already configured, understood, and working. Its operational cost is currently close to zero.

## Compatibility test

I ran the unmodified site configuration with:

```console
uvx zensical build --clean
```

The first build stopped in `overrides/partials/comments.html`. The template checks `page.file.src_uri`, which is available in the existing MkDocs rendering context but was undefined in Zensical.

I then temporarily disabled the custom template directory to test the rest of the build. Zensical reported a successful build, but the result was not an equivalent blog:

| Requirement | MkDocs output | Zensical 0.0.50 test |
| --- | --- | --- |
| Blog home page | Post summaries, newest first | No generated post listing |
| Stable post URL | `/2026/07/13/<slug>/` | Changed to the source path under `/posts/` |
| RSS | `feed_rss_updated.xml` generated | No RSS file generated |
| Tags | Generated tag listings | Existing tags page rendered without post listings |
| Giscus override | Works | Build failure without migration |
| GitHub Pages | Existing `mkdocs gh-deploy` workflow | Requires a different Pages artifact workflow |

The Zensical build was fast, but it did less work. Its timing is therefore not a meaningful comparison.

## What the upstream project says

Zensical is intentionally compatible with Material for MkDocs and can read an existing `mkdocs.yml`. That makes it a promising future replacement. However, compatibility is being delivered in phases and third-party MkDocs plugins do not run directly in Zensical's new module system.

At the time of this evaluation:

- Blog compatibility is listed in Tier 2 of the [plugin support backlog](https://zensical.org/compatibility/plugins/).
- RSS compatibility is also listed in Tier 2.
- Zensical is still on a `0.0.x` release and its API is changing, although the team aims to keep user-facing configuration stable ([FAQ](https://zensical.org/docs/community/faqs/)).
- `gh-deploy` is intentionally not implemented. Zensical recommends a GitHub Pages artifact workflow instead ([publishing guide](https://zensical.org/docs/publish-your-site/)).

## Assessment

Zensical is interesting technically. It combines the generator and Material theme, has an actively designed module system, retains much of the familiar configuration, and may eventually remove several separately maintained dependencies.

It is not an interesting migration for this blog today. The missing behavior is the blog's core behavior, not an optional edge case. Reimplementing the home page, dated routes, tags, and RSS locally would increase maintenance and defeat the reason for migrating. It would also introduce URL migration and SEO risk for no user-visible benefit.

The current MkDocs installation should therefore remain in place. A working, boring system is the lower-energy choice.

## When to revisit

Re-evaluate Zensical only after all of these are true:

1. The official compatibility documentation marks both blog and RSS support as shipped.
2. The existing `mkdocs.yml` produces the same post index, dated URLs, tags, and RSS feed without custom replacement code.
3. The Giscus override either works unchanged or needs only a documented, small template adjustment.
4. The supported GitHub Pages workflow has demonstrated stable releases for a few months.
5. A migration can reduce the dependency list rather than replacing dependencies with local maintenance.

At that point, repeat the build comparison, crawl both generated sites, compare URLs, and deploy a preview before changing `main`.
