## Deploying Twingate Clients with Jamf

How to distribute the Twingate macOS and iOS Clients via Jamf -- including a Configuration Profile for fully silent macOS deployment.

**macOS Distribution:**
- Deploy as a **package** (PKG) via Jamf
- Download the latest .pkg from the Twingate download page
- Standard Jamf Computers > Packages workflow

**iOS Distribution:**
- Add Twingate Client to **Apple Business Manager** first
- Link Jamf to ABM (per Jamf's official docs)
- Then distribute the iOS app from Jamf

**Pre-Migration Step (Important):**
- If end users have manually installed Twingate previously, **uninstall those Clients first** via a temporary Jamf policy
- Why: manually-installed Clients may not match the MDM-distributed version, causing config drift and update conflicts
- Deactivate the cleanup policy before rolling out the MDM-managed Client

### Silent macOS Deployment -- Configuration Profile Recipe

**Preference Domain:** `com.twingate.macos`

**Custom JSON Schema Properties:**
- `PresentedDataPrivacy` (boolean) -- skip data privacy screen
- `PresentedEducation` (boolean) -- skip education screen
- `automaticallyInstallSystemExtension` (boolean) -- auto-install the network extension
- `network` (string) -- pre-populate Twingate tenant subdomain
- `LaunchApp` (boolean) -- start at login (set **false** if also deploying the Twingate Launch Agent)
- `SUEnableAutomaticChecks` (boolean) -- auto-check for updates
- `SUAutomaticallyUpdate` (boolean) -- auto-download and apply updates

**Recommended Values for Silent Install (Jamf manages updates):**
```
Suppress Data Privacy Screen:        true
Suppress Education Screen:           true
Install System Extension:            true
Define Twingate Network:             <your-tenant-subdomain>
Start At Login:                      false
Enable Automatic Update Checks:      false
Enable Automatic Updates:            false
```

**Required Adjacent Settings in the Profile:**

**Managed Login Items:** add Team Identifier `6GX8KVTR9H`

**Notifications:** add an entry with App Name `Twingate`, Bundle ID `com.twingate.macos`, ensure Notifications **Enabled**

**System Extensions** (Configure):
- System Extension Types: **Allowed system extensions**
- Team Identifier: `6GX8KVTR9H`
- Allowed System Extension: `com.twingate.macos.tunnelprovider`

**System Extensions (macOS 15 Sequoia +):** add a second entry
- System Extension Types: **Non-removable system extensions from UI**
- Team Identifier: `6GX8KVTR9H`
- Non-removable: `com.twingate.macos.tunnelprovider`
- (Harmless on earlier macOS versions; just doesn't apply)

**VPN** (Configure):
- Connection Name: `Twingate`
- VPN Type: `VPN`
- Connection Type: `Custom SSL`
- Identifier: `com.twingate.macos`
- Server: `null` (any value -- the field is required but unused)
- Provider Bundle Identifier: `com.twingate.macos.tunnelprovider`
- Provider Designated Requirement (paste exactly):
  ```
  anchor apple generic and identifier "com.twingate.macos.tunnelprovider" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = "6GX8KVTR9H")
  ```
- Optionally tick **Prohibit users from disabling on-demand VPN settings**

**Always Scope to a test group first**, then expand to all devices.

### Updating the Client via Jamf

1. Download the new .pkg from Twingate's site
2. Upload as a new Jamf package (same priority as the previous package)
3. Edit the existing Jamf policy: remove the old package, add the new one
4. Test on a device by manually triggering the policy and reviewing logs
5. Flush the policy on test devices; let it re-run per its triggers to update the fleet

**Gotchas:**
- Without the Configuration Profile, the Client install will prompt the user to allow the network extension -- not silent
- VPN profile's Provider Designated Requirement must match exactly (whitespace included) -- typos cause silent failures
- Macs upgraded to Sequoia (15+) without the "Non-removable system extensions from UI" entry will let users disable the extension via System Settings

**Related Docs:**
- /docs/macos-and-ios -- All Client preference keys
- /docs/kandji-mdm, /docs/intune-configuration, /docs/omnissa-workspace-one-mdm -- Other MDM equivalents
