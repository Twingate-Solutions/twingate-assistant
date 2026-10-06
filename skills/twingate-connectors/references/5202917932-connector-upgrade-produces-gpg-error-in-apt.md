---
source: https://help.twingate.com/articles/5202917932-connector-upgrade-produces-gpg-error-in-apt
type: help
fetched: 2026-10-04
source_version: adb3f872e3d7972a5711775857d8975500820ce0a0ae79e453002b445af83257
trust: official
---

# Connector Upgrade Produces GPG Error in APT

## Summary
When updating a Twingate Connector on Ubuntu/Debian via APT, you may encounter a `NO_PUBKEY` GPG verification error. This occurs because older installations lack the current Twingate signing key or use outdated repository configuration. The fix involves installing the current GPG key and updating the repository definition to use `signed-by`.

## Key Information
- Affected systems: Ubuntu/Debian with older Twingate APT installs
- Error signature: `NO_PUBKEY 5C363F09A9174A9E`
- Current Twingate approach: dedicated GPG keyring + `signed-by` APT option
- Legacy workaround (`trusted=yes`) is no longer recommended

## Prerequisites
- `curl`, `gpg`, `ca-certificates` installed
- sudo access

## Step-by-Step Resolution

1. **Install required utilities**
   ```bash
   sudo apt install -y curl gpg ca-certificates
   ```

2. **Install the Twingate GPG signing key** (source: `packages.twingate.com`)
   Download from `https://packages.twingate.com/apt/gpg.key`, dearmor, and write to `/usr/share/keyrings/twingate-client-keyring.gpg`. Confirm replacement if prompted.

3. **Update the repository configuration**
   ```bash
   echo "deb [signed-by=/usr/share/keyrings/twingate-client-keyring.gpg] https://packages.twingate.com/apt/ * *" \
     | sudo tee /etc/apt/sources.list.d/twingate.list
   ```

4. **Refresh APT**
   ```bash
   sudo apt update
   ```

## Configuration Values
| Item | Value |
|------|-------|
| GPG key URL | `https://packages.twingate.com/apt/gpg.key` |
| Keyring path | `/usr/share/keyrings/twingate-client-keyring.gpg` |
| Sources file | `/etc/apt/sources.list.d/twingate.list` |
| Repo URL | `https://packages.twingate.com/apt/` |

## Gotchas
- **Do not use `trusted=yes`** in the repo definition — older docs may suggest this; it bypasses signature verification and is unnecessary with the current setup
- **Check for duplicate entries** if the error persists:
  ```bash
  grep -R "packages.twingate.com" /etc/apt/sources.list /etc/apt/sources.list.d/ 2>/dev/null
  ```
  Conflicting or duplicate entries can cause ongoing failures

## Related Docs
- Twingate Linux Connector installation documentation
- Twingate package repository: `https://packages.twingate.com/apt/`