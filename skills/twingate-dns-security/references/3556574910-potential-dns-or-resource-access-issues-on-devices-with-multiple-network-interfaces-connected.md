---
source: https://help.twingate.com/articles/3556574910-potential-dns-or-resource-access-issues-on-devices-with-multiple-network-interfaces-connected
type: help
fetched: 2026-10-04
source_version: 1998910c3494ba54c02bac4e6818e733152cd5f3987d56f710e3ad6b112f4a74
trust: official
---

# Potential DNS or Resource Access Issues on Devices With Multiple Network Interfaces

## Summary
Windows and Linux clients may experience Twingate Resource access failures or system DNS resolution issues when a device has both wired and wireless network interfaces active on the same subnet simultaneously. The root cause is not fully identified but is linked to driver issues or traffic-shaping software interfering with Twingate's network routing.

## Key Information
- **Affected components:** Windows Client, Linux Client
- **Trigger condition:** Multiple network interfaces (wired + wireless) connected to the same subnet concurrently
- **Symptom on Windows:** Twingate Resource inaccessible
- **Symptom on Linux:** System DNS resolution failures
- **Common hardware factor:** Realtek chipset NICs are frequently implicated

## Prerequisites
- Twingate client installed on Windows or Linux
- Device connected to both wired and wireless interfaces on the same subnet

## Resolution Steps

### 1. Update Network Drivers (Primary Fix)
Most users resolve the issue this way.

**Windows:**
1. Open **Windows Update**
2. Navigate to **View all optional updates**
3. Install any available NIC/network driver updates (Realtek drivers especially)

**Linux:**
- Check your distro's package manager for NIC driver updates
- For Realtek chipsets, third-party driver sources may be required (consult your hardware vendor or distro forums)

### 2. Disable Traffic Shaping / Network Optimizing Software
- OEM system images often bundle traffic shapers or network optimizers
- These tools can intercept traffic before it reaches the Twingate interface, breaking routing
- Identify and **disable or uninstall** any such software (examples: Killer Network Manager, Nahimic, etc.)

## Workaround (If Unresolved)
- **Disconnect one interface** — use only a single network interface per subnet while Twingate is active
- Either disconnect the wired or wireless adapter, not both simultaneously on the same subnet

## Configuration Values
None — no specific env vars, CLI flags, or API parameters involved.

## Gotchas
- Issue only manifests when **both interfaces share the same subnet**; dual interfaces on different subnets may not trigger it
- Traffic-shaping software is often silently pre-installed on OEM (manufacturer) images and easy to overlook
- Twingate engineering has not been able to fully reproduce this — resolution may vary by environment

## Related Docs
- Twingate Windows Client documentation
- Twingate Linux Client documentation