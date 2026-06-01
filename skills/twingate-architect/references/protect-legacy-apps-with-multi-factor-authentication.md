# Protect Legacy Apps with Multi-Factor Authentication

## Summary
Twingate enables MFA enforcement on legacy technologies (SSH, RDP, databases, file servers) that were not designed with MFA support by intercepting requests at the network level. Security Policies are applied to resources without requiring changes to the legacy applications themselves. Identity Provider integration means access revocation is handled by disabling the SSO account.

## Key Information
- Twingate adds MFA to any resource regardless of whether the application natively supports it
- Works at network level — no application reconfiguration required
- Leverages existing Identity Provider (IdP/SSO) for authentication
- Unauthorized requests never leave the user device (resource is completely invisible)
- Revoking access requires only disabling the SSO account — no app-specific intervention

## Target Technologies
- **Remote access**: SSH, RDP, Citrix, Windows Remote Desktop Services
- **Databases**: MSSQL, MySQL, Oracle, PostgreSQL
- **Other**: File sharing servers, custom internal web apps

## Prerequisites
- Twingate deployed with at least one Connector on the network hosting the legacy resource
- Identity Provider configured in Twingate
- Resource defined in Twingate Admin Console
- Security Policy with MFA requirement created

## How It Works (Step-by-Step)
1. User attempts to access a resource protected by Twingate
2. Twingate intercepts the request at the network level
3. Twingate checks the applicable Security Policy for that resource
4. If MFA is required and user is authorized, Twingate prompts for MFA
5. On successful MFA, request is forwarded to the resource
6. If user is unauthorized, request is blocked at the device — resource is unreachable

## Configuration Values
| Component | Setting |
|-----------|---------|
| Security Policy | Enable MFA requirement |
| Resource | Assign the Security Policy |
| Identity Provider | Must be configured in Twingate |

## Gotchas
- MFA prompt is triggered by Twingate, not the legacy app — users may find this flow unfamiliar
- If SSO account is disabled, access is revoked across all Twingate-protected resources simultaneously
- No changes needed to legacy app config, but the Twingate Client must be installed and running on user devices
- Resource is fully hidden from unauthorized users even if they possess valid application credentials

## Related Docs
- Security Policies
- Identity Provider configuration
- Twingate Connectors (for network deployment)
- Resource configuration