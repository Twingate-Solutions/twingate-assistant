---
source: https://www.twingate.com/docs/openclaw-digitalocean
type: docs
fetched: 2026-08-14
source_version: 64865f8d503f19c5d137f7027e54344f482e45e3d247c97413b218277e1acf5f
---

# Setup and Secure OpenClaw on DigitalOcean

## Summary
Deploy OpenClaw (AI-powered WhatsApp/Telegram assistant) on a DigitalOcean Droplet using the Marketplace image, then secure access using Twingate Zero Trust. The result is a privately-accessible gateway with no public ports exposed, controlled via Twingate policies and audit logs.

## Key Information
- OpenClaw runs on `localhost:18789` (Node.js); Caddy reverse proxies to private IP only
- Twingate Connector runs on the same Droplet, creating outbound-only connections (no inbound ports needed)
- Gateway token stored in `/opt/openclaw.env`
- Total setup time: 20–30 minutes

## Prerequisites
- DigitalOcean account with SSH key added
- Twingate account (free tier works)
- Optional: Terraform for automated deployment

## Step-by-Step

1. **Deploy Droplet** – Use [OpenClaw Marketplace](https://marketplace.digitalocean.com) image; select `s-2vcpu-4gb` or larger; note private IP
2. **Configure Caddy** – Restrict reverse proxy to private IP only:
   ```bash
   PRIVATE_IP=$(hostname -I | awk '{print $2}')
   sudo tee /etc/caddy/Caddyfile > /dev/null <<EOF
   ${PRIVATE_IP} {
     reverse_proxy localhost:18789
   }
   EOF
   sudo systemctl restart caddy
   ```
3. **Get Gateway Token** – `cat /opt/openclaw.env`
4. **Install Twingate Connector** on Droplet:
   ```bash
   curl "https://binaries.twingate.com/connector/setup.sh" | \
   sudo TWINGATE_ACCESS_TOKEN="$TOKEN" TWINGATE_REFRESH_TOKEN="$REFRESH" \
   TWINGATE_NETWORK="yourcompany" bash
   ```
5. **Create Twingate Resource** – Address: `<droplet-private-ip>`, assign to group
6. **Lock down DigitalOcean Firewall** – Zero inbound rules; all outbound allowed
7. **Access Gateway** – `https://<droplet-private-ip>/?token=<gateway-token>` via Twingate Client

## Configuration Values

| Parameter | Value |
|---|---|
| OpenClaw port | `18789` |
| Gateway token file | `/opt/openclaw.env` |
| Caddy config | `/etc/caddy/Caddyfile` |
| Twingate label | `TWINGATE_LABEL_DEPLOYED_BY=openclaw` |
| Droplet image (API) | `openclaw` |
| Recommended size | `s-2vcpu-4gb` |

## Terraform Variables (`terraform.tfvars`)
- `do_token` – DigitalOcean API token
- `twingate_access_token` / `twingate_refresh_token`
- `twingate_network` – network name without `.twingate.com`
- `ssh_fingerprint`, `region`, `droplet_size`

## Gotchas
- Caddy defaults may expose public IP; must explicitly restrict to private IP
- Twingate Resource must be assigned to the same Remote Network where the Connector is installed
- After firewall lockdown, SSH only works via Twingate Client (private IP); public IP SSH will timeout by design
- Gateway prompts for AI provider key on first run; can skip with `CTRL-C`
- Connector tokens must be regenerated from Admin Console if Connector goes offline

## Related Docs
- [Twingate Connector Setup](https://www.twingate.com/docs/connectors)
- [OpenClaw Documentation](https://openclaw.ai/docs)
- [Terraform Reference Repo](https://github.com/Twingate-Community/secure-openclaw)