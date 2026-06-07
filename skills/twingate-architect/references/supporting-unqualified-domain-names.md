# Supporting Unqualified Domain Names

## Summary
Twingate supports accessing private resources via unqualified domain names (e.g., `http://employeeportal`) instead of FQDNs. This requires adding the unqualified name as a separate Resource in the Admin Console and configuring search domains on the Connector host.

## Key Information
- Unqualified domain Resources must be added **in addition to** the FQDN Resource, not as a replacement
- The Connector resolves unqualified names using the host machine's configured search domains
- Twingate virtual IPs resolve in the `100.64.0.0–100.127.255.255` range

## Prerequisites
- Existing FQDN Resource already defined in Twingate Admin Console
- Access to Connector host machine to configure DNS search domains

## Step-by-Step

### 1. Define Resources in Admin Console
- Create a Resource for the unqualified name (e.g., `employeeportal`)
- Keep the existing FQDN Resource (e.g., `employeeportal.yourcompany.com`)
- Both must exist simultaneously

### 2. Set Search Domain on Connector Host

**Docker (non-ECS):** Add before `--restart=unless-stopped` in the run command:
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
sudo nmcli con mod "CONNECTION NAME" ipv4.dns-search "yourcompany.com"
sudo systemctl restart NetworkManager
```

**AWS ECS:** Configure under Network Settings → Advanced Container Configuration

## Configuration Values
| Platform | Config Location | Parameter |
|----------|----------------|-----------|
| Docker | Run command flag | `--dns-search <domain>` |
| Ubuntu | `/etc/systemd/resolved.conf` | `DOMAINS=<domain>` |
| CentOS/Fedora | nmcli | `ipv4.dns-search "<domain>"` |
| AWS ECS | Container Network Settings | DNS Search Domains field |

## Gotchas
- **Must define both** unqualified and FQDN as separate Resources — omitting the unqualified Resource means the Client won't intercept that traffic (split-tunnel limitation)
- **Browsers may treat unqualified names as search terms** — prefix with `http://` (e.g., `http://employeeportal`) to force URL interpretation; browser history will remember it afterward
- Connector restart is **not required** after search domain changes on the host
- Unqualified DNS must resolve on the **Connector machine first** (`nslookup employeeportal`) before Twingate can route it

## Troubleshooting
1. Run `nslookup employeeportal` on the Connector VM — must resolve
2. Run same lookup on Client device — should return IP in `100.64.0.0–100.127.255.255`
3. Test browser access with explicit `http://` prefix

## Related Docs
- Twingate Resources configuration
- Split tunneling behavior
- Connector deployment guides