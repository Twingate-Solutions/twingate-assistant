---
source: https://help.twingate.com/articles/5202917932-connector-upgrade-produces-gpg-error-in-apt
type: help
fetched: 2026-10-18
source_version: f8a0dba060d6102edffc95dd16c2231fb42c7a8e1f19404f5e98be33fc41f40b
trust: official
---

# Connector Upgrade Produces GPG Error in APT

## Summary
When upgrading Twingate Connectors on Ubuntu/Debian via APT, a `NO_PUBKEY` GPG error may occur due to outdated repository configuration. The fix involves reinstalling the current Twingate GPG signing key and updating the repo config to use the `signed-by` option.

## Key Information
- Affects Ubuntu/Debian installations using APT
- Error signature: `NO_PUBKEY 5C363F09A9174A9E`
- Root cause: old installations lack the current GPG keyring or use deprecated `trusted=true` workaround
- Current approach uses a dedicated keyring at `/usr/share/keyrings/twingate-client-keyring.gpg`

## Prerequisites
- `curl`, `gpg`, `ca-certificates` installed
- Sudo access

## Step-by-Step Resolution

1. **Install required utilities**
   ```bash
   sudo apt install -y curl gpg ca-certificates
   ```

2. **Install the Twingate GPG signing key** (downloads from `packages.twingate.com`, Twingate's official package host)
   ```bash
   curl -fsSL https://packages.twingate.com/apt/gpg.key \
     | sudo gpg --dearmor -o /usr/share/keyrings/twingate-client-keyring.gpg
   ```
   Confirm replacement if prompted for an existing keyring.

3. **Update the APT repository configuration**
   ```bash
   echo "deb [signed-by=/usr/share/keyrings/twingate-client-keyring.gpg] https://packages.twingate.com/apt/ * *" \
     | sudo tee /etc/apt/sources.list.d/twingate.list
   ```

4. **Verify config**
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
| Keyring path | `/usr/share/keyrings/twingate-client-keyring.gpg` |
| GPG key URL | `https://packages.twingate.com/apt/gpg.key` |
| Sources list | `/etc/apt/sources.list.d/twingate.list` |
| Repo URL | `https://packages.twingate.com/apt/` |

## Gotchas
- **Do not use `trusted=true`** — older guides recommended this as a workaround; it is not needed and should be removed
- Duplicate repo entries can cause conflicts — check with:
  ```bash
  grep -R "packages.twingate.com" /etc/apt/sources.list /etc/apt/sources.list.d/ 2>/dev/null
  ```
  Remove or consolidate any duplicates found.

## Related Docs
- Twingate Linux Connector installation documentation
- APT `signed-by` option documentation (`man sources.list`)