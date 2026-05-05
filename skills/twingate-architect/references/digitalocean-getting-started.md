# Getting Started with DigitalOcean and Twingate

## Summary
Deploy a Twingate Connector on a DigitalOcean Droplet using `doctl` CLI and `cloud-init`. The setup generates unique connector tokens from the Twingate Admin Console and provisions the Droplet automatically via a single installation command.

## Key Information
- Connector is deployed as a DigitalOcean Droplet configured via `cloud-init`
- Installation command is generated directly in the Twingate Admin Console (includes tokens pre-embedded)
- Each Connector requires its own unique Access/Refresh token pair — never reuse tokens
- Verify success in both DigitalOcean Control Panel and Twingate Admin Console

## Prerequisites
- DigitalOcean account with API access
- `doctl` CLI installed and authenticated with DigitalOcean credentials
- Twingate account with Admin Console access
- Basic familiarity with DigitalOcean Droplets and `cloud-init`

## Step-by-Step

1. Log in to Twingate Admin Console → **Remote Networks**
2. Select the target Remote Network
3. Add a new Connector or select an undeployed one
4. Click **See More** → select **DigitalOcean** option
5. Scroll to **Step 2** → click **Generate Tokens** (authenticate when prompted)
6. Scroll to **Step 4** → copy the generated installation command
7. Paste and run the command in your terminal (`doctl` executes it)
8. Verify Droplet is running in DigitalOcean Control Panel → **Droplets**
9. In Admin Console, confirm Connector shows **Controller** and **Relay** status as `connected`

## Configuration Values
- **Access Token** and **Refresh Token**: Generated per-connector in Admin Console, embedded in the `doctl` command
- Tokens are injected into the `cloud-init` script automatically via the copied command

## Gotchas
- **Do not reuse token sets** — each Connector must have unique tokens
- Terminal white-space/copy-paste issues may corrupt the command; paste into a script file if needed
- `doctl` must be authenticated before running the installation command
- Troubleshoot Droplet creation with: `doctl compute droplet list`

## Troubleshooting
| Issue | Fix |
|-------|-----|
| Token errors | Verify tokens are correctly copied into `cloud-init` |
| Copy/paste errors | Paste command into a script file first |
| Connectivity issues | Run `doctl compute droplet list`; check Connector service status |
| `doctl` not found | Install/authenticate via DigitalOcean docs |

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- Connector Management (Twingate Admin Console)
- Setting Up Resources (configuring private app/service access)
- [doctl Installation (DigitalOcean)](https://docs.digitalocean.com/reference/doctl/)