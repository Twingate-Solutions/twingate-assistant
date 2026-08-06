---
source: https://help.twingate.com/articles/8044397985-windows-client-upgrades-via-intune-from-2024-63-and-older-to-2024-142-fail-to-honor-network-param
type: help
fetched: 2026-08-06
source_version: 2691da9d11d23d738dd38f6ed5658db07ebe1c38a79c0fd31f806a6272ed3c5f
---

# [Windows Client] Intune Upgrade Bug: NETWORK= Param Ignored (2024.63 → 2024.142)

## Summary
When upgrading the Windows Client via Intune from version 2024.63 or older directly to 2024.142, the `NETWORK=` parameter in the config file is silently ignored. This is caused by an unpopulated secure storage credential that overrides config file contents during the upgrade process.

## Key Information
- **Affected path**: Intune upgrade from 2024.63 (or older) → 2024.142
- **Not affected**: Upgrades from 2024.123 and newer to 2024.142 work correctly
- **Root cause**: Secure storage credential (Windows Credential Manager) is unpopulated during upgrade, causing config file to be ignored
- **Deployment method affected**: Intune-managed upgrades only

## Affected Configuration Values
- `NETWORK=` parameter in Windows Client config file is the impacted setting

## Workaround (Step-by-Step)

1. Open **Control Panel**
2. Navigate to **User Accounts** → **Web Credential Manager**
3. Locate the `twingate-client` **AppSettings** entry
4. Click **Remove** to delete the entry
5. **Restart** the Twingate client

After restart, the client will repopulate the credential store and honor the config file parameters.

## Gotchas
- No workaround is needed if upgrading from 2024.123 or later — only the 2024.63-and-older → 2024.142 jump is affected
- The issue is silent — the client appears to function but uses incorrect network configuration
- Must be performed per-user since Windows Credential Manager entries are user-scoped

## Prerequisites
- Windows Client installed via Intune
- Affected version range: source ≤ 2024.63, target = 2024.142

## Related Docs
- Twingate Windows Client deployment documentation
- Intune Windows Client configuration guide