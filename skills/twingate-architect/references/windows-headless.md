## Windows Headless Mode

Runs the Twingate Windows Client as a background service authenticated by a Service Key, without user interaction. Installation via command-line installer; service managed through Windows Services.

**Key Information:**
- Requires a Service Key from a configured Service Account
- GUI installer does not support headless mode -- must use command-line installer
- Service does not start automatically by default -- configure startup type in Windows Services
- Service Key is securely stored by the Client after installation; original file can be removed
- Logs: `C:\ProgramData\Twingate\logs`
- Optional config: `C:\Program Files\Twingate\headless.conf`

**Installation:**
```powershell
# Silent install
TwingateWindowsInstaller.exe service_secret=C:\path	o\service_key.json /qn

# With debug logging
TwingateWindowsInstaller.exe service_secret=C:\path	o\service_key.json log_level=debug /qn
```

**Key Rotation:**
```powershell
# Option 1 via sc
sc stop twingate.service
sc start twingate.service --config --service_secret C:\path	o\service\secret.json

# Option 2: re-run installer
TwingateWindowsInstaller.exe service_secret=C:\path	o
ew\service_key.json

# Delete stored key
sc start twingate.service --config --reset
```

**Gotchas:**
- A valid Service Key is required for upgrades and reinstalls -- have it available before running the installer
- If previously installed without a Service Key, `sc` cannot add one; perform a fresh install with `service_secret`
- Service must be restarted for any configuration changes to take effect

**Related Docs:**
- /docs/services -- Service Account and Service Key creation
- /docs/linux-headless -- Linux equivalent
