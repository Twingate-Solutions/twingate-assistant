## Securing OpenClaw on DigitalOcean with Twingate

End-to-end deployment of **OpenClaw** (community-built AI assistant for WhatsApp/Telegram, formerly ClawdBot/MoltBot) on a DigitalOcean Droplet, fronted by a Twingate Connector for Zero Trust access.

### Architecture

- **DigitalOcean Droplet** runs OpenClaw Gateway (Node.js, listens on `localhost:18789`)
- **Caddy** reverse-proxies to private IP only (no public exposure)
- **Twingate Connector** on the same Droplet provides outbound-only secure access
- **Team members** access via Twingate Client -- no SSH, no VPN, no public ports

### Build Pattern (4 stages)

**Stage 1: Deploy Droplet from Marketplace**
- Visit DigitalOcean Marketplace -> OpenClaw -> Create Droplet
- Recommended size: `s-2vcpu-4gb` or larger (4-8 GB RAM)
- Or via API: `image: openclaw`, region of choice
- Includes: Ubuntu 22.04 LTS, OpenClaw + Node.js pre-installed

**Stage 2: Configure Caddy for Private IP Only**
- SSH in (initial public access via SSH key)
- Get private IP: `hostname -I | awk '{print $2}'`
- Edit `/etc/caddy/Caddyfile` to bind only to the private IP
- Restart Caddy: `sudo systemctl restart caddy`
- Locate gateway token: `cat /opt/openclaw.env`

**Stage 3: Deploy Twingate Connector**
- Twingate Admin Console -> Remote Networks -> Add Connector (Linux)
- Generate Access + Refresh Tokens
- On the Droplet:
  ```
  curl https://binaries.twingate.com/connector/setup.sh | sudo \
    TWINGATE_ACCESS_TOKEN=... \
    TWINGATE_REFRESH_TOKEN=... \
    TWINGATE_NETWORK=yourcompany \
    TWINGATE_LABEL_DEPLOYED_BY="openclaw" \
    bash
  ```
- Verify: `sudo systemctl status twingate-connector`
- Create a Twingate Resource for the Droplet's private IP
- Add Group access; install Twingate Client on user devices to test

**Stage 4: Lock Down the VPC**
- DigitalOcean Console -> Networking -> Firewalls -> Create
- **Inbound rules: leave EMPTY** (zero inbound, including SSH)
- **Outbound rules: allow all** (Connector needs outbound; AI providers need API access)
- Apply to Droplet
- Verify: SSH from a non-Twingate machine should time out

### Connector Configuration Values

- `TWINGATE_NETWORK`: tenant subdomain (no `.twingate.com` suffix)
- `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`: per-Connector tokens
- `TWINGATE_LABEL_DEPLOYED_BY=openclaw`: useful for filtering Connectors in Admin Console

### Decision Notes

- The "zero inbound" pattern is the strongest possible network isolation -- combined with Twingate, no port (including SSH) is exposed
- For team deployments: create a dedicated Group for OpenClaw access; use Resource Approvers (per /docs/resources-reviewing-access-requests) for delegated approval
- A Terraform variant exists at `Twingate-Community/secure-openclaw` (terraform/digitalocean/) for IaC deployments

### Gotchas

- Forgetting to update Caddyfile to private-IP-only leaves OpenClaw publicly reachable -- always verify with `curl http://<droplet-public-ip>` (should fail)
- Connector goes "Disconnected" if outbound is blocked -- verify firewall outbound rules before locking inbound
- Marketplace image versions can lag -- always update via `apt` after deploy

### Related Docs

- /docs/openclaw -- Multi-platform OpenClaw deployment overview
- /docs/openclaw-docker-compose -- Local/Docker deployment
- /docs/connector-deployment -- Generic Connector install
- /docs/connector-best-practices -- Connector deployment guidance
- /docs/resources, /docs/groups -- Resource + Group management
