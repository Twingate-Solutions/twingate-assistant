# Setup and Secure OpenClaw on DigitalOcean

## Summary
Deploy OpenClaw (AI-powered WhatsApp/Telegram assistant) on a DigitalOcean Droplet using the Marketplace image, then secure access via Twingate Zero Trust. The Droplet is completely locked down with no inbound ports; all access routes through the Twingate Connector.

## Key Information
- OpenClaw runs on `localhost:18789` (Node.js gateway)
- Caddy acts as reverse proxy, restricted to private IP only
- Twingate Connector creates outbound-only connections—no inbound ports needed
- Gateway requires a token for authentication (stored in `/opt/openclaw.env`)
- Total setup time: 20–30 minutes

## Prerequisites
- DigitalOcean account with SSH key added
- Twingate account
- (Optional) Terraform for automated deployment

## Step-by-Step

1. **Deploy Droplet** — Use DigitalOcean Marketplace OpenClaw image; 2 vCPU / 4 GB RAM minimum; note the private IP
2. **Configure Caddy** — Restrict reverse proxy to private IP only:
   ```bash
   PRIVATE_IP=$(hostname -I | awk '{print $2}')
   sudo tee /etc/caddy/Caddyfile > /dev/null <<EOF
   ${PRIVATE_IP} { reverse_proxy localhost:18789 }
   EOF
   sudo systemctl restart caddy
   ```
3. **Get Gateway Token** — `cat /opt/openclaw.env`
4. **Install Twingate Connector** on the Droplet using tokens from Admin Console
5. **Create Twingate Resource** — Address: `<droplet-private-ip>`, assign to group
6. **Create DigitalOcean Firewall** — Zero inbound rules, all outbound allowed; apply to Droplet
7. **Access Gateway** — `https://<droplet-private-ip>/?token=<your-token>` via Twingate Client

## Configuration Values

| Item | Value |
|------|-------|
| Gateway port | `18789` |
| Gateway token location | `/opt/openclaw.env` |
| Caddy config | `/etc/caddy/Caddyfile` |
| Connector env vars | `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`, `TWINGATE_NETWORK` |
| Connector label | `TWINGATE_LABEL_DEPLOYED_BY="openclaw"` |
| Droplet size (min) | `s-2vcpu-4gb` |
| Marketplace image slug | `openclaw` |

## Gotchas
- SSH must be used on **private IP** via Twingate after firewall lockdown—public SSH no longer works
- Caddy must be reconfigured post-deploy; default marketplace image may expose public IP
- Twingate Resource must be assigned to the same Remote Network where the Connector is installed
- First SSH login prompts for AI provider API key; can skip with `CTRL-C`
- For FQDN alias resource, use `127.0.0.1` as address with the alias set to your domain

## Terraform Alternative
```bash
git clone https://github.com/Twingate-Community/secure-openclaw.git
cd secure-openclaw/terraform/digitalocean
cp terraform.tfvars.example terraform.tfvars
terraform init && terraform apply
```
Required vars: `do_token`, `twingate_access_token`, `twingate_refresh_token`, `twingate_network`, `ssh_fingerprint`

## Related Docs
- [Twingate Connector Installation](https://www.twingate.com/docs)
- [OpenClaw Documentation](https://openclaw.ai/docs)
- [Twingate Community Subreddit](https://reddit.com/r/twingate)