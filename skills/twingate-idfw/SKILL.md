---
name: twingate-idfw
description: |
  Twingate Identity Firewall — SSH PAM, Kubernetes gateway, session recording,
  and privileged access management. Use this skill whenever the user mentions
  SSH with Twingate, privileged access, identity firewall, session recording,
  the Twingate gateway, SSH certificates, SSH PAM module, Ansible with Twingate
  SSH, contractor SSH access, or 'idfw'. This skill covers protocol-level
  identity enforcement, not just network-level access.
---

# twingate-idfw

## When to Use

Load this skill when the user asks about any of the following:

- SSH access via Twingate (certificates, PAM, key replacement)
- Identity Firewall (IDFW) — the term itself or the feature
- Twingate gateway — deployment, configuration, or troubleshooting
- Session recording for SSH or Kubernetes
- Privileged access management (PAM) with Twingate
- Contractor or vendor SSH access patterns
- `kubectl` access via the Twingate gateway
- Ansible playbooks using Twingate SSH certificates
- `twingate_gateway_config` Terraform resource
- K8s kubectl proxy with Twingate identity enforcement

Do NOT load this skill for general network connectivity questions — those belong in `twingate-connectors` or `twingate-architect`.

---

## Quick Reference

| Concept | Key Point |
|---|---|
| What IDFW is | Protocol-level identity enforcement, not just network access |
| Gateway vs. Connector | Gateway understands SSH/K8s semantics; connectors are transparent TCP tunnels |
| SSH username field | Defined in **gateway config YAML** — not in the admin console or API |
| Certificate lifetime | Short-lived (minutes to hours); expiry = automatic revocation |
| Session recording | Configured in gateway YAML; linked to Twingate user identity |
| PAM module | Must be installed on **each** target server |
| Terraform resource | `twingate_gateway_config` — generates YAML locally, no API call |
| K8s access | Gateway acts as an authenticated kubectl proxy with RBAC enforcement |
| Ansible | Works transparently — no plugin needed, cert is the SSH auth mechanism |
| Gateway repo | `github.com/Twingate/gateway` — inspect `deploy/` for Helm and Compose examples |

## Current Documentation

Twingate Identity Firewall documentation is available in `./references/`. If reference files are not yet populated, fetch directly:

```bash
# IDFW overview
curl -s https://www.twingate.com/docs/identity-firewall

# SSH PAM module setup
curl -s https://www.twingate.com/docs/ssh-pam

# Session recording
curl -s https://www.twingate.com/docs/session-recording

# Kubernetes gateway / kubectl proxy
curl -s https://www.twingate.com/docs/kubernetes-gateway
```

---

## Evergreen Knowledge

### What Identity Firewall (IDFW) Is

IDFW is protocol-level identity enforcement layered on top of Twingate's network-level access control.

A standard Twingate connector brokers TCP connections to resources — it is a transparent tunnel. The connector does not understand what protocol flows through it; it simply routes packets. IDFW goes one layer deeper: the Twingate **gateway** validates identity at the protocol level.

- For SSH: validates the user's Twingate-issued SSH certificate and maps it to the correct UNIX username.
- For Kubernetes: acts as an authenticated `kubectl` proxy, enforcing Twingate identity against K8s RBAC.

The gateway is an active protocol mediator. It understands SSH handshake semantics and Kubernetes API semantics, and it enforces identity rules inside the protocol — not just at the network boundary.

**Critical distinction:**
- Connectors = transparent TCP tunnels (network layer)
- Gateway = active protocol mediator (application layer)

These are complementary, not interchangeable. A connector alone cannot enforce SSH certificate validation or K8s RBAC — only the gateway can.

---

### The Gateway as the Enforcement Point

The gateway sits between the Twingate Client and the backend resource. Traffic flows:

```
Twingate Client → [Twingate network] → Gateway → Backend resource (SSH server / K8s API)
```

For SSH:
1. User authenticates to Twingate and requests access to an SSH resource.
2. Twingate issues a short-lived SSH certificate signed by Twingate's CA.
3. The user's SSH client connects through the Twingate network to the gateway.
4. The gateway validates the certificate (expiry, signature, principal).
5. The gateway maps the Twingate identity to the UNIX username defined in the gateway config YAML.
6. The gateway forwards the session to the backend SSH server using that UNIX username.
7. The target server's PAM module validates the certificate against Twingate's CA public key.

For Kubernetes:
1. User authenticates to Twingate; `kubectl` traffic routes through the gateway.
2. The gateway enforces K8s RBAC using Twingate identity attributes.
3. The gateway proxies valid requests to the K8s API server.

---

### SSH PAM Integration

SSH PAM is the most common IDFW use case. It replaces static SSH keys with short-lived certificates.

**How it works:**
- No static SSH keys are distributed. Users receive a short-lived SSH certificate from Twingate upon authentication.
- The PAM module is installed on each target server. When an SSH connection arrives, PAM validates the certificate signature against Twingate's CA public key.
- Certificates expire naturally — no revocation infrastructure, no key rotation, no `authorized_keys` management.

**Requirements:**
- Twingate gateway deployed and configured
- PAM module installed on every target server
- `sshd_config` updated on every target server to enable certificate authentication and disable password/key auth
- Gateway config YAML specifying the resource, UNIX username, and CA public key

**The `username` field — the most common source of confusion:**

The UNIX username that users log in as is defined in the **gateway config YAML** under `ssh.resources[].username`. It is not a field in:
- The Twingate admin console resource definition
- The `twingate_resource` Terraform resource
- The GraphQL API

If a user asks "where do I set the SSH username?", the answer is always: in the gateway config YAML.

---

### Gateway Config YAML — Critical Detail

The gateway config YAML is the central configuration artifact for IDFW. It controls:
- Which resources the gateway handles
- The UNIX username for each SSH resource
- The Twingate CA public key for certificate validation
- Session recording settings

Full annotated example:

```yaml
# gateway-config.yaml
# Generated by twingate_gateway_config Terraform resource
# Deploy this file to the gateway host at the path the gateway expects

ssh:
  resources:
    - resource_id: "UmVzb3VyY2U6MTIz"    # Base64-encoded Twingate resource ID
      username: "ec2-user"                 # UNIX account users log in as
      certificate_authority: |            # Twingate CA public key (from admin console)
        ssh-rsa AAAAB3NzaC1yc2EAAAADAQAB...

    - resource_id: "UmVzb3VyY2U6NDU2"
      username: "contractor_user"          # Restricted UNIX account for contractors
      certificate_authority: |
        ssh-rsa AAAAB3NzaC1yc2EAAAADAQAB...

recording:
  enabled: true
  output_dir: "/var/log/twingate/recordings"  # Gateway writes structured session logs here
```

The `twingate_gateway_config` Terraform resource generates this YAML locally — it makes no API call and creates no remote state. It is functionally equivalent to a `local_file` resource. Use a provisioner, Ansible, or your config management tool to deploy the resulting file to the gateway host.

---

### Session Recording

The gateway captures SSH sessions as structured audit logs associated with the Twingate user identity — not just the UNIX username. This is the key compliance advantage over traditional SSH logging: you know which Twingate user (email, IdP identity) performed every action, even if multiple users share a UNIX account.

**Configuration:**
- Set `recording.enabled: true` in the gateway config YAML.
- Specify `recording.output_dir` — the gateway writes structured session logs here.
- Playback is available via the Twingate admin console or by exporting the raw log files.

**Compliance note:** Deploy session recording from day one if your environment has any audit or compliance requirement. Retroactively enabling recording does not capture past sessions. Deploying the gateway without recording when compliance is required is an anti-pattern.

---

### Contractor and Vendor SSH Access Pattern

IDFW provides a clean, auditable pattern for granting contractors time-bounded SSH access without distributing credentials.

Step-by-step:

1. Create a dedicated UNIX account on the target server(s) with appropriate restrictions — e.g., `contractor_user` with a restricted shell or limited sudo rules.

2. Create a Twingate group for contractors, e.g., `contractors-linux-prod`.

3. Assign the group to the Twingate SSH resource in the admin console.

4. In the gateway config YAML, set `username: contractor_user` for that resource. All members of the Twingate group will log in as this UNIX account.

5. Add the contractor's Twingate user to the group. If JIT provisioning is configured, this happens automatically on first login.

6. Optionally, set a group membership expiry (time-bounded access). When the expiry passes, the contractor's group membership is removed — no SSH key rotation, no `authorized_keys` cleanup needed.

**Why this works:**
- The contractor never receives a static credential.
- Access is tied to Twingate group membership, which you control.
- Session recording ties every action to the contractor's Twingate identity.
- Revoking access is instant: remove the user from the Twingate group.

---

### PAM Configuration on Target Servers

Every target SSH server must have the PAM module installed and `sshd_config` updated.

**`sshd_config` changes:**

```sshd
# /etc/ssh/sshd_config

# Enable certificate authentication
TrustedUserCAKeys /etc/ssh/twingate_ca.pub   # Twingate CA public key

# Disable password and static key auth (recommended)
PasswordAuthentication no
PubkeyAuthentication no
ChallengeResponseAuthentication no

# Enable PAM
UsePAM yes
```

**`/etc/pam.d/sshd` — add the Twingate PAM module:**

```pam
# /etc/pam.d/sshd
# Add at the top of the auth stack

auth required pam_twingate.so
```

**Twingate CA public key (`/etc/ssh/twingate_ca.pub`):**
Obtain this from the Twingate admin console under the IDFW/gateway configuration section. Copy it to each target server. This is the public key that PAM uses to validate incoming certificates.

**After changes, restart sshd:**

```bash
sudo systemctl restart sshd
```

---

### Kubernetes Privileged Access via Gateway

The gateway can proxy `kubectl` commands with Twingate identity enforcement, eliminating the need for long-lived kubeconfig credentials or VPN for cluster access.

**How it works:**
1. Create a Twingate resource pointing to the K8s API server (e.g., `https://k8s-api.internal:6443`).
2. Deploy the gateway in kubectl proxy mode.
3. Users authenticate via Twingate; `kubectl` requests route through the gateway.
4. The gateway enforces K8s RBAC based on the user's Twingate identity attributes.
5. Valid requests are forwarded to the K8s API server.

**Benefits:**
- No long-lived kubeconfig credentials distributed to developers.
- Cluster access is gated by Twingate authentication and group membership.
- Session recording captures `kubectl` commands associated with the Twingate user identity.
- Works alongside the `twingate-kubernetes` skill's operator/Helm deployment patterns.

Refer to `Twingate/gateway` repo `deploy/` directory for Helm chart values specific to kubectl proxy mode.

---

### Ansible Automation with Twingate SSH Certificates

Twingate SSH certificates work transparently with Ansible. No special Ansible plugin or inventory extension is needed.

**How it works:**
Ansible uses SSH for transport. When the Twingate Client is running on the Ansible control node and the control node's user has authenticated to Twingate, SSH connections from Ansible to Twingate-protected SSH resources use the Twingate-issued certificate automatically.

**`ansible.cfg` — ensure SSH agent forwarding and certificate use:**

```ini
[defaults]
remote_user = ec2-user          # Must match the username in the gateway config YAML

[ssh_connection]
ssh_args = -o ForwardAgent=yes  # Forward the SSH agent so the cert is available
pipelining = True
```

**Inventory example:**

```ini
# inventory/hosts.ini

[linux_servers]
app-01 ansible_host=10.0.1.10
app-02 ansible_host=10.0.1.11

[linux_servers:vars]
ansible_user=ec2-user           # Match gateway config YAML username
# Use accept-new (trust-on-first-use) rather than no — reconnects verify host keys
ansible_ssh_common_args='-o StrictHostKeyChecking=accept-new'
```

**Requirements:**
- Twingate Client running on the Ansible control node.
- Control node user authenticated to Twingate with access to the SSH resources.
- SSH agent running with the Twingate certificate loaded.
- Target servers have PAM configured and `sshd_config` updated.

---

### Terraform for IDFW

The `twingate_gateway_config` resource generates the gateway YAML configuration file locally. It does not make any API call — it is a local code generation resource.

**Generate gateway YAML for an SSH resource:**

```hcl
# Fetch the resource ID (base64 encoded)
data "twingate_resource" "ssh_server" {
  id = var.ssh_resource_id
}

# Generate the gateway config YAML
resource "twingate_gateway_config" "ssh_gateway" {
  output_path = "${path.module}/gateway-config.yaml"

  ssh {
    resource {
      resource_id           = data.twingate_resource.ssh_server.id
      username              = "ec2-user"
      certificate_authority = var.twingate_ca_public_key
    }
  }

  recording {
    enabled    = true
    output_dir = "/var/log/twingate/recordings"
  }
}

# Write the generated YAML to a local file for deployment
resource "local_file" "gateway_config" {
  content  = twingate_gateway_config.ssh_gateway.content
  filename = "${path.module}/gateway-config.yaml"
}
```

**Deploy the generated config to the gateway host using a null provisioner or Ansible:**

```hcl
resource "null_resource" "deploy_gateway_config" {
  depends_on = [local_file.gateway_config]

  triggers = {
    config_hash = sha256(twingate_gateway_config.ssh_gateway.content)
  }

  provisioner "file" {
    source      = local_file.gateway_config.filename
    destination = "/etc/twingate/gateway-config.yaml"

    connection {
      type        = "ssh"
      user        = "ubuntu"
      host        = aws_instance.gateway.private_ip
      # Key file must have 0600 permissions; do not commit the key path variable value to source control
      private_key = file(var.gateway_ssh_key_path)
    }
  }

  provisioner "remote-exec" {
    inline = [
      "sudo systemctl restart twingate-gateway"
    ]

    connection {
      type        = "ssh"
      user        = "ubuntu"
      host        = aws_instance.gateway.private_ip
      private_key = file(var.gateway_ssh_key_path)
    }
  }
}
```

For provider setup and authentication, refer to the `twingate-terraform` skill.

---

### Gateway Deployment

The gateway is deployed separately from its config. It is not a Twingate connector — do not confuse the two.

**Deployment options (refer to `github.com/Twingate/gateway` `deploy/` for current examples):**

- **Docker Compose** — fastest for single-host evaluation:
  ```bash
  # From Twingate/gateway repo
  docker compose -f deploy/docker-compose.yaml up -d
  ```

- **Helm chart** — recommended for Kubernetes-hosted gateways:
  ```bash
  helm repo add twingate https://twingate.github.io/gateway
  helm install twingate-gateway twingate/gateway \
    --namespace twingate \
    --set config.path=/etc/twingate/gateway-config.yaml
  ```

- **systemd** — for VM or bare-metal deployments.

**High availability:** Run at least two gateway instances behind a load balancer. A single gateway instance is a single point of failure for all SSH access to resources it serves.

---

### Expansion-Ready Protocols

Web application gating and additional protocols beyond SSH and K8s are on the IDFW roadmap. Before assuming the current feature set is complete, check the Twingate docs sitemap for new IDFW sub-pages. The `references/` directory may contain an auto-updated summary of new capabilities added since this skill was authored.

---

## Common Patterns

### Pattern 1: Terraform — Generate Gateway Config for SSH Resource

```hcl
resource "twingate_gateway_config" "prod_ssh" {
  output_path = "${path.module}/gateway-config.yaml"

  ssh {
    resource {
      resource_id           = twingate_resource.linux_servers.id
      username              = "ec2-user"
      certificate_authority = var.twingate_ssh_ca_key
    }
  }

  recording {
    enabled    = true
    output_dir = "/var/log/twingate/recordings"
  }
}
```

### Pattern 2: Full Gateway Config YAML with Two Resources

```yaml
# gateway-config.yaml
ssh:
  resources:
    # Production Linux servers — full-time staff
    - resource_id: "UmVzb3VyY2U6MTIz"
      username: "ec2-user"
      certificate_authority: |
        ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC...

    # Contractor access — restricted account
    - resource_id: "UmVzb3VyY2U6NDU2"
      username: "contractor_user"
      certificate_authority: |
        ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC...

recording:
  enabled: true
  output_dir: "/var/log/twingate/recordings"
```

### Pattern 3: Contractor Access — End-to-End Flow

```
1. Admin creates UNIX account:
   $ sudo useradd -m -s /bin/rbash contractor_user
   $ sudo usermod -aG limited_tools contractor_user

2. Admin creates Twingate group "contractors-linux-prod" in admin console.

3. Admin assigns group to Twingate SSH resource in admin console.

4. Admin updates gateway config YAML:
   ssh.resources[].username = "contractor_user"

5. Admin restarts the gateway to reload config.

6. Admin adds contractor's Twingate user to "contractors-linux-prod" group.
   (Optionally set membership expiry for time-bounded access.)

7. Contractor authenticates to Twingate → receives short-lived SSH cert.

8. Contractor SSHs to the resource → logs in as contractor_user.

9. Session is recorded under the contractor's Twingate identity.

10. Access expiry → contractor auto-removed from group → cert issuance blocked.
    No key rotation. No authorized_keys cleanup.
```

### Pattern 4: PAM Configuration on Target Server

```bash
# 1. Install Twingate PAM module (Ubuntu/Debian)
# Production: download, review, then run. Quick install for dev/staging:
curl -s https://binaries.twingate.com/pam/install.sh | sudo bash
# Production alternative: curl -so install-pam.sh https://binaries.twingate.com/pam/install.sh && sudo bash install-pam.sh

# 2. Copy Twingate CA public key to server
sudo cp twingate_ca.pub /etc/ssh/twingate_ca.pub
sudo chmod 644 /etc/ssh/twingate_ca.pub

# 3. Update /etc/ssh/sshd_config
sudo tee -a /etc/ssh/sshd_config <<EOF
TrustedUserCAKeys /etc/ssh/twingate_ca.pub
PasswordAuthentication no
PubkeyAuthentication no
UsePAM yes
EOF

# 4. Add PAM module to auth stack
sudo sed -i '1s/^/auth required pam_twingate.so\n/' /etc/pam.d/sshd

# 5. Restart sshd
sudo systemctl restart sshd
```

### Pattern 5: Ansible with Twingate SSH Certificates

```ini
# ansible.cfg
[defaults]
remote_user = ec2-user
# host_key_checking = False  # Avoid in production — disables MITM protection entirely

[ssh_connection]
# Use accept-new (TOFU) not no — verifies host key on reconnect, prevents MITM
ssh_args = -o ForwardAgent=yes -o StrictHostKeyChecking=accept-new
pipelining = True
```

```yaml
# playbook.yml
---
- name: Configure application servers
  hosts: linux_servers
  become: true

  tasks:
    - name: Ensure app directory exists
      file:
        path: /opt/app
        state: directory
        owner: ec2-user

    - name: Deploy application config
      template:
        src: templates/app.conf.j2
        dest: /opt/app/app.conf
```

```bash
# Run — Twingate Client must be running and authenticated
ansible-playbook -i inventory/hosts.ini playbook.yml
```

---

## Anti-Patterns and Gotchas

**Do not configure the SSH username in the Twingate admin console resource definition.**
The `username` field does not exist there. The admin console resource definition controls network access (which groups can reach the resource). The UNIX username is configured exclusively in the gateway config YAML. Searching the admin console or GraphQL API for a username field wastes time.

**Do not deploy the gateway without session recording when audit compliance is required.**
Recording must be enabled before sessions begin — it is not retroactive. If your environment has compliance requirements (SOC 2, HIPAA, PCI-DSS), enable `recording.enabled: true` in the gateway config on day one.

**Do not leave static SSH keys in place alongside Twingate SSH certificates.**
Disabling static key authentication (`PubkeyAuthentication no`) in `sshd_config` is required to close the credential bypass path. Leaving keys active defeats the purpose of certificate-based authentication — a compromised static key grants access regardless of Twingate policy.

**Do not run a single gateway instance in production.**
A single gateway is a single point of failure for all SSH and K8s access to the resources it serves. Deploy at least two gateway instances behind a load balancer. Loss of the gateway = loss of SSH access to all governed resources.

**Do not confuse the gateway with connectors.**
Connectors handle network-layer TCP routing and cannot validate SSH certificates or enforce K8s RBAC. The gateway is a separate binary deployed separately. Adding more connectors will not provide IDFW capabilities — you need a gateway.

**Do not skip PAM module installation on target servers.**
The gateway validates the certificate before forwarding the connection, but the target server also needs the PAM module to complete the validation chain. Servers without the PAM module may fall back to password or key auth (depending on `sshd_config`), creating a bypass path.

---

## Related Skills

- [twingate-terraform](../twingate-terraform/SKILL.md) — `twingate_gateway_config` resource details, provider setup, and state management for IDFW Terraform configurations.
- [twingate-connectors](../twingate-connectors/SKILL.md) — connector deployment and the fundamental distinction between connectors (network layer) and the gateway (protocol layer).
- [twingate-kubernetes](../twingate-kubernetes/SKILL.md) — K8s operator, Helm chart, and resource routing; complements the gateway's kubectl proxy mode.
- [twingate-identity](../twingate-identity/SKILL.md) — group membership management, JIT access provisioning, device trust, and time-bounded access patterns used in the contractor SSH flow.
- [twingate-architect](../twingate-architect/SKILL.md) — overall Twingate architecture context, including how the gateway fits into the control plane and data plane.
