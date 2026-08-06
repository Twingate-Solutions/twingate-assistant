---
source: https://github.com/Twingate-Labs/tg-coder
type: github
fetched: 2026-08-06
source_version: 2fa305be5ff336d50bbaaeb657c026b3568810ea
---

<!-- triage: unassigned -->

# Twingate + Coder

## Summary
Example configuration for running a Twingate client inside Coder workspaces. Supports both interactive user authentication and service account (headless) authentication. Based on modified Coder Docker starter templates.

## Key Information
- Two authentication modes: regular user account (interactive) and service account (automated)
- Provided as Terraform template files replacing Coder's default `main.tf`
- Requires privileged Docker containers (known limitation)
- Templates located in `./templates/` directory; additional docs in `docs/OTHER_TEMPLATE.md`

## Prerequisites
- Twingate account
- Coder server installed ([install docs](https://coder.com/docs/v2/latest/install))
- For service account mode: a generated Twingate Service Account Key

## Usage

### Interactive (Regular User Account)
1. Create a new Coder Docker starter template
2. Replace `main.tf` with `templates/docker_interactive.tf`
3. In template Settings → Variables, set `twingate_tenant` to your tenant name (e.g., `acme` for `acme.twingate.com`)
4. Create a workspace and open the terminal
5. Run `twingate status`:
   - If `authenticating`: follow the displayed URL to authenticate
   - If `not running`: run `twingate start`, then `/usr/bin/twingate-notifier console` and follow the URL

### Service Account (Headless)
1. Generate a Twingate Service Account Key
2. Create a new Coder Docker starter template
3. Replace `main.tf` with `templates/docker_serviceaccount.tf`
4. In template Settings → Variables, set the Service Key variable
5. Create a workspace; `twingate status` should return `online`

## Configuration Values

| Variable | Description | Example |
|----------|-------------|---------|
| `twingate_tenant` | Twingate tenant subdomain | `acme` (for `acme.twingate.com`) |
| Twingate Service Key | Service account key for headless auth | Set via template variable |

## Gotchas
- Docker containers **must run as privileged** — no workaround documented
- Interactive auth requires manual URL follow-up if the client is in `authenticating` or `not running` state; `twingate-notifier console` may be needed in addition to `twingate start`

## Related Docs
- [Coder template tutorial](https://coder.com/docs/v2/latest/templates/tutorial)
- [Twingate Service Accounts](https://www.twingate.com/docs/services)
- [Other template types (Kubernetes, etc.)](docs/OTHER_TEMPLATE.md)
- [Issues](https://github.com/Twingate-Labs/tg-coder/issues/new)