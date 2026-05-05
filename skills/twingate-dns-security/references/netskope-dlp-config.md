## Netskope DLP Configuration with Twingate

How to configure Netskope DLP so its client coexists with the Twingate Client on the same device. Required when both endpoint security stacks intercept network traffic.

### The Problem

Netskope intercepts and may inspect traffic from all installed apps. Without explicit exception, it can disrupt the Twingate Client's TLS connection or DNS resolution.

### Three-Step Configuration

#### Step 1: Define Twingate as a Certificate-Pinned Application

In the Netskope console:
1. **Settings (bottom-left) -> App Definition**
2. Create a **certificate-pinned application** -- name it "Twingate"
3. Add entries for each platform:

**macOS** (Exact match):
```
Twingate, Tunnel Provider macos
```

**Windows** (Exact match):
```
twingate.exe, twingate.service.exe, twingateupdater.exe
```

These names are the Twingate Client process names that Netskope will recognize as off-limits for traffic interception.

#### Step 2: Create an Exception in Steering Configuration

1. **Settings -> Steering Configuration**
2. Open existing config, or create new
3. **Exceptions** tab -> create new exception
4. Exception type: **Certificate Pinned Application**
5. Select the **Twingate** application created in Step 1
6. **Custom app domains**: `*` (all domains)
7. For each operating system: select **bypass**
8. Save

#### Step 3: Apply the Configuration

1. Click the Netskope client tray icon
2. **Configuration -> Update**
3. This pulls the updated policy down to the local Netskope agent
4. **Restart the Twingate Client**

After these steps, Netskope leaves Twingate's traffic alone, and both clients operate normally.

### Decision Notes

- Process names must match exactly -- typos cause silent partial failures
- Custom app domains = `*` is broad but appropriate; the bypass is gated by the Twingate process names, not the domains
- For mixed Windows + macOS fleets: configure both platforms in the same App Definition

### Gotchas

- "Update Configuration" is required after policy changes -- without it, the Netskope agent is using stale rules
- Restart the Twingate Client after Netskope policy changes -- existing connections may have been disrupted
- Future Twingate Client process renames could break this -- if Twingate adds a new process name in a Client update, add it to the App Definition

### Related Docs

- /docs/configuring-zscaler-with-twingate -- Sibling pattern for Zscaler
- /docs/configuring-anyconnect-with-umbrella -- Cisco AnyConnect / Umbrella
- /docs/firewalls-and-twingate -- Firewall coexistence overview
- /docs/troubleshooting -- General troubleshooting
