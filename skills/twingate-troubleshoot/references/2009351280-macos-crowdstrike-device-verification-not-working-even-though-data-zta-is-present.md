---
source: https://help.twingate.com/articles/2009351280-macos-crowdstrike-device-verification-not-working-even-though-data-zta-is-present
type: help
fetched: 2026-10-04
source_version: ab1b3958b36352dcb75d2615e8eddbfc417100c71555d3e63725ca90ceca6b96
trust: official
---

# [macOS] CrowdStrike Device Verification Not Working Despite data.zta Present

## Summary
On macOS, Twingate's CrowdStrike Device Verification can fail even when `data.zta` exists and is populated. The root cause is incorrect file/directory ownership — specifically, files owned by `root:admin` instead of the required `root:wheel` group.

## Key Information
- Twingate client requires CrowdStrike directories and `data.zta` to be owned by `root` user and `wheel` group
- Common misconfiguration: files are `root:admin` instead of `root:wheel`
- Affects macOS only

## Prerequisites
- Terminal access with `sudo` privileges
- CrowdStrike installed with `data.zta` confirmed present and populated at `/Library/Application Support/CrowdStrike/ZeroTrustAssessment/data.zta`

## Required Permission Values

| Path | Owner | Group | Mode |
|------|-------|-------|------|
| `/Library/Application Support/CrowdStrike` | root | wheel | 755 |
| `/Library/Application Support/CrowdStrike/ZeroTrustAssessment` | root | wheel | 744 |
| `/Library/Application Support/CrowdStrike/ZeroTrustAssessment/data.zta` | root | wheel | 644 |

## Step-by-Step Fix

Run the following commands in Terminal:

```bash
sudo chown root:wheel /Library/Application\ Support/CrowdStrike
sudo chmod 755 /Library/Application\ Support/CrowdStrike

sudo chown root:wheel /Library/Application\ Support/CrowdStrike/ZeroTrustAssessment
sudo chmod 744 /Library/Application\ Support/CrowdStrike/ZeroTrustAssessment

sudo chown root:wheel /Library/Application\ Support/CrowdStrike/ZeroTrustAssessment/data.zta
sudo chmod 644 /Library/Application\ Support/CrowdStrike/ZeroTrustAssessment/data.zta
```

## Gotchas
- Verification failure gives no obvious indication that permissions are the cause — the symptom looks identical to CrowdStrike not being installed or `data.zta` being absent
- Confirm ownership with `ls -la` before and after: look for `root wheel` in the output
- This issue has been observed after certain CrowdStrike updates or macOS upgrades that reset group ownership to `admin`

## Related Docs
- Twingate article on confirming `data.zta` exists and is populated (referenced as "this article" in source)
- CrowdStrike Zero Trust Assessment documentation