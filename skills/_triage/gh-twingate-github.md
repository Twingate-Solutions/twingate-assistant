---
source: https://github.com/Twingate/.github
type: github
fetched: 2026-08-06
source_version: 224301243fdc36576d1ce0f1cb01639d088a48e4
---

<!-- triage: unassigned -->

# Twingate/.github

## Summary
This is Twingate's organization-level `.github` repository, which holds community health files that apply across all public repositories in the Twingate GitHub organization. It contains the organization profile README, issue templates, and contribution guidelines.

## Key Information
- Organization-wide GitHub community health files (apply to all repos lacking their own)
- Contains the public-facing organization profile (`profile/README.md`)
- Provides standardized issue templates for bug reports and feature requests
- Houses the contributing guide (`CONTRIBUTING.md`)
- No deployable code; documentation and GitHub metadata only

## Prerequisites
- GitHub account to submit issues or pull requests
- Familiarity with GitHub's [community health files](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file) spec

## Usage / Step-by-Step

**Submitting an issue:**
1. Navigate to any Twingate public repository's Issues tab
2. Select the appropriate template (Bug Report or Feature Request)
3. Fill in the required fields and submit

**Contributing changes:**
1. Fork this repository
2. Make changes on a feature branch
3. Open a pull request against `master`
4. Follow guidelines in `CONTRIBUTING.md`

## Configuration Values
None. This repo contains no environment variables, CLI flags, or API parameters.

## Gotchas
- Files here act as **defaults** — they are overridden by any matching file in an individual Twingate repository
- Changes to issue templates here affect all Twingate repos that don't define their own
- The `profile/README.md` renders only on the [Twingate organization page](https://github.com/Twingate); it is not a project README
- The default branch is `master`, not `main`

## Related Docs
- [GitHub: Default community health files](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)
- [GitHub: Organization profile README](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile)
- [Twingate Documentation](https://docs.twingate.com)
- [Twingate GitHub Organization](https://github.com/Twingate)