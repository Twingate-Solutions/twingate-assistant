# SSH Access Management with Twingate + Smallstep

## Page Title
How to Manage Access to SSH Resources (Twingate + Smallstep Integration)

## Summary
Twingate integrates with Smallstep Certificate Authority to provide application-layer authentication for SSH servers, complementing Twingate's network-level access controls. This guide deploys the combination in AWS using Pulumi, with OAuth 2.0 (Google) as the identity provider for short-lived SSH certificates.

## Key Information
- Provides two-layer security: Twingate (network) + Smallstep CA (application/SSH certificate)
- Works across AWS, Azure, GCP, OracleCloud, and on-premises
- Smallstep open-source version does **not** manage user accounts on SSH hosts — must create manually
- Short-lived SSH certificates are issued via OAuth 2.0 provider
- Infrastructure-as-code via Pulumi; repo: `github.com/twingate/pulumi-twingate-smallstep`

## Prerequisites
- AWS CLI installed and configured
- Pulumi CLI installed and configured
- Twingate API token with **Read/Write and Provision** permissions
- Git
- Twingate Client installed on local machine
- OAuth 2.0 credentials (guide uses Google Cloud — create **Desktop app** credentials)
- AWS SSH Keypair (fallback access)

## Step-by-Step

1. Clone repo: `git clone https://github.com/twingate/pulumi-twingate-smallstep && cd pulumi-twingate-smallstep`
2. Create Google OAuth Desktop app credentials; note Client ID and Secret
3. Init Pulumi stack: `pulumi stack init dev`
4. Copy config: `cp ./Pulumi.example.yaml ./Pulumi.dev.yaml`
5. Set config values (see below)
6. Deploy: `pulumi up`
7. Grant user access to Connector resource in `smallstep_demo` Remote Network via Admin Console
8. Install `step` CLI on client machine
9. Log in to Twingate Client
10. Create local user on SSH host: `sudo adduser --quiet --disabled-password --gecos '' YOUR_USERNAME`
11. Bootstrap CA trust on client: `./bootstrap_user.sh`
12. Obtain SSH certificate: `step ssh login YOUR_USERNAME@YOUR_DOMAIN --provisioner "Google"`
13. Configure SSH: `step ssh config && step ssh hosts`
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
- Open-source Smallstep does **not** auto-provision user accounts — must manually `adduser` on each SSH host
- `bootstrap_user.sh` implicitly trusts the CA cert — use MDM distribution in production
- Only OAuth subjects matching `ca_oauth_allowed_domain` can connect
- Twingate must be connected before SSH attempt (network layer prerequisite)

## Related Docs
- [Smallstep Managed SSH](https://smallstep.com/ssh/) — eliminates manual user management
- Smallstep blog: *DIY Single Sign-On for SSH*
- Twingate blog: *The Many Layers of Zero Trust*
- [AWS SSH Keypair setup](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html)
- [step CLI install docs](https://smallstep.com/docs/step-cli/installation)