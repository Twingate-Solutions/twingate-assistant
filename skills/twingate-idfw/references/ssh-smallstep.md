## SSH with Twingate + Smallstep CA (Application-Layer Auth)

How to combine Twingate's network-layer access with Smallstep's certificate authority for SSH access -- giving you both invisible network access *and* short-lived, identity-bound SSH credentials.

**What This Pattern Solves:**
- **Network layer**: Twingate keeps SSH hosts off the public internet, gates network reach by Group
- **Application layer**: Smallstep issues short-lived SSH certificates tied to OAuth identity (e.g., `charles@example.com`) -- replaces long-lived SSH keys
- Together: even if a Twingate-authorized user has network access, they still need a fresh Smallstep cert (typically 16h or shorter) to actually SSH in

**Architecture (deployed via Pulumi from twingate/pulumi-twingate-smallstep):**
- AWS VPC with public + private subnets
- 2 Twingate Connectors in the public subnet
- Smallstep CA on an EC2 instance in the private subnet
- Route53 Private Hosted Zone (`tgdemo.int`) for friendly hostnames
- Twingate Resources for each Connector + the CA

**Prerequisites:**
- AWS CLI + Pulumi CLI installed
- Twingate API token (Read/Write/Provision)
- OAuth 2.0 provider (guide uses Google Cloud "Desktop app" credentials)
- AWS SSH keypair for emergency access
- Twingate Client installed
- Smallstep `step` CLI: `brew install step` (macOS) / `sudo dpkg -i step-cli_amd64.deb` (Ubuntu) / `winget install Smallstep.step` (Windows)

**Pulumi Config (key values):**
```
pulumi config set --path ca_config.ca_oauth_client_id "<CLIENT_ID>"
pulumi config set --secret --path ca_config.ca_oauth_client_secret "<CLIENT_SECRET>"
pulumi config set --path ca_config.ca_oauth_allowed_domain "<your-domain>"
pulumi config set twingate:apiToken <TOKEN> --secret
pulumi config set twingate:network <TENANT>
pulumi config set --path ca_config.ca_email "<your@email>"
pulumi config set --path data.key_name "<aws-keypair-name>"
pulumi up
```

**End-User Flow After Deployment:**
1. Admin grants user access to the Connector Resource in the `smallstep_demo` Remote Network (Admin Console)
2. User connects to Twingate Client
3. User runs `./bootstrap_user.sh` once to trust the Smallstep root CA (use MDM in production)
4. User generates a short-lived SSH cert via OAuth:
   ```
   step ssh login YOUR_USERNAME@YOUR_DOMAIN --provisioner "Google"
   step ssh config
   step ssh hosts
   ```
5. SSH normally: `ssh YOUR_USERNAME@xxx.tgdemo.int` -- Smallstep injects the short-lived cert

**Open-Source Smallstep Limitation:**
- Does **not** manage Linux user accounts on SSH hosts -- you must manually `sudo adduser --quiet --disabled-password --gecos '' <username>` on each host
- For automated user provisioning + lifecycle, use the **managed Smallstep SSH** service

**Gotchas:**
- SSH with long-lived public keys still works on the hosts unless you disable `PubkeyAuthentication` in `sshd_config` -- explicitly disable for full Smallstep enforcement
- Root CA distribution: `bootstrap_user.sh` is fine for demos; production must distribute the CA cert via MDM/configuration management
- OAuth `allowed_domain` gates which OAuth subjects can request certs -- restrict to your corporate domain

**Twingate's IDFW (Identity Firewall) Note:**
This Smallstep pattern predates Twingate's native Identity Firewall for SSH. For new deployments, also evaluate /docs/ssh-privileged-access-overview which provides identity propagation natively without a separate CA.

**Related Docs:**
- /docs/ssh-privileged-access-overview -- Twingate's native SSH IDFW (newer, integrated)
- /docs/identity-firewall -- IDFW overview
- /docs/private-dns-best-practices -- Private hosted zone patterns
