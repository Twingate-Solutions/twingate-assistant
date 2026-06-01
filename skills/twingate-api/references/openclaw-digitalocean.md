# Setup and Secure OpenClaw on DigitalOcean

## Summary
Deploy OpenClaw (AI-powered WhatsApp/Telegram assistant) on a DigitalOcean Droplet using the Marketplace image, then secure it with Twingate Zero Trust access. The result is a privately-accessible gateway with no exposed public ports, accessed exclusively via Twingate Connector.

## Key Information
- OpenClaw runs on `localhost:18789` (Node.js app)
- Caddy reverse proxy restricts access to private IP only
- Twingate Connector creates outbound-only connections — no inbound ports required
- Total setup time: 20–30 minutes
- Recommended Droplet size: 2–4 vCPU, 4–8 GB RAM (e.g., `s-2vcpu-4gb`)

## Prerequisites
- DigitalOcean account with SSH key added
- Twingate account
- (Optional) Terraform for automated deployment

## Step-by-Step

### 1. Create Droplet
- Deploy from [OpenClaw Marketplace](https://marketplace.digitalocean.com/) or via API using image `openclaw`
- Note the Droplet's **private IP address**

### 2. Configure OpenClaw
```bash
# Restrict Caddy to private IP only
PRIVATE_IP=$(hostname -I | awk '{print $2}')
sudo tee /etc/caddy/Caddyfile > /dev/null <<EOF
${PRIVATE_IP} {
  reverse_proxy localhost:18789
}
EOF
sudo systemctl restart caddy

# Retrieve Gateway token
cat /opt/openclaw.env
```

### 3. Deploy Twingate Connector
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

### 4. Create Twingate Resource
- **Name:** OpenClaw Gateway
- **Address:** `<droplet-private-ip>`
- Assign to the Remote Network where Connector is installed
- Add group access under Resources tab

### 5. Lock Down Firewall
- In DigitalOcean → Networking → Firewalls: create firewall with **zero inbound rules**
- Allow all outbound (TCP, UDP, ICMP) to all IPv4/IPv6
- Apply to the OpenClaw Droplet

## Configuration Values

| Variable | Description |
|---|---|
| `TWINGATE_ACCESS_TOKEN` | From Twingate Admin Console → Connectors |
| `TWINGATE_REFRESH_TOKEN` | From Twingate Admin Console → Connectors |
| `TWINGATE_NETWORK` | Network name without `.twingate.com` |
| `TWINGATE_LABEL_DEPLOYED_BY` | Set to `openclaw` |
| `OPENCLAW_GATEWAY_TOKEN` | Found in `/opt/openclaw.env` |

**Access URL:** `https://<droplet-private-ip>/?token=<gateway-token>`

## Gotchas
- Twingate Connector must be installed on the **same Droplet** as OpenClaw
- When creating the Twingate Resource, ensure it's assigned to the correct Remote Network — multi-network setups can cause connectivity failures
- SSH to the Droplet must use the **private IP** (via Twingate Client), not public IP after firewall lockdown
- Caddy must be restarted after updating the Caddyfile

## Terraform (Optional)
```bash
git clone https://github.com/Twingate-Community/secure-openclaw.git
cd secure-openclaw/terraform/digitalocean
cp terraform.tfvars.example terraform.tfvars