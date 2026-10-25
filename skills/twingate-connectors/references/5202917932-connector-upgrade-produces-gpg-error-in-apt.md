---
source: https://help.twingate.com/articles/5202917932-connector-upgrade-produces-gpg-error-in-apt
type: help
fetched: 2026-10-25
source_version: 34d2c7062a20372cf84c8831145b7c325c082a419114a2f39b0e8bc2a39ee3c7
trust: official
---

# Connector Upgrade Produces GPG Error in APT

## Summary
When updating a Twingate Connector on Ubuntu/Debian via APT, you may see a `NO_PUBKEY` GPG error. This occurs because older installations lack the current signing key or use an outdated repo configuration. The fix involves installing the current GPG key into a dedicated keyring and updating the repo config to use `signed-by`.

## Key Information
- Affected platforms: Ubuntu, Debian (APT-based systems)
- Error signature: `NO_PUBKEY 5C363F09A9174A9E`
- Twingate's current config uses a dedicated GPG keyring + `signed-by` APT option
- Old workaround (`trusted=true`) is deprecated and should not be used

## Prerequisites
- `curl`, `gpg`, `ca-certificates` installed
- `sudo` access

## Step-by-Step Resolution

**1. Install required utilities**
```bash
sudo apt install -y curl gpg ca-certificates
```

**2. Install the Twingate GPG signing key**

Download from `packages.twingate.com` (Twingate's official package host) and install into the dedicated keyring:
```bash
curl -fsSL https://packages.twingate.com/apt/gpg.key \
  | sudo gpg --dearmor -o /usr/share/keyrings/twingate-client-keyring.gpg
```
Confirm replacement if prompted.

**3. Update the repository configuration**
```bash
echo "deb [signed-by=/usr/share/keyrings/twingate-client-keyring.gpg] https://packages.twingate.com/apt/ * *" \
  | sudo tee /etc/apt/sources.list.d/twingate.list
```

**4. Verify config (optional)**
```bash
cat /etc/apt/sources.list.d/twingate.list
```

**5. Refresh APT**
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
- **Do not use `trusted=true`** in the repo config — this was an older workaround and bypasses signature verification
- **Duplicate repo entries** can cause conflicts; check with:
  ```bash
  grep -R "packages.twingate.com" /etc/apt/sources.list /etc/apt/sources.list.d/ 2>/dev/null
  ```
  Remove or reconcile any duplicate/conflicting entries found

## Related Docs
- Twingate Linux Connector installation documentation (see help.twingate.com for current installer guidance)