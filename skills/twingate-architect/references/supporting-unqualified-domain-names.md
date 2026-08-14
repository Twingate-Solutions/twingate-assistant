---
source: https://www.twingate.com/docs/supporting-unqualified-domain-names
type: docs
fetched: 2026-08-14
source_version: a9a1893c4fd3911f4dd51492f9f911c07d62c90491a730d1455928686084761d
---

# Supporting Unqualified Domain Names

## Summary
Twingate supports accessing private resources via unqualified domain names (e.g., `http://employeeportal`) instead of FQDNs. This requires defining the unqualified name as a separate Resource in the Admin Console and configuring search domains on the Connector host.

## Key Information
- Unqualified domain Resource must be added **in addition to** the FQDN Resource, not as a replacement
- Twingate uses split-tunneling, so the Client must explicitly know to intercept unqualified domain traffic
- Connector inherits search domains from its host machine; no Connector restart required for search domain changes
- Successful resolution via Twingate shows IPs in the `100.64.0.0–100.127.255.255` range (virtual IPs)

## Prerequisites
- FQDN Resource already defined in Twingate Admin Console
- Access to Connector host machine to configure DNS search domains

## Step-by-Step

### 1. Define Resources in Admin Console
- Create a Resource for the unqualified name (e.g., `employeeportal`)
- Keep existing FQDN Resource (e.g., `employeeportal.yourcompany.com`)
- Both must exist simultaneously

### 2. Set Search Domain on Connector Host

**Docker (non-ECS):** Add before `--restart=unless-stopped` in run command:
```
--dns-search yoursearchdomain.com
```

**AWS ECS:** Set via Network Settings → Advanced Container Configuration

**Ubuntu:**
```bash
# Edit /etc/systemd/resolved.conf
DOMAINS=yourcompany.com
sudo systemctl restart systemd-resolved
```

**CentOS/Fedora:**
```bash
nmcli dev status
sudo nmcli con mod "CONNECTION_NAME" ipv4.dns-search "yourcompany.com"
sudo systemctl restart NetworkManager
```

## Configuration Values
| Platform | Setting | Location |
|----------|---------|----------|
| Docker | `--dns-search <domain>` | Run command flag |
| Ubuntu | `DOMAINS=` | `/etc/systemd/resolved.conf` |
| CentOS/Fedora | `ipv4.dns-search` | nmcli connection property |
| AWS ECS | DNS Search Domains | Advanced Container Configuration |

## Gotchas
- **Do not replace FQDN Resource** — removing it and only using unqualified name causes connection errors
- **Web browsers** may treat unqualified names as search queries instead of URLs; prefix with `http://` to force URL interpretation. Browser history will cache the behavior afterward.
- `nmcli` requires the **Connection name**, not the Device name
- Search domain changes on the host do not require a Connector restart

## Troubleshooting Checklist
1. On Connector host: `nslookup employeeportal` — must resolve successfully
2. On Client device: same lookup should return IP in `100.64.0.0–100.127.255.255`
3. In browser: explicitly type `http://employeeportal` to avoid search engine redirection

## Related Docs
- Twingate Resource configuration (Admin Console)
- Split-tunneling behavior
- Connector deployment guides (Docker, ECS, Ubuntu, CentOS)