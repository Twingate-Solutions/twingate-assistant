## Jamf Configuration (Trust Method)

Integrate Jamf Pro with Twingate -- gates Twingate access on Jamf-managed device verification.

**Plan Requirement:**
- **Business or Enterprise** Twingate plans only

### How It Works

- Twingate uses the Jamf API to pull the list of Jamf-managed devices
- Twingate Client returns the device serial number; matched against Jamf's list
- A device is **Jamf-verified** when:
  - Its serial is in Jamf's managed list
  - It has reported to Jamf **within the last 7 days**

### Supported Platforms

- **macOS only** -- Jamf Pro is Apple-focused
- For Windows / Linux fleets: pair with another Trust Method (CrowdStrike, Intune, SentinelOne)

### Setup

**Stage 1: Get Jamf API Credentials**
- Use Jamf admin user credentials with API access
- This user should have admin capabilities

**Stage 2: Connect in Twingate**
1. Twingate Admin Console -> **Settings -> Device Integration**
2. Click **Connect** next to Jamf
3. Enter Jamf credentials
4. Save

Device Settings page shows current sync status.

### Add to Trusted Profiles

- Device Security -> Trusted Profiles
- Create/edit a Trusted Profile for **macOS**
- Add **Jamf** as a Trust Method
- Apply via Resource Policies requiring Trusted Devices

### Troubleshooting

**Initial sync**: up to **10 minutes** -- be patient

**Sync errors:**
- **Recoverable** (Jamf API briefly down): shows last success + most recent failure timestamps; auto-resolves
- **Unrecoverable** (credentials invalid/deleted, permissions altered): integration stops; admins emailed. Recovery: regenerate API credentials, reconfigure in Twingate

### Decision Notes

- Jamf is the right Trust Method for **Apple-heavy orgs** that already use Jamf Pro
- For mixed Apple+Windows fleets: combine Jamf (macOS) + Intune (Windows) in separate Trusted Profiles
- The 7-day reporting window: devices off for vacation may temporarily lose access -- communicate to users
- Use a **dedicated Jamf admin account** for the integration (not a person's account) -- avoids breakage when employees leave

### Gotchas

- The 10-minute initial sync delay can confuse rollouts -- communicate the wait window
- Jamf credential rotation breaks the integration silently until you reconfigure -- monitor admin email
- Jamf only supports macOS in Twingate -- don't try to add it to a Windows Trusted Profile (it won't satisfy the requirement)

### Related Docs

- /docs/device-security-guide -- Trusted Profiles model
- /docs/trusted-devices -- Trusted Devices policy rule
- /docs/jamf-mdm -- Deploying the Twingate Client via Jamf (different doc -- Client distribution, not device verification)
- /docs/kandji-configuration -- Kandji as alternative macOS Trust Method
- /docs/intune-configuration -- Intune for cross-platform
- /docs/managed-devices -- Trust Methods overview
