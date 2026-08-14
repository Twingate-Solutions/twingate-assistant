---
source: https://www.twingate.com/docs/ssh-smallstep
type: docs
fetched: 2026-08-14
source_version: 4e171566dd7c8f2a286fc4a9033a4b6bc4c66ed9539b9078fdf2819ba2ff766f
---

# SSH Access Management with Twingate + Smallstep

## Page Title
How to Manage Access to SSH Resources (Twingate + Smallstep Integration)

## Summary
Twingate integrates with Smallstep Certificate Authority to provide application-layer authentication for SSH servers, augmenting Twingate's network-level protections. This guide uses Pulumi to deploy the full stack on AWS with OAuth 2.0-based short-lived SSH certificates.

## Key Information
- Combines Twingate (network access) + Smallstep CA (SSH certificate auth)
- Works on any cloud/on-prem (AWS, Azure, GCP, OracleCloud)
- Uses Pulumi IaC for deployment
- Smallstep open-source does **not** manage user accounts on SSH hosts — manual user creation required
- Short-lived SSH certificates issued via OAuth 2.0 (Google in this example)

## Prerequisites
- AWS CLI configured (or CloudShell)
- Pulumi CLI installed
- Twingate API token with **Read/Write and Provision** permissions
- Git
- Twingate Client installed
- OAuth 2.0 server access (Google Cloud used here — Desktop app credentials)
- AWS SSH Keypair (emergency fallback access)

## Step-by-Step

1. **Clone repo**: `git clone https://github.com/twingate/pulumi-twingate-smallstep`
2. **Create OAuth credentials** (GCP Desktop app): note Client ID and Client Secret
3. **Init Pulumi stack**: `pulumi stack init dev` + `cp ./Pulumi.example.yaml ./Pulumi.dev.yaml`
4. **Set config values** (see Configuration Values below)
5. **Deploy**: `pulumi up`
6. **Grant user access** in Twingate Admin Console to the connector resource in `smallstep_demo` Remote Network
7. **Install `step` CLI** on client machine
8. **Log in to Twingate Client**
9. **Create local user on SSH host**: `sudo adduser --quiet --disabled-password --gecos '' YOUR_USERNAME`
10. **Bootstrap CA trust**: run `./bootstrap_user.sh` on client
11. **Obtain SSH certificate**: `step ssh login YOUR_USERNAME@YOUR_DOMAIN --provisioner "Google"`
12. **Configure SSH**: `step ssh config` then `step ssh hosts`
13. **Connect**: `ssh YOUR_USERNAME@xxx.tgdemo.int`

## Configuration Values

```bash
pulumi config set --path ca_config.ca_oauth_client_id "CLIENT_ID"
pulumi config set --secret --path ca_config.ca_oauth_client_secret "CLIENT_SECRET"
pulumi config set --path ca_config.ca_oauth_allowed_domain "YOUR_DOMAIN_NAME"
pulumi config set twingate:apiToken TWINGATE_API_TOKEN --secret
pulumi config set twingate:network TWINGATE_ACCOUNT_NAME
pulumi config set --path ca_config.ca_email "YOUR_EMAIL_ADDRESS"
pulumi config set --path data.key_name "SSH_KEYPAIR_NAME"
```

## `step` CLI Install Commands
| OS | Command |
|----|---------|
| macOS | `brew install step` |
| Ubuntu | `sudo wget https://dl.smallstep.com/cli/docs-cli-install/latest/step-cli_amd64.deb && sudo dpkg -i step-cli_amd64.deb` |
| Windows | `winget install Smallstep.step` |

## Gotchas
- Open-source Smallstep does **not** manage user accounts — must manually `adduser` on each SSH host
- Root CA certificate must be distributed to clients; `bootstrap_user.sh` is for demo only — use MDM in production
- Only OAuth subjects matching `ca_oauth_allowed_domain` can connect
- Twingate access must be explicitly granted per user in Admin Console after deploy

## Related Docs
- [Smallstep SSH managed service](https://smallstep.com/ssh/) — eliminates manual user management
- [DIY Single Sign-On for SSH (Smallstep blog)](https://smallstep.com/blog/diy-single-sign-on-for-ssh/)
- [