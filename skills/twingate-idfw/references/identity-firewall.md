# Twingate Identity Firewall

## Summary
Twingate Identity Firewall extends Zero Trust and PAM controls to users, resources, and agents via a Layer 7 reverse proxy (Twingate Gateway). It propagates IdP identity to protected resources (Kubernetes, SSH, and future protocols) without static credentials. Free for up to 5 Resources on all plans.

## Key Information
- **Core component**: Twingate Gateway — open-source Layer 7 reverse proxy deployed in your environment
- **Current protocol support**: Kubernetes API, SSH
- **Planned protocol support**: HTTPS, database protocols, Model Context Protocol (MCP)
- **Authentication flow**: User authenticates via existing IdP → identity propagates to all accessed resources automatically
- **Access model**: Just-in-time, dynamic — permissions auto-revoked when no longer needed
- **Visibility**: Per-user/agent logging of commands, API calls, queries; session replay available
- **No static credentials or separate auth tokens required**

## Prerequisites
- Existing Identity Provider (IdP) integrated with Twingate
- Twingate account (any plan)
- Twingate Gateway deployed within your environment

## Configuration Values
- None documented on this overview page (see protocol-specific docs)

## Gotchas
- Gateway must be self-hosted within your environment (not Twingate-managed infrastructure)
- MCP server support is future/not yet available
- Database and HTTPS protocol support not yet released
- Free tier limited to 5 Resources

## Related Docs
- [Privileged Access for Kubernetes](https://www.twingate.com/docs/privileged-access-kubernetes)
- [Privileged Access for SSH](https://www.twingate.com/docs/privileged-access-ssh)