---
source: https://www.twingate.com/docs/ssh-installation
type: docs
fetched: 2026-11-13
source_version: 75136bd6d22451d44740f45b02fb24d5a72aa6f90fee363068763669b68486e0
trust: official
---

# Installing Privileged Access for SSH

## Summary
Twingate recommends deploying Privileged Access for SSH with the Twingate Terraform provider, which publishes complete, runnable examples per cloud (AWS, DigitalOcean, GCE). Each example covers the CAs, Twingate objects, SSH Resource, Gateway VM, and target SSH server configuration. A manual Docker/GraphQL path and a Vault-backed SSH CA option are also available.

## Key Information
- Terraform guides include full configuration, startup scripts, and deployment steps for a specific cloud.
- Quick-start guides use a **local SSH CA**: the Gateway holds the CA private key and signs certificates directly. Intended for trying out SSH access.
- For production, the Gateway can use **HashiCorp Vault's SSH secrets engine** instead of a local CA.
- Two CAs are involved:
  - **X.509 CA**: secures TLS between the Twingate Client and the Gateway.
  - **SSH CA**: signs the short-lived certificates the Gateway uses to sign in to target servers.

## Prerequisites
- Twingate account with administrator privileges
- A Remote Network
- Twingate Client meeting the minimum version requirements
- Terraform installed

## Step-by-Step (what each Terraform guide provisions, in order)
1. Create the X.509 CA and SSH CA.
2. Create Twingate objects: Remote Network, CA registrations, `twingate_gateway`, and a Connector with tokens.
3. Create a `twingate_ssh_resource` bound to the Gateway, with access granted to a Group.
4. Deploy the Gateway VM running Twingate Gateway with a YAML config pointing to its TLS certificate, the SSH CA key, and the sign-in account.
5. Configure the target SSH server: `sshd` trusts the SSH CA and has a Linux account matching `ssh.gateway.username`.

## Configuration Values
- Terraform resources:
  - `twingate_x509_certificate_authority`
  - `twingate_ssh_certificate_authority`
  - `twingate_gateway`
  - `twingate_ssh_resource`
- Gateway YAML: `ssh.gateway.username` (account the Gateway signs in as on target servers)
- sshd: `TrustedUserCAKeys` (path to the SSH CA public key)

## Gotchas
- The Linux account on each target server must match `ssh.gateway.username`.
- Local SSH CA is for evaluation; use Vault for production.
- The Gateway YAML must reference the correct TLS certificate and SSH CA key.
- The Client must meet the minimum version requirements.

## Manual Alternative
Run the Gateway as a Docker container and register it via the Twingate GraphQL API using the Gateway SSH installation guide. It covers generating both CAs, creating the Gateway and SSH Resource, writing the Gateway config, and configuring SSH servers to trust the CA.

## Related Docs
- Terraform guides: Local SSH CA on AWS, DigitalOcean, GCE
- Gateway SSH installation guide (manual/Docker)
- Vault integration guide (Vault as SSH CA)
- Remote Development with VS Code (VS Code Remote SSH setup)