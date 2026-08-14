---
source: https://www.twingate.com/docs/protect-legacy-apps-with-multi-factor-authentication
type: docs
fetched: 2026-08-14
source_version: a30ecc2dee9cc5b5e077c3ece1973b7476b42008e982e2edc5ae15742d21b51e
---

# Protect Legacy Apps with Multi-Factor Authentication

## Summary
Twingate enables MFA enforcement on legacy technologies (SSH, RDP, databases, file servers) that lack native MFA support by intercepting requests at the network level. Security Policies are applied to resources, and users must authenticate via your Identity Provider before access is granted. No changes to the legacy application itself are required.

## Key Information
- Works with any legacy technology: SSH, RDP, Citrix, MSSQL, MySQL, Oracle, PostgreSQL, file shares, custom web apps
- MFA enforcement happens at network level—no app reconfiguration needed
- Integrates with existing Identity Provider (SSO) for user lifecycle management
- Unauthorized requests never leave the user's device (resource is invisible without authorization)
- Disabling SSO account immediately revokes access to all protected resources

## Prerequisites
- Twingate deployed with a Connector on your network
- Identity Provider (SSO) configured with Twingate
- Legacy resource registered as a Twingate Resource
- Security Policy with MFA requirement created

## How It Works (Step-by-Step)
1. User device makes a request to a legacy resource
2. Twingate intercepts the request at the network level
3. Twingate checks the Security Policy associated with that resource
4. If MFA is required, Twingate prompts the user for MFA via the Identity Provider
5. On successful MFA: request passes through to the resource
6. On failed auth or no authorization: request is dropped, resource remains invisible

## Configuration Values
| Component | Setting |
|-----------|---------|
| Resource | Register legacy resource (IP/hostname) in Twingate Admin Console |
| Security Policy | Set MFA requirement on the policy |
| Policy Assignment | Attach Security Policy to the target Resource |
| Identity Provider | Must be configured for SSO/MFA support |

## Gotchas
- MFA prompt is triggered by Twingate, not the legacy app—user experience differs from app-native MFA
- Requires Twingate Client running on user devices to intercept network requests
- SSO account deprovisioning removes access; app-specific credentials alone are insufficient to bypass Twingate
- Legacy app credentials (username/password) still exist—Twingate adds a layer but doesn't eliminate them

## Related Docs
- Security Policies
- Identity Provider configuration
- Resources setup
- Twingate Connectors