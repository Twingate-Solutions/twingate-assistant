# Getting Started with CasaOS and Twingate

## Summary
Deploys a Twingate Connector on CasaOS via Docker Compose using the CasaOS custom app store installation method. Enables secure remote access to CasaOS dashboard and local network resources without exposing ports publicly.

## Key Information
- Connector is deployed as a Docker container via CasaOS's "Custom Install" feature
- Each Connector requires its own unique Access and Refresh token pair (no reuse)
- After deployment, verify Connector shows `Connected` for both Controller and Relay status
- CasaOS dashboard resource uses the local IP (e.g., `192.168.x.x`) as the resource address

## Prerequisites
- Running CasaOS instance with web UI accessible locally
- Twingate account with Admin Console access
- Existing Remote Network in Twingate Admin Console

## Step-by-Step

1. **Generate tokens**: Admin Console → Remote Networks → select network → add/select Connector → choose **CasaOS** option → click **Generate Tokens** → copy Docker Compose config
2. **Deploy Connector**: CasaOS web UI → App Store → **Custom Install** → **Import** → paste Docker Compose config → **Submit** → **Install**
3. **Verify**: Admin Console → Remote Networks → select network → select Connector → confirm Controller and Relay status = `Connected`
4. **Add Resource**: Admin Console → Resources → **+ Resource** → select Remote Network → name it → enter dashboard private IP → assign group → **Grant Access**

## Configuration Values
- Docker Compose config contains:
  - Network name
  - `ACCESS_TOKEN`
  - `REFRESH_TOKEN`
- Resource address format: `192.168.x.x` (same IP used for local dashboard access)

## Gotchas
- **Do not reuse token sets** — each Connector must have its own unique Access/Refresh token pair
- Token errors are a common failure point; double-check tokens are copied completely and correctly
- Connectivity issues: confirm CasaOS web UI is accessible locally before troubleshooting Twingate

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- Home Assistant Setup Guide
- Unraid Helper Script Guide
- ZimaOS Setup Guide