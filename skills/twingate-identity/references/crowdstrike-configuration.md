---
source: https://www.twingate.com/docs/crowdstrike-configuration
type: docs
fetched: 2026-10-25
source_version: 8096903919e0f5c6b243bdd9f9dd9f36fe6263475a2ae170be5e0ec75acbaad7
trust: official
---

# CrowdStrike Configuration

## Page Title
CrowdStrike Configuration (Twingate Device Security Integration)

## Summary
Twingate integrates with CrowdStrike Falcon to verify device posture as a condition for accessing private resources. The integration uses the CrowdStrike API to match managed devices against Twingate clients, leveraging either the CrowdStrike Agent ID or ZTA file on the endpoint. Once configured, CrowdStrike verification can be enforced via Device Security Trusted Profiles and Security Policies.

## Key Information
- **Plan requirement:** Business & Enterprise only
- **CrowdStrike prerequisite:** Zero Trust Assessment (ZTA) feature must be explicitly enabled on your Falcon CID by contacting CrowdStrike Support
- Integration pulls device list via CrowdStrike API; Twingate client reads local Agent ID or ZTA file to confirm device identity
- Initial sync after setup takes **up to 10 minutes**; devices show "Waiting to sync" during this period

## Prerequisites
- Business or Enterprise Twingate plan
- CrowdStrike Falcon Zero Trust Assessment enabled on your CID (contact CrowdStrike Support)
- Verify ZTA is active by confirming the ZTA file exists and is non-empty:
  - **Windows:** `%ProgramData%\CrowdStrike\ZeroTrustAssessment\data.zta`
  - **macOS:** `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/data.zta`

## Step-by-Step

1. **Generate CrowdStrike API Client** in Falcon platform with these scopes:
   - `Hosts: Read`
   - `Zero Trust Assessment: Read`
   - Save the **API Client ID**, **API Client Secret**, and **Base URL**

2. In Twingate Admin Console, go to **Settings → Device Settings**

3. Click **Connect** next to CrowdStrike; enter API Client ID, API Client Secret, and Base URL

4. Confirm integration status on the Device Settings page

5. Create a **Trusted Profile** (macOS/Windows/Linux) requiring CrowdStrike as a Trust Method

6. Incorporate the Trusted Profile into a **Security Policy**

## Configuration Values

| Field | Description |
|---|---|
| `API Client ID` | Generated in CrowdStrike Falcon |
| `API Client Secret` | Generated in CrowdStrike Falcon |
| `Base URL` | CrowdStrike tenant base URL |

**Required API Scopes:** `Hosts:Read`, `Zero Trust Assessment:Read`

## Gotchas
- ZTA feature is **not enabled by default**; must be requested from CrowdStrike Support per CID
- Initial sync delay of up to 10 minutes after setup — devices may incorrectly show unverified during this window
- **Recoverable errors** (API unresponsive): integration auto-retries; last successful sync time is displayed
- **Unrecoverable errors** (API client deleted, permissions changed): integration halts, admin email notification sent — requires full reconfiguration with new API credentials

## Related Docs
- Twingate Device Security Trusted Profiles
- Twingate Security Policies
- [Twingate Pricing](https://www.twingate.com/pricing)