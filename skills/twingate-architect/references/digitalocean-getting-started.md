# Getting Started with DigitalOcean and Twingate

## Summary
Deploys a Twingate Connector on a DigitalOcean Droplet using `doctl` CLI and `cloud-init`. The Connector enables secure remote access to private DigitalOcean resources without exposing them publicly.

## Key Information
- Deployment method: `doctl` CLI + `cloud-init` script
- The Admin Console generates a ready-to-use `doctl` command with tokens pre-embedded
- Each Connector requires its own unique Access/Refresh token pair (never reuse)
- Verify success by checking both DigitalOcean Droplet status and Twingate Admin Console Connector status

## Prerequisites
- DigitalOcean account with API access
- `doctl` CLI installed and authenticated with DigitalOcean credentials
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate

## Step-by-Step

1. Log into Twingate Admin Console → **Remote Networks**
2. Select target Remote Network → Add or select an undeployed Connector
3. Click **See More** → select **DigitalOcean** option
4. Scroll to **Step 2** → click **Generate Tokens** (authenticate when prompted)
5. Scroll to **Step 4** → copy the generated installation command
6. Paste and run the command in your terminal (`doctl` creates Droplet via cloud-init)
7. Verify in DigitalOcean Control Panel → **Droplets** → confirm Droplet is running
8. Verify in Admin Console → Remote Network → Connector → confirm **Controller** and **Relay** statuses show **connected**

## Configuration Values
- Tokens are embedded in the generated command (no manual env var configuration)
- Token types: Access Token + Refresh Token (both generated together)

## Gotchas
- **Never reuse token sets** — each Connector must have unique tokens
- Terminal whitespace/copy-paste issues may corrupt the command; paste into a script file if needed
- `doctl` must be authenticated before running the generated command
- Token errors are the most common failure cause — verify tokens are correctly copied

## Troubleshooting Commands
```bash
# Check if Droplet was created
doctl compute droplet list

# Check Connector service on Droplet (SSH in first)
systemctl status twingate-connector
```

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [DigitalOcean doctl Installation](https://docs.digitalocean.com/reference/doctl/how-to/install/)
- Connector Management (Twingate docs)
- Setting Up Resources (Twingate docs)