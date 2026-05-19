# Supporting Unqualified Domain Names in Twingate

## Summary
Twingate supports access to resources via unqualified domain names (e.g., `http://employeeportal`) instead of FQDNs. This requires defining the unqualified name as a separate Resource in addition to the FQDN, and configuring search domains on the Connector host.

## Key Information
- Unqualified domain Resource must be added **in addition to** the FQDN Resource, not as a replacement
- Twingate uses split-tunneling, so the Client must explicitly know to intercept unqualified domain traffic
- Connector inherits search domains from the host OS — no Connector restart needed for search domain changes
- Client resolves unqualified names to virtual IPs in the `100.64.0.0–100.127.255.255` range

## Prerequisites
- Existing FQDN Resource already defined in Admin Console
- Access to Connector host to configure DNS search domains
- Appropriate OS-level permissions (sudo)

## Step-by-Step

### 1. Define Resources in Admin Console
- Create Resource for FQDN: `employeeportal.yourcompany.com`
- Create **separate** Resource for unqualified name: `employeeportal`

### 2. Set Search Domain on Connector Host

**Docker (non-ECS):** Add before `--restart=unless-stopped` in run command:
```
--dns-search yoursearchdomain.com
```

**AWS ECS:** Set via Network Settings → Advanced Container Configuration.

**Ubuntu:**
```bash
# Edit /etc/systemd/resolved.conf
DOMAINS=yourcompany.com
sudo systemctl restart systemd-resolved
```

**CentOS/Fedora:**
```bash
nmcli dev status
sudo nmcli con mod "CONNECTION NAME" ipv4.dns-search "yourcompany.com"
sudo systemctl restart NetworkManager
```

## Configuration Values
| Platform | Parameter | Location |
|---|---|---|
| Docker | `--dns-search <domain>` | Docker run command |
| Ubuntu | `DOMAINS=<domain>` | `/etc/systemd/resolved.conf` |
| CentOS/Fedora | `ipv4.dns-search "<domain>"` | nmcli connection config |

## Gotchas
- **Both** unqualified and FQDN Resources are required — omitting either causes connection errors
- Web browsers may interpret unqualified names as search queries; force URL interpretation by prefixing with `http://` (browser history will cache the behavior afterward)
- Search domain must resolve on the Connector host first — verify with `nslookup employeeportal` on the Connector machine before troubleshooting the Client

## Debugging Checklist
1. On Connector host: `nslookup employeeportal` must resolve successfully
2. On Client device: same lookup should resolve to `100.64.x.x–100.127.x.x` range
3. For browsers: explicitly type `http://employeeportal` to force domain interpretation

## Related Docs
- Twingate Resources configuration (Admin Console)
- Split-tunneling behavior documentation
- Connector deployment guides (Docker, ECS, Ubuntu, CentOS)