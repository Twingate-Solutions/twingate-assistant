## Intune Configuration (Trust Method)

Integrate Microsoft Intune with Twingate -- gates Twingate access on Intune compliance state.

**Plan Requirement:**
- **Business or Enterprise** Twingate plans only

### How It Works

- Twingate uses the Intune API (Microsoft Graph) to pull the list of Intune-managed devices
- Twingate Client returns the device's serial number; Twingate matches it against Intune's list
- A device is **Intune-verified** when ALL of:
  - Its serial is in Intune's managed list
  - It has reported to Intune **within the last 7 days**
  - Intune classifies it as **Compliant** OR **In-grace period**

### Setup -- Two Stages

**Stage 1: Generate Azure App Credentials**

In the Azure portal:

1. **Azure Active Directory -> App registrations -> New registration**
2. **API permissions** tab -> Add permissions:
   - **Microsoft Graph -> Delegated permissions -> `DeviceManagementManagedDevices.Read.All`**
   - **Microsoft Graph -> Application permissions -> `DeviceManagementManagedDevices.Read.All`**
3. Click **Grant admin consent for...**
4. **Overview** tab -> **Client credentials** -> **New client secret**
   - **Save the Value immediately** -- it's not retrievable later
5. Save the **Application (client) ID** and **Directory (tenant) ID**

**Stage 2: Connect in Twingate**

1. Twingate Admin Console -> **Settings -> Device Integration**
2. Click **Connect** next to Intune
3. Enter:
   - Application (client) ID
   - Client Secret (Value)
   - Directory (tenant) ID
4. Save

The Device Settings page shows current sync status.

### Add to Trusted Profiles

- Device Security -> Trusted Profiles
- Create/edit a Trusted Profile (macOS or Windows -- iOS/Android not yet supported for Intune Trust Method)
- Add **Intune** as a Trust Method
- Apply via Resource Policies that require Trusted Devices

### Troubleshooting

**"Waiting to sync":**
- Initial sync takes a few minutes -- normal
- Devices may show wrong state during this window

**Device shows "Intune not verified":**
- Not managed by Intune
- Compliance State is not Compliant or In-grace period
- Device hasn't reported to Intune in 7+ days
- Twingate couldn't read the serial number from the device
- Twingate couldn't fetch Intune data for the device

**Recoverable errors** (Intune API down, transient): show "failed to sync" + last success timestamp; auto-resolve when API recovers.

**Unrecoverable errors** (credentials revoked, permissions stripped): integration stops; admins emailed. Recovery: regenerate Azure credentials, reconfigure Twingate integration.

### Decision Notes

- Use Intune if you're on Microsoft 365 / Entra ID for identity -- consolidates vendor footprint
- For multi-platform fleets: Intune handles Windows + macOS; for Linux/iOS/Android, pair with another Trust Method
- The 7-day reporting window means devices that go offline for vacation/extended off-hours may temporarily lose access -- communicate this to users

### Gotchas

- App permissions require **both Delegated AND Application** scopes for `DeviceManagementManagedDevices.Read.All`
- Admin consent is required after granting -- forget this step and the integration fails silently
- Client secret expires per Azure's policy -- set a calendar reminder to rotate before expiry
- Devices in non-Compliant state are blocked even if they're in the managed list -- review your Intune compliance policies

### Related Docs

- /docs/device-security-guide -- Trusted Profiles model
- /docs/trusted-devices -- Trusted Devices policy rule
- /docs/managed-devices -- Other Trust Methods (sibling integrations)
- /docs/jamf-configuration, /docs/kandji-configuration, /docs/crowdstrike-configuration, /docs/sentinelone-configuration -- Alternative MDM/EDR Trust Methods
