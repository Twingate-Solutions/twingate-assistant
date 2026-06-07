# CrowdStrike Configuration

## Page Title
CrowdStrike Configuration (Twingate Integration)

## Summary
Twingate integrates with CrowdStrike Falcon to verify device security posture as part of Device Security Trusted Profiles and Security Policies. The integration uses the CrowdStrike API to validate that devices are managed under the customer's tenant. Available on Business and Enterprise plans only.

## Key Information
- Integration verifies devices via CrowdStrike Agent ID or ZTA file on the endpoint
- CrowdStrike-verified devices can be required for resource access via Security Policies
- Linux support requires Twingate client version 2024.018+
- Initial sync takes up to 10 minutes after setup

## Prerequisites
- Twingate Business or Enterprise plan
- CrowdStrike Falcon Zero Trust Assessment (ZTA) feature must be enabled on your Falcon CID (contact CrowdStrike Support to enable)
- Verify ZTA is active by checking for non-empty `data.zta` file:
  - **Windows:** `%ProgramData%\CrowdStrike\ZeroTrustAssessment\data.zta`
  - **macOS:** `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/data.zta`

## Step-by-Step

1. **Generate CrowdStrike API client** in the Falcon platform with these scopes:
   - `Hosts: Read`
   - `Zero Trust Assessment: Read`
   - Save the **API Client ID**, **API Client Secret**, and **Base URL**

2. In Twingate, go to **Settings → Device Settings**

3. Click **Connect** next to CrowdStrike and input:
   - API Client ID
   - API Client Secret
   - Base URL (your CrowdStrike tenant URL)

4. Confirm integration status on the Device Settings page

5. Create a **Trusted Profile** under Device Security, requiring CrowdStrike as a Trust Method (supports macOS, Windows, Linux)

6. Incorporate the Trusted Profile into **Security Policies**

## Configuration Values
| Parameter | Source |
|---|---|
| API Client ID | Generated in CrowdStrike Falcon |
| API Client Secret | Generated in CrowdStrike Falcon |
| Base URL | Your CrowdStrike tenant base URL |

## Gotchas
- ZTA feature is **not enabled by default** — must be explicitly requested from CrowdStrike Support
- Initial sync delay of up to **10 minutes**; devices show "Waiting to sync" during this period
- **Recoverable errors** (API unresponsive): auto-resolves when API becomes reachable; last successful sync time is displayed
- **Unrecoverable errors** (API client deleted, permissions changed): integration stops retrying; admin email notification sent; requires full reconfiguration with new API credentials
- Without ZTA enabled, ZTA score won't exist on devices and Twingate cannot assess posture

## Related Docs
- Device Security Trusted Profiles
- Security Policies
- Twingate Pricing Page