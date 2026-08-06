---
source: https://help.twingate.com/articles/2009351280-macos-crowdstrike-device-verification-not-working-even-though-data-zta-is-present
type: help
fetched: 2026-08-06
source_version: f9fa1a20298416e118552c6e08584052e416e36983e856d9c96211e2c479d1a6
---

# [macOS] CrowdStrike Device Verification Not Working Despite data.zta Present

## Summary
CrowdStrike Device Verification may fail on macOS even when `data.zta` exists and is populated. The root cause is incorrect file/directory ownership — specifically, directories or files owned by the `admin` group instead of the required `wheel` group. Twingate cannot read the ZTA file without correct permissions.

## Key Information
- Twingate requires CrowdStrike directories and `data.zta` to be owned by `root:wheel`
- Common misconfiguration: ownership set to `root:admin` instead of `root:wheel`
- Affects macOS only
- Fix requires running `sudo` commands in Terminal

## Prerequisites
- macOS with Twingate client installed
- CrowdStrike installed with `data.zta` file present and populated
- Terminal access with sudo privileges
- Confirm `data.zta` exists before applying this fix

## Step-by-Step Fix

Run the following commands in Terminal:

```bash
# Fix CrowdStrike parent directory
sudo chown root:wheel /Library/Application\ Support/CrowdStrike
sudo chmod 755 /Library/Application\ Support/CrowdStrike

# Fix ZeroTrustAssessment subdirectory
sudo chown root:wheel /Library/Application\ Support/CrowdStrike/ZeroTrustAssessment
sudo chmod 744 /Library/Application\ Support/CrowdStrike/ZeroTrustAssessment

# Fix data.zta file
sudo chown root:wheel /Library/Application\ Support/CrowdStrike/ZeroTrustAssessment/data.zta
sudo chmod 644 /Library/Application\ Support/CrowdStrike/ZeroTrustAssessment/data.zta
```

## Configuration Values

| Path | Owner | Group | Permissions |
|------|-------|-------|-------------|
| `/Library/Application Support/CrowdStrike` | root | wheel | 755 |
| `/Library/Application Support/CrowdStrike/ZeroTrustAssessment` | root | wheel | 744 |
| `/Library/Application Support/CrowdStrike/ZeroTrustAssessment/data.zta` | root | wheel | 644 |

## Gotchas
- This fix only applies if `data.zta` already exists and is populated — verify this first
- Simply having the file present is not sufficient; group ownership must be `wheel`, not `admin`
- Permissions may revert after CrowdStrike updates; reapply if verification breaks again

## Related Docs
- Twingate article on verifying `data.zta` exists and is populated (referenced as "this article" in source)
- CrowdStrike Device Verification setup documentation