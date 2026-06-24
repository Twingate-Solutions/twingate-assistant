# CrowdStrike Configuration

## Page Title
CrowdStrike Configuration (Twingate Integration)

## Summary
Twingate integrates with CrowdStrike Falcon to verify device security posture as a condition for accessing private resources. The integration uses the CrowdStrike API to validate that devices are managed under the customer's tenant. Verified devices can satisfy Trusted Profile requirements within Security Policies.

## Key Information
- **Plan requirement**: Business & Enterprise only
- **CrowdStrike prerequisite**: Zero Trust Assessment (ZTA) feature must be enabled on the Falcon CID — requires contacting CrowdStrike Support directly
- **Supported OS**: macOS, Windows, Linux (Linux requires Twingate client v2024.018+)
- **Sync delay**: Up to 10 minutes for initial sync after configuration

## Prerequisites
- CrowdStrike Falcon Zero Trust Assessment feature enabled on your CID
- Verify ZTA is active by confirming the file exists and is not empty (not 0KB):
  - **Windows**: `%ProgramData%\CrowdStrike\ZeroTrustAssessment\data.zta`
  - **macOS**: `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/data.zta`

## Step-by-Step Configuration

1. **Generate CrowdStrike API client** in Falcon platform with these scopes:
   - `Hosts: Read`
   - `Zero Trust Assessment: Read`
   - Save the **API Client ID**, **API Client Secret**, and **Base URL**

2. In Twingate, go to **Settings → Device Settings**

3. Click **Connect** next to CrowdStrike; enter:
   - API Client ID
   - API Client Secret
   - Base URL (your CrowdStrike tenant URL)

4. Confirm integration status on Device Settings page

5. Create a **Trusted Profile** requiring CrowdStrike as a Trust Method, then incorporate into Security Policies

## Configuration Values
| Parameter | Description |
|---|---|
| `API Client ID` | From CrowdStrike Falcon API client |
| `API Client Secret` | From CrowdStrike Falcon API client |
| `Base URL` | CrowdStrike tenant base URL |

## Gotchas
- ZTA feature is **not enabled by default** — must be explicitly requested from CrowdStrike Support
- Initial sync takes up to **10 minutes**; devices may show incorrect state during this window
- **Recoverable errors** (API unresponsive): Integration shows last successful sync time; auto-resolves when API is reachable
- **Unrecoverable errors** (API client deleted, permissions changed): Integration stops retrying; admin email notification sent — requires full reconfiguration with new API credentials
- Linux support requires Twingate client version 2024.018 or later

## Related Docs
- [Device Security Trusted Profiles](https://www.twingate.com/docs/device-security-trusted-profiles)
- [Security Policies](https://www.twingate.com/docs/security-policies)
- [Twingate Pricing](https://www.twingate.com/pricing)