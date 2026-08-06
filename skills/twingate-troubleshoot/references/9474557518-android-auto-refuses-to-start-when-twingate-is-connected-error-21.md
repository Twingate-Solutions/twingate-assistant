---
source: https://help.twingate.com/articles/9474557518-android-auto-refuses-to-start-when-twingate-is-connected-error-21
type: help
fetched: 2026-08-06
source_version: d4acd0cde0e8d3dd261925d28f221d4a55af44ca576f46c0c715323245f00e9e
---

# Android Auto Error 21 with Twingate Connected

## Page Title
Android Auto Refuses to Start when Twingate is connected (Error 21)

## Summary
Android Auto throws Error 21 when any VPN is detected on the device, regardless of whether it affects Android Auto traffic. Since Twingate uses Android's VPN framework, it triggers this error. The only workaround is disconnecting Twingate before launching Android Auto.

## Key Information
- Error message: *"Communication error 21 - Being connected to a VPN may prevent Android Auto from starting"*
- Android Auto detects **any VPN presence** on the device, not just VPNs that route Android Auto traffic
- Twingate uses the Android VPN framework for resource connections, making it indistinguishable from a traditional VPN to Android Auto
- This is an **Android Auto limitation**, not a Twingate bug

## Prerequisites
- Affects Android devices running Twingate while attempting to use Android Auto

## Resolution
1. **Log out of Twingate** (not just disconnect — full logout) on the Android device
2. Reconnect the device to Android Auto in the vehicle
3. Android Auto will start successfully without the VPN detected

## Gotchas
- Simply pausing or disconnecting Twingate may not be sufficient — full logout is required
- No configuration change within Twingate can resolve this; it is an Android Auto enforcement issue
- Twingate cannot use an alternative framework on Android to avoid VPN detection
- No selective split-tunneling workaround exists since Android Auto's check is binary (VPN present = blocked)

## Related Docs
- Twingate Android client documentation
- Android Auto support documentation (Google)