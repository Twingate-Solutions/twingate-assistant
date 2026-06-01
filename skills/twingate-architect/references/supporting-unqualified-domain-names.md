# Supporting Unqualified Domain Names

## Summary
Twingate supports access to resources via unqualified domain names (e.g., `http://employeeportal`) with additional configuration. Requires defining the unqualified name as a separate Resource and configuring search domains on the Connector host.

## Key Information
- Unqualified domains must be added as **separate Resources** alongside the FQDN—not as replacements
- The Connector uses the host machine's search domain settings
- Twingate virtual IPs resolve in the `100.64.0.0–100.127.255.255` range

## Prerequisites
- Existing FQDN Resource already defined in Admin Console
- Access to Connector host to configure DNS search domains

## Step-by-Step

### 1. Define Resources in Admin Console
- Add unqualified name (e.g., `employeeportal`) as a **new, separate Resource**
- Keep the existing FQDN Resource (e.g., `employeeportal.yourcompany.com`)
- Both must exist to prevent connection errors

### 2. Set Search Domain on Connector Host

**Docker (non-ECS):** Add before `--restart=unless-stopped` in the run command:
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
| Platform | Config Location | Parameter |
|----------|----------------|-----------|
| Docker | Run command flag | `--dns-search <domain>` |
| Ubuntu | `/etc/systemd/resolved.conf` | `DOMAINS=<domain>` |
| CentOS/Fedora | nmcli | `ipv4.dns-search "<domain>"` |

## Gotchas
- **Connector restart not required** for search domain changes (on VM-based deployments)
- **Both Resource entries required**: omitting the unqualified name means the Client cannot intercept that traffic (split-tunnel limitation)
- **Browser behavior**: Browsers may interpret unqualified names as search queries. Force URL interpretation by typing `http://employeeportal` explicitly; browser history will cache it afterward
- Verify the Connector can resolve the unqualified name (`nslookup employeeportal`) before troubleshooting the Client

## Troubleshooting Checklist
1. SSH into Connector VM → `nslookup employeeportal` must resolve
2. On Client device → same lookup should return IP in `100.64.x.x–100.127.x.x` range
3. In browser → prefix with `http://` to force domain interpretation

## Related Docs
- Twingate Resources configuration
- Connector deployment guides (Docker, ECS, Ubuntu, CentOS)