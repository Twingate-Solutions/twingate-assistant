# How to Cloak strongDM with Twingate

## Summary
Hides strongDM gateways behind Twingate so they require no publicly exposed TCP/IP ports. The strongDM gateway becomes accessible only through Twingate, making the network perimeter invisible externally.

## Key Information
- Eliminates need for public IP or publicly resolvable hostname on strongDM gateway
- No inbound firewall ports required on the host
- strongDM default proxy port: **5000**
- Analogous approach to cloaking Bastion hosts

## Prerequisites
- Twingate Connector deployed on same private subnet as strongDM gateway
- Access to Twingate Admin Console
- Access to strongDM Admin UI
- Twingate Client installed on end-user devices

## Step-by-Step

1. **Deploy Twingate Connector** on the same private subnet as the strongDM gateway
2. **Add strongDM gateway as a Twingate Resource** via Twingate Admin Console using its internal hostname or IP address
3. **Apply port restriction** to the Resource (default strongDM proxy port: `5000`)
4. **Update strongDM gateway advertised host** in strongDM Admin UI — set it to the internal hostname/IP configured as the Twingate Resource

## Testing Procedure
1. While **disconnected** from Twingate, attempt to access strongDM resources — access should be **blocked**
2. Connect to Twingate via Client app
3. Attempt strongDM resource access again — connection should **succeed**

## Configuration Values
| Parameter | Value |
|-----------|-------|
| strongDM default proxy port | `5000` |
| Connector placement | Same private subnet as strongDM gateway |
| Resource address | Internal hostname or IP of strongDM gateway |

## Gotchas
- The strongDM gateway's **advertised host must be updated** to the internal address — leaving it as a public address defeats the cloaking
- Port restriction must match the actual strongDM proxy port in use (verify if non-default)

## Related Docs
- Twingate Connector deployment
- Adding Resources in Twingate Admin Console
- Port restrictions on Resources
- Cloaking Bastion host servers
- Twingate Client installation (platform-specific)