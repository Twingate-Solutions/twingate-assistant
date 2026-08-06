---
source: https://help.twingate.com/articles/5202917932-connector-upgrade-produces-gpg-error-in-apt
type: help
fetched: 2026-08-06
source_version: 55850789585cf8026a563fbf177cfaca09b3db41ff0a6c0011cb2d97279d2e72
---

# Connector Upgrade Produces GPG Error in APT

## Summary
A backend change to Twingate's package serving infrastructure causes GPG signature verification errors when running `apt update` on systems using the Twingate APT repository. In most cases this is a warning only and upgrades proceed normally, but some systems may fail to upgrade if the repository isn't marked as trusted.

## Key Information
- Error appears as: `NO_PUBKEY 5C363F09A9174A9E`
- The Twingate Connector package is **not currently signed** — this is expected behavior
- Systems deployed via the official Twingate Admin Console deployment script should already have `trusted=true` configured
- The fix does not eliminate the warning — it only allows upgrades to proceed

## Symptoms
```
W: GPG error: https://packages.twingate.com/apt InRelease: The following signatures 
couldn't be verified because the public key is not available: NO_PUBKEY 5C363F09A9174A9E
```

## Resolution

### Quick Check
First try running the upgrade directly — the warning may not block it:
```bash
sudo apt upgrade
```

### Fix (if upgrade fails)

1. Edit the Twingate APT source list:
   ```bash
   sudo nano /etc/apt/sources.list.d/twingate.list
   ```

2. Modify the repository line to add `trusted=true`:
   ```
   deb [trusted=true] https://packages.twingate.com/apt/ /
   ```

3. Save the file, then run:
   ```bash
   sudo apt update && sudo apt upgrade
   ```

## Configuration Values
| File | Setting | Value |
|------|---------|-------|
| `/etc/apt/sources.list.d/twingate.list` | `trusted` | `true` |

## Gotchas
- Adding `trusted=true` suppresses the upgrade failure but **does not remove** the GPG warning from `apt update` output
- Only apply the fix if `apt upgrade` actually fails — most systems only show a warning and work fine
- Systems installed via Admin Console deployment script are likely already configured correctly

## Related Docs
- Twingate Connector deployment (Admin Console)
- APT repository: `https://packages.twingate.com/apt/`