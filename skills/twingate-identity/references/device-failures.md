## Device Failures (Troubleshooting)

Diagnostic playbook for "Twingate Client won't connect" / "Resource list is empty" / "Stuck disconnected" issues.

### Common Symptoms

- Client UI stuck on "Disconnected", connect button unresponsive
- Client fails to start; Windows logs show `TapAdapterExistence` or "Twingate adapter is missing"
- User is connected but Resource list is empty

### Triage in Order

#### 1. Check the Twingate Service / Daemon

The Client UI is a front-end; the actual work is done by a background service. UI symptoms often mean the service isn't running.

| Platform | Diagnostic |
|---|---|
| **Windows** | `services.msc` -> find "Twingate Service" -> ensure Status = Running, Startup Type = Automatic. If stopped, start manually. If start fails, check Windows Event Viewer (Application Log) for crashes. |
| **macOS** | `log show --process Twingate --last 1h` |
| **Linux (systemd)** | `sudo journalctl -u twingate --since "1 hour ago"` |

#### 2. Verify the Virtual Network Adapter

The Client creates a TUN/TAP virtual interface; missing or disabled = service won't start.

| Platform | Diagnostic |
|---|---|
| **Windows** | Check "Twingate TAP-Windows Adapter" in Network Connections, OR `ipconfig | findstr "Twingate"`. Missing/disabled? Reinstall the Client. |
| **macOS** | `scutil --nc list` -- look for Twingate network extension |
| **Linux** | `ip a` -- look for `sdwan0` interface. Missing? Reinstall the Client. |

#### 3. Hunt for Software Conflicts

Very common cause. Any software that controls or inspects network traffic can interfere.

**Common culprits:**
- **Other VPNs / ZTNA Clients** running simultaneously (most common)
- **Antivirus / EDR / Firewall** doing deep packet inspection or network filtering
- **Network Optimizers** -- pre-installed OEM "traffic shaping" software

**How to test:**
- The reliable test is **uninstall**, then restart, then test Twingate -- merely "disabling" some security tools leaves their drivers active in the network stack
- If uninstalling resolves: reinstall the conflict + create explicit exceptions for Twingate processes and `*.twingate.com`

#### 4. Collect and Review Client Logs

The logs usually have the answer.

**Quick access from the UI:**
- **More -> Troubleshoot -> View Logs**

**Log file locations:**
- **Windows**: `%LOCALAPPDATA%\Twingate\logs`
  - `Twingate.log` -- UI logs
  - `Twingate.Service.log` -- background service logs (most useful)
- **macOS**: `~/Library/Group Containers/6GX8KVTR9H.com.twingate.com/Logs/private/var/log/twingate/`

#### Special Case: Connected but Resource Unreachable

If the Client appears healthy and connected but a specific Resource by name fails -- this is almost always **DNS**, not a Client problem. See /docs/dns-failures.

### Decision Notes

- **Reinstall is fast and effective** for adapter / driver issues -- don't spend hours tracing them
- **Antivirus / EDR conflicts**: the user's IT team may need to add exceptions; users alone often can't bypass enterprise security policies
- **Multiple VPN clients running** is one of the most common end-user issues -- always ask "is anything else running?"

### Gotchas

- "Disabled" antivirus/EDR isn't enough -- driver-level filtering may persist; full uninstall + restart is the reliable test
- Windows TAP adapter can be in a partially-installed state after a botched update -- reinstall fixes most of these
- macOS network extensions require user approval after install -- if the user denied the prompt, the Client looks installed but the kext/sysext isn't loaded

### Related Docs

- /docs/dns-failures -- Connected-but-resource-unreachable diagnostics
- /docs/connector-failures, /docs/firewall-failures, /docs/split-tunnel-failures -- Other failure modes
- /docs/how-to-troubleshoot -- Decision tree across failure types
- /docs/troubleshooting -- Top-level troubleshooting hub
- /docs/managing-devices -- Devices tab for admin-side device state
