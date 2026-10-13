---
source: https://help.twingate.com/articles/5202917932-connector-upgrade-produces-gpg-error-in-apt
type: help
fetched: 2026-10-11
source_version: e898a96f13d217a6afccfcf8581a4a540551cbb5061a73dc1055ca746c465885
trust: official
---

# Connector Upgrade Produces GPG Error in APT

## Summary
When upgrading a Twingate Connector on Ubuntu/Debian via APT, a `NO_PUBKEY` GPG error may appear during `sudo apt update`. This occurs because older installations lack the current Twingate signing key or use a deprecated `trusted=true` workaround. The fix involves installing the current GPG key and updating the repository configuration to use `signed-by`.

## Key Information
- Affected systems: Ubuntu/Debian with older Twingate APT repository configurations
- Error signature: `NO_PUBKEY 5C363F09A9174A9E`
- Current approach: Dedicated GPG keyring at `/usr/share/keyrings/twingate-client-keyring.gpg` with `signed-by` APT option
- Deprecated approach: `trusted=true` in repo config — no longer needed or recommended

## Prerequisites
- `curl`, `gpg`, `ca-certificates` installed
- Sudo access

## Step-by-Step Resolution

1. **Install required utilities**
   ```bash
   sudo apt install -y curl gpg ca-certificates
   ```

2. **Install Twingate GPG signing key** (downloads from `packages.twingate.com`)
   ```bash
   curl -fsSL https://packages.twingate.com/apt/gpg.key \
     | sudo gpg --dearmor -o /usr/share/keyrings/twingate-client-keyring.gpg
   ```
   Confirm replacement if prompted.

3. **Update repository configuration**
   ```bash
   echo "deb [signed-by=/usr/share/keyrings/twingate-client-keyring.gpg] https://packages.twingate.com/apt/ * *" \
     | sudo tee /etc/apt/sources.list.d/twingate.list
   ```

4. **Verify configuration**
   ```bash
   cat /etc/apt/sources.list.d/twingate.list
   ```

5. **Refresh APT**
   ```bash
   sudo apt update
   ```

## Configuration Values
| Item | Value |
|------|-------|
| GPG key URL | `https://packages.twingate.com/apt/gpg.key` |
| Keyring path | `/usr/share/keyrings/twingate-client-keyring.gpg` |
| Repo config file | `/etc/apt/sources.list.d/twingate.list` |
| Repo URL | `https://packages.twingate.com/apt/` |

## Gotchas
- Do **not** add `trusted=true` to the repo entry — it's a legacy workaround and masks key verification
- Check for duplicate/conflicting repo entries if the error persists:
  ```bash
  grep -R "packages.twingate.com" /etc/apt/sources.list /etc/apt/sources.list.d/ 2>/dev/null
  ```
- Multiple entries for `packages.twingate.com` will cause conflicts; remove or consolidate them

## Related Docs
- Twingate Linux Connector installation documentation
- APT `signed-by` option: Debian/Ubuntu APT documentation