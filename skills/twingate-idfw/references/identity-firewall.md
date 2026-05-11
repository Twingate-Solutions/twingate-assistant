# Twingate Identity Firewall

## Summary
Twingate Identity Firewall extends Zero Trust and PAM controls to users, resources, and agents via a Layer 7 reverse proxy (Twingate Gateway). It propagates IdP identity to protected resources (Kubernetes, SSH, future: HTTPS, databases, MCP) without static credentials. Available on all plans, free for up to 5 Resources.

## Key Information
- **Current protocol support**: Kubernetes API, SSH
- **Planned support**: HTTPS, database protocols, Model Context Protocol (MCP)
- **Core component**: Twingate Gateway — open-source Layer 7 reverse proxy deployed in your environment
- **Access model**: Just-in-time, dynamic zero-standing access based on identity, device posture, location, context
- **No static credentials** or separate authentication tokens required
- Provides session recording and forensic-level audit (per-command, per-API-call logging)
- Permissions auto-revoked when no longer needed

## Prerequisites
- Existing IdP configured with Twingate
- Twingate account (any plan)
- Twingate Gateway deployed within target environment

## Architecture
```
User → IdP Authentication → Twingate Policy Enforcement → Twingate Gateway (L7 proxy) → Protected Resource
```

## Configuration Values
None specified in this overview page. See protocol-specific docs for deployment parameters.

## Gotchas
- Gateway must be deployed **inside** your environment (self-hosted reverse proxy)
- MCP support is not yet available (listed as future)
- Free tier limited to 5 Resources

## Related Docs
- [Privileged Access for Kubernetes](https://www.twingate.com/docs/privileged-access-kubernetes)
- [Privileged Access for SSH](https://www.twingate.com/docs/privileged-access-ssh)