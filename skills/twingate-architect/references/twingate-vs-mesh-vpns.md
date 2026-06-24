# Twingate vs. Mesh VPNs

## Summary
Twingate is an enterprise-first zero-trust access solution that differs from mesh VPNs primarily in deployment simplicity, network architecture requirements, and security feature depth. Key advantages include no infrastructure changes required, overlapping IP support, and enhanced security features beyond basic access control.

## Key Information

**Architecture Differences:**
- Mesh VPNs require unique IP addresses across entire private network; Twingate supports overlapping IP ranges
- Mesh VPNs require agent installation on every device (including servers); Twingate only requires client agents + one Controller per Remote Network
- Twingate can coexist with existing VPN solutions; mesh VPNs typically require rip-and-replace

**Deployment:**
- No network infrastructure changes required
- No resource re-addressing needed
- Can be evaluated alongside existing access solutions without disruption

**Administration:**
- Point-and-click admin console (vs. JSON-based policy config in some mesh VPNs)
- Full administrative API for automation (user provisioning, server access provisioning)

**Security Features (beyond mesh VPN baseline):**
- Universal 2FA: applies to any resource type including SSH, no application changes required
- Device posture-based access policies
- Identity-indexed network flow logs with centralized analytics

**Integrations:**
- Identity providers: Okta, OneLogin, Google Workspace, Entra ID (Azure AD), social SSO
- Compatible with DNS filtering tools (e.g., DNSFilter)

## Prerequisites
None specified — comparison/conceptual document only.

## Configuration Values
None specified in this document.

## Gotchas
- Mesh VPN IP re-addressing has significant knock-on effects: settings, bookmarks, workflows, and end-user habits all require updating
- Mesh VPN agent-on-every-device model becomes operationally complex at enterprise scale
- When evaluating mesh VPNs, verify compatibility with existing security stack (IdP, DNS filtering, etc.)

## Related Docs
- Twingate Connectors (Controller/Remote Network setup)
- Identity Provider integrations (Okta, OneLogin, Google Workspace, Entra ID)
- Device posture policies
- Universal 2FA configuration
- Administrative API reference