---
source: https://help.twingate.com/articles/2009351280-macos-crowdstrike-device-verification-not-working-even-though-data-zta-is-present
type: help
fetched: 2026-11-01
source_version: aac7d56003fcdb75c4472a46eb67bb9b51a07b547a10338b52968d8b77fe1478
trust: official
---

# [macOS] CrowdStrike Device Verification Not Working Despite data.zta Present

## Summary
On macOS, Twingate's CrowdStrike Device Verification can fail even when `data.zta` exists and is populated. The root cause is incorrect file/directory ownership — specifically, directories or files owned by the `admin` group instead of the required `wheel` group.

## Key Information
- Twingate client requires CrowdStrike directories and `data.zta` to be owned by `root:wheel`
- Common misconfiguration: ownership is `root:admin` instead of `root:wheel`
- Affects device verification flow even when ZTA data is present and valid

## Prerequisites
- macOS with CrowdStrike installed
- `data.zta` confirmed to exist and be populated at `/Library/Application Support/CrowdStrike/ZeroTrustAssessment/data.zta`
- Terminal access with `sudo` privileges

## Required Permission Configuration

| Path | Owner | Group | Mode |
|------|-------|-------|------|
| `/Library/Application Support/CrowdStrike` | `root` | `wheel` | `755` |
| `/Library/Application Support/CrowdStrike/ZeroTrustAssessment` | `root` | `wheel` | `744` |
| `/Library/Application Support/CrowdStrike/ZeroTrustAssessment/data.zta` | `root` | `wheel` | `644` |

## Fix: Reset Permissions

Run the following commands in Terminal:

```bash
sudo chown root:wheel "/Library/Application Support/CrowdStrike"
sudo chmod 755 "/Library/Application Support/CrowdStrike"

sudo chown root:wheel "/Library/Application Support/CrowdStrike/ZeroTrustAssessment"
sudo chmod 744 "/Library/Application Support/CrowdStrike/ZeroTrustAssessment"

sudo chown root:wheel "/Library/Application Support/CrowdStrike/ZeroTrustAssessment/data.zta"
sudo chmod 644 "/Library/Application Support/CrowdStrike/ZeroTrustAssessment/data.zta"
```

## Gotchas
- Verify both ownership (`chown`) and permissions (`chmod`) — one incorrect setting is sufficient to break verification
- This issue can persist silently; no obvious error beyond verification failure
- Check existing permissions first with `ls -la "/Library/Application Support/CrowdStrike/"` before applying fixes

## Related Docs
- [Verifying data.zta exists and is populated](https://help.twingate.com) — referenced as prerequisite check before applying this fix
- Twingate CrowdStrike Device Verification setup documentation