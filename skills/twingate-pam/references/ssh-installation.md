---
source: https://www.twingate.com/docs/ssh-installation
type: docs
fetched: 2026-11-22
source_version: bcfd1a7e4c9a337fc71c5ebd5ea195f64cfa2e155602a4dbfa2ebd3dc8a31a49
trust: official
---

# Installing Privileged Access for SSH

## Summary
Twingate recommends deploying Privileged Access for SSH with the Twingate Terraform provider. Each cloud-specific guide has full Terraform config, startup scripts, and deployment steps. A manual Docker/GraphQL path and a Vault-backed SSH CA option are also available.

## Key Information
- Terraform creates, in order:
  1. **Two CAs**: an X.509 CA (TLS between Client and Gateway) and an SSH CA (signs short-lived certs the Gateway uses to log in to targets).
  2. **Twingate objects**: Remote Network, `twingate_x509_certificate_authority`, `twingate_ssh_certificate_authority`, `twingate_gateway`, and a Connector with tokens.
  3. **SSH Resource**: `twingate_ssh_resource` bound to the Gateway, with access granted to a Group.
  4. **Gateway**: a VM running the Twingate Gateway (https://github.com/Twingate/gateway), with YAML config pointing to the TLS cert, SSH CA key, and sign-in account (`ssh.gateway.username`).
  5. **Target SSH server**: `sshd` trusting the SSH CA (`TrustedUserCAKeys`), with a Linux account matching `ssh.gateway.username`.
- Quick-start guides use a **local SSH CA** (Gateway holds the CA private key). Suited to trials.
- For production, use HashiCorp Vault's SSH secrets engine as the CA.

## Prerequisites
- Twingate account with administrator privileges
- A Remote Network
- Twingate Client meeting minimum version requirements (see the SSH Privileged Access overview, https://www.twingate.com/docs/ssh-privileged-access-overview#client-version)
- Terraform installed (https://developer.hashicorp.com/terraform/install)

## Step-by-Step: Sign target host keys (removes TOFU)
By default the Gateway trusts host keys on first use. To verify against the CA instead:
1. On each target server, sign the host key:
   ```
   sudo ssh-keygen -s ssh_ca -I <hostname> -h \
   -n <hostname>,<address> -V +52w \
   /etc/ssh/ssh_host_ed25519_key.pub
   ```
   This writes `/etc/ssh/ssh_host_ed25519_key-cert.pub`.
2. Add to sshd config (e.g. `/etc/ssh/sshd_config.d/twingate.conf`):
   ```
   HostKey /etc/ssh/ssh_host_ed25519_key
   HostCertificate /etc/ssh/ssh_host_ed25519_key-cert.pub
   TrustedUserCAKeys /etc/ssh/twingate_ca.pub
   ```
3. Reload `sshd`.

## Configuration Values
- Terraform resources: `twingate_x509_certificate_authority`, `twingate_ssh_certificate_authority`, `twingate_gateway`, `twingate_ssh_resource`
- Gateway YAML: `ssh.gateway.username`
- sshd: `TrustedUserCAKeys`, `HostKey`, `HostCertificate`
- `ssh-keygen`: `-s` (CA key), `-I` (identity), `-h` (host cert), `-n` (principals), `-V +52w` (validity)

## Gotchas
- Host certificates expire after 52 weeks (`-V +52w`); re-sign before expiry.
- The Linux account on each target must match `ssh.gateway.username`.
- The local SSH CA quick-starts keep the CA private key on the Gateway; not the production recommendation.

## Related Docs
- Terraform quick-starts (local SSH CA):
  - AWS (https://registry.terraform.io/providers/Twingate/twingate/latest/docs/guides/aws-gateway-ssh-self-signed-guide)
  - DigitalOcean (https://registry.terraform.io/providers/Twingate/twingate/latest/docs/guides/do-gateway-ssh-self-signed-guide)
  - GCE (https://registry.terraform.io/providers/Twingate/twingate/latest/docs/guides/gce-gateway-ssh-self-signed-guide)
- Vault integration guide (https://registry.terraform.io/providers/Twingate/twingate/latest/docs/guides/gce-gateway-ssh-vault-guide)
- Manual Gateway SSH installation, Docker + GraphQL API (https://github.com/Twingate/gateway/wiki/SSH-Installation)
- Remote Development with VS Code (https://www.twingate.com/docs/ssh-remote-development)