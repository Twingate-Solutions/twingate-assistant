# SSH Access Management with Twingate + Smallstep

## Page Title
How to Manage Access to SSH Resources (Twingate + Smallstep Integration)

## Summary
Twingate integrates with Smallstep Certificate Authority to provide application-layer authentication for SSH servers, layering certificate-based auth on top of Twingate's network-level access controls. This guide deploys the full stack on AWS using Pulumi, with Smallstep CA in a private subnet and Twingate Connectors in a public subnet.

## Key Information
- Provides dual-layer security: Twingate (network) + Smallstep (application/certificate)
- Uses short-lived SSH certificates issued via OAuth 2.0 (e.g., Google)
- Pulumi automates full AWS infrastructure (VPC, subnets, EC2, Route53, Twingate resources)
- Open-source Smallstep does **not** manage user accounts on SSH hosts — manual account creation required
- Smallstep managed service (`Smallstep SSH`) eliminates manual user management

## Prerequisites
- AWS CLI installed and configured (or AWS CloudShell)
- Pulumi CLI installed and configured
- Twingate API token with **Read/Write and Provision** permissions
- Git
- Twingate Client installed
- OAuth 2.0 server (guide uses Google Cloud — create **Desktop app** credentials)
- AWS SSH Keypair (fallback access)

## Step-by-Step

1. `git clone https://github.com/twingate/pulumi-twingate-smallstep && cd pulumi-twingate-smallstep`
2. Create Google OAuth Desktop app credentials; note Client ID and Secret
3. `pulumi stack init dev`
4. `cp ./Pulumi.example.yaml ./Pulumi.dev.yaml`
5. Set config values (see below)
6. `pulumi up`
7. In Twingate Admin Console, grant user access to the Connector resource in `smallstep_demo` Remote Network
8. Install `step` CLI on client machine
9. Log in to Twingate Client
10. Manually create user account on SSH host: `sudo adduser --quiet --disabled-password --gecos '' YOUR_USERNAME`
11. Run `./bootstrap_user.sh` to trust CA certificate on client
12. Authenticate and configure SSH:
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

## Gotchas
- Open-source Smallstep requires **manual user account creation** on each SSH host before certificate login works
- Bootstrap script (`bootstrap_user.sh`) implicitly trusts the CA — use MDM for production certificate distribution
- Only OAuth subjects matching `ca_oauth_allowed_domain` can connect
- Twingate must be connected before SSH attempts; Connectors are in the public subnet, CA in private

## Related Docs
- [Twingate Connector best practices](https://www.twingate.com/docs)
- [Smallstep SSH (managed)](https://smallstep.com/ssh/)
- [Smallstep DIY SSO for SSH blog post](https://smallstep.com/blog/diy-single-sign-on-for-ssh/)
- [Twingate Zero Trust blog post](https://www.twingate.com/blog)