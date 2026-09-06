---
source: https://help.twingate.com/articles/9287595551-self-serve-troubleshooting-guide
type: help
fetched: 2026-09-06
source_version: 51710f279dc0b49e4e344d1b28d1681cb8a0fe2c0af1c483c7e37ac4a0ab3755
---

# Self-Serve Troubleshooting Guide

## Page Title
Self-Serve Troubleshooting Guide

## Summary
Structured troubleshooting guide for common Twingate issues. Covers two primary failure scenarios: Client unable to join the Twingate network, and Client unable to connect to a specific Resource.

## Key Information

### Client Cannot Join Twingate Network
- Verify Twingate Network Interface exists on the device
- **(Windows)** Confirm Network Interface is enabled
- **(Windows)** Confirm Twingate Service is running
- Verify outbound ports are not blocked by local network
- Check for incompatible clients/agents running alongside Twingate Client
- Check if device region is geo-blocking Twingate access

### Client Cannot Connect to a Resource
- Validate Resource definition is correctly configured
- Verify user has permissions for the Resource
- **(Windows)** Ensure Domain Controllers are declared as Resources
- Review Network Events for the specific Resource
- Check for Resource ambiguity (overlapping definitions)

## Prerequisites
- Twingate Client installed on affected device
- Admin access to Twingate Admin Console (for checking permissions, Resource definitions, Network Events)

## Step-by-Step
1. Identify which failure scenario applies (network join vs. resource access)
2. Work through the relevant checklist above
3. If unresolved, collect logs and escalate

## Configuration Values
- No specific env vars or CLI flags documented on this page
- Outbound port requirements referenced but not listed inline (check linked Knowledge Base)

## Gotchas
- Windows has additional requirements not applicable to other platforms: Service must be running AND Network Interface must be explicitly enabled
- Domain Controllers must be explicitly declared as Resources on Windows — omitting this is a common Windows-specific failure
- Resource ambiguity (multiple Resources with overlapping address ranges) can silently break connectivity
- Regional network blocks can prevent Client from reaching Twingate infrastructure entirely

## Log Collection (for escalation)
- **Client logs**: Collect from affected end-user devices
- **Connector logs**: Collect when troubleshooting Resource access failures
- Share both with Twingate support if issue persists

## Related Docs
- [Twingate Docs](https://www.twingate.com/docs)
- [Twingate Help Center / Knowledge Base](https://help.twingate.com)
- [Known Incompatibilities](https://help.twingate.com) — check before running alongside other VPN/agent software
- [Twingate Forum](https://forum.twingate.com)
- [Service Status](https://status.twingate.com)
- [Twingate Changelog](https://www.twingate.com/changelog)
- Subscription Management (billing)