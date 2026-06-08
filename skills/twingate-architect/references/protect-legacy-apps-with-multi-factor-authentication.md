# Protect Legacy Apps with Multi-Factor Authentication

## Page Title
How to Protect Legacy Technologies with MFA

## Summary
Twingate enables MFA enforcement on legacy technologies (SSH, RDP, databases, file servers) that lack native MFA support by intercepting network requests and applying Security Policies before allowing access. No changes to the legacy application or infrastructure are required. Identity Provider integration also simplifies access revocation when employees leave.

## Key Information
- MFA can be layered onto any resource via a **Security Policy** — no app modification needed
- Works at **network level**, intercepting requests before they reach the target resource
- Integrates with your **Identity Provider (IdP/SSO)** — disabling an SSO account removes access automatically
- If a user lacks authorization, requests never leave the device (resource is invisible)
- Supports prompt-based MFA flow: user is challenged before request is forwarded

## Supported Legacy Technology Types
- Secure Shell (SSH)
- Remote Desktop (RDP, Citrix, Windows Remote Desktop Services)
- Database servers (MSSQL, MySQL, Oracle, PostgreSQL)
- File sharing servers
- Custom web apps on internal web servers

## Prerequisites
- Twingate deployed with a Connector on the target network
- Resource defined in Twingate admin console
- Identity Provider configured and integrated with Twingate
- Security Policy with MFA requirement created

## Step-by-Step
1. Define the legacy resource in the Twingate admin console
2. Create or edit a **Security Policy** to require MFA
3. Assign the Security Policy to the resource
4. Assign user/group access to the resource
5. Users accessing the resource will be prompted for MFA via their IdP before the connection proceeds

## Configuration Values
| Item | Location |
|------|----------|
| Security Policy | Admin Console → Security Policies |
| MFA requirement | Security Policy settings (enable MFA prompt) |
| Resource assignment | Admin Console → Resources → assign policy |
| IdP integration | Admin Console → Authentication |

## Gotchas
- MFA enforcement depends on the IdP integration being properly configured — if IdP is misconfigured, policy enforcement may fail
- No app-side changes required, but the **Twingate Client must be running** on the user device for enforcement to occur
- Access revocation via IdP account disable requires IdP to be the auth source; local Twingate accounts won't benefit from this automatically

## Related Docs
- Security Policies
- Identity Provider Integration
- Resources configuration
- Twingate Connector setup