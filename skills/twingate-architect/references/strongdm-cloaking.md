# How to Cloak strongDM with Twingate

## Summary
Hides strongDM gateways behind Twingate so no public TCP/IP ports are required. The strongDM gateway becomes accessible only through Twingate, eliminating inbound firewall rules and public IP/hostname exposure.

## Key Information
- strongDM default proxy port: **5000**
- No inbound firewall ports need to be opened on the strongDM host
- strongDM gateway does not need a publicly resolvable IP or hostname after configuration
- Approach mirrors Twingate's Bastion host cloaking pattern

## Prerequisites
- Twingate account with Admin console access
- strongDM account with Admin UI access
- strongDM gateway deployed on a private subnet
- Twingate Connector deployable to the same private subnet

## Step-by-Step

1. **Deploy Twingate Connector** onto the same private subnet as the strongDM gateway
2. **Add strongDM gateway as a Twingate Resource** in the Twingate Admin console using the internal hostname or IP address
3. **Apply port restriction** on the Resource (port 5000 by default)
4. **Update strongDM gateway advertised host** in the strongDM Admin UI — set it to the internal hostname or IP configured as the Twingate Resource

## Configuration Values

| Parameter | Value |
|-----------|-------|
| strongDM proxy port | `5000` (default) |
| Twingate Resource address | Internal hostname or IP of strongDM gateway |
| strongDM setting to change | Advertised host |

## Testing

1. While **disconnected** from Twingate, attempt to connect to strongDM resources — access should be **blocked**
2. Connect via Twingate Client application
3. Retry strongDM resource access — connection should **succeed**

## Gotchas
- Connector must be on the **same private subnet** as the strongDM gateway, not just the same network region
- The strongDM advertised host must match exactly what is registered as the Twingate Resource
- If strongDM port is changed from 5000, update the Twingate Resource port restriction accordingly

## Related Docs
- [Twingate Connector deployment](https://www.twingate.com/docs/connectors)
- [Adding Resources in Twingate Admin console](https://www.twingate.com/docs/resources)
- [Port restrictions on Resources](https://www.twingate.com/docs/port-restrictions)
- [Cloaking Bastion host servers](https://www.twingate.com/docs/bastion-cloaking)
- [Twingate Client applications](https://www.twingate.com/docs/clients)