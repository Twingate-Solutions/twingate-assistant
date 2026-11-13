---
source: https://help.twingate.com/articles/5974826840-unable-to-access-a-resource
type: help
fetched: 2026-11-13
source_version: 0331376094e7013760a26c0ad91d6d83fe8b32c316cf34df4099b1afe0589094
trust: official
---

# Page Title
Unable to access a Resource (Twingate Help Center)

## Summary
Troubleshooting checklist for cases where a user cannot reach a Twingate Resource. Causes are ordered from most to least common, covering permissions, DNS interception, client-side interference, network blocking, Connector-side resolution, and destination availability.

## Key Information
- Applies to: Twingate Client and Resources.
- If the Remote Network shows green but the Resource is missing from the Client's Resource list (tray menu on Windows/macOS), it is likely a permissions problem. A Resource not shown in the client is unreachable.
- DNS Resources are first "resolved" by the Client (if the lookup matches the user's ACL), then the Connector performs the real DNS lookup. A wrong or failed Connector resolution breaks the connection.
- Network Traffic in the Admin Console shows flows reaching the Connector. No flow means the issue is likely at the Client level. A flow means checking Connector-to-Resource access.

## Prerequisites
- Admin Console access (to check Groups and Network Traffic).
- Shell access to the Connector host (systemd or AWS AMI deployments) for connectivity tests.
- For support escalation: a Technical Support Entitlement.

## Step-by-Step Troubleshooting
1. **Check authorization:** confirm the user is in a Group that contains the Resource.
2. **Check Client DNS:** run `nslookup` or `dig` on the Resource name. It should return a CGNAT IP, not the real IP. If not, something resolves the lookup before Twingate.
3. **Check the hosts file:** remove entries for the Resource. Windows: `c:\windows\system32\drivers\etc\hosts`; macOS/Linux: `/etc/hosts`.
4. **Check for incompatible software:** endpoint security, DNS, VPN, or VPN-like tools (see Known Incompatibilities).
5. **Check outbound access:** the device must reach `*.twingate.com` and the full Google Cloud Provider external IP range.
6. **Review Network Traffic** in the Admin Console.
7. **Verify the destination is up:** SSH to the Connector and test the port, e.g. `curl -v telnet://<host>:<port>`.
8. **(DNS Resources)** Run `dig` or `nslookup` from the Connector to confirm the correct real IP.
9. **Consider geo blocking:** Google Cloud Platform blocks some regions/countries (see Unsupported Regions).
10. **Consider DNS rebind protection:** for private IP/CIDR Resources resolved via public DNS, routers/ISPs may block the lookup, returning an empty `dig`/`nslookup` response.

## Configuration Values
- Domains to allow: `*.twingate.com`
- IP ranges: Google Cloud Provider external IPs (list is updated periodically by Google)
- Test command: `curl -v telnet://<host>:<port>` (run from the Connector)

## Gotchas
- Port tests/scans from the Client side to a Twingate Resource give false positives. Test from the Connector instead.
- Browser access to `*.twingate.com` may work while other Controller/Relay services are geo-blocked.
- The GCP IP list changes over time, so firewall allowlists can go stale.
- Local hosts file entries bypass Twingate DNS interception.

## Related Docs
- How DNS Works with Twingate
- Known Incompatibilities
- Unsupported Regions
- Address Resolution of Resources
- TCP/IP port tests or scans produce inaccurate results
- Collecting detailed client logs, and opening a support request (include timestamps, Resource name/IP, and steps tried)