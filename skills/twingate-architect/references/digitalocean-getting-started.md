# Getting Started with DigitalOcean and Twingate

## Summary
Deploy a Twingate Connector on a DigitalOcean Droplet using `doctl` CLI and `cloud-init`. The Admin Console generates a pre-configured installation command that handles connector setup automatically.

## Key Information
- Connector is deployed as a DigitalOcean Droplet via `cloud-init` script
- Installation command is generated directly from the Twingate Admin Console (DigitalOcean-specific option)
- Connector health verified via two statuses: **Controller** and **Relay** (both must show `connected`)

## Prerequisites
- DigitalOcean account with API access
- `doctl` CLI installed and authenticated with DigitalOcean credentials
- Twingate account with Admin Console access
- Existing Remote Network in Twingate

## Step-by-Step

1. **Generate Tokens**: Admin Console → Remote Networks → select network → add/select Connector → See More → select **DigitalOcean** option → Step 2 → **Generate Tokens**
2. **Copy Command**: Scroll to Step 4 in the connector setup wizard and copy the full installation command
3. **Deploy**: Paste command into terminal; `doctl` creates a Droplet with Twingate Connector via `cloud-init`
4. **Verify in DigitalOcean**: Control Panel → Droplets → confirm Droplet is running
5. **Verify in Twingate**: Admin Console → Remote Networks → select network → select Connector → confirm Controller and Relay show `connected`

## Configuration Values
- Tokens are embedded in the generated `doctl` command (Access Token + Refresh Token)
- No manual env vars to set — command is fully pre-populated by Admin Console

## Gotchas
- **Never reuse token sets** — each Connector requires its own unique Access/Refresh token pair
- Copy/paste issues: terminal whitespace interpretation may corrupt the command; paste into a script file if needed
- Tokens must be correctly embedded in the `cloud-init` script or connector will fail to authenticate

## Troubleshooting Commands
```bash
# Verify Droplet was created
doctl compute droplet list

# Check connector service on Droplet
# SSH in and verify Twingate Connector service is running
```

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [DigitalOcean doctl Installation](https://docs.digitalocean.com/reference/doctl/how-to/install/)
- Connector Management (Admin Console)
- Setting Up Resources (post-install configuration)