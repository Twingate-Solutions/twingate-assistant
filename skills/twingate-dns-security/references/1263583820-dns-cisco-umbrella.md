---
source: https://help.twingate.com/articles/1263583820-dns-cisco-umbrella
type: help
fetched: 2026-08-06
source_version: 78cd12bd42173acede6c86878416e18bb14e02288f19e489e152592a9013f8fd
---

# DNS: Cisco Umbrella

## Summary
Cisco Umbrella is incompatible with the Twingate Client due to DNS resolution conflicts. Both products require the same system-level DNS functionality, causing neither to work properly when installed together.

## Key Information
- **Conflict type**: DNS resolution system-level conflict
- **Affected component**: Twingate Client
- **Result of conflict**: Both Twingate and Cisco Umbrella fail to function properly when running simultaneously
- **AnyConnect exception**: Cisco AnyConnect (with Umbrella module) can be configured to work alongside Twingate

## Prerequisites
- N/A — this is a known incompatibility, not a configuration issue

## Resolution Steps
1. **Option A**: Uninstall Cisco Umbrella entirely
2. **Option B**: Stop the Cisco Umbrella **service** AND disable it from running on startup
   - Note: Simply exiting the Umbrella application (system tray quit) is **not sufficient** — the background service must be stopped and disabled

## Configuration Values
- None applicable

## Gotchas
- Quitting/exiting the Cisco Umbrella UI does **not** resolve the conflict — the underlying service continues running and will still interfere with Twingate
- The service must be explicitly stopped and disabled at the OS service level (e.g., Windows Services or macOS launchd)
- Cisco AnyConnect with Umbrella is a separate case — it **can** coexist with Twingate with proper configuration (see Related Docs)

## Related Docs
- [Configuring AnyConnect (with Umbrella)](https://help.twingate.com/articles/configuring-anyconnect-with-umbrella) — guide for running Twingate alongside AnyConnect when the Umbrella module is in use