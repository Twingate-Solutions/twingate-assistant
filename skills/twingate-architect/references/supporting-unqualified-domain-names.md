# Supporting Unqualified Domain Names

## Summary
Twingate supports accessing private resources via unqualified domain names (e.g., `http://employeeportal`) instead of FQDNs. This requires defining the unqualified name as a separate Resource in the Admin Console and configuring search domains on the Connector host.

## Key Information
- Unqualified resource must be added **in addition to** the FQDN resource, not as a replacement
- Twingate uses split-tunneling; without the unqualified name as a Resource, traffic won't be intercepted
- Search domains are configured at the OS/container level on the Connector machine
- Connector does **not** need to restart after search domain changes

## Prerequisites
- Existing FQDN Resource already defined in Admin Console
- Access to Connector host machine or container configuration
- Admin Console access to create Resources

## Step-by-Step

### 1. Define Resources in Admin Console
- Create Resource for unqualified name: `employeeportal`
- Keep existing Resource for FQDN: `employeeportal.yourcompany.com`
- Both must exist simultaneously

### 2. Set Search Domain on Connector Host

**Docker (non-ECS):** Add before `--restart=unless-stopped` flag:
```
--dns-search yoursearchdomain.com
```

**Ubuntu:**
```bash
# Edit /etc/systemd/resolved.conf
DOMAINS=yourcompany.com
sudo systemctl restart systemd-resolved
```

**CentOS/Fedora:**
```bash
nmcli dev status
sudo nmcli con mod "YOUR CONNECTION NAME" ipv4.dns-search "yourcompany.com"
sudo systemctl restart NetworkManager
```

**AWS ECS:** Configure via Network Settings → Advanced Container Configuration in the console UI.

## Configuration Values
| Platform | Setting | Location |
|---|---|---|
| Docker | `--dns-search <domain>` | Run command flag |
| Ubuntu | `DOMAINS=<domain>` | `/etc/systemd/resolved.conf` |
| CentOS/Fedora | `ipv4.dns-search` | nmcli connection property |
| AWS ECS | DNS Search Domains | Container Network Settings |

## Gotchas
- **Browser behavior:** Browsers may interpret unqualified names as search queries. Force URL interpretation by prepending `http://` explicitly (e.g., `http://employeeportal`); browser history will remember it afterward
- **Resolution prerequisite:** `nslookup employeeportal` must resolve on the Connector host before it can work through Twingate
- **Client-side IP range:** Successful resolution on a Client device should return an IP in `100.64.0.0–100.127.255.255` (Twingate virtual IP range)
- Omitting the unqualified Resource causes connection errors even if search domains are correctly set

## Troubleshooting Checklist
1. Run `nslookup <unqualified-name>` on Connector host — must resolve
2. Run same lookup on Client device — should return `100.64.x.x–100.127.x.x`
3. In browser, prefix with `http://` to force domain interpretation

## Related Docs
- Twingate Resource configuration (Admin Console)
- Split tunneling behavior
- Connector deployment guides (Docker, ECS, Ubuntu, CentOS)