# How to Cloak strongDM with Twingate

## Summary
Hides strongDM gateways behind Twingate to eliminate publicly exposed TCP/IP ports. The strongDM gateway's advertised host is changed to an internal hostname/IP registered as a Twingate Resource, making the network perimeter invisible externally.

## Key Information
- strongDM default proxy port: **5000**
- No inbound firewall ports need to be opened on the host
- strongDM gateway does not need a publicly resolvable IP or hostname after configuration
- Pattern mirrors Twingate's Bastion host cloaking approach

## Prerequisites
- Existing strongDM gateway deployed on a private subnet
- Twingate account with Admin console access
- Twingate Client application installed on end-user devices

## Step-by-Step

1. **Deploy Twingate Connector** on the same private subnet as the strongDM gateway
2. **Add strongDM gateway as a Twingate Resource** via the Twingate Admin console using its internal hostname or IP address
3. **Apply port restriction** to the Resource (default: port 5000)
4. **Update strongDM advertised host** in the strongDM Admin UI — change it to the internal hostname/IP configured as the Twingate Resource

## Configuration Values

| Parameter | Value |
|-----------|-------|
| strongDM default proxy port | `5000` |
| strongDM setting to change | Advertised host (in strongDM Admin UI) |
| Twingate Resource address | Internal hostname or IP of strongDM gateway |

## Testing

1. Attempt strongDM resource access **without** Twingate connected → should be **blocked**
2. Connect via Twingate Client
3. Attempt strongDM resource access again → should **succeed**

## Gotchas
- The strongDM **advertised host** must be updated to the internal address; leaving it as a public hostname defeats the cloaking
- Port restriction must match the actual strongDM proxy port (verify if changed from default 5000)
- Connector must be on the **same private subnet** as the gateway to reach it internally

## Related Docs
- [Twingate Connector deployment](https://www.twingate.com/docs/connector)
- [Adding Resources in Twingate Admin console](https://www.twingate.com/docs/resources)
- [Port restrictions](https://www.twingate.com/docs/port-restrictions)
- [Cloaking Bastion hosts](https://www.twingate.com/docs/bastion-cloaking)
- [Twingate Client applications](https://www.twingate.com/docs/clients)