# Protect Legacy Apps with Multi-Factor Authentication

## Page Title
How to Protect Legacy Technologies with MFA

## Summary
Twingate enables MFA enforcement on legacy technologies (SSH, RDP, databases, file servers) that were never designed to support it, by intercepting requests at the network level and applying Security Policies before allowing access. No changes to the legacy applications themselves are required.

## Key Information
- MFA can be layered onto any resource via a **Security Policy** — no app modification needed
- Works at the **network level**, intercepting requests before they reach the target resource
- Integrates with your **Identity Provider (IdP)** for centralized access management
- Unauthorized requests never leave the user's device — the resource is completely invisible to unauthorized users
- Revoking access is handled by disabling the SSO/IdP account — no app-specific intervention required

## Supported Legacy Technologies
- Secure Shell (SSH)
- Remote Desktop (RDP, Citrix, Windows Remote Desktop Services)
- Database servers (MSSQL, MySQL, Oracle, PostgreSQL)
- File sharing servers
- Custom internal web applications

## Prerequisites
- Twingate deployed with a configured **Identity Provider**
- Target resources added to Twingate
- **Security Policy** created with MFA requirement

## How It Works (Flow)
1. User device makes a request to a Twingate-protected resource
2. Twingate intercepts the request at the network level
3. Twingate checks the applicable **Security Policy**
4. If MFA is required, Twingate prompts the user for MFA authentication
5. On success → request is forwarded to the resource
6. On failure or no authorization → request is dropped; resource remains inaccessible

## Configuration Values
- **Security Policy**: Must be configured to require MFA for the target resource/group
- **Identity Provider**: Must be integrated with Twingate for SSO-based auth enforcement

## Gotchas
- MFA prompt is handled by Twingate, not the legacy application — users may find the flow unfamiliar
- Access revocation relies on disabling the **IdP/SSO account**; if the IdP account remains active, access may persist
- No legacy app reconfiguration needed, but the resource must be properly registered in Twingate

## Related Docs
- Security Policies
- Identity Provider Integration
- Resources configuration
- Single Sign-On (SSO) setup