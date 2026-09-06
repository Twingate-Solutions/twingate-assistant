---
source: https://help.twingate.com/articles/8044397985-windows-client-upgrades-via-intune-from-2024-63-and-older-to-2024-142-fail-to-honor-network-param
type: help
fetched: 2026-09-06
source_version: 22ad16d6510f8e3ceeed83f7a79b31b488d1820390f795e2626ed5aaf689fb9a
---

# [Windows Client] Intune Upgrade Bug: NETWORK= Param Ignored (2024.63 → 2024.142)

## Summary
When upgrading the Windows Client via Intune from version 2024.63 or older directly to 2024.142, the `NETWORK=` parameter in the config file is silently ignored. This is caused by a secure storage credential becoming unpopulated during the upgrade, causing config file contents to be skipped entirely.

## Key Information
- **Affected component:** Windows Client
- **Affected upgrade path:** 2024.63 (and older) → 2024.142
- **Not affected:** Upgrades from 2024.123 and newer to 2024.142
- **Trigger:** Intune-managed upgrades only; the config file `NETWORK=` param is not honored post-upgrade

## Root Cause
Version 2024.142 uses a secure storage credential (Windows Credential Manager) for client settings. During upgrade from ≤2024.63 via Intune, the `twingate-client AppSettings` credential entry becomes unpopulated, causing the config file to be bypassed entirely.

## Workaround (Manual Fix Per Affected User)

1. Open **Control Panel**
2. Navigate to **User Accounts** → **Web Credential Manager**
3. Locate and **Remove** the `twingate-client AppSettings` entry
4. **Restart** the Twingate client

After restart, the client will repopulate the credential entry and honor the config file parameters.

## Configuration Values
- **Affected parameter:** `NETWORK=` (in Twingate Windows Client config file)
- **Credential Manager entry to remove:** `twingate-client AppSettings`

## Gotchas
- This fix must be applied per user/device — no known automated remediation via Intune
- Skipping intermediate versions (e.g., not staging through 2024.123) triggers the issue
- **Staging fix:** Upgrading through an intermediate version (≥2024.123) before moving to 2024.142 avoids the bug entirely

## Prerequisites
- Users need access to Windows Credential Manager (Control Panel access)
- Identify all devices upgraded directly from ≤2024.63 to 2024.142 via Intune

## Related Docs
- Twingate Windows Client deployment documentation
- Intune Windows Client configuration guide