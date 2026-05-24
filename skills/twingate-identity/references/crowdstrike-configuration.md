# CrowdStrike Configuration

## Page Title
CrowdStrike Configuration (Twingate Device Security Integration)

## Summary
Twingate integrates with CrowdStrike Falcon to verify device security posture as a requirement for accessing private resources. The integration uses CrowdStrike's API to validate managed devices and can be incorporated into Security Policies via Trusted Profiles. Requires Business or Enterprise plan.

## Key Information
- Integration validates devices against CrowdStrike-managed tenant via API
- Twingate client reads either the CrowdStrike Agent ID or ZTA file on the device
- Supports macOS, Windows, and Linux (Linux requires client v2024.018+)
- Initial sync after setup takes up to 10 minutes

## Prerequisites
- Twingate Business or Enterprise plan
- CrowdStrike Falcon Zero Trust Assessment (ZTA) feature must be enabled by CrowdStrike Support for your CID
- Verify ZTA is active by confirming file exists and is non-empty:
  - **Windows:** `%ProgramData%\CrowdStrike\ZeroTrustAssessment\data.zta`
  - **macOS:** `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/data.zta`

## Step-by-Step

1. **CrowdStrike Falcon Console:** Create a new API client with these scopes:
   - `Hosts: Read`
   - `Zero Trust Assessment: Read`
   - Save the **API Client ID**, **API Client Secret**, and **Base URL**

2. **Twingate Admin:** Navigate to **Settings → Device Settings**

3. Click **Connect** next to CrowdStrike; input API Client ID, API Client Secret, and Base URL

4. Confirm integration status on the Device Settings page

5. Create a **Trusted Profile** requiring CrowdStrike as a Trust Method

6. Incorporate the Trusted Profile into a **Security Policy**

## Configuration Values
| Field | Description |
|-------|-------------|
| API Client ID | From CrowdStrike Falcon API client |
| API Client Secret | From CrowdStrike Falcon API client |
| Base URL | CrowdStrike tenant base URL |

**Required API Scopes:**
- `Hosts: Read`
- `Zero Trust Assessment: Read`

## Gotchas
- ZTA feature is **not enabled by default**—must be explicitly requested from CrowdStrike Support
- Initial sync delay: up to **10 minutes** before devices show correct verification state
- **Recoverable errors** (API unresponsive): integration auto-retries; last successful sync time is displayed
- **Unrecoverable errors** (API client deleted/permissions changed): sync stops entirely, admin email notification sent, requires full reconfiguration with new API credentials
- ZTA file must be **non-zero size**; a 0KB file indicates ZTA is not properly enabled

## Related Docs
- [Device Security Trusted Profiles](https://www.twingate.com/docs/device-security-trusted-profiles) (referenced inline)
- Twingate Pricing Page (for plan eligibility)