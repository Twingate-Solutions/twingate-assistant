# How to Cloak strongDM with Twingate

## Summary
This guide explains how to make strongDM gateways private by routing traffic through Twingate, eliminating the need for publicly exposed TCP/IP ports. The result is no inbound firewall rules required and an invisible network perimeter.

## Key Information
- strongDM normally requires a publicly exposed TCP/IP port
- Twingate removes the need for a public IP or resolvable hostname on the strongDM gateway
- strongDM default proxy port: **5000**
- Approach mirrors the Bastion host cloaking pattern

## Prerequisites
- Twingate Connector deployed on the same private subnet as the strongDM gateway
- Access to Twingate Admin Console
- Access to strongDM Admin UI
- Twingate Client installed on end-user devices

## Step-by-Step

1. **Deploy Twingate Connector** on the same private subnet as the strongDM gateway

2. **Add strongDM as a Twingate Resource** via the Twingate Admin Console:
   - Use the internal hostname or IP address of the strongDM gateway
   - Apply a port restriction (default: port **5000**)

3. **Update strongDM Gateway advertised host**:
   - In strongDM Admin UI, change the `advertised host` setting to the internal hostname or IP configured as the Twingate Resource

## Configuration Values

| Parameter | Value |
|-----------|-------|
| strongDM default proxy port | `5000` |
| Twingate Resource type | Internal hostname or IP |
| Port restriction | Set to `5000` (or match strongDM config) |

## Testing Procedure
1. Attempt strongDM resource access **without** Twingate connected — verify access is **blocked**
2. Connect to Twingate via the client app
3. Attempt strongDM resource access again — verify connection **succeeds**

## Gotchas
- The Connector must be on the **same private subnet** as the strongDM gateway, not just network-adjacent
- The strongDM `advertised host` must be updated to the internal address; leaving it as a public address defeats the cloaking
- Port restrictions in Twingate must match the port strongDM is actually listening on

## Related Docs
- [Cloaking Bastion Hosts](https://www.twingate.com/docs) — same pattern applied here
- Twingate Connector deployment
- Adding Resources in Twingate Admin Console
- Port restrictions on Resources
- Twingate Client installation by platform