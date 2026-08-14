---
source: https://www.twingate.com/docs/crowdstrike-configuration
type: docs
fetched: 2026-08-14
source_version: 3fe5220362c4477ae784a7c8b1ae68efd2f70be4965e4f8a2d88f43c148f36d4
---

# CrowdStrike Configuration

## Page Title
CrowdStrike Configuration (Twingate Device Security Integration)

## Summary
Twingate integrates with CrowdStrike Falcon to verify device security posture as a condition for accessing private resources. The integration uses the CrowdStrike API to validate managed devices against a customer's tenant. Verified devices can be required via Device Security Trusted Profiles and Security Policies.

## Key Information
- **Plan requirement**: Business & Enterprise only
- **CrowdStrike prerequisite**: Zero Trust Assessment (ZTA) feature must be explicitly enabled by CrowdStrike Support for your Falcon CID
- Integration checks either CrowdStrike Agent ID or ZTA file on the device
- Supports macOS, Windows, and Linux (Linux requires Twingate client v2024.018+)
- Initial sync after setup takes up to 10 minutes

## Prerequisites
- Business or Enterprise Twingate plan
- CrowdStrike Falcon Zero Trust Assessment enabled on your CID (contact CrowdStrike Support)
- Verify ZTA feature is active by checking ZTA file exists and is non-empty:
  - **Windows**: `%ProgramData%\CrowdStrike\ZeroTrustAssessment\data.zta`
  - **macOS**: `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/data.zta`

## Step-by-Step Configuration

1. **Generate CrowdStrike API client** in Falcon platform with these scopes:
   - `Hosts: Read`
   - `Zero Trust Assessment: Read`
   - Save the API Client ID and API Client Secret

2. **In Twingate**: Navigate to **Settings → Device Settings**

3. **Click "Connect"** next to CrowdStrike; input:
   - API Client ID
   - API Client Secret
   - Base URL for your CrowdStrike tenant

4. **Verify status** on the Device Settings page

5. **Create a Trusted Profile** requiring CrowdStrike as a Trust Method, then incorporate into Security Policies

## Configuration Values

| Field | Description |
|-------|-------------|
| API Client ID | From CrowdStrike Falcon API client |
| API Client Secret | From CrowdStrike Falcon API client |
| Base URL | Your CrowdStrike tenant base URL |

## Gotchas
- ZTA feature is **not enabled by default**—must be requested from CrowdStrike Support; without it, ZTA scores won't exist on devices
- Initial sync delay of up to 10 minutes after setup; devices may show incorrect state during this window
- **Recoverable errors** (API unresponsive): integration auto-retries; Device Settings shows last successful sync time
- **Unrecoverable errors** (API client deleted or permissions changed): integration stops retrying, admin email notification sent, requires full reconfiguration with new API credentials

## Related Docs
- Device Security Trusted Profiles
- Security Policies
- Twingate Pricing Page (plan requirements)