---
source: https://github.com/Twingate-Solutions/idp-migrator
type: github
fetched: 2026-08-06
source_version: cdbfd05f4b54cbccdafe80d28d8d76059a0b17ad
---

<!-- triage: unassigned -->

# Twingate IDP Migrator

## Summary
A desktop GUI tool for Twingate administrators to re-map group-to-resource access assignments when switching identity providers. It connects to the Twingate Admin API, performs fuzzy matching between old and new IdP groups, and applies access grants additively. A mandatory dry-run step and full JSON changelog with rollback support are included.

## Key Information
- **Not an official Twingate product** — community-supported, Apache 2.0 license, LLM-assisted development
- Additive only: never removes existing group access
- Mandatory dry-run before any API writes
- Writes a changelog to `~/twingate-migration-<timestamp>.json` for rollback
- Built with PySide6; API calls run in background QThread via asyncio/httpx
- Pre-built single-file binaries for Windows x64, macOS arm64/x64, Linux x64
- Demo mode available without a Twingate account

## Prerequisites
- Twingate account with administrator access
- API token with **Read** and **Write** scope (Settings → API → Generate Token)
- Tenant subdomain (e.g., `acme` from `acme.twingate.com`)
- New IdP groups must already be synced into Twingate before running
- **Source only:** Python 3.12+

## Usage / Step-by-Step
1. **Connect** — Enter tenant name and API key; tool fetches groups/resources (read-only)
2. **Select Groups** — Categorize groups into "Old IdP (From)" and "New IdP (To)" buckets
3. **Review Mappings** — Confirm fuzzy-matched pairings; adjust via dropdown; unconfirmed rows are skipped
4. **Preview (Dry Run)** — Review full tree of planned access grants; cannot be skipped
5. **Execute** — Tool applies grants, shows per-resource status, saves changelog
6. **Rollback (optional)** — File → Rollback from Changelog → load JSON → roll back all or one group

## Configuration Values
| Input | Description |
|---|---|
| Tenant Name | Subdomain of your Twingate admin URL |
| API Key | Twingate admin API token (held in memory only, never written to disk) |
| `TEST` / `TEST` | Enter in both fields to activate offline demo mode |

## Platform Notes
- **macOS:** Run `xattr -d com.apple.quarantine <binary> && chmod +x <binary>` before executing
- **Linux:** `chmod +x` required before executing
- **Windows:** SmartScreen warning expected (self-signed); click More info → Run anyway. If blocked by Group Policy, run from source instead

## Gotchas
- Old group access is never cleaned up automatically — decommission old groups manually after migration
- Rollback only removes access granted by the specific changelog file loaded; it does not affect other access
- API key is never persisted, so credentials must be re-entered each session
- SHA-256 checksums for binaries are listed on the Releases page — verify before running

## Related Docs
- [GitHub Releases](https://github.com/Twingate-Solutions/idp-migrator/releases/latest)
- [CONTRIBUTING.md](https://github.com/Twingate-Solutions/idp-migrator/blob/main/CONTRIBUTING.md)
- [Twingate API documentation](https://docs.twingate.com/docs/api-overview)