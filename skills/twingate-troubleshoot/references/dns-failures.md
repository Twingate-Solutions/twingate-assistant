## DNS Failures (Troubleshooting)

Diagnostic playbook for "Twingate Client connected but Resource unreachable by name" -- almost always a DNS issue, not a connectivity issue.

### Common Symptoms

- Connected to Twingate, but browser shows `DNS_PROBE_FINISHED_NXDOMAIN` / "This site can't be reached"
- App fails to connect: "host not found" / "cannot resolve hostname"
- Admin Console -> Resource **Activity** report shows **DNS lookup error** events

### Triage in Order

#### 1. Test DNS Resolution on the Client Device

Run on the user's machine:
```
nslookup <resource_fqdn>
# e.g., nslookup jira.mycompany.internal
```

**Expected (correct) behavior:**
- Returns an IP in the **CGNAT range `100.96.0.0/12`** (NOT the actual private IP)
- This is Twingate's virtual IP -- confirms the Client is intercepting the FQDN as a Resource
- The Client uses this CGNAT IP internally to route traffic through Twingate

**Incorrect behavior:**
- Times out
- Returns a **public** IP
- Returns an error (NXDOMAIN, etc.)

If incorrect, the Client is **not intercepting**. Possible causes:
- Resource not defined correctly in Admin Console
- User not in a Group with access to the Resource
- Client itself is misbehaving (see /docs/device-failures)

#### 2. Check for CGNAT IP Address Conflicts

**Critical issue often overlooked.** Twingate reserves `100.96.0.0/12` (i.e., `100.96.0.0` to `100.127.255.255`).

**Conflict**: if the user's local network OR ISP uses any address in that range for **device IPs OR DNS server addresses**, traffic gets misrouted.

**Diagnose:**
- Windows: `ipconfig /all`
- macOS: `scutil --dns`
- Look at assigned IPs and DNS server addresses

If anything (other than the Twingate adapter) falls within `100.96.0.0/12` -> there's a conflict.

**Resolution:**
- Manually configure the device's DNS to a public resolver: Google (`8.8.8.8`, `8.8.4.4`) or Quad9 (`9.9.9.9`)
- This bypasses the conflicting ISP DNS

#### 3. Check DNS Resolution on the Connector Host

If the Admin Console **explicitly** shows "DNS lookup error", the Client successfully sent the request to the Connector, but the **Connector** can't resolve it.

**Diagnose** (from the Connector host):
```
nslookup <resource_fqdn>
# or
dig <resource_fqdn>
```

If this fails on the Connector host -> DNS issue at the Connector network layer.

**Resolution:**
- Edit `/etc/resolv.conf` (Linux)
- Check VPC DNS settings (cloud)
- Ensure the host has a network path to your internal DNS servers
- **Best practice for troubleshooting**: shut down all but one Connector to isolate the problem to a specific host

#### 4. Check for Multiple Active Network Interfaces

On Windows / Linux: having BOTH wired (Ethernet) AND Wi-Fi active **on the same subnet** can cause unpredictable routing.

**Resolution:**
- Update NIC drivers (especially Realtek chipsets, which have known issues)
- Workaround: disconnect one interface (unplug Ethernet OR turn off Wi-Fi)

### When DNS Works But Connection Still Fails

If DNS resolves correctly to a `100.x.x.x` CGNAT IP but the connection still fails -> the issue is **further down the path**:
- Connector connectivity to the actual private IP
- Network route from Connector to Resource
- Firewall between Connector and Resource

Move to /docs/connector-failures or /docs/firewall-failures.

### Decision Notes

- The CGNAT range conflict is the **single most common DNS issue** in real-world deployments -- always check it
- For consistent diagnostics: shut down all Connectors except one when troubleshooting
- Dual-NIC issues are subtle and Windows-specific -- if a user has both adapters active, just disable one as a quick test

### Gotchas

- The CGNAT IP being returned is **not** a bug -- it's how Twingate works. Users who don't understand this often "fix" things by adding the real IP to a Resource (defeats DNS)
- ISP-provided DNS servers in the `100.x` range are fairly common in some regions -- don't assume just because public DNS works that ISP DNS doesn't conflict
- The "DNS lookup error" status in Admin Console specifically means **Connector**-side resolution failure, not Client-side

### Related Docs

- /docs/device-failures -- Client-side issues (different failure class)
- /docs/connector-failures -- Connector-host issues
- /docs/firewall-failures -- Network path issues
- /docs/how-dns-works-with-twingate, /docs/how-twingate-forwards-dns -- DNS architecture
- /docs/how-to-troubleshoot -- Top-level troubleshooting decision tree
