---
source: https://help.twingate.com/articles/3556574910-potential-dns-or-resource-access-issues-on-devices-with-multiple-network-interfaces-connected
type: help
fetched: 2026-08-06
source_version: 4f480a08a0777ae2d2f596af75d867f41dc753c4efb4f31909c9eeec88d6a555
---

# Potential DNS or Resource Access Issues on Devices With Multiple Network Interfaces

## Page Title
Potential DNS or Resource Access Issues on Devices With Multiple Network Interfaces Connected

## Summary
Windows and Linux clients may experience Twingate Resource accessibility or DNS resolution issues when both wired and wireless network interfaces are active simultaneously on the same subnet. The root cause is not fully identified but is linked to driver issues or traffic shaping software. Interim solutions exist while engineering investigates.

## Key Information
- **Affected platforms:** Windows Client, Linux Client
- **Trigger condition:** Both wired and wireless interfaces active on the same subnet simultaneously
- **Windows symptom:** Twingate Resource accessibility issues
- **Linux symptom:** System DNS resolution failures
- **Common hardware factor:** Realtek chipset NICs are frequently involved

## Prerequisites
- Device has multiple active network interfaces (wired + wireless)
- Both interfaces connected to the same subnet

## Resolution Steps

### 1. Update Network Drivers
- **Windows:** Navigate to `Windows Update > View all optional updates` and install available NIC driver updates (particularly Realtek chipset drivers)
- **Linux:** Check third-party sources or vendor-provided drivers for updated Realtek or other NIC drivers

### 2. Disable Traffic Shaping / Network Optimizing Software
- OEM-installed traffic shapers or network optimizers can intercept traffic before it reaches the Twingate interface
- Identify and disable any such software on the system
- Common on OEM device images (laptops from major manufacturers)

### Workaround (if above steps fail)
- Disconnect from either wired or wireless interface
- Use only **one network interface per subnet** while Twingate is active

## Configuration Values
None applicable — issue is environmental/driver-level, not Twingate configuration.

## Gotchas
- Traffic shaping software may interfere with system-defined routing tables, bypassing the Twingate virtual interface entirely
- Linux users must seek drivers outside standard OS update channels in some cases
- Root cause is unconfirmed; Twingate engineering has been unable to reproduce consistently
- Issue is subnet-specific — using both interfaces on *different* subnets may not trigger the problem

## Related Docs
- Twingate Windows Client documentation
- Twingate Linux Client documentation