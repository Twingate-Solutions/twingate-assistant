# Supporting Unqualified Domain Names

## Summary
Twingate supports accessing private resources via unqualified domain names (e.g., `http://employeeportal` instead of `http://employeeportal.yourcompany.com`). This requires adding the unqualified name as a separate Resource in the Admin Console AND configuring search domains on the Connector host.

## Key Information
- Unqualified resource must be added **in addition to** the FQDN, not as a replacement
- Twingate uses split-tunneling, so the Client must explicitly know to intercept unqualified name traffic
- Virtual IPs resolve in the `100.64.0.0–100.127.255.255` range on Client devices
- Connector inherits search domains from its host OS (no Connector restart required for DNS changes)

## Prerequisites
- Existing FQDN Resource defined in Twingate Admin Console
- Access to Connector host machine to configure DNS search domains

## Step-by-Step

### 1. Define Resources in Admin Console
- Add the unqualified name (e.g., `employeeportal`) as a separate Resource
- Keep the FQDN Resource (e.g., `employeeportal.yourcompany.com`) — do not remove it

### 2. Set Search Domain on Connector Host

**Docker (non-ECS):** Add before `--restart=unless-stopped` in the run script:
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

**AWS ECS:** Configure under Network Settings → Advanced Container Configuration when adding/editing a container.

## Configuration Values
| Platform | Setting | Value |
|----------|---------|-------|
| Docker | CLI flag | `--dns-search <domain>` |
| Ubuntu | File: `/etc/systemd/resolved.conf` | `DOMAINS=yourcompany.com` |
| CentOS/Fedora | nmcli property | `ipv4.dns-search "yourcompany.com"` |

## Gotchas
- **Must define both** unqualified and FQDN Resources — omitting FQDN causes connection errors
- **Browsers may misinterpret** unqualified names as search queries; force URL mode by prepending `http://` (e.g., `http://employeeportal`)
- `nslookup employeeportal` on the Connector host must resolve before it will work through Twingate
- On Client devices, unqualified names should resolve to `100.64.x.x–100.127.x.x` range; if not, DNS search domain is not propagating correctly

## Troubleshooting Checklist
1. SSH into Connector VM → `nslookup employeeportal` must resolve
2. On Client device → same lookup should return IP in `100.64.0.0–100.127.255.255`
3. In browser → explicitly type `http://employeeportal` to avoid search engine redirect

## Related Docs
- Twingate Resources configuration (Admin Console)
- Split tunneling behavior
- Connector deployment guides (Docker, ECS, Ubuntu, CentOS)