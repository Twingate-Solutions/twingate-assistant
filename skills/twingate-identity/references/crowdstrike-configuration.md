# CrowdStrike Configuration

## Page Title
CrowdStrike Configuration (Twingate Device Security Integration)

## Summary
Twingate integrates with CrowdStrike Falcon to verify device security posture as a condition for accessing private resources. The integration uses CrowdStrike's API to match managed devices against Twingate clients, incorporating ZTA scores into Security Policy enforcement.

## Key Information
- Available on **Business and Enterprise plans only**
- Supports **macOS, Windows, and Linux** (Linux requires client version 2024.018+)
- CrowdStrike Zero Trust Assessment (ZTA) must be pre-enabled by CrowdStrike Support on your Falcon CID
- Initial sync after setup takes **up to 10 minutes**

## Prerequisites
- CrowdStrike Falcon Zero Trust Assessment feature enabled (contact CrowdStrike Support)
- Verify ZTA is active by confirming non-empty file exists:
  - Windows: `%ProgramData%\CrowdStrike\ZeroTrustAssessment\data.zta`
  - macOS: `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/data.zta`
- CrowdStrike API client with required scopes

## Step-by-Step Configuration

1. **Generate CrowdStrike API client** in Falcon platform with these scopes:
   - `Hosts: Read`
   - `Zero Trust Assessment: Read`
2. Save the **API Client ID**, **API Client Secret**, and **Base URL**
3. In Twingate: **Settings → Device Settings → Connect (CrowdStrike)**
4. Input API Client ID, API Client Secret, and Base URL
5. Verify integration status on Device Settings page
6. Create a **Trusted Profile** requiring CrowdStrike as a Trust Method
7. Incorporate the Trusted Profile into **Security Policies**

## Configuration Values
| Parameter | Source |
|-----------|--------|
| API Client ID | CrowdStrike Falcon API client creation |
| API Client Secret | CrowdStrike Falcon API client creation |
| Base URL | CrowdStrike tenant URL |

## Gotchas
- **ZTA must be explicitly enabled by CrowdStrike Support** — not self-service; integration will silently fail without it
- Devices show incorrect verification state during the initial 10-minute sync window ("Waiting to sync")
- **Recoverable errors** (API unresponsive): auto-resolves when API is reachable; last successful sync time displayed
- **Unrecoverable errors** (deleted client, altered permissions): integration stops retrying; admin email notification sent; requires full reconfiguration with new API credentials

## Related Docs
- Device Security Trusted Profiles
- Security Policies
- Twingate Pricing (plan eligibility)