# Gateway Terraform and Ansible Patterns

Reference for the `twingate-idfw` skill. Contains the `twingate_gateway_config`
Terraform resource pattern, Ansible `ansible.cfg` configuration, and requirements
checklist for Ansible + Twingate SSH certificate integration.

---

## Terraform — Full Reference Pattern

### variables.tf

```hcl
variable "twingate_ca_public_key" {
  description = "Twingate CA public key — obtain from admin console, IDFW section"
  type        = string
  sensitive   = true   # Treat as sensitive — do not output in plaintext
}

variable "ssh_resource_id" {
  description = "Base64-encoded Twingate resource ID for the SSH target"
  type        = string
}

variable "gateway_ssh_key_path" {
  description = "Path to SSH private key for provisioner access to gateway host"
  type        = string
  sensitive   = true
}
```

### main.tf

```hcl
resource "twingate_gateway_config" "prod_ssh" {
  output_path = "${path.module}/gateway-config.yaml"

  ssh {
    resource {
      resource_id           = var.ssh_resource_id
      username              = "ec2-user"
      certificate_authority = var.twingate_ca_public_key
    }
  }

  recording {
    enabled    = true
    output_dir = "/var/log/twingate/recordings"
  }
}

resource "local_file" "gateway_config_file" {
  content         = twingate_gateway_config.prod_ssh.content
  filename        = "${path.module}/gateway-config.yaml"
  file_permission = "0600"   # Config contains CA key material — restrict permissions
}

# Deploy the config to the gateway host.
# `null_resource` (hashicorp/null provider) is still fully supported.
# Terraform 1.4+ introduced `terraform_data` as a native alternative if preferred.
# For deploying to multiple gateway instances, use the Ansible pattern below —
# provisioners work best for single-host demos.
resource "null_resource" "deploy_gateway_config" {
  depends_on = [local_file.gateway_config_file]

  triggers = {
    config_hash = sha256(twingate_gateway_config.prod_ssh.content)
  }

  provisioner "file" {
    source      = local_file.gateway_config_file.filename
    destination = "/etc/twingate/gateway-config.yaml"

    connection {
      type        = "ssh"
      user        = "ubuntu"
      host        = aws_instance.gateway.private_ip
      private_key = file(var.gateway_ssh_key_path)
    }
  }

  provisioner "remote-exec" {
    inline = ["sudo systemctl restart twingate-gateway"]

    connection {
      type        = "ssh"
      user        = "ubuntu"
      host        = aws_instance.gateway.private_ip
      private_key = file(var.gateway_ssh_key_path)
    }
  }
}
```

For provider setup, authentication, and state management, refer to the
`twingate-terraform` skill.

---

## Ansible Configuration

```ini
# ansible.cfg
[defaults]
remote_user = ec2-user          # Must match username in gateway config YAML

[ssh_connection]
ssh_args = -o ForwardAgent=yes -o StrictHostKeyChecking=accept-new
pipelining = True
```

Use `StrictHostKeyChecking=accept-new` (trust-on-first-use), not `=no`. `accept-new`
verifies the host key on subsequent connections, preventing MITM attacks. `=no` disables
all host key checking and should never be used in production.

---

## Ansible Requirements Checklist

- Twingate Client running on the Ansible control node.
- Control node user authenticated to Twingate with access to the target resources.
- SSH agent running with the Twingate certificate loaded.
- Target servers have PAM configured and `sshd_config` updated (see
  `ssh-pam-deployment-guide.md`).
