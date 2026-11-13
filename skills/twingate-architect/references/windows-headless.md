---
source: https://www.twingate.com/docs/windows-headless
type: docs
fetched: 2026-11-13
source_version: a3fc6fa8e8f36056007723a7669f973b4e095c35cda7b2519b98a0e04443abd7
trust: official
---

# Windows Headless Mode

## Summary
The Twingate Windows Client can run in headless mode, authenticating with a Service Key instead of an interactive user login. Headless mode is enabled by installing the Client from the command line with the `service_secret` switch pointing to a Service Key file. The Client is then controlled as the `Twingate Service` in Windows Services.

## Key Information
- Headless mode requires a Service Account and Service Key (created in the Twingate Admin Console under Services).
- The existing Windows client EXE installer is used; download it from Twingate's public changelog.
- Installer options can also be set in `headless.conf`.
- The Service Key is stored and managed securely by the Client, so the original file doesn't need to stay in place.
- The Client does **not** start automatically by default; change the Windows service startup settings if you want that.
- Logs are written to `C:\ProgramData\Twingate\logs`.

## Prerequisites
- Service Account and Service Key (JSON file) from the Admin Console
- Windows Client EXE installer
- Administrator permissions (for `sc` commands and installation)

## Step-by-Step
**Install silently in headless mode:**
```
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json /quiet
```
**Install with debug logging:**
```
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json log_level=debug /quiet
```
**Rotate the Service Key (option 1, via sc):**
```
sc stop twingate.service
sc start twingate.service --config --service_secret C:\path\to\service\secret.json
```
**Rotate the Service Key (option 2):** re-run the installer with `service_secret` pointing to the new key.

**Delete the stored Service Key:**
```
sc start twingate.service --config --reset
```
This disconnects the Client; a new key is required to reconnect.

**Upgrade:** re-run the installer with `service_secret` pointing to a valid Service Key.

## Configuration Values
| Option | Required | Description |
|---|---|---|
| `service_secret` | Yes | Path to Service Key file |
| `log_level` | No | Defaults to `info`; levels are documented in `headless.conf` |
| `/quiet` | No | Silent install switch for automated deployment |

- Config file: `C:\Program Files\Twingate\headless.conf`
- Service name: `twingate.service`

## Gotchas
- A valid Service Key is required when updating or reinstalling the Client.
- The service must be restarted for Service Key changes to take effect.
- If the Client was originally installed without a Service Key, you must do a fresh install with `service_secret`; the `sc` command can't add a key in that case.
- `sc` commands need Administrator permissions.
- Deleting the key disconnects the Client from Twingate.

## Related Docs
- Twingate Services documentation (creating Service Accounts and Keys)
- Twingate public changelog (installer downloads)
- Windows Client documentation