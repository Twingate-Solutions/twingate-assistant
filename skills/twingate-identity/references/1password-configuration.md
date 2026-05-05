## 1Password XAM (Device Trust) Configuration

Integrate 1Password Extended Access Management (XAM) Device Trust with Twingate -- gates Twingate access on 1Password's device verification.

**Plan Requirement:**
- **Business or Enterprise** Twingate plans only
- Customer must have 1Password XAM Device Trust subscription

### How It Works

- Twingate matches **device serial numbers** returned by the Twingate Client against the device list managed by 1Password
- Device is considered **1Password-verified** when:
  1. Its serial number is in 1Password Device Trust's managed list
  2. The device passes 1Password Device Trust's device checks (its `auth_state` is not `blocked`)

### Setup -- Three Steps

**Step 1: Generate a 1Password Device Trust API Key**

In the 1Password Device Trust Console:
- Click your user account (upper right) -> **Settings**
- Left panel -> **Developers**
- **Create New Key** -> name it -> Save
- **No special write permissions** are required -- read-only is sufficient

**Step 2: Configure in Twingate Admin Console**

- **Settings -> Device Integrations**
- Click **Connect** next to 1Password
- Paste the API Key
- Save

The Device Integrations page shows the current sync status.

**Step 3: Add to Trusted Profiles**

- Navigate to Device Security -> Trusted Profiles
- Create or edit a Trusted Profile (macOS / Windows / Linux supported)
- Add **1Password Device Trust** as a Trust Method
- Now only devices verified by 1Password Device Trust satisfy this Profile
- Apply the Profile via Resource Policies that require Trusted Devices

### Troubleshooting

**"Waiting to sync" status:**
- Initial sync takes a few minutes -- normal
- Devices may show wrong verification state during this window

**"1Password not verified":**
- Device is not managed by 1Password, OR
- Device's `auth_state` in 1Password is `blocked`

**Persistent sync failures:**
- Twingate retries for **28 hours** before giving up
- Recoverable errors (1Password API briefly down) auto-resolve
- After 28 hours: integration stops; admin gets an email
- Recovery: regenerate API key, reconfigure integration

### Decision Notes

- Use 1Password Device Trust if your org already uses 1Password for password management + device security -- consolidates vendor footprint
- For mixed environments: 1Password Trust can be one of multiple Trust Methods in a Trusted Profile (e.g., 1Password OR CrowdStrike)
- Read-only API key keeps blast radius small -- always use minimum permissions

### Gotchas

- Initial sync is slow (a few minutes) -- don't expect immediate verification
- 28-hour failure window means sync issues can silently degrade access for a full day -- monitor email alerts
- Devices not managed by 1Password silently fail verification -- ensure 1Password device enrollment is thorough before relying on this for access gating

### Related Docs

- /docs/device-security-guide -- Trusted Profiles + Device Security
- /docs/trusted-devices -- Trusted Device policy rule
- /docs/managed-devices -- Other Trust Method integrations
- /docs/crowdstrike-configuration, /docs/sentinelone-configuration -- Alternative EDR Trust Methods
