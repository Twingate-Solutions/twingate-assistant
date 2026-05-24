# How to Cloak strongDM with Twingate

## Summary
Hides strongDM gateways behind Twingate so no public TCP/IP ports are required. The strongDM gateway's advertised host is set to an internal address exposed only via Twingate Resource, making the network perimeter invisible externally.

## Key Information
- Default strongDM proxy port: **5000**
- No inbound firewall ports need to be opened on the host
- Twingate Connector must be on the **same private subnet** as the strongDM gateway
- Approach mirrors the Bastion host cloaking pattern

## Prerequisites
- Twingate Connector deployed
- Access to Twingate Admin Console
- Access to strongDM Admin UI
- strongDM gateway running on a private subnet

## Step-by-Step

1. **Deploy Twingate Connector** onto the same private subnet as the strongDM gateway
2. **Add strongDM gateway as a Twingate Resource** via Twingate Admin Console:
   - Use the internal hostname or IP of the strongDM gateway
   - Apply a port restriction (default: port **5000**)
3. **Update strongDM gateway advertised host** in strongDM Admin UI:
   - Change the advertised host to the internal hostname/IP configured as the Twingate Resource

## Configuration Values

| Parameter | Value |
|-----------|-------|
| strongDM default proxy port | `5000` |
| Twingate port restriction | Set to `5000` (or match strongDM config) |
| strongDM advertised host | Internal hostname or IP (same as Twingate Resource) |

## Testing / Verification

1. **Without Twingate connected** — attempt to connect to strongDM resources; access should be **blocked**
2. **Connect Twingate client** for your platform
3. **With Twingate connected** — attempt to connect to strongDM resources; access should **succeed**

## Gotchas
- The strongDM `advertised host` setting must match exactly the internal hostname/IP registered as the Twingate Resource
- Connector placement on the **same subnet** as the gateway is required; cross-subnet routing may not resolve correctly
- Port restriction must match the actual port strongDM listens on (verify if changed from default 5000)

## Related Docs
- [Cloaking Bastion Hosts](https://www.twingate.com/docs/) — same architectural pattern
- [Deploy a Twingate Connector](https://www.twingate.com/docs/)
- [Add a Resource](https://www.twingate.com/docs/)
- [Port Restrictions](https://www.twingate.com/docs/)
- [Twingate Client Apps](https://www.twingate.com/docs/)