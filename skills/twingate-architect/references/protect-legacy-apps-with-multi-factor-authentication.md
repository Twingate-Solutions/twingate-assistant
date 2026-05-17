# Protect Legacy Apps with Multi-Factor Authentication

## Summary
Twingate enables MFA enforcement on legacy technologies (SSH, RDP, databases, file servers) that lack native MFA support by intercepting requests at the network level. Security Policies are applied without modifying the legacy applications themselves. Identity Provider integration simplifies access revocation when employees leave.

## Key Information
- MFA enforcement works at **network level** — no changes required to legacy applications
- Twingate intercepts requests destined for protected resources before they leave the device
- If user lacks authorization, requests never leave the device (resource is invisible even with valid credentials)
- IdP integration means revoking SSO account removes all resource access automatically
- Applies to any resource type: SSH, RDP, Citrix, databases, file shares, custom web apps

## Prerequisites
- Twingate account with Security Policy configuration access
- Identity Provider (IdP) connected to Twingate
- Twingate Connector deployed in network where legacy resources reside
- Resources defined in Twingate

## Step-by-Step
1. Define the legacy resource in Twingate (hostname/IP + port)
2. Create or select a **Security Policy** that requires MFA
3. Assign the Security Policy to the resource
4. Assign user/group access to the resource
5. Users attempting access will be prompted for MFA via IdP before connection is permitted

## How It Works
- Twingate client monitors outbound network requests on user devices
- Requests matching protected resources are intercepted
- Security Policy is evaluated; if MFA required, user is prompted
- On successful MFA: request is forwarded to resource
- On failed auth or no authorization: request is dropped at device level

## Configuration Values
| Component | Purpose |
|-----------|---------|
| Security Policy | Defines MFA requirement applied to resource |
| Identity Provider | Handles MFA challenge/authentication |
| Resource definition | Maps legacy app to Twingate protection |

## Gotchas
- MFA prompt occurs at **Twingate authentication layer**, not the application — users may still need app-level credentials separately
- Revoking access requires disabling the **IdP/SSO account**; app-specific credentials alone are insufficient to bypass Twingate but don't auto-revoke
- Legacy apps with hardcoded connection strings may have UX friction when Twingate prompts interrupt automated flows

## Related Docs
- Security Policies configuration
- Identity Provider integration
- Twingate Connector deployment
- Resource access management