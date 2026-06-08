# Getting Started with CasaOS and Twingate

## Summary
Deploy a Twingate Connector on CasaOS via the Custom App Store to enable secure remote access to your home network. Uses Docker Compose import through the CasaOS web UI. After setup, create Twingate Resources pointing to private IPs for remote access.

## Key Information
- Connector runs as a Docker container via CasaOS custom app install
- Each Connector requires its own unique Access/Refresh token pair
- Container image: `twingate/connector:1`
- Supports architectures: amd64, arm64, arm
- Memory reservation: 500M (adjustable)
- Network mode: `default`; not run in privileged mode

## Prerequisites
- Running CasaOS instance with web UI accessible
- Twingate account with Admin Console access
- Remote Network already created in Twingate Admin Console

## Step-by-Step

1. **Generate tokens**: Admin Console → Remote Networks → select network → add/select Connector → "See More" → Manual → Step 2 → Generate Tokens → copy both tokens
2. **Open CasaOS App Store**: Click "Custom Install" (top right)
3. **Import config**: Click "Import" → paste Docker Compose YAML → Submit → OK
4. **Configure Web UI link**: Set to `https://{network_name}.twingate.com/networks/overview`
5. **Fill environment variables** with tokens and network name → Install
6. **Verify**: Admin Console → Remote Networks → Connector → confirm Controller and Relay show "Connected"
7. **Add Resource**: Admin Console → Resources → "+ Resource" → select Remote Network → set name → add dashboard private IP (e.g., `192.168.x.x`) → assign group access

## Configuration Values

| Environment Variable | Description | Example |
|---|---|---|
| `TWINGATE_NETWORK` | Network subdomain name | `example` |
| `TWINGATE_ACCESS_TOKEN` | Generated from Admin Console | — |
| `TWINGATE_REFRESH_TOKEN` | Generated from Admin Console | — |
| `TWINGATE_LABEL_DEPLOYED_BY` | Hardcoded label | `"casaos"` |
| `TWINGATE_LABEL_HOSTNAME` | Hostname label for connector | — |

## Gotchas
- **Never reuse token sets** — each Connector must have its own unique Access/Refresh token pair
- Network name is the subdomain only (e.g., `example` from `https://example.twingate.com`)
- Resource IP must be the same local IP used to access CasaOS dashboard on LAN
- If tokens are wrong, Connector will fail to connect — re-generate if unsure

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- Home Assistant Setup Guide
- Unraid Helper Script Guide
- ZimaOS Setup Guide