# Protect Legacy Apps with Multi-Factor Authentication

## Page Title
How to Protect Legacy Technologies with MFA

## Summary
Twingate enables MFA enforcement on legacy systems (SSH, RDP, databases, file servers) that were never designed to support it by intercepting requests at the network level and applying Security Policies before allowing access. No changes to the legacy application or infrastructure are required.

## Key Information
- MFA enforcement works at the **network level** — no reconfiguration of target apps needed
- Twingate integrates with your existing **Identity Provider (IdP)** for authentication
- Supported legacy technology types:
  - SSH
  - RDP, Citrix, Windows Remote Desktop Services
  - Database servers (MSSQL, MySQL, Oracle, PostgreSQL)
  - File sharing servers
  - Custom web apps
- Access revocation is simplified: disable SSO account → access removed automatically, no per-app manual cleanup

## Prerequisites
- Twingate account with an Identity Provider configured
- Security Policy with MFA requirement created
- Twingate deployed and resources defined

## How It Works (Step-by-Step)
1. User device sends a request to a resource
2. Twingate intercepts the request at the network level
3. Twingate checks the applicable **Security Policy** for that resource
4. If MFA is required and not yet satisfied, Twingate prompts the user for MFA
5. On successful MFA, Twingate forwards the request to the resource
6. If user lacks authorization, the request never leaves the device (resource is invisible)

## Configuration Values
- **Security Policy**: Must be configured with MFA requirement and assigned to the target resource
- **Identity Provider**: Must be connected to Twingate for SSO-based authentication

## Gotchas
- MFA prompt is triggered by Twingate, not the legacy app — users may be confused by the unexpected auth step
- Unauthorized resources are completely hidden from users (not just blocked) — useful for security posture but worth documenting for helpdesk
- Relies on IdP being available; if IdP is down, MFA enforcement behavior should be tested in advance

## Related Docs
- Security Policies
- Identity Provider integration
- Resources configuration