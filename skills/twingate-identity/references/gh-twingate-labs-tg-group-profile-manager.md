---
source: https://github.com/Twingate-Labs/tg-group-profile-manager
type: github
fetched: 2026-08-06
source_version: a0eef17c253d8fb8ac1fa7eed55fde0b7dc8412b
---

<!-- triage: unassigned -->

# tg-group-profile-manager

## Summary
A Slackbot that enables Twingate users to self-serve access to resource groups via configurable "profiles." Network administrators define profiles in JSON, and users can switch between them directly from Slack. Supports approval workflows and time-bound access.

## Key Information
- Profiles map to Twingate groups and are configured in JSON
- Access to profiles can be restricted by group membership
- Supports request/approve workflows and time-limited group access
- Uses Slack's event subscription and interactivity APIs
- Primary deployment target is Google Cloud Run (one-click button provided); manual deployment docs also available

## Prerequisites
- Slack workspace with admin access
- Twingate account with API access (Read + Write permissions)
- GCP project (owner-level) for Cloud Run deployment, or custom host for manual deployment

## Usage / Step-by-Step

1. **Create Slack App** — Create a new app at api.slack.com/apps using the provided `manifest.yml`
2. **Collect credentials** — Retrieve signing secret (Basic Information) and bot token (OAuth & Permissions)
3. **Configure parameters** — Prepare all values listed in the Configuration section below
4. **Deploy** — Use the Cloud Run button or follow `docs/MANUAL_DEPLOYMENT.md`
5. **Update Slack App URLs** — Set Request URL for Event Subscriptions and Interactivity & Shortcuts to `https://{your-url}/slack/events`
6. **Define profiles** — Write profile JSON per the schema in `docs/SCHEMA.md`

## Configuration Values

| Variable | Description |
|---|---|
| `SLACK_SIGNING_SECRET` | From Slack App Basic Information page |
| `SLACK_BOT_TOKEN` | Bot token from OAuth & Permissions (prefix: `xoxb-`) |
| `TG_API_KEY` | Twingate API key with Read + Write permissions |
| `TG_ACCOUNT` | Twingate network address (e.g., `test1.twingate.com`) |
| `PROFILE_CONFIG` | JSON profile definitions (see `docs/SCHEMA.md`) |
| `PROJECT_ID` | GCP project ID (Cloud Run deployment only) |

Cloud Run deployment stores all values as GCP Secrets automatically.

## Gotchas
- **Duplicate group names**: Only the first result from the Twingate API is used; avoid duplicate group names
- **IdP-synced groups not supported**: Only native Twingate groups work
- **Email matching required**: Slack user email must exactly match the Twingate account email
- **Propagation delay**: Group changes take ~20 seconds to reach connected Twingate clients
- **No automatic reconnect needed**: Clients receive group updates without disconnecting, but inform users of the delay

## Related Docs
- [`docs/SCHEMA.md`](./docs/SCHEMA.md) — Profile JSON schema reference
- [`docs/MANUAL_DEPLOYMENT.md`](./docs/MANUAL_DEPLOYMENT.md) — Manual deployment instructions
- [`manifest.yml`](./manifest.yml) — Slack app manifest
- [`app.json`](./app.json) — Cloud Run deployment steps
- [`tg-group-profile-manager.conf`](./tg-group-profile-manager.conf) — Example configuration file