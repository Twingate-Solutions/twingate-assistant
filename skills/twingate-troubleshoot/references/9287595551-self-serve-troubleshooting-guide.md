---
source: https://help.twingate.com/articles/9287595551-self-serve-troubleshooting-guide
type: help
fetched: 2026-10-04
source_version: 789d5338b8421e479c0ad274cdf77e0a7a656f4005fb17b32ac7ddb0fc65ef49
trust: official
---

# Self-Serve Troubleshooting Guide

## Page Title
Self-Serve Troubleshooting Guide

## Summary
High-level troubleshooting reference for common Twingate issues. Covers two primary failure modes: Client unable to join the Twingate network, and Client unable to connect to a specific Resource. Points to log collection and KB articles for escalation.

## Key Information

### Client Cannot Join Twingate Network
- Verify Twingate network interface exists on the device
- **(Windows only)** Confirm the network interface is enabled
- **(Windows only)** Confirm the Twingate Service is running
- Check that outbound ports are not blocked by the local network
- Check for incompatible clients or agents running concurrently
- Check if the device's region blocks Twingate access

### Client Cannot Connect to a Resource
- Validate the Resource definition is correctly configured
- Verify the user has permission to access the Resource
- **(Windows only)** Ensure Domain Controllers are declared as Resources
- Review Network Events for the specific Resource in the Admin Console
- Check for Resource ambiguity (overlapping CIDR ranges or hostnames)

## Escalation Steps
**For network join failures:** Collect Client logs from affected devices.  
**For Resource connection failures:** Collect both Client logs and Connector logs.

## Configuration Values
- Outbound ports must be open (specific ports not listed on this page — see Connector/firewall docs)

## Gotchas
- Windows requires both the network interface to be enabled **and** the Twingate Service to be running — two separate checks
- Domain Controllers must be explicitly declared as Resources on Windows environments
- Resource ambiguity (overlapping definitions) can silently cause connection failures
- Regional network blocks may prevent Client from joining the network entirely

## Additional Self-Serve Resources
| Resource | Purpose |
|----------|---------|
| [Twingate Docs](https://docs.twingate.com) | Full product documentation |
| [Twingate Help Center](https://help.twingate.com) | Knowledge base & KB articles |
| Known Incompatibilities KB | Check for conflicting software |
| [Twingate Forum](https://forum.twingate.com) | Community discussion |
| [Subscription Management](https://help.twingate.com) | Billing |
| [Service Status](https://status.twingate.com) | Twingate uptime/incidents |
| [Twingate Changelog](https://www.twingate.com/changelog) | New features and fixes |

## Related Docs
- Twingate Client Knowledge Base
- Client log collection guide
- Connector log collection guide
- Connector firewall/port requirements