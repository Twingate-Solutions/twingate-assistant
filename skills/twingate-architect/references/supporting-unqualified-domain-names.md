# Supporting Unqualified Domain Names

## Summary
Twingate supports accessing private resources via unqualified domain names (e.g., `http://employeeportal`) instead of FQDNs. This requires defining the unqualified name as a separate Resource in the Admin Console and configuring search domains on the Connector host.

## Key Information
- Unqualified domain resources must be added **in addition to** the FQDN resource, not as a replacement
- The Connector uses the host machine's configured search domains for DNS resolution
- Twingate assigns virtual IPs in the `100.64.0.0–100.127.255.255` range for resolved resources

## Prerequisites
- Existing Twingate setup with Connector deployed
- FQDN resource already defined in Admin Console
- Access to Connector host OS or container configuration

## Step-by-Step

### 1. Define Resources in Admin Console
- Create a resource for the unqualified name (e.g., `employeeportal`)
- Keep the existing FQDN resource (e.g., `employeeportal.yourcompany.com`)
- Both must exist simultaneously

### 2. Set Search Domain on Connector Host

**Docker (non-ECS):** Add before `--restart=unless-stopped` in the run command:
```
--dns-search yoursearchdomain.com
```

**AWS ECS:** Set via Network Settings in Advanced Container Configuration.

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
| Platform | Config Location | Parameter |
|----------|----------------|-----------|
| Docker | Run flags | `--dns-search <domain>` |
| Ubuntu | `/etc/systemd/resolved.conf` | `DOMAINS=` |
| CentOS/Fedora | nmcli | `ipv4.dns-search` |

## Gotchas
- Omitting the unqualified name as a Resource causes silent failures — the Client won't intercept that traffic
- Connector restart is **not** required after search domain changes on the host
- Web browsers may interpret unqualified names as search queries; force URL by prepending `http://` (e.g., `http://employeeportal`). Browser history will cache the correct behavior after first use.
- DNS must resolve the unqualified name on the Connector host before it will work through Twingate

## Troubleshooting Checklist
1. Run `nslookup employeeportal` on the Connector VM — must resolve successfully
2. Run same lookup on a Client device — should return IP in `100.64.0.0–100.127.255.255`
3. For browsers, explicitly type `http://employeeportal` to force domain interpretation

## Related Docs
- Twingate Resources configuration (Admin Console)
- Split tunneling behavior
- Connector deployment guides