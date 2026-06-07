# How to Cloak strongDM with Twingate

## Summary
Hides strongDM gateway ports from public internet by routing traffic through Twingate, eliminating the need for publicly exposed TCP/IP ports. The strongDM gateway's advertised host is changed to an internal address accessible only via Twingate Connector.

## Key Information
- strongDM default proxy port: **5000**
- No inbound firewall ports required after configuration
- Twingate Connector must be on the same private subnet as strongDM gateway
- strongDM gateway no longer needs a publicly resolvable IP or hostname

## Prerequisites
- Twingate Connector deployed
- Access to Twingate Admin Console
- Access to strongDM Admin UI
- strongDM gateway running on a private subnet

## Step-by-Step

1. **Deploy Twingate Connector** on the same private subnet as the strongDM gateway
2. **Add Resource** in Twingate Admin Console:
   - Add the internal hostname or IP of the strongDM gateway
   - Apply port restriction (port 5000 by default)
3. **Update strongDM gateway** in strongDM Admin UI:
   - Change the **advertised host** to the internal hostname/IP configured as a Twingate Resource

## Configuration Values

| Parameter | Value |
|-----------|-------|
| strongDM default proxy port | `5000` |
| Advertised host | Internal hostname or IP (set in strongDM Admin UI) |

## Testing
1. Attempt strongDM resource access **without** Twingate connected → verify blocked
2. Connect Twingate Client
3. Attempt strongDM resource access again → verify success

## Gotchas
- Connector must be on the **same private subnet** as the gateway — not just reachable, co-located
- Port restriction must match strongDM's configured proxy port (default 5000, may differ if changed)
- strongDM's advertised host must be updated; leaving it as the public address defeats the cloaking

## Related Docs
- [Cloaking Bastion Hosts](https://www.twingate.com/docs) (referenced as similar pattern)
- Twingate Connector deployment
- Adding Resources in Twingate Admin Console
- Port restrictions on Resources
- Twingate Client installation by platform