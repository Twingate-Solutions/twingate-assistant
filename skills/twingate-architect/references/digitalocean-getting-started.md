# Getting Started with DigitalOcean and Twingate

## Summary
Deploys a Twingate Connector on a DigitalOcean Droplet using `doctl` CLI and `cloud-init`. The connector enables secure remote access to private DigitalOcean resources. Setup generates unique tokens via the Twingate Admin Console and provisions the Droplet in a single command.

## Prerequisites
- DigitalOcean account with API access
- `doctl` CLI installed and authenticated with DigitalOcean credentials
- Twingate account with Admin Console access
- Basic familiarity with DigitalOcean Droplets and `cloud-init`

## Step-by-Step

1. **Generate Connector Tokens**
   - Admin Console → Remote Networks → select target network
   - Add or select an undeployed Connector → See More → DigitalOcean
   - Step 2: Click **Generate Tokens** (authenticate when prompted)
   - Step 4: Copy the generated installation command

2. **Deploy via doctl**
   - Paste the copied command into terminal
   - Command creates a Droplet with Connector installed via `cloud-init`

3. **Verify Installation**
   - DigitalOcean Control Panel → Droplets → confirm Droplet is running
   - Admin Console → Remote Networks → select Connector → confirm **Controller** and **Relay** statuses show `connected`

## Configuration Values
- Tokens are auto-generated and embedded in the `doctl` command from the Admin Console
- No manual env vars to configure — `cloud-init` script handles Connector configuration

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Token errors | Verify Access and Refresh tokens are correctly included in `cloud-init` script |
| Copy/paste errors | Paste command into a script file first if terminal mishandles whitespace |
| Connectivity problems | Run `doctl compute droplet list` to confirm Droplet exists; check Connector service is running |
| `doctl` not found | Install and authenticate `doctl` per [DigitalOcean docs](https://docs.digitalocean.com/reference/doctl/) |

## Gotchas
- **Never reuse token sets** — each Connector requires its own unique Access/Refresh token pair
- Token generation requires re-authentication in the Admin Console
- Connector must show both `Controller` and `Relay` as `connected` to confirm successful deployment

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- Connector Management (Twingate Admin Console)
- Setting Up Resources (Twingate Admin Console)
- [doctl Installation](https://docs.digitalocean.com/reference/doctl/)