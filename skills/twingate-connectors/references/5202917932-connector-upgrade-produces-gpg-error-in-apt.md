---
source: https://help.twingate.com/articles/5202917932-connector-upgrade-produces-gpg-error-in-apt
type: help
fetched: 2026-09-06
source_version: 83e63bdcb21114a88192ff39e45da95ea9d9e411a75d1b7ccdb63d274a2d1f6f
---

# Connector Upgrade Produces GPG Error in APT

## Summary
A backend change in Twingate's package serving infrastructure causes GPG verification errors when running `apt update` against the Twingate APT repository. The connector package is not currently signed, but systems without explicit trust configuration may block updates. Most cases result in a warning only, not a failure.

## Key Information
- Error affects systems using `https://packages.twingate.com/apt` repository
- Systems deployed via official Twingate Admin Console deployment script are typically unaffected (trusted config already set)
- Warning does not prevent `apt upgrade` from working in most cases
- Fix is required only if `sudo apt upgrade` fails to upgrade the connector

## Symptoms
```
W: GPG error: https://packages.twingate.com/apt InRelease: The following signatures 
couldn't be verified because the public key is not available: NO_PUBKEY 5C363F09A9174A9E
```

## Resolution

### Step-by-Step (if upgrade fails)

1. Edit the Twingate APT source list:
   ```bash
   sudo nano /etc/apt/sources.list.d/twingate.list
   ```

2. Modify the repository line to add `trusted=true`:
   ```
   deb [trusted=true] https://packages.twingate.com/apt/ /
   ```

3. Save and exit, then run:
   ```bash
   sudo apt update && sudo apt upgrade
   ```

## Configuration Values
| File | Setting | Value |
|------|---------|-------|
| `/etc/apt/sources.list.d/twingate.list` | `trusted` option | `true` |

## Gotchas
- Adding `trusted=true` does **not** suppress the GPG warning — it only allows package updates to proceed
- If you only see a warning (not a failure), no action is required; run `sudo apt upgrade` directly
- The connector package is **not currently signed** — this is expected behavior, not a security incident

## Related Docs
- Twingate Connector deployment (Admin Console deployment script)
- Twingate APT repository: `https://packages.twingate.com/apt`