# Supporting Unqualified Domain Names

## Summary
Twingate supports access to resources via unqualified domain names (e.g., `http://employeeportal` instead of `http://employeeportal.yourcompany.com`). This requires defining the unqualified name as a separate Resource in addition to the FQDN, and configuring search domains on the Connector host.

## Key Information
- Unqualified domain Resources must be added **in addition to** FQDN Resources, not as replacements
- Twingate uses split-tunneling; the Client can only intercept traffic for explicitly defined Resources
- Virtual IPs resolve in the `100.64.0.0–100.127.255.255` range on Client devices

## Prerequisites
- Existing FQDN Resource already defined in Twingate Admin Console
- Access to Connector host machine to configure DNS search domains

## Step-by-Step

### 1. Define Resources in Admin Console
- Create a Resource for the unqualified name (e.g., `employeeportal`)
- Keep the existing FQDN Resource (e.g., `employeeportal.yourcompany.com`)
- Both must exist simultaneously

### 2. Set Search Domain on Connector Host

**Docker (non-ECS):**
```
--dns-search yoursearchdomain.com
```
Add this flag before `--restart=unless-stopped` in the generated run script.

**Ubuntu:**
```
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

**AWS ECS:** Configure via Network Settings → Advanced Container Configuration when adding/editing a container instance.

## Gotchas
- Adding only the unqualified name without the FQDN causes connection errors — both must exist
- Connector does **not** require restart after search domain changes on the host OS (Docker may differ)
- Web browsers may interpret unqualified names as search queries; force URL behavior by prefixing with `http://` (e.g., `http://employeeportal`). Browser history will cache correct behavior after first use.

## Troubleshooting Checklist
1. SSH into Connector VM → run `nslookup employeeportal` — must resolve successfully
2. On Client device → run same lookup → should resolve to `100.64.x.x–100.127.x.x` range
3. In browser → explicitly type `http://employeeportal` to prevent search query interpretation

## Configuration Values
| Platform | Config Location | Key Parameter |
|----------|----------------|---------------|
| Docker | Run script flag | `--dns-search <domain>` |
| Ubuntu | `/etc/systemd/resolved.conf` | `DOMAINS=<domain>` |
| CentOS/Fedora | NetworkManager | `ipv4.dns-search "<domain>"` |
| AWS ECS | Container Advanced Network Settings | DNS search domain field |

## Related Docs
- Twingate Resource configuration (Admin Console)
- Split-tunneling behavior
- Connector deployment guides