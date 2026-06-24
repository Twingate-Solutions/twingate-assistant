# Protect Legacy Apps with Multi-Factor Authentication

## Summary
Twingate enables MFA enforcement on legacy technologies (SSH, RDP, databases, file servers) that lack native MFA support by intercepting requests at the network level. Security Policies are applied to resources, requiring IdP authentication before access is granted. No changes to the legacy application itself are required.

## Key Information
- Works with any resource regardless of whether it natively supports MFA or SSO
- MFA enforcement happens at the network layer, not the application layer
- Twingate intercepts requests on the client device before they leave; unauthorized requests never reach the network
- Revoking SSO/IdP account immediately removes access to all protected resources — no per-app intervention needed
- Covered resource types:
  - SSH servers
  - RDP, Citrix, Windows Remote Desktop Services
  - Database servers (MSSQL, MySQL, Oracle, PostgreSQL)
  - File sharing servers
  - Custom web applications

## Prerequisites
- Twingate account with at least one configured Resource
- Identity Provider (IdP) integrated with Twingate
- Security Policy configured with MFA requirement
- Twingate Client installed on user devices

## How It Works (Step-by-Step)
1. User device makes a request to a resource protected by Twingate
2. Twingate client intercepts the request at the network level
3. Twingate checks the applicable Security Policy for that resource
4. If policy requires MFA, Twingate prompts the user for MFA via the configured IdP
5. On successful MFA: request is forwarded to the resource
6. On failed MFA or no authorization: request is dropped on the device; resource is unreachable

## Configuration Values
- **Security Policy**: Must have MFA requirement enabled and be assigned to the target Resource
- **Identity Provider**: Must be connected to Twingate (handles authentication challenges)

## Gotchas
- MFA prompt is triggered by Twingate's Security Policy, not the application — ensure the correct policy is assigned to each resource
- If a user's IdP account is disabled, access is revoked immediately across all Twingate-protected resources; no additional cleanup needed per legacy app
- Unauthorized users receive no network-level response — the resource appears completely inaccessible, providing resource hiding in addition to MFA

## Related Docs
- Security Policies
- Identity Provider integration
- Resources configuration
- Twingate Client setup