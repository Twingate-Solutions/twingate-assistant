## Page Title
Bastion Server Cloaking

## Summary
Explains why bastion servers are used, their security drawbacks, and how Twingate addresses each drawback to effectively replace the bastion pattern. Key improvements: resources become internet-invisible, IdP sync ensures only active employees have access, and SSO/2FA policies apply to any resource type without application changes.

## Key Information
- **Why bastions exist**: single hardened ingress point for security monitoring; single access management point (disable bastion access = disable all private access)
- **Bastion drawbacks Twingate solves**:
  - Bastion has a public IP that can be probed/attacked; Twingate resources have no public exposure
  - SSH key management often not coupled to IdP; Twingate syncs in real-time with IdP -- inactive employees automatically lose access
  - 2FA on SSH is difficult to implement; Twingate applies IdP SSO policy (including 2FA) to any resource at the network layer, no app changes required
- **Twingate as bastion replacement**: Connector replaces the bastion as the network ingress point; the Connector itself is also not publicly accessible

## Prerequisites
None -- conceptual/use-case page.

## Step-by-Step
Not applicable -- see `/docs/cloak-your-bastion-server` for the implementation guide.

## Configuration Values
None.

## Gotchas
- Twingate's 2FA enforcement is at the network authorization layer (OSI Layer 4), not the application layer; the underlying application can still have its own auth
- IdP sync means that Twingate access revocation is as fast as IdP deprovisioning -- ensure IdP deprovisioning is prompt

## Related Docs
- `/docs/cloak-your-bastion-server` -- step-by-step cloaking guide
- `/docs/two-factor-authentication-security-policies` -- configuring 2FA policies
- `/docs/identity-providers` -- IdP integration
