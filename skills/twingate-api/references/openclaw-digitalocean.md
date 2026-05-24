# Setup and Secure OpenClaw on DigitalOcean

## Summary
Deploy OpenClaw (AI-powered WhatsApp/Telegram assistant) on a DigitalOcean Droplet using the Marketplace image, then secure it with Twingate Zero Trust access. The result is a privately-accessible AI gateway with no public ports exposed—all access routed through Twingate Connector.

## Key Information
- OpenClaw Gateway runs on `localhost:18789` (Node.js)
- Caddy reverse proxy restricts access to private IP only
- Twingate Connector installed on same Droplet handles all remote access
- No inbound firewall rules needed; Connector uses outbound-only connections
- Gateway token stored at `/opt/openclaw.env`
- Total setup time: 20–30 minutes

## Prerequisites
- DigitalOcean account with SSH key added
- Twingate account (free tier works)
- SSH access to Droplet during setup
- Optional: Terraform for automated deployment

## Step-by-Step

**1. Deploy Droplet** — Create from [DigitalOcean Marketplace](https://marketplace.digitalocean.com/) using OpenClaw image; recommended size: `s-2vcpu-4gb` or larger, Ubuntu 22.04 LTS.

**2. Configure Caddy** — SSH in, restrict Caddyfile to private IP only:
```bash
PRIVATE_IP=$(hostname -I | awk '{print $2}')
sudo tee /etc/caddy/Caddyfile > /dev/null <<EOF
${PRIVATE_IP} {
  reverse_proxy localhost:18789
}
EOF
sudo systemctl restart caddy
```

**3. Get Gateway Token** — `cat /opt/openclaw.env`

**4. Install Twingate Connector** — Generate tokens in Twingate Admin Console, then:
```bash
curl "https://binaries.twingate.com/connector/setup.sh" | \
sudo TWINGATE_ACCESS_TOKEN="$TOKEN" \
TWINGATE_REFRESH_TOKEN="$REFRESH" \
TWINGATE_NETWORK="yourcompany" \
bash
```

**5. Add Twingate Resource** — In Admin Console: Resources → Add Resource → set Address to `<droplet-private-ip>`, assign to group.

**6. Lock Down Firewall** — In DigitalOcean: Networking → Firewalls → zero inbound rules, all outbound allowed (TCP/UDP/ICMP).

**7. Access Gateway** — With Twingate Client connected: `https://<droplet-private-ip>/?token=<gateway-token>`

## Configuration Values

| Variable | Description |
|---|---|
| `TWINGATE_ACCESS_TOKEN` | Connector access token from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Connector refresh token from Admin Console |
| `TWINGATE_NETWORK` | Twingate network name (without `.twingate.com`) |
| `TWINGATE_LABEL_DEPLOYED_BY` | Set to `openclaw` for labeling |
| Gateway port | `18789` |
| Terraform repo | `github.com/Twingate-Community/secure-openclaw` |

## Gotchas
- Caddy defaults to public IP; must explicitly reconfigure to private IP only
- Resource must be assigned to the Remote Network where the Connector is installed (easy to miss with multiple networks)
- After firewall lockdown, SSH only works via Twingate Client + private IP—public SSH will timeout by design
- Gateway prompts for AI provider API key on first SSH login; can skip with CTRL-C
- Terraform does **not** auto-create the Twingate Resource—must be added manually post-deploy

## Related Docs
- [OpenClaw Documentation](https://openclaw.ai/docs)
- [Twingate Connector Setup](https://www.twingate.com/docs/connectors)
- [Terraform Reference Repo](https://github.com/Twingate-Community/secure-openclaw)