# SSH PAM Deployment Guide

Reference for the `twingate-idfw` skill. Contains annotated config examples, install
commands, and the full end-to-end deployment walkthrough for Twingate SSH PAM.

---

## Gateway Config YAML

The gateway config YAML drives all IDFW behavior. Write it manually or generate it with
`twingate_gateway_config` (see `gateway-terraform-patterns.md`).

```yaml
# gateway-config.yaml
ssh:
  resources:
    - resource_id: "UmVzb3VyY2U6MTIz"      # Base64-encoded Twingate resource ID
      username: "ec2-user"                   # UNIX account — NOT set in admin console
      certificate_authority: |              # Twingate CA public key (from admin console)
        ssh-rsa AAAAB3NzaC1yc2EAAAADAQAB...

recording:
  enabled: true
  output_dir: "/var/log/twingate/recordings"
```

---

## Gateway Deployment Commands

Inspect the `Twingate/gateway` repo for current deployment configurations:

```bash
git clone https://github.com/Twingate/gateway
# Review deploy/ directory for Helm chart and Docker Compose examples
ls deploy/
```

**Docker Compose (fastest for evaluation):**

```bash
docker compose -f deploy/docker-compose.yaml up -d
```

**Helm (recommended for Kubernetes-hosted gateways):**

```bash
helm repo add twingate https://twingate.github.io/gateway
helm install twingate-gateway twingate/gateway \
  --namespace twingate \
  --set config.path=/etc/twingate/gateway-config.yaml
```

**systemd** — for VM or bare-metal deployments; see the `deploy/` directory for the
service unit file.

Deploy at least two gateway instances behind a load balancer. A single gateway instance
is a single point of failure for all SSH access to the resources it serves.

---

## PAM Module Install on Target Servers

Every target SSH server must have the Twingate PAM module installed.

```bash
# Ubuntu/Debian — quick install (review the script before running in production)
curl -s https://binaries.twingate.com/pam/install.sh | sudo bash

# Production alternative: download first, review, then run
curl -so install-pam.sh https://binaries.twingate.com/pam/install.sh
sudo bash install-pam.sh
```

---

## sshd_config Settings

On every target server:

```sshd
# /etc/ssh/sshd_config

# Point sshd to the Twingate CA public key
TrustedUserCAKeys /etc/ssh/twingate_ca.pub

# Disable static credentials — required to eliminate the bypass path
PasswordAuthentication no
PubkeyAuthentication no
ChallengeResponseAuthentication no

# PAM must be enabled
UsePAM yes
```

---

## PAM Stack Config

```pam
# /etc/pam.d/sshd — add at the TOP of the auth stack
auth required pam_twingate.so
```

---

## CA Public Key Deployment

Obtain the Twingate CA public key from the admin console under IDFW/gateway settings,
then deploy to each target server:

```bash
sudo cp twingate_ca.pub /etc/ssh/twingate_ca.pub
sudo chmod 644 /etc/ssh/twingate_ca.pub
sudo systemctl restart sshd
```

---

## End-to-End Verification Steps

1. User authenticates to Twingate on their device.
2. User SSHes to the resource FQDN/IP.
3. Twingate Client intercepts the connection and routes it through the gateway.
4. Gateway issues a short-lived SSH certificate signed by Twingate's CA.
5. SSH client presents the certificate; PAM on the target server validates it.
6. User is logged in as the UNIX username defined in the gateway config YAML.
7. If recording is enabled, the session is captured under the user's Twingate identity.
