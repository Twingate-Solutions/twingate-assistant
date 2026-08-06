---
source: https://github.com/Twingate-Community/twindeck
type: github
fetched: 2026-08-06
source_version: 9c603b9d5f2029eab0af8f204fd646069cd3709f
---

<!-- triage: unassigned -->

# Twindeck

## Summary
A Decky Loader plugin that runs the Twingate Headless Client on Steam Deck, enabling VPN-style network connections from the Quick Access Menu (QAM) without leaving gaming mode. Requires a Twingate Service Account key and an existing Decky Loader installation.

## Key Information
- Plugin type: Decky Loader (Steam Deck QAM plugin)
- Uses Twingate Headless Client binary (fetched during build)
- Supports connect/disconnect toggle, connection status display, auto-connect, and daemon crash recovery
- Available via Decky plugin store or manual install from release zip

## Prerequisites
- Steam Deck with [Decky Loader](https://github.com/SteamDeckHomebrew/decky-loader) installed
- Twingate Service Account key (JSON file) from Twingate Admin Console
- For development: `pnpm`

## Installation

### Via Decky Plugin Store (recommended)
Search "Twindeck" in the Decky plugin browser and install.

### Manual – From URL
1. Get zip URL from [latest release](https://github.com/Twingate-Community/twindeck/releases)
2. QAM → Decky gear icon → Enable Developer mode
3. Developer panel → "Install Plugin from URL" → paste URL

### Manual – From Local Zip
1. Copy zip to Steam Deck: `scp twindeck-v*.zip deck@<deck-ip>:~/`
2. QAM → Decky gear icon → Enable Developer mode
3. Developer panel → "Install Plugin from ZIP File" → browse to file

## Setup
1. Open plugin via QAM (lock icon in sidebar)
2. Add Service Account key — browse for JSON file or paste contents directly
3. Toggle connection on
4. Optionally enable auto-connect on plugin load

## Development

```bash
pnpm i
pnpm run build       # build frontend only
pnpm run bundle      # build frontend + fetch binaries + output zip to out/
```

## Configuration Values
| Setting | Description |
|---|---|
| Service Account key | JSON file or raw content from Twingate Admin Console |
| Auto-connect | Toggle; connects automatically when plugin loads |

## Gotchas
- Twingate binaries are fetched automatically during `pnpm run bundle`; not included in the repo
- Developer mode must be enabled in Decky settings before manual zip/URL installation
- Service Account key is specific to Twingate's headless/service-account flow — standard user credentials will not work

## Related Docs
- [Decky Loader](https://github.com/SteamDeckHomebrew/decky-loader)
- [Twingate Service Accounts (Admin Console)](https://www.twingate.com/docs/service-accounts)
- [Twingate Headless Client](https://www.twingate.com/docs/linux-headless)
- [Twindeck Releases](https://github.com/Twingate-Community/twindeck/releases)