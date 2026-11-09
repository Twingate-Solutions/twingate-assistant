---
source: https://help.twingate.com/articles/5202917932-connector-upgrade-produces-gpg-error-in-apt
type: help
fetched: 2026-11-08
source_version: bb2d5fa2c0d476f01e965d9d447b24ad00ce2f595ffea4f280de212fbf9dcf04
trust: official
---

# Connector Upgrade Produces GPG Error in APT

## Summary
When upgrading a Twingate Connector on Ubuntu/Debian via APT, a `NO_PUBKEY` GPG error may appear during `sudo apt update`. This occurs because older installations lack the current Twingate signing key or use an outdated repo configuration without the `signed-by` option.

## Key Information
- Affected error: `NO_PUBKEY 5C363F09A9174A9E` from `https://packages.twingate.com/apt`
- Root cause: Old repo configs may use `trusted=true` workaround instead of proper GPG keyring
- Fix: Install current Twingate GPG key into a dedicated keyring and update the repo source entry

## Prerequisites
- Ubuntu or Debian system
- `curl`, `gpg`, `ca-certificates` installed
- Sudo access

## Step-by-Step Resolution

1. **Install required utilities:**
   ```bash
   sudo apt install -y curl gpg ca-certificates
   ```

2. **Install the Twingate GPG signing key** (source: `packages.twingate.com`):
   ```bash
   curl -fsSL https://packages.twingate.com/apt/gpg.key \
     | sudo gpg --dearmor -o /usr/share/keyrings/twingate-client-keyring.gpg
   ```
   Confirm replacement if prompted.

3. **Update the APT repository configuration:**
   ```bash
   echo "deb [signed-by=/usr/share/keyrings/twingate-client-keyring.gpg] https://packages.twingate.com/apt/ * *" \
     | sudo tee /etc/apt/sources.list.d/twingate.list
   ```

4. **Refresh APT:**
   ```bash
   sudo apt update
   ```

## Configuration Values
| Item | Value |
|------|-------|
| GPG key URL | `https://packages.twingate.com/apt/gpg.key` |
| Keyring path | `/usr/share/keyrings/twingate-client-keyring.gpg` |
| Sources list file | `/etc/apt/sources.list.d/twingate.list` |
| Repo URL | `https://packages.twingate.com/apt/` |

## Gotchas
- **Do not use `trusted=true`** in the repo config — older guidance recommended this as a workaround; it is unnecessary and less secure with the current signed repo setup
- Duplicate or conflicting repo entries can persist the error — check with:
  ```bash
  grep -R "packages.twingate.com" /etc/apt/sources.list /etc/apt/sources.list.d/ 2>/dev/null
  ```
  Remove or consolidate any duplicate entries found.

## Related Docs
- Twingate Linux Connector installation documentation
- Official APT repository: `https://packages.twingate.com/apt`