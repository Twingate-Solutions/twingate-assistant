# Supporting Unqualified Domain Names

## Summary
Twingate supports access to resources via unqualified domain names (e.g., `http://employeeportal` instead of `http://employeeportal.yourcompany.com`) with additional configuration. This requires defining the unqualified name as a separate Resource and configuring search domains on the Connector host.

## Key Information
- Unqualified domain Resources must be added **in addition to** the FQDN Resource, not as a replacement
- The Connector uses the search domains configured on its host machine
- Twingate assigns virtual IPs in the `100.64.0.0–100.127.255.255` range for Resources

## Prerequisites
- Existing FQDN Resource already defined in Twingate Admin Console
- Access to the Connector host machine to configure DNS search domains

## Step-by-Step

### Step 1: Define Resources in Admin Console
1. Create a Resource for the unqualified name (e.g., `employeeportal`)
2. Ensure the FQDN Resource also exists (e.g., `employeeportal.yourcompany.com`)
3. Both must coexist — removing the FQDN causes connection errors

### Step 2: Set Search Domain on Connector Host

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

**AWS ECS:** Set under Network Settings → Advanced Container Configuration when adding/editing a container instance.

## Configuration Values
| Platform | Setting | Location |
|---|---|---|
| Docker | `--dns-search <domain>` | CLI flag in run script |
| Ubuntu | `DOMAINS=<domain>` | `/etc/systemd/resolved.conf` |
| CentOS/Fedora | `ipv4.dns-search "<domain>"` | nmcli connection property |
| AWS ECS | DNS Search Domain | Network Settings in container config |

## Gotchas
- **Connector restart not required** for search domain changes on the host (OS-level DNS changes apply immediately)
- **Browsers may interpret unqualified names as search queries** — force URL behavior by prepending `http://` (e.g., `http://employeeportal`); browser history will remember it afterward
- DNS must resolve the unqualified name on the **Connector host** first — verify with `nslookup employeeportal` on the Connector machine before debugging client-side

## Troubleshooting Checklist
1. Run `nslookup <unqualified-name>` on Connector host — must resolve successfully
2. Run same lookup on Client device — should resolve to `100.64.x.x–100.127.x.x` range
3. For browsers, explicitly type `http://<unqualified-name>` to force domain interpretation

## Related Docs
- Twingate Resources configuration
- Split tunneling behavior
- Connector deployment guides