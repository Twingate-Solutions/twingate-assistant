# How to Cloak strongDM with Twingate

## Summary
Hides strongDM gateways behind Twingate, eliminating the need for publicly exposed TCP/IP ports. The strongDM gateway becomes accessible only through Twingate, making the network perimeter invisible externally.

## Key Information
- strongDM by default requires a publicly exposed TCP/IP port for SSH/RDP auditing and replay
- Twingate removes the need for public inbound firewall ports or publicly resolvable IPs/hostnames
- Default strongDM proxy port: **5000**
- Approach mirrors the Twingate Bastion host cloaking pattern

## Prerequisites
- Existing strongDM gateway deployed on a private subnet
- Access to Twingate Admin Console
- Access to strongDM Admin UI
- Twingate Client application installed on end-user devices

## Step-by-Step

1. **Deploy Twingate Connector** on the same private subnet as the strongDM gateway
2. **Add strongDM gateway as a Twingate Resource** via Twingate Admin Console using the internal hostname or IP address
3. **Apply port restriction** to the Resource (port 5000 by default)
4. **Update strongDM gateway advertised host** in strongDM Admin UI to use the internal hostname/IP configured as the Twingate Resource

## Configuration Values
| Parameter | Value |
|-----------|-------|
| strongDM default proxy port | `5000` |
| Twingate Resource address | Internal hostname or IP of strongDM gateway |

## Testing
1. Disconnect from Twingate → attempt strongDM resource access → confirm **blocked**
2. Connect via Twingate Client → attempt strongDM resource access → confirm **successful**

## Gotchas
- The strongDM **advertised host** must be changed to the internal address; leaving it as a public address defeats the cloaking
- Twingate Connector must be on the **same private subnet** as the strongDM gateway to reach it
- No inbound firewall rules needed — all connectivity is outbound from the Connector

## Related Docs
- [Cloaking Bastion Host Servers](https://www.twingate.com/docs) (referenced pattern)
- Twingate Connector deployment
- Adding Resources in Twingate Admin Console
- Port restrictions on Resources
- Twingate Client installation by platform