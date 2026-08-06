---
source: https://www.twingate.com/docs/casaos-getting-started
type: docs
fetched: 2026-08-05
source_version: caf231ab857b5e8303dfe964e3dcf1b2d05c5ff06be624074366b396f4f81dd7
---

# Getting Started with CasaOS and Twingate

## Summary
Deploys a Twingate Connector on CasaOS via Docker Compose using the CasaOS Custom Install feature. Enables secure remote access to the CasaOS dashboard and other private resources without exposing them publicly.

## Key Information
- Connector is deployed as a Docker container via CasaOS App Store "Custom Install"
- Each Connector requires its own unique Access/Refresh token pair (never reuse tokens)
- After deployment, verify Connector shows `Controller` and `Relay` as **Connected** in Admin Console

## Prerequisites
- Running CasaOS instance with web UI accessible locally
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate

## Step-by-Step

1. **Generate tokens**: Admin Console → Remote Networks → select network → add/select Connector → choose **CasaOS** option → **Generate Tokens** → copy Docker Compose config
2. **Deploy via CasaOS**: App Store → **Custom Install** → **Import** → paste Docker Compose config → **Submit** → **Install**
3. **Verify**: Admin Console → Remote Networks → select network → select Connector → confirm Controller and Relay show **Connected**
4. **Add Resource**: Admin Console → Resources → **+ Resource** → select Remote Network → name it → enter private IP (e.g., `192.168.x.x`) → assign group access

## Configuration Values
- Docker Compose config contains three values auto-populated from Admin Console:
  - Network name
  - Access token
  - Refresh token
- Dashboard IP format: `192.168.x.x` (same address used for local access)

## Gotchas
- **Do not reuse token sets** — each Connector deployment must use a unique Access/Refresh token pair
- Tokens must be accurately copied; token errors are the most common failure mode
- CasaOS Custom Install path: App Store → top-right "Custom Install" button → "Import" button (not direct paste)
- Connector must be running before Resources become accessible

## Troubleshooting
- **Token errors**: Re-verify Access and Refresh tokens are correctly pasted
- **Connectivity**: Confirm CasaOS web UI is locally accessible and the Twingate Connector app shows as running in CasaOS

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)
- [ZimaOS Setup Guide](https://www.twingate.com/docs/zimaos-getting-started)
- [Setting Up Additional Resources](https://www.twingate.com/docs/resources)