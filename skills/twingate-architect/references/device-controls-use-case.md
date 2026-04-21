## Page Title
Device Security Controls

## Summary
Use case overview for enforcing device-based access policies. Posture checks screen for OS type, screen lock, MDM enrollment, EDR enrollment, and custom criteria. Integrates with leading MDM and EDR platforms to delegate device trust decisions.

## Key Information
- **Posture checks**: OS type, screen lock enabled, MDM enrolled, EDR enrolled, custom criteria
- **MDM integrations**: Intune, Jamf, Kandji — for device trust delegation
- **EDR integrations**: CrowdStrike (ZTA score threshold), SentinelOne
- **IdP integrations**: Okta, JumpCloud, Entra ID, OneLogin, Google Workspace
- Access policies enforced at the edge (on the client device), not centrally
- Split-tunnel by default — no performance degradation for non-Twingate traffic
- Admin Console for policy management; Public API for programmatic configuration
- Python and JavaScript CLI tools for automating device trust operations

## Prerequisites
- Business or Enterprise plan required for MDM/EDR integrations
- Trusted Profile configured in Admin Console to define device trust requirements

## Step-by-Step
Not applicable on this page — see integration-specific guides linked below.

## Configuration Values
None on this page.

## Gotchas
- Device posture checks require the Twingate Client to be running and the device registered
- CrowdStrike integration uses ZTA score — configure minimum score threshold in Trusted Profile
- "Device-only" security policies allow resource access without user authentication — use deliberately and sparingly

## Related Docs
- `/docs/device-security-guide` — Trusted Profile configuration
- `/docs/device-posture-checks` — full posture check reference
- `/docs/crowdstrike-configuration` — CrowdStrike ZTA integration
- `/docs/sentinelone-configuration` — SentinelOne integration
- `/docs/intune-configuration` — Intune integration
- `/docs/jamf-configuration` — Jamf integration
- `/docs/kandji-configuration` — Kandji integration
