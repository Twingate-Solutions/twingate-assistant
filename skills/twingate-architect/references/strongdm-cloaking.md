# How to Cloak strongDM with Twingate

## Summary
Hides strongDM gateway from public internet by routing traffic through Twingate, eliminating the need for publicly exposed TCP/IP ports. The strongDM gateway's advertised host is changed to an internal address accessible only via Twingate.

## Key Information
- strongDM by default requires a publicly exposed TCP/IP port
- After cloaking: no inbound firewall ports required, network perimeter invisible externally
- strongDM gateway no longer needs a publicly resolvable IP or hostname
- Default strongDM proxy port: **5000**

## Prerequisites
- Twingate Connector deployed on the same private subnet as the strongDM gateway
- Access to Twingate Admin Console
- Access to strongDM Admin UI

## Step-by-Step

1. **Deploy Twingate Connector** on the same private subnet as the strongDM gateway
2. **Add strongDM gateway as a Twingate Resource** via Twingate Admin Console using the internal hostname or IP address
3. **Apply port restriction** on the Resource (default port: 5000)
4. **Update strongDM gateway advertised host** in strongDM Admin UI to the internal hostname/IP configured as the Twingate Resource

## Configuration Values
| Parameter | Value |
|-----------|-------|
| strongDM proxy port | `5000` (default) |

## Testing
1. Disconnect from Twingate → verify strongDM resources are **inaccessible**
2. Connect via Twingate Client → verify strongDM resources are **accessible**

## Gotchas
- Twingate Connector must be on the **same private subnet** as the strongDM gateway (not just reachable — co-location on subnet is specified)
- Must change strongDM's `advertised host` setting; simply adding a Twingate Resource is insufficient
- Port restriction must match strongDM's actual listening port if changed from default 5000

## Related Docs
- [Cloaking Bastion Hosts](https://www.twingate.com/docs) — referenced as analogous pattern
- Twingate Connector deployment
- Twingate Admin Console — adding Resources with port restrictions
- Twingate Client installation by platform