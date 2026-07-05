# CrowdStrike Configuration

## Page Title
CrowdStrike Configuration (Twingate Device Security Integration)

## Summary
Twingate integrates with CrowdStrike Falcon to enforce device trust verification as a requirement for accessing private resources. The integration uses CrowdStrike's API to validate that devices are managed under the customer's tenant. CrowdStrike status can be incorporated into Security Policies via Device Security Trusted Profiles.

## Key Information
- **Plan requirement**: Business & Enterprise only
- **CrowdStrike prerequisite**: Zero Trust Assessment (ZTA) feature must be explicitly enabled by CrowdStrike Support on your Falcon CID
- **Platform support**: macOS, Windows, Linux (Linux requires Twingate client v2024.018+)
- **Initial sync delay**: Up to 10 minutes after setup; devices show "Waiting to sync" during this period
- **Sync verification files**:
  - Windows: `%ProgramData%\CrowdStrike\ZeroTrustAssessment\data.zta`
  - macOS: `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/data.zta`

## Prerequisites
- Twingate Business or Enterprise plan
- CrowdStrike Falcon with ZTA feature enabled (contact CrowdStrike Support)
- ZTA file present and non-empty (non-0KB) on endpoint devices
- CrowdStrike API credentials with correct scopes

## Step-by-Step

1. **Generate CrowdStrike API client** in Falcon platform with these scopes:
   - `Hosts: Read`
   - `Zero Trust Assessment: Read`
2. Copy **API Client ID**, **API Client Secret**, and **Base URL**
3. In Twingate: **Settings → Device Settings → Connect** (next to CrowdStrike)
4. Enter API Client ID, API Client Secret, and Base URL
5. Confirm integration status on Device Settings page
6. Create a **Trusted Profile** requiring CrowdStrike as a Trust Method
7. Incorporate the Trusted Profile into a **Security Policy**

## Configuration Values

| Field | Description |
|-------|-------------|
| API Client ID | From CrowdStrike Falcon API client |
| API Client Secret | From CrowdStrike Falcon API client |
| Base URL | CrowdStrike tenant base URL |

**Required API Scopes**: `Hosts: Read`, `Zero Trust Assessment: Read`

## Gotchas
- ZTA feature is **not enabled by default**—must be requested from CrowdStrike Support separately
- Without ZTA enabled, the `.zta` file won't exist and integration will fail silently
- **Recoverable errors** (API unresponsive): auto-resolves when API becomes reachable; last successful sync time is shown
- **Unrecoverable errors** (API client deleted, permissions changed): integration stops retrying; admin email notification sent; requires full reconfiguration with new API credentials
- Linux support requires Twingate client v2024.018 or newer

## Related Docs
- [Device Security Trusted Profiles](https://www.twingate.com/docs/device-security-trusted-profiles)
- Twingate Pricing Page (for plan eligibility)