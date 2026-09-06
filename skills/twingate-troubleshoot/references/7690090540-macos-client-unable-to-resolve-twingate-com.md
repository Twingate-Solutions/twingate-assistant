---
source: https://help.twingate.com/articles/7690090540-macos-client-unable-to-resolve-twingate-com
type: help
fetched: 2026-09-06
source_version: 3041f0431dc076de0a7984ca9d77f0f96e593009d4b3618ea74f798d20eebffa
---

# [macOS Client] Unable to Resolve .twingate.com

## Summary
A rare bug where the Twingate macOS client fails to resolve `.twingate.com` after updating to version 2025.227 via Kandji Auto Apps. The issue is caused by Kandji force-quitting the running client during the update process. Resolution is simple: restart the client or device.

## Key Information
- Affects Twingate macOS client version **2025.227**
- Only triggered when updated via **Kandji Auto Apps**
- Root cause: Kandji agent force-quits the running Twingate client before/during update
- Symptom: Error on relaunch stating client is unable to connect/resolve `.twingate.com`
- Occurrence is rare

## Prerequisites
- macOS with Twingate client installed
- Kandji MDM with Auto Apps enabled for Twingate deployment

## Resolution Steps
1. Restart the Twingate client, **or**
2. Restart the device

## Gotchas
- Issue is specific to Kandji Auto Apps delivery method — other update mechanisms are not implicated
- No configuration changes or reinstallation required; a simple restart resolves the state corruption
- If restart does not resolve the issue, consider checking for additional Kandji/Twingate conflicts

## Related Docs
- Twingate macOS client release notes
- Kandji Auto Apps documentation