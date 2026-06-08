# Device Security Controls Use Case

## Page Title
Device Security Controls Use Case

## Summary
Twingate provides granular device-based access controls that screen users and devices against permitted characteristics (OS type, screen lock, MDM/EDR status, etc.). Policies are enforced at the edge on client devices rather than centrally, reducing latency. Integrations with major IdPs, MDM, and EDR providers enable automated device trust delegation.

## Key Information
- Access policies enforce principle of least privilege based on device characteristics
- Split tunneling enabled by default (unlike traditional VPNs)
- Policy enforcement happens on client devices (edge), not in the cloud
- Web-based admin console available; programmatic config via Public API
- Supports delegating device trust to third-party security tools

## Supported Integrations
**Identity Providers:** Okta, JumpCloud, Entra ID, OneLogin, Google

**MDM Providers:** Intune, Jamf, Iru

**EDR Solutions:** CrowdStrike, SentinelOne

**Other:** 1Password XAM

## Device Posture Checks (Examples)
- Operating system type
- Screen lock enabled/disabled
- MDM enrollment status
- EDR agent presence

## Configuration Paths
| Use Case | Reference |
|----------|-----------|
| General device security setup | Device Security Guide |
| Available posture checks | List of Device Security Posture Checks |
| Automate device trust | Python CLI or JavaScript CLI guides |
| Delegate trust to CrowdStrike | Dedicated how-to guide |
| Delegate trust to SentinelOne | Dedicated how-to guide |
| Delegate trust to Intune | Dedicated how-to guide |
| Delegate trust to Jamf | Dedicated how-to guide |
| Delegate trust to Iru | Dedicated how-to guide |
| Delegate trust to 1Password XAM | Dedicated how-to guide |

## Prerequisites
- Twingate account with admin access
- Resources and networks configured in admin console
- Relevant IdP integration configured (if using IdP-based controls)
- MDM/EDR integration configured before delegating device trust

## Gotchas
- Device trust delegation requires separate configuration per MDM/EDR provider
- Programmatic configuration requires Public API access (may depend on plan tier)
- Split tunneling is on by default — verify this aligns with your security requirements before deployment

## Related Docs
- Device Security Guide
- List of Device Security Posture Checks
- Twingate Public API
- IdP integration guides (Okta, JumpCloud, Entra ID, OneLogin, Google)
- MDM/EDR delegation guides (CrowdStrike, SentinelOne, Intune, Jamf, Iru, 1Password XAM)
- Resources, Networks, and Policies documentation