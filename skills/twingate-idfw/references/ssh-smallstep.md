# SSH Access Management with Twingate + Smallstep CA

## Summary
Integrates Twingate (network-layer access control) with Smallstep Certificate Authority (application-layer SSH authentication) on AWS. Uses Pulumi for infrastructure deployment. Provides short-lived SSH certificates via OAuth 2.0 instead of static keys.

## Key Information
- Deploys AWS VPC with public/private subnets, Route53 private hosted zone
- Two Twingate Connectors in public subnet; Smallstep CA in private subnet
- Smallstep open-source version requires manual user account creation on SSH hosts
- Short-lived certificates issued via OAuth 2.0 (Google Cloud used as example)
- Applies to any cloud/on-prem environment (Azure, GCP, OracleCloud)

## Prerequisites
- AWS CLI configured (or CloudShell)
- Pulumi CLI installed
- Twingate API token with **Read/Write and Provision** permissions
- Git
- Twingate Client installed
- OAuth 2.0 server (Google Cloud OAuth **Desktop app** credentials)
- AWS SSH Keypair (emergency fallback access)

## Step-by-Step

1. **Clone repo:** `git clone https://github.com/twingate/pulumi-twingate-smallstep && cd pulumi-twingate-smallstep`
2. **Create GCP OAuth Desktop app credentials** — note Client ID and Secret
3. **Init Pulumi stack:** `pulumi stack init dev && cp ./Pulumi.example.yaml ./Pulumi.dev.yaml`
4. **Set config values** (see Configuration Values below)
5. **Deploy:** `pulumi up`
6. **Grant user access** in Twingate Admin Console to the connector resource in `smallstep_demo` network
7. **Install step CLI** (see CLI commands below)
8. **Connect Twingate Client** on local machine
9. **Create local user on SSH host** (open-source Smallstep limitation): `sudo adduser --quiet --disabled-password --gecos '' YOUR_USERNAME`
10. **Bootstrap CA trust:** `./bootstrap_user.sh`
11. **Obtain SSH certificate:** `step ssh login YOUR_USERNAME@YOUR_DOMAIN --provisioner "Google"`
12. **Configure SSH:** `step ssh config && step ssh hosts`
13. **Connect:** `ssh YOUR_USERNAME@xxx.tgdemo.int`

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

## step CLI Install
| OS | Command |
|----|---------|
| macOS | `brew install step` |
| Ubuntu | `sudo wget https://dl.smallstep.com/cli/docs-cli-install/latest/step-cli_amd64.deb && sudo dpkg -i step-cli_amd64.deb` |
| Windows | `winget install Smallstep.step` |

## Gotchas
- Open-source Smallstep **does not manage user accounts** on SSH hosts — must manually `adduser` for each user
- `bootstrap_user.sh` implicitly trusts CA cert — use MDM for production certificate distribution
- Twingate network access must be granted before SSH certificate flow works
- OAuth domain restriction: only users matching `ca_oauth_allowed_domain` can authenticate

## Related Docs
- [Smallstep SSH managed service](https://smallstep.com/ssh/) — eliminates manual user management
- [Smallstep DIY SSO for SSH blog post](https://smallstep.com/blog/diy-single-sign-on-for-ssh/)
- Twingate blog: *The Many Layers of Zero Trust*
- [AWS SSH