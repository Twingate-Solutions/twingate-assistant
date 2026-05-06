# Twingate Open Source Software

## Summary
Twingate publishes source code for open source components used in their software. Currently, one open source component is available for download: a fork of the tap-windows6 driver licensed under GPLv2.

## Key Information
- Twingate provides source code downloads for software released under open source licenses
- Currently one component listed: **tap-windows6** (GPLv2 license)
- tap-windows6 is a Windows TAP driver used for virtual network adapter functionality

## Available Components

| Component | License | Notes |
|-----------|---------|-------|
| twingate tap-windows6 | GPLv2 | Windows TAP virtual network driver |

## Prerequisites
- None specified for downloading source code
- Building tap-windows6 from source requires Windows driver development tools (WDK)

## Configuration Values
- None applicable — this page is a source code distribution page only

## Gotchas
- Only GPLv2-licensed components are listed; proprietary Twingate components are not available here
- Page appears minimal — check back for additional components as Twingate's open source obligations expand
- The tap-windows6 component is Windows-specific (TAP driver for VPN tunnel interface on Windows)

## Related Docs
- [Twingate Client installation docs](https://www.twingate.com/docs/clients) — context for where tap-windows6 is used
- [tap-windows6 upstream project](https://github.com/OpenVPN/tap-windows6) — original OpenVPN project this is forked from