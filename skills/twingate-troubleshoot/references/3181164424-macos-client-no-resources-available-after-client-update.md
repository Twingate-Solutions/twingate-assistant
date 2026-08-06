---
source: https://help.twingate.com/articles/3181164424-macos-client-no-resources-available-after-client-update
type: help
fetched: 2026-08-06
source_version: fb2565f5a309883d4c95d94eac95f44941897c78dd2a826aad5a89b0cc7105cc
---

# macOS Client: No Resources Available After Client Update

## Summary
After upgrading to the App Store version of Twingate over a previously installed standalone client, users may see instant login with no resources listed and cannot access protected resources. This is caused by an orphaned system extension left over from the standalone client conflicting with the App Store version.

## Key Information
- **Affected clients**: App Store Client, Standalone Client on macOS
- **Root cause**: Standalone client installs a system extension that becomes orphaned when App Store version is installed on top of it
- **Symptom**: Client appears to login instantly (no auth prompt), zero resources visible, protected resources inaccessible
- **Not applicable if**: You've never installed the standalone client and confirmed no system extension is present

## Diagnosis Commands

Check for orphaned system extension:
```bash
systemextensionsctl list
```
Look for `com.twingate.macos.tunnelprovider` in `[activated enabled]` state.

Check installation history for mixed installs:
```bash
plutil -p /Library/Receipts/InstallHistory.plist | grep -B5 -A3 "com.twingate.macos"
```
Look for alternating `processName` values of `appstored` and `Installer` — the latter indicates standalone client.

## Resolution (Step-by-Step)

**Option A (Recommended)**: Switch to standalone client permanently for fuller feature set.

**Option B**: Retain App Store client with orphaned extension cleanup:
1. Install the standalone client — this terminates the orphaned extension and installs a new one
2. Remove the standalone client via drag-to-trash (not `rm -f`)
3. Verify extension removal: `systemextensionsctl list`
4. Restart if required
5. Reinstall/use App Store version

> ⚠️ Use drag-to-trash uninstall method, not `rm -f` in terminal — the standard uninstaller properly removes the system extension.

## Proactive Remediation for Admins

Identify devices with standalone client installed before MDM pushes App Store update:

**Method 1 – Admin Console**:
- Devices tab → Device page → apply filters → scroll to bottom → copy/paste table to Excel

**Method 2 – GraphQL API**:
- Use the `Devices` query to list all devices with client version and user email
- API docs: `https://www.twingate.com/docs/api#group-Operations-Queries`

## Gotchas
- MDM-managed environments are high risk: if users can install standalone client locally, a subsequent MDM-pushed App Store update will orphan the extension automatically
- A system restart may be required after extension removal
- If system extension is confirmed absent and issue persists, this fix is not applicable — different root cause

## Related Docs
- Twingate client uninstall documentation (referenced in article for stubborn extension removal)
- [Twingate API documentation](https://www.twingate.com/docs/api#group-Operations-Queries)