# Cloak strongDM with Twingate

## Summary
Hides strongDM gateways behind Twingate to eliminate publicly exposed TCP/IP ports. The strongDM gateway's advertised host is set to an internal address exposed only via Twingate, making the network perimeter invisible externally.

## Key Information
- strongDM by default requires a publicly exposed TCP/IP port
- Twingate removes the need for public IP/hostname on strongDM gateways
- No inbound firewall ports required after cloaking
- strongDM default proxy port: **5000**
- Similar pattern to cloaking Bastion host servers

## Prerequisites
- Twingate Connector deployed on same private subnet as strongDM gateway
- Access to Twingate Admin Console
- Access to strongDM Admin UI
- Twingate Client installed on end-user devices

## Step-by-Step

1. **Deploy Twingate Connector** on the same private subnet as the strongDM gateway
2. **Add strongDM as a Twingate Resource** via Twingate Admin Console using the internal hostname or IP of the gateway
3. **Apply port restriction** to the Resource (default strongDM proxy port: 5000)
4. **Update strongDM advertised host** in strongDM Admin UI — set it to the internal hostname/IP configured as the Twingate Resource

## Configuration Values

| Parameter | Value |
|---|---|
| strongDM default proxy port | `5000` |
| Twingate Resource address | Internal hostname or IP of strongDM gateway |
| strongDM advertised host | Set to same internal hostname/IP as Twingate Resource |

## Testing

1. **Without Twingate connected** — attempt to connect to strongDM resources; access should be blocked
2. **Connect Twingate Client** on your platform
3. **With Twingate connected** — attempt to access strongDM resources; connection should succeed

## Gotchas
- strongDM's advertised host must match the internal address registered as a Twingate Resource exactly
- Connector must be on the **same private subnet** as the strongDM gateway to reach the internal address
- Port restriction must match the actual port strongDM is listening on (verify if changed from default 5000)

## Related Docs
- [Twingate Connector deployment](https://www.twingate.com/docs/connector)
- [Adding Resources in Twingate Admin Console](https://www.twingate.com/docs/resources)
- [Port restrictions](https://www.twingate.com/docs/port-restrictions)
- [Cloaking Bastion hosts](https://www.twingate.com/docs/bastion-cloaking)
- [Twingate Client platforms](https://www.twingate.com/docs/client)