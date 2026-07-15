---
title: "Two Small Measures to Reduce Python Supply-Chain Risk"
date: 2026-07-13
description: "Adding a seven-day dependency cooldown and a pre-commit vulnerability audit to Python Minimal Boilerplate."
tags: ["python", "security", "supply-chain", "uv", "pre-commit", "boilerplate"]
---

A dependency is code that I allow to run on my machine and, eventually, in production. That makes every package installation a supply-chain decision. I recently added two small, complementary safeguards to [Python Minimal Boilerplate](https://github.com/cast42/python-minimal-boilerplate): delay the adoption of newly published packages and audit the locked dependency set before every commit.

<!-- more -->

Neither measure proves that a package is safe. Together, however, they reduce the chance that a freshly published malicious package—or a dependency with a known vulnerability—silently enters a project.

## Give new releases a seven-day cooldown

The first change is one setting in `pyproject.toml`:

```toml
[tool.uv]
exclude-newer = "7 days"
```

When uv performs a new resolution, it now ignores package artifacts uploaded during the previous seven days. In effect, the resolver sees the package index as it looked one week ago.

That delay creates a useful observation window. Automated scanners, maintainers, and the wider Python community have time to identify suspicious releases, report them, and have them removed or quarantined before my resolver considers them. This is particularly valuable against short-lived attacks that depend on developers installing a malicious release immediately after publication.

The trade-off is deliberate: I receive dependency updates at least seven days later. For a minimal project template, I prefer that small loss of freshness over being among the first users of every new release.

uv calls this a [dependency cooldown](https://docs.astral.sh/uv/concepts/resolution/#dependency-cooldowns). The cutoff is based on the upload time of each distribution artifact. When uv resolves a lockfile, it records the calculated timestamp in that lockfile, preserving reproducibility.

## Audit dependencies before every commit

The second change adds `uv audit` as a local pre-commit hook:

```yaml
- repo: local
  hooks:
    - id: uv-audit
      name: uv audit
      entry: uv audit --locked
      language: system
      pass_filenames: false
```

`uv audit` checks the project's dependencies for known vulnerabilities and adverse package statuses such as deprecation or quarantine. The `--locked` option also asserts that the existing `uv.lock` remains unchanged during the check.

To run `uv audit` in CI, add [`https://api.osv.dev`](https://api.osv.dev/) to the network allowlist.

Because the command runs through pre-commit, a failed audit stops the commit. This moves the check into the normal development loop: there is no separate security command to remember and a known issue is caught before the change reaches the repository.

`uv audit` is still a relatively new and evolving part of uv. I am comfortable adopting it now based on Astral's track record with uv and Ruff, and I expect integrated auditing to become a standard check in Python projects. Its current behavior and options are documented in the [`uv audit` command reference](https://docs.astral.sh/uv/reference/cli/#uv-audit).

## Alternatives

The word "trusted" needs some care in this comparison. [You shouldn't trust Trusted Publishing](https://blog.yossarian.net/2026/07/07/You-shouldnt-trust-trusted-publishing) explains that PyPI Trusted Publishing is an authentication method between a machine identity, such as a CI workflow, and a package on PyPI. It confirms that the upload was authorized for that package name. It does not confirm that the code is safe, well maintained, or free of malware. A malicious package can still be uploaded through Trusted Publishing.

The same limit applies to every audit tool. An audit compares package names and versions with known vulnerability reports. A clean result only means that the service returned no matching report. It does not prove that the package is trustworthy or that nobody has compromised it.

The vulnerability records in the PyPI JSON API are separate from the metadata supplied by a package publisher. The [PyPI JSON API documentation](https://docs.pypi.org/api/json/#known-vulnerabilities) identifies the source of each vulnerability record, and the [Python Packaging Advisory Database](https://github.com/pypa/advisory-database) publishes its data through both PyPI and OSV. The argument about Trusted Publishing therefore does not make PyPI vulnerability records less accurate by itself. It warns against treating an authenticated upload as a safety endorsement.

The distinction affects my choice as follows:

- I still prefer `uv audit`. It works directly with `uv.lock`, batches lookups through OSV, and supports a custom OSV compatible service through `--service-url`. Using OSV avoids making PyPI the delivery path for the audit data, but it does not turn a clean audit into proof that a package is safe.
- [`uv-secure`](https://github.com/owenlamont/uv-secure) parses `uv.lock` and queries the PyPI JSON API for every package. The required network allowlist is approximately `https://pypi.org` and `https://files.pythonhosted.org` if package metadata or downloads are also needed. For a project with 250 packages, it may make about 250 HTTPS requests. Its maintainer now marks it as deprecated and recommends `uv audit` for new use. Its use of PyPI is a difference in data delivery, not a stronger package trust signal.
- [`pip-audit`](https://mkennedy.codes/posts/python-supply-chain-security-made-easy/) uses the Python Packaging Advisory Database through PyPI by default, but it can also query OSV and use a custom OSV service. It offers more choices for the vulnerability source, but it has the same limit. It finds known reports and does not establish package trust.
- If all vulnerability data must come from an internally managed source, [Trivy](https://www.trivy.dev/) might be an option. Its vulnerability database can be copied to an internal registry or built internally. An internal copy gives an organization control over distribution and updates. The accuracy of the scan still depends on the advisory sources and the organization's update process.

## Two layers, two different moments

These measures act at different points:

1. `exclude-newer` reduces exposure **before resolution** by withholding very recent package artifacts.
2. `uv audit --locked` checks the selected dependency set **before a commit** for issues that are already known.

The cooldown cannot detect malicious code, and the audit cannot flag a vulnerability that has not yet been reported. They are modest layers rather than a complete defence. But they are automatic, inexpensive, and live close to the dependency workflow—exactly the kind of security defaults I want in a minimal boilerplate.

You can find the template at [cast42/python-minimal-boilerplate](https://github.com/cast42/python-minimal-boilerplate).
