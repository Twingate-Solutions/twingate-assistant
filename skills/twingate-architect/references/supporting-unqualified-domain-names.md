## Supporting Unqualified Domain Names

Explains how to allow access to resources using short (unqualified) hostnames like `employeeportal` instead of `employeeportal.yourcompany.com`. Requires both the short name and the FQDN to be defined as separate Resources, plus a search domain configured on the Connector host.

**Key Information:**
- Both the unqualified name (e.g., `employeeportal`) AND the FQDN (e.g., `employeeportal.yourcompany.com`) must be defined as separate Resources -- do not replace the FQDN with the short name
- The Connector resolves the unqualified name using the search domain set on its host OS
- Twingate virtual IPs fall in the `100.64.0.0`-`100.127.255.255` range -- use this to verify Client-side resolution
- No Connector restart required after changing search domain settings

**Prerequisites:**
- FQDN Resource already defined in Twingate
- Admin access to the Connector host OS

**Step-by-Step:**
1. In Admin Console, add a second Resource using the unqualified name (e.g., `employeeportal`) in the same Remote Network
2. Configure the search domain on the Connector host:
   - **Docker (non-ECS):** add `--dns-search yoursearchdomain.com` before `--restart=unless-stopped` in the deploy script
   - **AWS ECS:** set under Network Settings → Advanced Container Configuration
   - **Ubuntu:** edit `/etc/systemd/resolved.conf`, add `DOMAINS=yourcompany.com`, run `sudo systemctl restart systemd-resolved`
   - **CentOS/Fedora:** `sudo nmcli con mod "CONNECTION" ipv4.dns-search "yourcompany.com"`, then `sudo systemctl restart NetworkManager`

**Gotchas:**
- Verify on the Connector host first: if `nslookup employeeportal` fails there, it will not work through Twingate
- Web browsers may interpret unqualified hostnames as search queries; prefix with `http://` (e.g., `http://employeeportal`) to force DNS resolution
- The unqualified Resource must be added in addition to the FQDN Resource, not as a replacement

**Related Docs:**
- /docs/resources -- Resource definition and address formats
- /docs/connector -- Connector configuration options
