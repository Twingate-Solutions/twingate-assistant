# Setup and Secure OpenClaw on DigitalOcean

## Summary
Deploy OpenClaw (AI-powered WhatsApp/Telegram assistant) on DigitalOcean using the Marketplace app, then secure access using Twingate Zero Trust. The result is a private gateway with no exposed ports—all access routed through Twingate Connector. Estimated time: 20-30 minutes.

## Key Information
- OpenClaw runs as Node.js app on `localhost:18789`
- Caddy acts as reverse proxy, restricted to private IP only
- Twingate Connector installed on same Droplet—creates outbound-only connections
- No inbound firewall rules needed (not even SSH) once Twingate is configured
- Gateway token stored at `/opt/openclaw.env`

## Prerequisites
- DigitalOcean account with SSH key added
- Twingate account
- (Optional) Terraform for automated deployment

## Step-by-Step

### 1. Create Droplet (2 min)
- Use [OpenClaw Marketplace page](https://marketplace.digitalocean.com/apps/openclaw)
- Size: `s-2vcpu-4gb` minimum; Region: closest to team
- Note the **private IP address**

### 2. Configure OpenClaw (2 min)
```bash
# SSH in
ssh root@<droplet-private-ip>

# Restrict Caddy to private IP only
PRIVATE_IP=$(hostname -I | awk '{print $2}')
sudo tee /etc/caddy/Caddyfile > /dev/null <<EOF
${PRIVATE_IP} {
  reverse_proxy localhost:18789
  header X-DO-MARKETPLACE "openclaw"
}
EOF
sudo systemctl restart caddy

# Get Gateway token
cat /opt/openclaw.env
```

### 3. Deploy Twingate Connector (15 min)
```bash
export TWINGATE_ACCESS_TOKEN="your-access-token"
export TWINGATE_REFRESH_TOKEN="your-refresh-token"
export TWINGATE_NETWORK="yourcompany"  # Without .twingate.com

curl "https://binaries.twingate.com/connector/setup.sh" | \
  sudo TWINGATE_ACCESS_TOKEN="$TWINGATE_ACCESS_TOKEN" \
  TWINGATE_REFRESH_TOKEN="$TWINGATE_REFRESH_TOKEN" \
  TWINGATE_NETWORK="$TWINGATE_NETWORK" \
  TWINGATE_LABEL_DEPLOYED_BY="openclaw" \
  bash
```

**Create Twingate Resource:** Address = `<droplet-private-ip>`, assign to group with access.

**Access URL:** `https://<droplet-private-ip>/?token=<gateway-token>`

### 4. Lock Down VPC (5 min)
- DigitalOcean Console → Networking → Firewalls → Create
- **Inbound rules:** None (leave empty)
- **Outbound rules:** Allow all TCP/UDP/ICMP

## Configuration Values

| Parameter | Value |
|-----------|-------|
| App port | `18789` |
| Gateway token location | `/opt/openclaw.env` |
| Caddy config | `/etc/caddy/Caddyfile` |
| Droplet size (min) | `s-2vcpu-4gb` |
| Marketplace image slug | `openclaw` |

## Gotchas
- Must configure Caddy to bind to **private IP only** before locking firewall—otherwise you lose access
- Twingate Resource must be assigned to the **same Remote Network** where Connector is installed
- SSH after firewall lockdown requires Twingate Client connected; use `ssh root@<private-ip>` not public IP
- First SSH login prompts for AI provider API key; can skip with Ctrl-C

## Terraform Automation
```bash
git clone https://github.com/Twingate-Community/secure-openclaw.git
cd secure-openclaw/terraform/digitalocean
cp terraform.tfvars.example terraform.tfvars
terraform init && terraform apply
```
Required vars: `do_token`, `twingate_access_token`, `t