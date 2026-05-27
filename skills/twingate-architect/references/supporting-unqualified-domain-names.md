# Supporting Unqualified Domain Names

## Summary
Twingate supports access to resources via unqualified domain names (e.g., `http://employeeportal`) with additional configuration. This requires defining the unqualified name as a separate Resource and configuring search domains on the Connector host.

## Key Information
- Unqualified domain names must be added as **separate Resources** alongside the FQDN—not as replacements
- The Connector uses search domains configured on its host OS
- Client resolves unqualified names to virtual IPs in range `100.64.0.0–100.127.255.255`

## Prerequisites
- Existing Twingate setup with Connector deployed
- Admin Console access to define Resources
- Host-level access to Connector machine for search domain configuration

## Step-by-Step

### 1. Define Resources in Admin Console
- Add unqualified name (e.g., `employeeportal`) as a Resource
- Keep existing FQDN Resource (e.g., `employeeportal.yourcompany.com`)
- Both must exist simultaneously

### 2. Set Search Domain on Connector Host

**Docker (non-ECS):** Add before `--restart=unless-stopped` in run command:
```
--dns-search yoursearchdomain.com
```

**Ubuntu:** Edit `/etc/systemd/resolved.conf`:
```
DOMAINS=yourcompany.com
```
Then: `sudo systemctl restart systemd-resolved`

**CentOS/Fedora:**
```bash
nmcli dev status
sudo nmcli con mod "CONNECTION NAME" ipv4.dns-search "yourcompany.com"
sudo systemctl restart NetworkManager
```

**AWS ECS:** Configure via Network Settings → Advanced Container Configuration

## Configuration Values
| Platform | Parameter | Example |
|----------|-----------|---------|
| Docker | `--dns-search` | `--dns-search yourcompany.com` |
| Ubuntu resolved.conf | `DOMAINS=` | `DOMAINS=yourcompany.com` |
| nmcli | `ipv4.dns-search` | `"yourcompany.com"` |

## Gotchas
- **Must define both** unqualified and FQDN Resources—omitting either causes connection errors
- Connector restart not required for search domain changes on the host
- Web browsers may interpret unqualified names as search queries; explicitly prefix with `http://` to force domain resolution (browser caches this after first use)
- `nmcli con mod` requires the Connection **name**, not the Device name

## Troubleshooting
1. On Connector VM: `nslookup employeeportal` — must resolve before Twingate can work
2. On Client device: same lookup should return IP in `100.64.0.0–100.127.255.255`
3. Browser issues: type full `http://employeeportal` explicitly

## Related Docs
- Twingate Resources configuration
- Connector deployment (Docker, ECS, Ubuntu, CentOS)
- Split tunneling behavior