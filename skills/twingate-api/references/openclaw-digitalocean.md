# Setup and Secure OpenClaw on DigitalOcean

## Summary
Deploy OpenClaw (AI-powered WhatsApp/Telegram assistant) on DigitalOcean via Marketplace, then secure access using Twingate Zero Trust. The setup removes all public inbound ports; access is exclusively through the Twingate Connector. Total setup time: 20-30 minutes.

## Key Information
- OpenClaw runs on `localhost:18789` (Node.js); Caddy acts as reverse proxy
- Twingate Connector runs on the same Droplet, creating outbound-only connections
- No inbound firewall rules needed—not even SSH
- Gateway token located at `/opt/openclaw.env`
- Recommended Droplet: 2-4 vCPU, 4-8 GB RAM (s-2vcpu-4gb minimum)
- OpenClaw version: 2026.1.24-1 on Ubuntu 22.04 LTS

## Prerequisites
- DigitalOcean account with SSH key added
- Twingate account
- (Optional) Terraform for automated deployment

## Step-by-Step

### 1. Deploy Droplet
- Use [OpenClaw Marketplace](https://marketplace.digitalocean.com) → Create Droplet
- Or via API: `image: "openclaw"`, size `s-2vcpu-4gb`

### 2. Configure Caddy (restrict to private IP only)
```bash
PRIVATE_IP=$(hostname -I | awk '{print $2}')
sudo tee /etc/caddy/Caddyfile > /dev/null <<EOF
${PRIVATE_IP} {
  reverse_proxy localhost:18789
  header X-DO-MARKETPLACE "openclaw"
}
EOF
sudo systemctl restart caddy
```

### 3. Get Gateway Token
```bash
cat /opt/openclaw.env
```

### 4. Install Twingate Connector
```bash
curl "https://binaries.twingate.com/connector/setup.sh" | \
sudo TWINGATE_ACCESS_TOKEN="$TWINGATE_ACCESS_TOKEN" \
TWINGATE_REFRESH_TOKEN="$TWINGATE_REFRESH_TOKEN" \
TWINGATE_NETWORK="$TWINGATE_NETWORK" \
TWINGATE_LABEL_DEPLOYED_BY="openclaw" bash
```

### 5. Create Twingate Resource
- Address: `<droplet-private-ip>`, Name: `OpenClaw Gateway`
- Optional FQDN resource: Address `127.0.0.1`, Alias: your domain

### 6. Lock Down Firewall
- DigitalOcean Console → Networking → Firewalls
- **Zero inbound rules**
- Outbound: Allow All TCP/UDP/ICMP

### 7. Access Gateway
```
https://<droplet-private-ip>/?token=<gateway-token>
```

## Configuration Values

| Variable | Description |
|---|---|
| `TWINGATE_ACCESS_TOKEN` | From Twingate Admin Console |
| `TWINGATE_REFRESH_TOKEN` | From Twingate Admin Console |
| `TWINGATE_NETWORK` | Network name without `.twingate.com` |
| `TWINGATE_LABEL_DEPLOYED_BY` | Set to `openclaw` |
| Port `18789` | OpenClaw Gateway (localhost only) |

## Gotchas
- SSH into Droplet must use **private IP** after firewall lockdown (requires Twingate Client active)
- Caddy defaults may expose public IP—must explicitly reconfigure to private IP only
- If multiple Remote Networks exist, ensure Twingate resource is assigned to the correct network where Connector is installed
- First SSH login prompts for AI provider API key; can skip with CTRL-C

## Troubleshooting
```bash
# Check Gateway listening
netstat -tlnp | grep 18789

# Check Connector status
systemctl status twingate-connector
journalctl -u twingate-connector -f

# Test Gateway health (on Droplet)
curl http://127.0.0.1:18789/health
```

## Terraform Automation
```bash
git clone