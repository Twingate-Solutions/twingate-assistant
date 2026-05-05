## CrowdStrike Configuration

Integrate CrowdStrike Falcon with Twingate -- gates Twingate access on CrowdStrike's Zero Trust Assessment (ZTA) of the device.

**Plan Requirement:**
- **Business or Enterprise** Twingate plans only

### Mandatory Prerequisite: ZTA Feature Enabled

The CrowdStrike Falcon **Zero Trust Assessment (ZTA)** feature must be enabled, and your CID must be shared with CrowdStrike Support.

**Without ZTA enabled, the integration cannot work** -- the ZTA file won't be deployed to devices.

**To enable**: contact CrowdStrike customer support directly to enable ZTA on your Falcon CID.

**Verify on a test device** (file should exist and be > 0 KB):
- Windows: `%ProgramData%\CrowdStrike\ZeroTrustAssessment\data.zta`
- macOS: `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/data.zta`

### How It Works

- Twingate uses CrowdStrike's API to pull the list of CrowdStrike-managed devices
- The Twingate Client reads the **CrowdStrike Agent ID** OR the local **ZTA file** on the device
- Cross-checks: is this device in the CrowdStrike-managed list AND does its ZTA file pass validity checks?
- If both pass: device is considered **CrowdStrike-verified** in Twingate

### Setup -- Four Steps

**Step 1: Generate a CrowdStrike API Client Token**

In the CrowdStrike Falcon platform:
- Required scopes:
  - **Hosts: Read**
  - **Zero Trust Assessment: Read**
- Save the **API Client ID** and **API Client Secret**

**Step 2: Configure in Twingate Admin Console**

- **Settings -> Device Settings**
- Click **Connect** next to CrowdStrike
- Enter:
  - API Client ID
  - API Client Secret
  - **Base URL** for your CrowdStrike tenant (e.g., `api.crowdstrike.com`, `api.us-2.crowdstrike.com`, `api.eu-1.crowdstrike.com`)

**Step 3: Wait for Initial Sync**

- Up to **10 minutes** for the first sync
- During this window, Device Settings shows "Waiting to sync"
- Devices may show wrong verification state until sync completes

**Step 4: Add to Trusted Profiles**

- Device Security -> Trusted Profiles
- Create/edit a Trusted Profile (macOS / Windows / Linux)
- Linux requires Twingate Client **2024.018+**
- Add **CrowdStrike** as a Trust Method
- Apply via Resource Policies that require Trusted Devices

### Troubleshooting

**Recoverable errors (CrowdStrike API down):**
- Sync state shows last successful + most recent failure timestamps
- Auto-resolves when the API recovers

**Unrecoverable errors (API key deleted, permissions revoked):**
- Twingate stops attempting sync
- Admins notified via email
- Recovery: regenerate API client + reconfigure integration in Twingate

### Decision Notes

- Most prevalent EDR Trust Method in production environments
- Combine with `Hosts: Read` + `Zero Trust Assessment: Read` only -- minimum permissions
- Linux client version 2024.018+ required for Linux device verification -- verify before applying to a Linux fleet
- Use CrowdStrike + native posture checks (encryption, screen lock) together in the Trusted Profile for defense in depth

### Gotchas

- ZTA feature is **not on by default** -- you must explicitly request CrowdStrike Support enable it
- The 10-minute initial sync delay can confuse rollouts -- communicate the wait window
- API client deletion silently breaks the integration until you notice the email -- monitor admin inbox
- Base URL differs by region -- get the exact URL from your CrowdStrike Falcon environment

### Related Docs

- /docs/device-security-guide -- Trusted Profiles + Device Security
- /docs/trusted-devices -- Trusted Device policy rule
- /docs/managed-devices -- Other Trust Method integrations
- /docs/sentinelone-configuration -- Alternative EDR (sibling pattern)
- /docs/1password-configuration -- Device-level Trust Method (sibling)
