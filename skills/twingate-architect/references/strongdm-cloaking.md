---
source: https://www.twingate.com/docs/strongdm-cloaking
type: docs
fetched: 2026-08-14
source_version: 5e06ed1953eb5394e30ded396a26a396c878d558eaaa00c9c96d4bdc2c24deb2
---

# How to Cloak strongDM with Twingate

## Summary
Twingate can hide strongDM gateways behind a private network, eliminating the need for publicly exposed TCP/IP ports. This makes the network perimeter invisible externally by routing strongDM traffic through a Twingate Connector on the same private subnet.

## Key Information
- strongDM by default requires a publicly exposed TCP/IP port
- Twingate removes inbound firewall port requirements entirely
- strongDM gateway no longer needs a publicly resolvable IP or hostname after setup
- strongDM proxy default port: **5000**

## Prerequisites
- Active Twingate account with Admin console access
- Deployed strongDM gateway on a private subnet
- Access to strongDM Admin UI
- Twingate Client application installed on end-user devices

## Step-by-Step

1. **Deploy Twingate Connector** onto the same private subnet as the strongDM gateway

2. **Add strongDM as a Twingate Resource**
   - In Twingate Admin console, add the internal hostname or IP of the strongDM gateway
   - Apply port restriction (default: port 5000)

3. **Update strongDM Gateway advertised host**
   - In strongDM Admin UI, change the gateway's advertised host to the internal hostname/IP configured as the Twingate Resource

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Default strongDM proxy port | `5000` |
| Twingate port restriction | Set to match strongDM proxy port |

## Testing
1. Attempt to connect to strongDM resources **without** Twingate connected → should be blocked
2. Connect via Twingate Client app
3. Attempt to access strongDM resources again → should succeed

## Gotchas
- The Connector must be on the **same private subnet** as the strongDM gateway for internal routing to work
- strongDM's advertised host must be updated to the internal address — leaving it as a public address defeats the cloaking
- No inbound firewall ports should be opened after this configuration

## Related Docs
- [Cloaking Bastion Hosts](https://www.twingate.com/docs) — same pattern applies
- [Deploy a Twingate Connector](https://www.twingate.com/docs)
- [Add a Resource (Twingate Admin Console)](https://www.twingate.com/docs)
- [Port Restrictions](https://www.twingate.com/docs)
- Twingate Client apps (platform-specific)