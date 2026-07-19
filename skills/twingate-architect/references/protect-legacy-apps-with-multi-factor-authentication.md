# Protect Legacy Apps with Multi-Factor Authentication

## Summary
Twingate enables MFA enforcement on legacy technologies (SSH, RDP, databases, file servers) that lack native MFA support by intercepting requests at the network level. Security Policies are applied to resources, requiring IdP authentication before access is granted. No changes to legacy applications are required.

## Key Information
- Works with: SSH, RDP, Citrix, Windows RDS, SQL Server, MySQL, Oracle, PostgreSQL, file sharing servers, custom web apps
- MFA enforcement happens at the **network level** — legacy app requires zero reconfiguration
- Twingate intercepts resource-bound requests on the client device before they leave
- Unauthorized requests never leave the device (resource is invisible to unauthorized users)
- User offboarding simplified: disabling SSO account revokes access to all protected resources automatically

## Prerequisites
- Twingate deployed with at least one Resource configured
- Identity Provider (IdP) integrated with Twingate
- Security Policy with MFA requirement created
- Twingate Client installed on user devices

## How It Works (Step-by-Step)
1. User device makes a network request to a protected resource
2. Twingate client intercepts the request
3. Twingate checks the applicable Security Policy for that resource
4. If MFA is required and not yet satisfied, user is prompted for MFA via IdP
5. On successful MFA: request is forwarded to resource
6. On failure or no authorization: request is dropped; resource remains inaccessible

## Configuration Values
| Component | Setting |
|-----------|---------|
| Security Policy | Enable MFA requirement |
| Resource | Assign the Security Policy |
| Identity Provider | Must be configured in Twingate admin |

## Gotchas
- MFA prompt is triggered by Twingate, not the legacy app — user experience differs from app-native MFA flows
- Relies on IdP integration being correctly configured; broken IdP = blocked access
- Users must have the Twingate client running for protection to apply
- Does not protect resources from lateral movement if accessed from a machine already on the network without Twingate

## Related Docs
- Security Policies
- Identity Provider configuration
- Resource configuration
- Twingate Client setup