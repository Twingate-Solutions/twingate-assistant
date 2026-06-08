# SaaS App Gating with OneLogin

## Summary
Configures OneLogin to restrict SaaS app access to users connecting through Twingate by allowlisting the Connector's exit IP. Uses OneLogin App Policies combined with Twingate Resources to enforce network-level access control for SaaS applications.

## Key Information
- OneLogin validates the source IP of authentication requests; only requests coming from Twingate Connector exit IPs are permitted
- Twingate acts as a network proxy — authenticated users route through Connectors, presenting the Connector's public IP to OneLogin
- Protects any OneLogin-integrated SaaS app (e.g., Google Workspace) without modifying the app directly

## Prerequisites
- Twingate admin access with ability to create Resources and Policies
- OneLogin admin access with Security and Applications permissions
- Know the public exit IP of your Twingate Remote Network's Connector(s)
- OneLogin tenant URL (e.g., `tenant.onelogin.com`)

## Step-by-Step

### Twingate Admin Console
1. Create a Twingate Resource for your OneLogin tenant FQDN (e.g., `tenant.onelogin.com`)
2. Associate that Resource with the appropriate Twingate Group(s)
3. Apply a **Device-only Policy** to the OneLogin Resource — prevents auth loops where IdP access requires prior Twingate auth

### OneLogin Admin Console
4. Navigate to **Security → Policies → New App Policy**
5. Name the policy (e.g., "Twingate SaaS App Gate")
6. In the **Allowed IP Addresses** field, enter the Connector's public exit IP
7. Navigate to **Applications → Applications**, select the target app (e.g., Google Workspace)
8. Go to **Access → Policies**, select your new App Policy, and save

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Twingate Resource | `tenant.onelogin.com` (your specific tenant) |
| Twingate Resource Policy | Device-only |
| OneLogin Allowed IP | Connector public exit IP |

## Gotchas
- **Auth loop risk**: Without a Device-only Policy on the IdP Resource, users can't reach OneLogin to authenticate because Twingate requires authentication first — apply Device-only Policy to the IdP Resource specifically
- **Multiple Connectors**: If you have multiple Connectors in the Remote Network, all their exit IPs must be added to the OneLogin Allowed IP list
- **IP changes**: If Connector IPs change (e.g., infrastructure updates), the OneLogin App Policy must be updated manually

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs/resources)
- [Device-only Resource Policy](https://www.twingate.com/docs/resource-policies)
- General SaaS App Gating pattern applies to other IdPs (Okta, Azure AD) with similar IP allowlist capabilities