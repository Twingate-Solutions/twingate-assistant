# Getting Started with DigitalOcean and Twingate

## Summary
Deploys a Twingate Connector on a DigitalOcean Droplet using `doctl` CLI and `cloud-init`. The Connector enables secure remote access to private DigitalOcean resources. Setup takes approximately 4 steps: generate tokens, deploy via `doctl`, and verify connectivity.

## Key Information
- Connector is deployed as a DigitalOcean Droplet via `cloud-init` script
- Twingate Admin Console generates a pre-built `doctl` command with embedded tokens
- Each Connector **must** have its own unique Access/Refresh token pair — never reuse tokens
- Verify success by checking both DigitalOcean Droplet status and Twingate Controller/Relay status

## Prerequisites
- DigitalOcean account with API access
- `doctl` CLI installed and authenticated with DigitalOcean credentials
- Twingate account with Admin Console access
- Existing Remote Network in Twingate to attach the Connector to

## Step-by-Step

1. Log in to Twingate Admin Console → **Remote Networks**
2. Select target Remote Network → Add or select an undeployed Connector
3. Click **See More** → select **DigitalOcean** option
4. Scroll to **Step 2** → click **Generate Tokens** (authenticate when prompted)
5. Scroll to **Step 4** → copy the generated installation command
6. Paste command into terminal — `doctl` creates the Droplet with `cloud-init` config
7. Verify Droplet is running in DigitalOcean Control Panel → Droplets
8. Verify in Admin Console that Connector shows `Controller` and `Relay` status as **connected**

## Configuration Values
- Tokens are embedded in the generated `doctl` command (Access Token + Refresh Token)
- No manual env vars to set — all config injected via `cloud-init`

## Gotchas
- **Copy/paste errors**: Terminal whitespace interpretation may corrupt the command — paste into a separate script file if needed
- **Token reuse**: Each Connector deployment requires freshly generated tokens; reusing tokens will cause failures
- **doctl not authenticated**: Must run `doctl auth init` before executing the deployment command

## Troubleshooting Commands
```bash
# Check droplet created successfully
doctl compute droplet list

# Verify connector service (on the Droplet)
# Check Twingate Admin Console for Controller/Relay connected status
```

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [Connector Management](https://www.twingate.com/docs/connectors)
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- [doctl Installation (DigitalOcean)](https://docs.digitalocean.com/reference/doctl/how-to/install/)