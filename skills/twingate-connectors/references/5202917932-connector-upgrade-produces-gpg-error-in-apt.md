---
source: https://help.twingate.com/articles/5202917932-connector-upgrade-produces-gpg-error-in-apt
type: help
fetched: 2026-09-27
source_version: c3d69aefe6cf48a5ffe77d92a641ceff5bf8b8d9a753301a56f5c21c0d897703
---

# Connector Upgrade Produces GPG Error in APT

## Summary
When upgrading Twingate Connector on Ubuntu/Debian via APT, a GPG signature verification error may occur due to outdated repository configuration or missing signing key. The fix involves installing the current Twingate GPG key into a dedicated keyring and updating the repository source entry to use `signed-by`.

## Key Information
- Affects: Ubuntu/Debian systems with older Twingate APT installations
- Error signature: `NO_PUBKEY 5C363F09A9174A9E`
- Current config uses `/usr/share/keyrings/twingate-client-keyring.gpg` + `signed-by` option
- Older workaround used `trusted=true` — no longer required or recommended

## Prerequisites
- `curl`, `gpg`, `ca-certificates` installed
- `sudo` access

## Step-by-Step Resolution

**1. Install required utilities**
```bash
sudo apt install -y curl gpg ca-certificates
```

**2. Install/replace the signing key**
```bash
curl -fsSL https://packages.twingate.com/apt/gpg.key \
  | sudo gpg --dearmor -o /usr/share/keyrings/twingate-client-keyring.gpg
```
Confirm replacement if prompted.

**3. Update repository configuration**
```bash
echo "deb [signed-by=/usr/share/keyrings/twingate-client-keyring.gpg] https://packages.twingate.com/apt/ * *" \
  | sudo tee /etc/apt/sources.list.d/twingate.list
```

**4. Refresh APT**
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
- Do **not** use `trusted=true` in the repo entry — older docs suggested this as a workaround but it bypasses signature verification
- Duplicate/conflicting repo entries will cause issues; check with:
  ```bash
  grep -R "packages.twingate.com" /etc/apt/sources.list /etc/apt/sources.list.d/ 2>/dev/null
  ```
- If multiple entries are found, remove or consolidate them before retrying

## Related Docs
- Twingate Linux Connector installation guide
- APT `signed-by` option documentation