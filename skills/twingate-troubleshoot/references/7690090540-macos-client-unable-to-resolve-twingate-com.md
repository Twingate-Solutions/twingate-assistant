---
source: https://help.twingate.com/articles/7690090540-macos-client-unable-to-resolve-twingate-com
type: help
fetched: 2026-08-06
source_version: 42843a6c3cbb8f23e38256923b16045b4db362f078ff8abe82eacb41707d9d22
---

# [macOS Client] Unable to Resolve .twingate.com

## Summary
A rare issue where the Twingate macOS client fails to resolve `.twingate.com` after updating to version 2025.227 via Kandji Auto Apps. The error occurs when Kandji force quits the running application during the update process. Restarting the client or device resolves it.

## Key Information
- Affects Twingate macOS client version **2025.227**
- Only triggered when updating via **Kandji Auto Apps**
- Root cause: Kandji agent force quits the running Twingate client before applying the update
- Presents as a connection error stating the client is unable to resolve `.twingate.com`
- Occurrence is rare

## Prerequisites
- macOS with Twingate client installed
- Kandji MDM managing the Twingate client via Auto Apps

## Resolution Steps
1. Restart the Twingate client, **or**
2. Restart the device

## Gotchas
- This is specific to the **Kandji Auto Apps** update mechanism — not a general Twingate update issue
- No configuration changes or reinstallation required; a simple restart is sufficient
- Issue does not indicate network misconfiguration or DNS problems

## Related Docs
- Twingate macOS client documentation
- Kandji Auto Apps configuration