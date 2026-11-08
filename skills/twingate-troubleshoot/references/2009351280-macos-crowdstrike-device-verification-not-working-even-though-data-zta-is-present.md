---
source: https://help.twingate.com/articles/2009351280-macos-crowdstrike-device-verification-not-working-even-though-data-zta-is-present
type: help
fetched: 2026-11-08
source_version: e87fa499ae25b799490ea16181892b1fd57d1f43012002d205781ae39f8359bc
trust: official
---

# [macOS] CrowdStrike Device Verification Not Working Despite data.zta Present

## Summary
When CrowdStrike Device Verification fails on macOS even though `data.zta` exists and is populated, the root cause is typically incorrect file/directory ownership or group membership. The Twingate client requires the CrowdStrike directories and `data.zta` to be owned by `root:wheel`; having `root:admin` instead will block verification.

## Key Information
- Twingate client cannot read `data.zta` unless ownership is `root` user + `wheel` group
- Common misconfiguration: directories/files are `root:admin` instead of `root:wheel`
- Affects macOS only

## Prerequisites
- Terminal access with `sudo` privileges
- CrowdStrike installed and `data.zta` already present and populated
- Confirm `data.zta` exists before proceeding (see [related article on verifying data.zta](https://help.twingate.com/articles/2009351280))

## Step-by-Step: Fix Permissions

Run the following commands in Terminal to reset ownership and permissions:

```bash
sudo chown root:wheel /Library/Application\ Support/CrowdStrike
sudo chmod 755 /Library/Application\ Support/CrowdStrike

sudo chown root:wheel /Library/Application\ Support/CrowdStrike/ZeroTrustAssessment
sudo chmod 744 /Library/Application\ Support/CrowdStrike/ZeroTrustAssessment

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
- **Do not skip the parent directory fix** — incorrect permissions on the parent directory alone will block access even if `data.zta` itself is correct
- Verify current ownership first with `ls -la "/Library/Application Support/CrowdStrike/"` before applying changes
- Changes take effect immediately; no restart of Twingate client documented as required, but re-testing verification after applying is recommended

## Related Docs
- Twingate article on verifying `data.zta` exists and is populated (linked as "this article" in source)
- CrowdStrike Zero Trust Assessment documentation