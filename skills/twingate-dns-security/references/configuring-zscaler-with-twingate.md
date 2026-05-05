## Configuring Zscaler with Twingate

How to make Zscaler coexist with the Twingate Client. Default Zscaler config intercepts Twingate's TLS sessions, breaking the Twingate Client's secure channel due to invalid certificates (cert pinning failure).

### Symptoms

In `twingate.log` (Windows):
```
[WARN] SSL check error from host: <twingate_network>.twingate.com. SSL Certificate is not pinned!
[ERROR] Failed to validate controller url
System.Net.Http.HttpRequestException: Could not establish trust relationship for SSL/TLS channel.
```

This indicates Zscaler is doing SSL inspection on the Twingate-Controller connection -- which the Twingate Client refuses (its cert pinning is intentional, not a bug).

### Two Options

**Option 1: Disable Zscaler**
- Uninstall, OR
- Stop/disable the Zscaler service (just exiting the UI is **not enough** -- the service must be disabled)
- Use this option only if Zscaler isn't required on these machines

**Option 2: Bypass SSL Inspection for Twingate (Recommended)**

In the Zscaler admin console:

1. **Administration -> IP & FQDN Groups -> Destination IPv4 Groups**
   - Create a group for SSL inspection bypass
   - Add `*.twingate.com` (or your specific tenant FQDN) to the group

2. **Policy -> Client Connector Portal -> Windows**
   - Add `<tenant>.twingate.com` as an exception under **VPN Gateway Bypass**

3. **Update policy on the Zscaler local agent** (force pull)

After this, Zscaler stops MITM-ing the Twingate Client's TLS connection, and both clients run simultaneously.

### Decision Notes

- Always prefer Option 2 -- preserves Zscaler protection on other traffic
- The bypass scope is narrow (only Twingate's domain) -- minimal security implication
- For users on macOS/Linux: similar bypass needed (consult Zscaler docs for the platform-specific path)

### Gotchas

- Stopping the Zscaler **UI** is not the same as disabling the **service** -- the kernel/network components keep running
- "Refresh / Update Configuration" on the Zscaler client is required after bypass policy changes -- wait for the policy to propagate before testing
- If you have multiple Twingate tenants, ensure the bypass covers the actual hostname, not just `*.twingate.com` (wildcard usually fine)

### Related Docs

- /docs/configuring-anyconnect-with-umbrella -- Sibling pattern for Cisco AnyConnect / Umbrella
- /docs/netskope-dlp-config -- Netskope DLP coexistence
- /docs/firewalls-and-twingate -- General firewall/security software interaction
- /docs/troubleshooting -- Top-level troubleshooting hub
