# Supporting Unqualified Domain Names

## Summary
Twingate supports accessing private resources via short/unqualified domain names (e.g., `http://employeeportal`) instead of FQDNs. This requires defining the unqualified name as a separate Resource in addition to the FQDN, and configuring search domains on the Connector host.

## Key Information
- Unqualified names must be added as **separate Resources** alongside their FQDN equivalents
- The Connector uses the host machine's configured search domains for DNS resolution
- Twingate assigns virtual IPs in the `100.64.0.0–100.127.255.255` range

## Prerequisites
- Existing Twingate setup with Admin Console access
- FQDN Resource already defined (e.g., `employeeportal.yourcompany.com`)
- Access to Connector host to configure DNS search domains

## Step-by-Step

### 1. Define Resources in Admin Console
- Add unqualified name (e.g., `employeeportal`) as a **new, separate Resource**
- Keep the existing FQDN Resource (`employeeportal.yourcompany.com`)
- Both must exist to avoid connection errors

### 2. Set Search Domain on Connector Host

**Docker (non-ECS):** Add before `--restart=unless-stopped` in run command:
```
--dns-search yoursearchdomain.com
```

**AWS ECS:** Set under Network Settings → Advanced Container Configuration

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
| Platform | Config Location | Parameter |
|----------|----------------|-----------|
| Docker | Run command flag | `--dns-search <domain>` |
| Ubuntu | `/etc/systemd/resolved.conf` | `DOMAINS=` |
| CentOS/Fedora | nmcli | `ipv4.dns-search` |

## Gotchas
- **Do not replace** the FQDN Resource — add the unqualified name as an additional Resource; omitting FQDN causes connection errors
- Connector restart is **not required** for search domain changes on the host
- Web browsers may interpret unqualified names as search queries — force URL behavior by prefixing with `http://` (e.g., `http://employeeportal`)
- If `nslookup employeeportal` fails on the Connector host, Twingate cannot resolve it either

## Troubleshooting Checklist
1. On Connector VM: `nslookup employeeportal` — must resolve successfully
2. On Client device: same lookup should return IP in `100.64.0.0–100.127.255.255`
3. In browser: explicitly type `http://employeeportal` to prevent search-term interpretation

## Related Docs
- Twingate Resources configuration (Admin Console)
- Split tunneling behavior
- Connector deployment guides