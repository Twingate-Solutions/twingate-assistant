# Protect Legacy Apps with Multi-Factor Authentication

## Page Title
How to Protect Legacy Technologies with MFA

## Summary
Twingate enables MFA enforcement on legacy technologies (SSH, RDP, databases, file servers) that were never designed to support it by applying Security Policies at the network level. No changes to the legacy application or infrastructure are required. Access management simplifies to disabling the SSO/IdP account when users leave.

## Key Information
- MFA protection applies to any resource Twingate secures, regardless of whether the app natively supports MFA
- Works at the **network level** — the legacy app requires zero reconfiguration
- Leverages your existing **Identity Provider (IdP)** for authentication
- Unauthorized requests never leave the user's device (resource is invisible to unauthorized users)
- Offboarding simplifies to disabling the SSO account — no app-specific credential cleanup needed

## Supported Legacy Technology Types
- **Remote access**: SSH, RDP, Citrix, Windows Remote Desktop Services
- **Databases**: MSSQL, MySQL, Oracle, PostgreSQL
- **File sharing servers**
- **Custom web applications**

## Prerequisites
- Twingate deployed with Connectors protecting target resources
- Identity Provider configured and integrated with Twingate
- Resources defined in Twingate admin console
- Security Policy with MFA requirement created

## How It Works (Flow)
1. User device makes a network request to a Twingate-protected resource
2. Twingate intercepts the request at network level
3. Twingate checks the applicable **Security Policy**
4. If policy requires MFA → user is prompted for MFA authentication
5. On success → request is forwarded to the resource
6. If user is unauthorized → request is dropped at the device; resource is unreachable

## Configuration Values
| Component | Action Required |
|-----------|----------------|
| Security Policy | Create/edit policy with MFA requirement enabled |
| Resource | Assign the MFA Security Policy to the resource |
| Identity Provider | Must be configured in Twingate tenant |

## Gotchas
- MFA prompt is triggered by Twingate, not the application — users may find the flow unfamiliar
- If the IdP account is active but Twingate access is not revoked, the user may retain access; both must be managed
- Policy enforcement depends on correct resource and policy assignment — verify resources are assigned the intended Security Policy

## Related Docs
- Security Policies
- Identity Provider configuration
- Twingate Connectors / Resource setup
- Single Sign-On (SSO) integration