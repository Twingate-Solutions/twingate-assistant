# SSH Access Management with Twingate + Smallstep CA

## Summary
Combines Twingate network-level access control with Smallstep Certificate Authority for application-layer SSH authentication. Uses short-lived OAuth2.0-backed SSH certificates alongside Twingate's network invisibility. Deployed via Pulumi on AWS.

## Key Information
- Twingate handles network access (resource invisibility, least-privilege)
- Smallstep CA handles SSH authentication via short-lived certificates
- OAuth2.0 (e.g., Google) used as identity provider for certificate issuance
- Open-source Smallstep does **not** manage user accounts on SSH hosts — manual account creation required
- Managed Smallstep SSH service available to avoid self-managing CA and user accounts

## Prerequisites
- AWS CLI configured (or CloudShell)
- Pulumi CLI installed
- Twingate API token with **Read/Write and Provision** permissions
- Git
- Twingate Client installed
- OAuth 2.0 credentials (Google Cloud "Desktop app" credentials)
- AWS SSH Keypair (fallback access)

## Step-by-Step

1. Clone repo: `git clone https://github.com/twingate/pulumi-twingate-smallstep`
2. Create GCP OAuth "Desktop app" credentials; note Client ID and Secret
3. Initialize Pulumi stack: `pulumi stack init dev`
4. Copy config: `cp ./Pulumi.example.yaml ./Pulumi.dev.yaml`
5. Set configuration values (see below)
6. Deploy: `pulumi up`
7. Grant user access to Connector Resource in `smallstep_demo` Remote Network via Admin Console
8. Install `step` CLI on client machine
9. Log in to Twingate Client
10. Manually create SSH user account on host: `sudo adduser --quiet --disabled-password --gecos '' YOUR_USERNAME`
11. Bootstrap CA trust on client: `./bootstrap_user.sh`
12. Obtain SSH certificate and connect:
```bash
step ssh login YOUR_USERNAME@YOUR_DOMAIN --provisioner "Google"
step ssh config
step ssh hosts
ssh YOUR_USERNAME@xxx.tgdemo.int
```

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

## Infrastructure Created
- AWS VPC with public/private subnets and internet gateway
- 2 EC2 Twingate Connectors (public subnet)
- Smallstep CA EC2 instance (private subnet)
- Route53 Private Hosted Zone (`*.tgdemo.int`)
- Twingate Remote Network with Resources for Connectors and Smallstep CA

## Gotchas
- Open-source Smallstep requires **manual user account creation** on each SSH host
- CA root certificate must be distributed to clients (use MDM in production; `bootstrap_user.sh` is demo-only)
- `ca_oauth_allowed_domain` restricts which OAuth users can authenticate — set to your org's domain
- Connector Resources are in `smallstep_demo` Remote Network; user access must be explicitly granted

## Related Docs
- [Smallstep DIY SSO for SSH](https://smallstep.com/blog/diy-single-sign-on-for-ssh/)
- [Smallstep Managed SSH](https://smallstep.com/ssh/)
- Twingate blog: "The Many Layers of Zero Trust"