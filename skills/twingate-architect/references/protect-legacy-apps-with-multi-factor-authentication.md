# Protect Legacy Apps with Multi-Factor Authentication

## Page Title
How to Protect Legacy Technologies with MFA

## Summary
Twingate enables MFA enforcement on legacy technologies (SSH, RDP, databases, file servers) that were never designed to support it. Security Policies intercept network requests and enforce MFA via your Identity Provider before allowing access. No changes to the legacy application or infrastructure are required.

## Key Information
- MFA is applied via **Security Policies** at the network level—no app reconfiguration needed
- Works with any legacy technology: SSH, RDP, Citrix, MSSQL, MySQL, Oracle, PostgreSQL, file shares, custom web apps
- Twingate intercepts requests **on the device** before they leave; unauthorized requests never reach the network
- Identity Provider integration means revoking SSO account removes access to all protected resources automatically
- If MFA is required by policy, Twingate prompts the user and only forwards the request upon successful authentication

## Prerequisites
- Twingate deployed with at least one Connector
- Identity Provider (IdP) configured and integrated with Twingate
- MFA enabled in your IdP
- Resources defined in Twingate admin console
- Security Policy created with MFA requirement

## Step-by-Step
1. Define the legacy resource in Twingate (IP/hostname, port, protocol)
2. Create or edit a **Security Policy** to require MFA
3. Assign the Security Policy to the resource
4. Assign user/group access to the resource
5. When a user attempts access, Twingate intercepts the request and prompts for MFA via IdP
6. On successful MFA, request is forwarded to the resource

## Configuration Values
- **Security Policy**: Set MFA requirement (configured in Twingate Admin Console under Policies)
- No CLI flags, env vars, or API parameters specific to this feature documented on this page

## Gotchas
- MFA prompt is triggered by Twingate's client, not the legacy app—users must have Twingate client installed and running
- Disabling an SSO account removes access, but **only if** access is gated through Twingate; any direct network paths to the resource bypass this protection
- Legacy app credentials (e.g., database passwords) still exist independently—Twingate prevents network access but does not manage app-level credentials

## Related Docs
- Security Policies
- Identity Provider configuration
- Resource configuration
- Twingate Connector setup