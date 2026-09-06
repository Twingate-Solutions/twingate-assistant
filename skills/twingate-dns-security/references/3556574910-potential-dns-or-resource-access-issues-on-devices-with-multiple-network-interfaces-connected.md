---
source: https://help.twingate.com/articles/3556574910-potential-dns-or-resource-access-issues-on-devices-with-multiple-network-interfaces-connected
type: help
fetched: 2026-09-06
source_version: 688cff0fc8809e79fe991f4b56b4236fb31e3797f4ae060d3e8cb5fe0670a1ca
---

# Potential DNS or Resource Access Issues: Multiple Network Interfaces

## Summary
Windows and Linux Twingate clients may experience resource accessibility or DNS resolution failures when a device uses both wired and wireless network interfaces simultaneously on the same subnet. Root cause is unconfirmed but likely involves driver issues or traffic shaping software interference.

## Affected Components
- Windows Client
- Linux Client

## Key Information
- Issue triggers when **wired + wireless interfaces are both active on the same subnet**
- Windows symptom: Twingate Resource inaccessibility
- Linux symptom: System-wide DNS resolution failures
- Realtek chipset NICs are commonly implicated
- OEM-installed traffic shaping/network optimization software is a known contributor

## Resolution Steps

### 1. Update Network Drivers
**Windows:**
1. Open **Windows Update**
2. Navigate to **View all optional updates**
3. Install any available NIC driver updates (especially Realtek)

**Linux:**
- Check third-party sources or vendor-provided drivers for updated NIC firmware

### 2. Disable Traffic Shaping / Network Optimization Software
- Identify any OEM-bundled traffic shapers or network optimizers
- Disable or uninstall them — they can intercept traffic **before it reaches the Twingate interface**, disrupting routing

### 3. Workaround (if unresolved)
- Disconnect from either the wired or wireless interface
- **Use only one network interface per subnet** while Twingate is active

## Gotchas
- Simply having two interfaces active (even if one is idle) can trigger the issue if both are on the same subnet
- Traffic shaping software may not be obvious — check OEM bloatware, especially on business laptops
- Twingate engineering has not been able to reproduce this reliably; fix may depend on local environment specifics
- Driver updates via OS update channels are preferred over manual downloads for stability

## Configuration Values
None applicable — resolution is environmental (drivers, software, interface configuration).

## Related Docs
- Twingate Windows Client documentation
- Twingate Linux Client documentation