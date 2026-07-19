# Setup and Secure OpenClaw on DigitalOcean

## Summary
Deploy OpenClaw (AI-powered WhatsApp/Telegram assistant) on a DigitalOcean Droplet via Marketplace, then secure it with Twingate Zero Trust access. The setup removes all public inbound ports, routing all access through a Twingate Connector running on the same Droplet.

## Key Information
- OpenClaw runs on `localhost:18789` (Node.js), exposed via Caddy reverse proxy on private IP only
- Twingate Connector on the Droplet creates outbound-only connections—no inbound ports needed
- Single Droplet hosts both OpenClaw and the Twingate Connector
- Gateway token located at `/opt/openclaw.env`
- Estimated setup time: 20–30 minutes

## Prerequisites
- DigitalOcean account with SSH key added
- Twingate account (free tier works)
- (Optional) Terraform for automated deployment

## Step-by-Step

### 1. Deploy Droplet (2 min)
- Use [OpenClaw Marketplace](https://marketplace.digitalocean.com/) → Create Droplet
- Recommended size: `s-2vcpu-4gb` or larger
- Note the **private IP** after creation

### 2. Configure Caddy for Private IP Only (2 min)
```bash
PRIVATE_IP=$(hostname -I | awk '{print $2}')
sudo tee /etc/caddy/Caddyfile > /dev/null <<EOF
${PRIVATE_IP} {
  reverse_proxy localhost:18789
}
EOF
sudo systemctl restart caddy
```
Retrieve gateway token:
```bash
cat /opt/openclaw.env
```

### 3. Install Twingate Connector (15 min)
```bash
export TWINGATE_ACCESS_TOKEN="..."
export TWINGATE_REFRESH_TOKEN="..."
export TWINGATE_NETWORK="yourcompany"
curl "https://binaries.twingate.com/connector/setup.sh" | \
  sudo TWINGATE_ACCESS_TOKEN="$TWINGATE_ACCESS_TOKEN" \
  TWINGATE_REFRESH_TOKEN="$TWINGATE_REFRESH_TOKEN" \
  TWINGATE_NETWORK="$TWINGATE_NETWORK" bash
```
In Twingate Admin Console: create Resource with Address = `<droplet-private-ip>`, assign to group.

Access URL: `https://<droplet-private-ip>/?token=<gateway-token>`

### 4. Lock Down DigitalOcean Firewall (5 min)
- **Inbound rules**: None (leave empty)
- **Outbound rules**: Allow all TCP, UDP, ICMP to all IPv4/IPv6

## Configuration Values

| Variable | Description |
|---|---|
| `TWINGATE_ACCESS_TOKEN` | From Twingate Admin Console → Connectors |
| `TWINGATE_REFRESH_TOKEN` | From Twingate Admin Console → Connectors |
| `TWINGATE_NETWORK` | Network name without `.twingate.com` |
| `TWINGATE_LABEL_DEPLOYED_BY` | Set to `openclaw` for identification |
| `OPENCLAW_GATEWAY_TOKEN` | Found in `/opt/openclaw.env` |

## Gotchas
- Use the Droplet's **private IP** (second IP from `hostname -I`), not public IP
- After applying the firewall, SSH via public IP will timeout—only private IP via Twingate works
- Twingate Resource must be assigned to the same Remote Network as the Connector
- Gateway prompts for AI provider API key on first run; Ctrl-C to skip and configure later
- Optional FQDN resource requires `tls internal` in Caddyfile and Alias set in Twingate

## Terraform Automation
```bash
git clone https://github.com/Twingate-Community/secure-openclaw
cd secure-openclaw/terraform/digitalocean
cp terraform.tfvars.example terraform.tfvars
terraform init && terraform apply
```
After deploy, manually add Twingate Resource using `terraform output openclaw_private_ip