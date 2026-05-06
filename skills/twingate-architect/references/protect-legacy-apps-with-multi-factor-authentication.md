# Protect Legacy Apps with Multi-Factor Authentication

## Summary
Twingate enables MFA enforcement on legacy technologies (SSH, RDP, databases, file shares) that were never designed to support it by operating at the network level. Security Policies intercept requests and enforce authentication before allowing traffic through, without requiring changes to the legacy applications themselves.

## Key Information
- Works with any legacy technology: SSH, RDP, Citrix, MSSQL, MySQL, Oracle, PostgreSQL, file servers, custom web apps
- MFA enforcement happens at network level—no reconfiguration of legacy apps required
- Integrates with existing Identity Provider (IdP) for unified access control
- Unauthorized requests never leave the user device (resource is invisible to unauthorized users)
- Offboarding simplification: disable SSO account = access revoked across all protected resources automatically

## How It Works
1. User device makes a request to a resource
2. Twingate intercepts the request at network level
3. Twingate checks the applicable Security Policy for that resource
4. If MFA is required and not yet satisfied, Twingate prompts the user for MFA
5. On successful MFA: request proceeds to the resource
6. On failed/missing authorization: request is dropped at the device

## Prerequisites
- Twingate account with Security Policies configured
- Identity Provider integrated with Twingate
- Twingate Client deployed on user devices
- Twingate Connector deployed in the network where legacy resources reside

## Configuration Values
- **Security Policy**: Assign a policy requiring MFA to the target Resource
- **Resource**: Define the legacy app/server as a Twingate Resource
- **Identity Provider**: Must be connected to Twingate for SSO/MFA enforcement

## Gotchas
- MFA prompt is triggered by Twingate, not the legacy app—user experience differs from app-native MFA
- Requires users to have Twingate Client installed and authenticated before accessing resources
- Disabling SSO account removes access, but only if Twingate is the sole access path to the resource (ensure no bypass routes exist)
- Legacy apps with their own credential systems remain unchanged—Twingate adds a layer but doesn't replace app-level credentials

## Related Docs
- Security Policies
- Identity Provider integration
- Twingate Resources configuration
- Twingate Connectors