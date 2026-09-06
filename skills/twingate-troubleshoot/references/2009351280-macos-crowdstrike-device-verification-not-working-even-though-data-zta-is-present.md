---
source: https://help.twingate.com/articles/2009351280-macos-crowdstrike-device-verification-not-working-even-though-data-zta-is-present
type: help
fetched: 2026-09-06
source_version: da2fb0e16307f4df5e366be465b20f57e8d790173bd729f49fc7dbcd192688cd
---

# [macOS] CrowdStrike Device Verification Not Working Despite data.zta Present

## Summary
When CrowdStrike device verification fails on macOS even though `data.zta` exists and is populated, the cause is incorrect file/directory permissions. Twingate requires the CrowdStrike directories and `data.zta` to be owned by `root:wheel`; ownership by `root:admin` is a known failure case.

## Key Information
- Twingate client cannot read `data.zta` unless ownership is `root` user + `wheel` group
- Symptom: device verification fails despite file being present and populated
- Root cause: directories/files owned by `root:admin` instead of `root:wheel`

## Prerequisites
- macOS with CrowdStrike installed
- Confirmed `data.zta` exists and is populated (verify via [linked article](https://help.twingate.com/articles/2009351280))
- Terminal access with `sudo` privileges

## Fix: Reset Permissions

Run all six commands in Terminal:

```bash
sudo chown root:wheel "/Library/Application Support/CrowdStrike"
sudo chmod 755 "/Library/Application Support/CrowdStrike"

sudo chown root:wheel "/Library/Application Support/CrowdStrike/ZeroTrustAssessment"
sudo chmod 744 "/Library/Application Support/CrowdStrike/ZeroTrustAssessment"

sudo chown root:wheel "/Library/Application Support/CrowdStrike/ZeroTrustAssessment/data.zta"
sudo chmod 644 "/Library/Application Support/CrowdStrike/ZeroTrustAssessment/data.zta"
```

## Configuration Values

| Path | Owner | Group | Permissions |
|------|-------|-------|-------------|
| `/Library/Application Support/CrowdStrike` | root | wheel | 755 |
| `/Library/Application Support/CrowdStrike/ZeroTrustAssessment` | root | wheel | 744 |
| `/Library/Application Support/CrowdStrike/ZeroTrustAssessment/data.zta` | root | wheel | 644 |

## Gotchas
- Using `root:admin` instead of `root:wheel` silently breaks verification — no obvious error indicates a permissions issue
- Run all six commands; fixing only the file without fixing parent directories may not resolve the issue
- Restart the Twingate client after applying permission changes

## Related Docs
- Verifying `data.zta` exists and is populated (referenced as "this article" in source)
- Twingate CrowdStrike Device Verification setup