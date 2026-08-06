---
source: https://help.twingate.com/articles/9287595551-self-serve-troubleshooting-guide
type: help
fetched: 2026-08-06
source_version: a335995ebcb816b43671ca05733ec6fedb4fab6fd3342d0234d5ff475acd2f8f
---

# Self-Serve Troubleshooting Guide

## Page Title
Self-Serve Troubleshooting Guide

## Summary
Covers common Twingate issues in two categories: Client unable to join the network, and Client unable to connect to a Resource. Provides ordered diagnostic steps for each scenario with escalation paths if issues persist.

## Key Information

### Client Cannot Join Twingate Network
- Verify Twingate Network Interface exists
- **Windows only:** Confirm Network Interface is enabled
- **Windows only:** Confirm Twingate Service is running
- Check that outbound ports are not blocked by local network
- Check for incompatible clients/agents running alongside Twingate Client
- Verify device is not in a region blocking Twingate access

### Client Cannot Connect to a Resource
- Verify Resource definition is correct and consistent
- Verify User has appropriate permissions
- **Windows only:** Ensure Domain Controllers are declared as Resources
- Check Network Events for the specific Resource
- Check for Resource ambiguity (overlapping Resource definitions)

## Prerequisites
- Twingate Client installed on affected device
- Admin access to Twingate Admin Console (for checking permissions, Resource definitions, Network Events)

## Escalation Steps

**If Client cannot join network:**
1. Review [Knowledge Base for Twingate Client](https://help.twingate.com)
2. Collect Twingate Client logs from affected devices and submit to support

**If Client cannot connect to Resource:**
1. Review Knowledge Base for Twingate Client
2. Collect both **Client logs** and **Connector logs** and submit to support

## Gotchas
- Windows requires two separate checks (Network Interface enabled AND Service running) not needed on other platforms
- Windows users must explicitly declare Domain Controllers as Resources — omitting this is a common connectivity failure
- Resource ambiguity (multiple Resources matching the same address) can silently break connectivity
- Regional network blocks can prevent Twingate network join entirely, not just Resource access

## Configuration Values
None specified — diagnostics are procedural/UI-based.

## Related Docs
- [Twingate Docs](https://docs.twingate.com)
- [Twingate Help Center Knowledge Base](https://help.twingate.com)
- [Known Incompatibilities](https://help.twingate.com) — check before assuming Client conflict is unique
- [Twingate Forum](https://forum.twingate.com)
- [Service Status](https://status.twingate.com)
- [Twingate Changelog](https://twingate.com/changelog)
- [Subscription Management](https://help.twingate.com)