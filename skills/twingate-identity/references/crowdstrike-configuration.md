# CrowdStrike Configuration

## Page Title
CrowdStrike Configuration (Twingate Device Security Integration)

## Summary
Twingate integrates with CrowdStrike Falcon to verify device security posture as a condition for accessing private resources. The integration uses the CrowdStrike API to validate devices against a customer tenant and incorporates verification into Security Policy Trusted Profiles. Requires Business or Enterprise plan.

## Key Information
- CrowdStrike verification can be required for Twingate sign-in or per-resource access via Security Policies
- Twingate checks the CrowdStrike Agent ID or ZTA file on the device for the unique device identifier
- Supports macOS, Windows, and Linux (Linux requires client version 2024.018+)
- Initial sync after setup takes up to 10 minutes

## Prerequisites
- Twingate Business or Enterprise plan
- CrowdStrike Falcon Zero Trust Assessment (ZTA) feature enabled on your Falcon CID (must be requested from CrowdStrike Support)
- Verify ZTA is active by confirming the data.zta file exists and is non-empty:
  - **Windows:** `%ProgramData%\CrowdStrike\ZeroTrustAssessment\data.zta`
  - **macOS:** `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/data.zta`

## Step-by-Step

1. **Generate CrowdStrike API client** in Falcon platform with these scopes:
   - `Hosts: Read`
   - `Zero Trust Assessment: Read`
   - Save the API Client ID, API Client Secret, and Base URL

2. In Twingate, go to **Settings → Device Settings**

3. Click **Connect** next to CrowdStrike; input:
   - API Client ID
   - API Client Secret
   - Base URL (your CrowdStrike tenant URL)

4. Confirm integration status on the Device Settings page

5. Create a **Trusted Profile** in Device Security requiring CrowdStrike as a Trust Method

6. Add the Trusted Profile to a **Security Policy**

## Configuration Values
| Parameter | Source |
|---|---|
| API Client ID | CrowdStrike Falcon API client |
| API Client Secret | CrowdStrike Falcon API client |
| Base URL | CrowdStrike tenant URL |

**Required API Scopes:** `Hosts: Read`, `Zero Trust Assessment: Read`

## Gotchas
- ZTA feature is **not enabled by default**; must contact CrowdStrike Support to enable it on your CID
- Without ZTA enabled, ZTA scores won't be deployed and Twingate cannot assess posture
- Initial sync delay of up to 10 minutes after configuration; devices may show incorrect state during this period
- **Recoverable errors** (API unresponsive): auto-resolves when API becomes available; shows last successful sync time
- **Unrecoverable errors** (API client deleted or permissions changed): integration halts, admin email notification sent, requires full reconfiguration with new API credentials

## Related Docs
- Device Security Trusted Profiles
- Security Policies
- Twingate Pricing Page (plan requirements)