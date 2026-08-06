---
source: https://github.com/Twingate-Labs/tg-github-codespaces
type: github
fetched: 2026-08-06
source_version: 5533fce2da2ecfdcf90ea2be94f9ee80d25a0f6b
---

<!-- triage: unassigned -->

# Twingate + GitHub Codespaces

## Summary
Example repository showing how to run a Twingate client inside a GitHub Codespace. Supports two connection modes: Service Account (automated) and interactive user login. Enables Codespace users to reach private resources protected by Twingate from the browser or VS Code.

## Key Information
- Provides a `Dockerfile` and two `devcontainer.json` variants for `.devcontainer` setup
- Service Account mode is the default/recommended approach for automated environments
- Interactive mode requires manual authentication steps after container start
- For GitHub Actions (not Codespaces), use the separate [Connect to Twingate](https://github.com/marketplace/actions/connect-to-twingate) Action instead

## Prerequisites
- GitHub repository with Codespaces access (may require org admin approval)
- `.devcontainer` directory present in your target repo
- A Twingate account with either:
  - A Service Account Key (generated in Twingate Admin Console), **or**
  - A regular Twingate user account

## Usage / Step-by-Step

### Service Account (automated)
1. Copy `.devcontainer/Dockerfile` from this repo into your repo's `.devcontainer/`
2. Copy `devcontainer.serviceaccount.json` → rename to `.devcontainer/devcontainer.json`
3. Add a Codespaces **User Secret** `TWINGATE_SERVICE_KEY` = your Service Account Key
4. Launch Codespace; verify with `twingate status` (expect `online`)
5. List resources: `twingate resources`

### Interactive Login
1. Copy `.devcontainer/Dockerfile` into your repo's `.devcontainer/`
2. Copy `devcontainer.interactive.json` → rename to `.devcontainer/devcontainer.json`
3. Add a Codespaces **Secret** `TWINGATE_ACCOUNT` = your account subdomain (e.g., `acme`)
4. Launch Codespace; run `twingate status` (without `sudo`)
   - If `authenticating`: follow the displayed URL
   - If `not running`: run `twingate start`, then `/usr/bin/twingate-notifier console` and follow the URL
5. Confirm `online`; list resources with `twingate resources`

## Configuration Values

| Name | Type | Mode | Description |
|---|---|---|---|
| `TWINGATE_SERVICE_KEY` | Codespaces User Secret | Service Account | Full Service Account Key from Admin Console |
| `TWINGATE_ACCOUNT` | Codespaces Secret | Interactive | Account subdomain only (e.g., `acme` from `acme.twingate.com`) |

## Gotchas
- Interactive mode commands must be run **without** `sudo`; `twingate report` for diagnostics requires `sudo`
- Secrets must be set before launching the Codespace; restarting after adding secrets is required
- Service Account Keys are scoped to specific resources—ensure the key has access to the resources you need
- `devcontainer.json` must be renamed exactly; both example files cannot coexist with the same name

## Related Docs
- [Twingate Service Accounts](https://docs.twingate.com/docs/services)
- [GitHub Codespaces Encrypted Secrets (User)](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-encrypted-secrets-for-your-codespaces)
- [GitHub Codespaces Encrypted Secrets (Org/Repo)](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/managing-encrypted-secrets-for-your-repository-and-organization-for-codespaces)
- [Connect to Twingate GitHub Action](https://github.com/marketplace/actions/connect-to-twingate)