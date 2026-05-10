# Getting Started with DigitalOcean and Twingate

## Summary
Deploys a Twingate Connector on a DigitalOcean Droplet using `doctl` CLI and `cloud-init`. The Connector enables secure remote access to private DigitalOcean resources. Setup takes approximately 4 steps: generate tokens, deploy via `doctl`, verify in both DigitalOcean and Twingate Admin Console.

## Key Information
- Deployment method: `doctl` CLI + `cloud-init` script
- The Admin Console generates a complete `doctl` command (including tokens) ready to paste into terminal
- Each Connector **must** have its own unique Access/Refresh token pair — never reuse tokens
- Verify success by checking both DigitalOcean Droplet status AND Twingate Connector status (Controller + Relay = "connected")

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
6. Paste command into terminal — `doctl` creates a Droplet with Connector via `cloud-init`
7. Verify Droplet is running in DigitalOcean Control Panel → Droplets
8. Verify Connector in Admin Console → Remote Networks → Connector → Controller and Relay both show **connected**

## Configuration Values
| Item | Details |
|------|---------|
| Tokens | Access Token + Refresh Token (generated per Connector in Admin Console) |
| Delivery method | Embedded in `doctl` command via `cloud-init` |

## Gotchas
- **Token reuse**: Never reuse token sets across Connectors — each requires unique tokens
- **Copy/paste whitespace**: Terminal whitespace interpretation may break the command; paste into a separate script file if needed
- **`doctl` not found**: Must be installed and authenticated before running the generated command

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