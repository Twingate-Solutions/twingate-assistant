# Getting Started with DigitalOcean and Twingate

## Summary
Deploys a Twingate Connector on a DigitalOcean Droplet using `doctl` CLI and `cloud-init`. The Connector enables secure remote access to private DigitalOcean resources. Setup is completed via a pre-generated installation command from the Twingate Admin Console.

## Key Information
- Connector is deployed as a DigitalOcean Droplet via `doctl` with `cloud-init` configuration
- Twingate Admin Console generates a complete `doctl` command (including tokens) that you paste directly into terminal
- Each Connector requires its own unique Access/Refresh token pair — never reuse tokens
- Verify success in both DigitalOcean Control Panel (Droplet running) and Twingate Admin Console (Controller + Relay show "connected")

## Prerequisites
- DigitalOcean account with API access
- `doctl` CLI installed and authenticated with DigitalOcean credentials
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate

## Step-by-Step

1. In Twingate Admin Console → **Remote Networks** → select target network
2. Add or select an undeployed Connector → **See More**
3. Select **DigitalOcean** option
4. Scroll to **Step 2** → click **Generate Tokens** (authenticate when prompted)
5. Scroll to **Step 4** → copy the generated installation command
6. Paste command into terminal — `doctl` creates Droplet with Connector pre-configured via `cloud-init`
7. Verify Droplet is running in DigitalOcean Control Panel → **Droplets**
8. Verify in Admin Console: Connector shows Controller and Relay status as **connected**

## Configuration Values
- Tokens are embedded in the generated `doctl` command — no manual env var setup required
- Token types: Access Token + Refresh Token (per-Connector, unique)

## Gotchas
- **Token reuse**: Never share token sets between Connectors
- **Copy/paste whitespace**: Terminal may misinterpret whitespace; paste into a script file if needed
- **doctl not authenticated**: Must run `doctl auth init` before using the install command
- Token errors will prevent Connector from connecting — double-check tokens if status doesn't show "connected"

## Troubleshooting Commands
```bash
# Check Droplet was created
doctl compute droplet list
```

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [DigitalOcean doctl installation](https://docs.digitalocean.com/reference/doctl/how-to/install/)
- Connector Management (Twingate docs)
- Setting Up Resources (Twingate docs)