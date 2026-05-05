## Kandji Configuration (Trust Method)

Integrate Kandji with Twingate -- gates Twingate access on Kandji-managed macOS device verification.

**Plan Requirement:**
- **Business or Enterprise** Twingate plans only

### How It Works

- Twingate uses the Kandji API to pull the list of Kandji-managed devices
- Twingate Client returns device serial number; matched against Kandji's list
- A device is **Kandji-verified** when ALL of:
  - Its serial is in Kandji's managed list
  - It has reported to Kandji **within the last 7 days**
  - Kandji agent is installed
  - MDM profile is installed
  - Device has not been removed from Kandji

### Supported Platforms

- **macOS only**

### Setup

**Stage 1: Generate Kandji API Token**

1. Kandji web app -> **Settings** (left panel)
2. Click **Access** in the top bar
3. Scroll to **API Token** -> **Add Token**
4. Set Name + Description
5. Save the **API token**

**Stage 2: Configure API Token Permissions**
- "Manage API Permissions" modal -> **Configure**
- Under **Devices**, enable:
  - **Device details**
  - **Device list**

**Stage 3: Connect in Twingate**
1. Twingate Admin Console -> **Settings -> Device Integration**
2. Click **Connect** next to Kandji
3. Enter the **Kandji URL** in the format:
   - US: `<subdomain>.api.kandji.io`
   - EU: `<subdomain>.api.eu.kandji.io`
4. Enter the API token
5. Save

Device Settings page shows current sync status.

### Add to Trusted Profiles

- Device Security -> Trusted Profiles
- Create/edit a Trusted Profile for **macOS**
- Add **Kandji** as a Trust Method
- Apply via Resource Policies requiring Trusted Devices

### Troubleshooting

**"Waiting to sync"**: initial sync takes a few minutes; devices may show wrong state until completion

**"Kandji not verified"** reasons:
- Device not managed by Kandji
- Hasn't reported in 7+ days
- Kandji agent uninstalled
- MDM profile missing
- Device removed from Kandji

**Recoverable errors**: shows last success + last failure; auto-resolves when API recovers

**Unrecoverable errors** (credentials revoked, permissions altered): integration stops; admins emailed. Recovery: regenerate API token, reconfigure.

### Decision Notes

- Kandji is the right Trust Method for **all-Apple orgs** that prefer Kandji over Jamf -- often newer, simpler operations than Jamf Pro
- The Kandji **Auto App** also exists (see /docs/kandji-mdm) for distributing the Twingate Client itself; that's a different integration
- Use minimum API permissions (Device details + Device list) -- Kandji has many other API scopes that aren't needed
- The 5 verification requirements are all-or-nothing -- a device losing its MDM profile is enough to fail verification, even if everything else is fine

### Gotchas

- Kandji URL format with EU vs. US suffix is easy to get wrong -- verify your tenant's region
- API token doesn't auto-expire (per Kandji), but rotate periodically as a hygiene practice
- Removed-from-Kandji devices fail verification immediately -- don't remove devices from Kandji during routine deprovisioning until Twingate access is also revoked

### Related Docs

- /docs/device-security-guide -- Trusted Profiles model
- /docs/trusted-devices -- Trusted Devices policy rule
- /docs/kandji-mdm -- Deploying the Twingate Client via Kandji (different doc -- Client distribution)
- /docs/jamf-configuration -- Jamf as alternative macOS Trust Method
- /docs/managed-devices -- Trust Methods overview
