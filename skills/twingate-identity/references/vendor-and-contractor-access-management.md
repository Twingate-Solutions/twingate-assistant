# Vendor and Contractor Access Management

## Page Title
How to Manage Access for Vendors and Contractors

## Summary
Twingate addresses the unique challenges of vendor/contractor access including transient relationships, need for targeted permissions, and unmanaged devices. It provides granular, time-limited access controls that overlay existing resources without requiring changes to those resources.

## Key Information
- Vendor access differs from employee access in three ways: higher onboarding/offboarding frequency, need for more targeted resource access, and use of unmanaged personal devices
- Twingate applies access controls without modifying underlying resources
- SSO integration means disabling a contractor's IdP account revokes all Twingate-secured resource access — even resources without native SSO support
- Access is granted at the application level (not network level), enabling least-privilege without network segmentation projects
- Network activity logging provides visibility into contractor devices, locations, and security posture

## Prerequisites
- Identity Provider (Okta, Google Workspace, etc.) configured for SSO delegation
- Resources defined in Twingate
- Groups configured for contractor/vendor assignment

## Configuration Options by Use Case

| Use Case | Twingate Feature | Reference |
|---|---|---|
| Onboarding/offboarding | SSO/IdP integration | Identity Providers guide |
| Least-privilege access | Resource-level permissions + Groups | Resources guide |
| Device visibility | Network traffic logging | Network Traffic guide |
| Time-limited engagements | Ephemeral Access (time-based auto-revoke) | Ephemeral Access guide |
| Over-provisioning prevention | Auto-lock (usage-based lockout) | Auto-lock guide |

## Step-by-Step: Recommended Vendor Setup
1. Create a dedicated Group for vendors/contractors
2. Assign only required Resources to that Group
3. Configure Ephemeral Access on Resources for fixed-term engagements
4. Enable Auto-lock on Resources to handle inactive accounts
5. Provision contractor via IdP — disable IdP account to offboard

## Gotchas
- Disabling access via IdP only works if Twingate is configured to delegate authentication to that IdP — verify integration is active
- Auto-lock and Ephemeral Access are separate mechanisms; Ephemeral Access revokes after a set time period, Auto-lock revokes after inactivity — use the appropriate one for the scenario
- Contractors using personal devices will be visible in logs, but device posture enforcement depends on additional configuration

## Related Docs
- Identity Providers
- Resources
- Network Traffic
- Ephemeral Access
- Auto-lock