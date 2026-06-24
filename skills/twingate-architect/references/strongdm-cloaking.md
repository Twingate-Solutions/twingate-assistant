# How to Cloak strongDM with Twingate

## Summary
Hides strongDM gateway ports from public internet by routing traffic through Twingate instead of exposing TCP/IP ports publicly. Eliminates inbound firewall rules and makes the network perimeter invisible externally. Mirrors the Bastion host cloaking pattern.

## Key Information
- strongDM default proxy port: **5000**
- No inbound firewall ports required after configuration
- strongDM gateway no longer needs a publicly resolvable IP or hostname
- Works by placing a Twingate Connector on the same subnet as the strongDM gateway

## Prerequisites
- Twingate Connector deployed and accessible
- Access to Twingate Admin Console
- Access to strongDM Admin UI
- strongDM gateway running on a private subnet

## Step-by-Step

1. **Deploy Twingate Connector** on the same private subnet as the strongDM gateway
2. **Add strongDM as a Twingate Resource** via Twingate Admin Console:
   - Use the internal hostname or IP of the strongDM gateway
   - Apply port restriction (default: port **5000**)
3. **Update strongDM gateway advertised host** in strongDM Admin UI:
   - Change the advertised host to the internal hostname/IP configured as the Twingate Resource

## Configuration Values

| Parameter | Value |
|-----------|-------|
| strongDM default proxy port | `5000` |
| Resource type | Internal hostname or IP |

## Testing

1. Disconnect from Twingate → attempt strongDM connection → **should fail**
2. Connect via Twingate Client
3. Attempt strongDM connection again → **should succeed**

## Gotchas
- The strongDM `advertised host` setting must be changed to the internal address — leaving it as a public hostname defeats the cloaking
- Connector must be on the **same private subnet** as the gateway to reach the internal address
- Port restriction in Twingate must match the actual strongDM proxy port (verify if port 5000 has been customized)

## Related Docs
- [Cloaking Bastion Hosts](https://www.twingate.com/docs/) — same pattern applies
- [Deploy a Twingate Connector](https://www.twingate.com/docs/)
- [Add a Resource with Port Restrictions](https://www.twingate.com/docs/)
- [Twingate Client Installation](https://www.twingate.com/docs/)