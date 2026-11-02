---
source: https://help.twingate.com/articles/3556574910-potential-dns-or-resource-access-issues-on-devices-with-multiple-network-interfaces-connected
type: help
fetched: 2026-11-01
source_version: 3305636d37e29fff6a48c72e581ee07bae5ca6d2ce11636c8d8281a4808ec3d9
trust: official
---

# Potential DNS or Resource Access Issues on Devices With Multiple Network Interfaces

## Page Title
Potential DNS or Resource Access Issues on Devices With Multiple Network Interfaces Connected

## Summary
Windows and Linux Twingate clients may experience resource access or DNS resolution failures when a device is connected to both wired and wireless interfaces on the same subnet simultaneously. Root cause is not definitively identified but is linked to network driver issues or traffic-shaping software. Workarounds and driver updates resolve most cases.

## Key Information
- **Affected platforms:** Windows Client, Linux Client
- **Trigger condition:** Wired + wireless interfaces active simultaneously on the **same subnet**
- **Symptoms:**
  - Windows: Twingate Resource inaccessible
  - Linux: System-wide DNS resolution failures
- **Common culprits:** Outdated Realtek NIC drivers; OEM-installed traffic shaping/network optimization software

## Prerequisites
- Identify whether device has multiple active network interfaces on the same subnet
- Check for OEM-installed traffic shaping or network optimizer software

## Step-by-Step Resolution

### 1. Update Network Drivers (Primary Fix)
**Windows:**
1. Open **Windows Update**
2. Navigate to **View all optional updates**
3. Install any available NIC driver updates (especially Realtek chipset drivers)

**Linux:**
1. Check your NIC chipset (e.g., `lspci | grep -i network`)
2. Source updated drivers from third-party or vendor sources for your chipset

### 2. Disable Traffic Shaping / Network Optimization Software
- Identify OEM-installed traffic shaper or network optimizer applications
- Disable or uninstall them — they can intercept traffic before it reaches the Twingate interface, disrupting routing

### 3. Workaround (If Above Steps Fail)
- Disconnect from either the wired **or** wireless interface
- Use **only one network interface per subnet** while Twingate is active

## Configuration Values
None — no CLI flags, env vars, or API parameters involved.

## Gotchas
- Issue only occurs when **both interfaces are on the same subnet** — using different subnets may not trigger the problem
- Traffic shaping software is often silently pre-installed on OEM system images and may not be obvious
- Twingate engineering has not been able to reliably reproduce the issue; a permanent platform-level fix is not guaranteed

## Related Docs
- Twingate Windows Client documentation
- Twingate Linux Client documentation