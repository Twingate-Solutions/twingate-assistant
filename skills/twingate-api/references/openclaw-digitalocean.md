# Setup and Secure OpenClaw on DigitalOcean

## Summary
Deploy OpenClaw (AI-powered WhatsApp/Telegram assistant) on DigitalOcean using the Marketplace app, then secure it with Twingate Zero Trust access. The result is a private gateway with no public ports exposed—all access routed through Twingate Connector.

## Key Information
- OpenClaw runs on `localhost:18789` (Node.js)
- Caddy reverse proxy restricts access to private IP only
- Twingate Connector uses outbound-only connections; zero inbound ports needed
- Single Droplet hosts both OpenClaw and Twingate Connector
- Gateway token stored at `/opt/openclaw.env`

## Prerequisites
- DigitalOcean account with SSH key added
- Twingate account
- Recommended Droplet: 2–4 vCPU, 4–8 GB RAM (e.g., `s-2vcpu-4gb`)
- Optional: Terraform for automated deployment

## Step-by-Step

### 1. Create Droplet (2 min)
- Deploy from [OpenClaw Marketplace](https://marketplace.digitalocean.com) or via API
- Note the Droplet's **private IP**

### 2. Configure OpenClaw (2 min)
```bash
# Restrict Caddy to private IP only
PRIVATE_IP=$(hostname -I | awk '{print $2}')
sudo tee /etc/caddy/Caddyfile > /dev/null <<EOF
${PRIVATE_IP} {
  reverse_proxy localhost:18789
  header X-DO-MARKETPLACE "openclaw"
}
EOF
sudo systemctl restart caddy

# Retrieve Gateway token
cat /opt/openclaw.env
```

### 3. Install Twingate Connector (15 min)
```bash
export TWINGATE_ACCESS_TOKEN="your-access-token"
export TWINGATE_REFRESH_TOKEN="your-refresh-token"
export TWINGATE_NETWORK="yourcompany"
curl "https://binaries.twingate.com/connector/setup.sh" | \
  sudo TWINGATE_ACCESS_TOKEN="$TWINGATE_ACCESS_TOKEN" \
  TWINGATE_REFRESH_TOKEN="$TWINGATE_REFRESH_TOKEN" \
  TWINGATE_NETWORK="$TWINGATE_NETWORK" \
  TWINGATE_LABEL_DEPLOYED_BY="openclaw" bash
```
- Add Twingate Resource: Address = `<droplet-private-ip>`, assign to your Remote Network
- Optional FQDN resource: Address = `127.0.0.1`, Alias = custom domain

### 4. Lock Down VPC (5 min)
- DigitalOcean Firewall: **zero inbound rules**
- Outbound: Allow All TCP/UDP/ICMP to all destinations
- Access via: `https://<private-ip>/?token=<gateway-token>`

## Configuration Values

| Variable | Description |
|---|---|
| `TWINGATE_ACCESS_TOKEN` | From Twingate Admin Console → Connectors |
| `TWINGATE_REFRESH_TOKEN` | From Twingate Admin Console → Connectors |
| `TWINGATE_NETWORK` | Network name without `.twingate.com` |
| `TWINGATE_LABEL_DEPLOYED_BY` | Set to `openclaw` for labeling |
| Gateway port | `18789` |
| Caddy config | `/etc/caddy/Caddyfile` |
| OpenClaw env | `/opt/openclaw.env` |

## Gotchas
- Private IP is `$2` from `hostname -I`—not the first/public IP
- If multiple Remote Networks exist, manually assign the Resource to the correct one
- SSH access also goes through Twingate after lockdown—connect via private IP, not public
- AI provider API key required on first run (can skip with CTRL-C and configure later)
- Terraform does **not** auto-create Twingate Resources—must be done manually in Admin Console post-deploy

## Terraform Quick Deploy
```bash
git clone https://github.com/T