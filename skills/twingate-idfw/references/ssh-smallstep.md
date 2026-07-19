# SSH Access Management with Twingate + Smallstep CA

## Page Title
How to Manage Access to SSH Resources (Twingate + Smallstep Integration)

## Summary
Twingate integrates with Smallstep Certificate Authority to provide application-layer authentication for SSH servers, complementing Twingate's network-level access controls. This guide deploys the complete stack on AWS using Pulumi, combining Twingate for network invisibility/least-privilege with Smallstep for short-lived SSH certificates via OAuth2.0.

## Key Information
- Provides two layers of security: Twingate (network layer) + Smallstep CA (application layer)
- Smallstep open-source version does **not** manage user accounts on SSH hosts — manual account creation required
- Works on any cloud/on-prem environment (AWS, Azure, GCP, OracleCloud)
- Infrastructure-as-code via Pulumi; repo: `github.com/twingate/pulumi-twingate-smallstep`
- Short-lived SSH certificates issued via OAuth2.0 (Google Cloud used in example)

## Prerequisites
- AWS CLI installed and configured
- Pulumi CLI installed and configured
- Twingate API token with **Read/Write and Provision** permissions
- Git
- Twingate Client installed on local machine
- OAuth 2.0 server access (Google Cloud Desktop app credentials)
- AWS SSH Keypair (emergency fallback access)
- `step` CLI installed on client machine

## Step-by-Step

1. Clone repo: `git clone https://github.com/twingate/pulumi-twingate-smallstep && cd pulumi-twingate-smallstep`
2. Create GCP OAuth Desktop app credentials; note Client ID and Secret
3. `pulumi stack init dev`
4. `cp ./Pulumi.example.yaml ./Pulumi.dev.yaml`
5. Set all config values (see Configuration Values below)
6. `pulumi up` — deploys AWS VPC, subnets, EC2 instances, Smallstep CA, Route53 zone, Twingate resources
7. In Twingate Admin Console, grant your user access to the Connector resource in `smallstep_demo` remote network
8. Install `step` CLI on local machine
9. Log in to Twingate Client
10. SSH into Connector host using keypair; create local user: `sudo adduser --quiet --disabled-password --gecos '' YOUR_USERNAME`
11. Run `./bootstrap_user.sh` on client to trust CA certificate
12. Obtain SSH certificate: `step ssh login YOUR_USERNAME@YOUR_DOMAIN --provisioner "Google"`
13. Run `step ssh config` and `step ssh hosts`
14. Connect: `ssh YOUR_USERNAME@xxx.tgdemo.int`

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

## Gotchas
- Open-source Smallstep requires **manual user account creation** on each SSH host — not automated
- `bootstrap_user.sh` implicitly trusts CA cert; use MDM for distributing root cert in production
- OAuth domain restriction (`ca_oauth_allowed_domain`) limits which users can authenticate — must match your org's domain
- Connectors deployed in **public subnet**; Smallstep CA in **private subnet** (only accessible via Twingate)

## Related Docs
- [Twingate Best Practices for Connectors](https://www.twingate.com/docs)
- [Smallstep SSH (managed service)](https://smallstep.com/ssh/)
- [Smallstep DIY SSO for SSH blog post](https://smallstep.com/blog/d