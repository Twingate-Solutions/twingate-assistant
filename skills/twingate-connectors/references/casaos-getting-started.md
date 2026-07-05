# Getting Started with CasaOS and Twingate

## Summary
Deploys a Twingate Connector on CasaOS via Docker Compose using the CasaOS custom app installation flow. Enables remote access to the CasaOS dashboard and other private resources through Twingate's zero-trust network.

## Key Information
- Connector is deployed as a Docker container via CasaOS App Store "Custom Install"
- Each Connector requires its own unique Access/Refresh token pair (never reuse tokens)
- Verification requires both Controller and Relay statuses to show "Connected" in Admin Console

## Prerequisites
- Running CasaOS instance with web UI accessible
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate

## Step-by-Step

1. **Generate tokens**: Admin Console → Remote Networks → select network → add/select Connector → choose "CasaOS" option → "Generate Tokens" → copy Docker Compose config
2. **Deploy Connector**: CasaOS App Store → "Custom Install" → "Import" → paste Docker Compose config → Submit → Install
3. **Verify**: Admin Console → Remote Networks → select Connector → confirm Controller and Relay show "Connected"
4. **Add Resource**: Admin Console → Resources → "+ Resource" → select Remote Network → set name → add private IP (e.g., `192.168.x.x`) → assign group access

## Configuration Values
- **Docker Compose config** contains three values auto-populated from Admin Console:
  - Network name
  - Access token
  - Refresh token

## Gotchas
- Do not reuse token sets across Connectors — each deployment needs unique tokens
- Dashboard IP must match the local LAN address (typically `192.168.x.x`) — use the same address used for local access
- Token errors are the most common failure; double-check copy/paste accuracy
- If connectivity fails, confirm CasaOS web interface is locally accessible and the Connector container is running

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- Home Assistant Setup Guide
- Unraid Helper Script Guide
- ZimaOS Setup Guide