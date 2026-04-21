## Protecting Legacy Applications with MFA via Twingate

Twingate enforces MFA on legacy technologies (SSH, RDP, Citrix, databases, file shares, custom web apps) at the network layer via Security Policies, requiring zero changes to the applications themselves. Authentication is delegated to the IdP, so deprovisioning is as simple as disabling the SSO account -- no app-specific cleanup needed.

**Key Information**
- Target technologies: SSH, RDP, Citrix, Windows Remote Desktop Services, SQL Server, MySQL, Oracle, PostgreSQL, file shares, custom web apps
- Twingate operates at network level (OSI Layer 4 and below) -- no application modifications required
- MFA enforcement mechanism: when a user requests a Resource, Twingate checks the Security Policy; if MFA is required, it prompts the user before the request is forwarded to the Connector
- Unauthorized requests never leave the device -- the application remains invisible to unauthorized users even if they have valid app credentials
- Deprovisioning: disable the SSO/IdP account; access to all Twingate-protected Resources is immediately revoked

**Prerequisites**
- Identity Provider configured in Twingate (Okta, Azure AD, Google Workspace, etc.)
- Twingate Connector deployed in the same network as legacy applications
- Security Policy configured with MFA requirement

**Step-by-Step**
1. Add legacy server(s) as Twingate Resources (IP or FQDN + port)
2. Create or edit a Security Policy to require MFA (via IdP 2FA)
3. Assign the Security Policy to the Group(s) with access to those Resources
4. Firewall/restrict direct access to the legacy servers from outside the Connector network

**Gotchas**
- Twingate MFA is enforced at Resource access time, not at application login -- if the app has no auth, users can still access it once through Twingate; use both Twingate access control and app-level auth where possible
- Legacy apps that require static credentials (not SSO) still need those credentials; Twingate only gates network access, it does not replace app authentication

**Related Docs**
- /docs/security-policies
- /docs/two-factor-authentication-security-policies
- /docs/protect-access-to-elasticsearch-and-kibana
- /docs/authentication
