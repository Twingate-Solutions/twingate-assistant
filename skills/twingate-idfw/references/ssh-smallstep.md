# SSH Access Management with Twingate + Smallstep CA

## Page Title
How to Manage Access to SSH Resources (Twingate + Smallstep Integration)

## Summary
Combines Twingate network-layer access control with Smallstep Certificate Authority for application-layer SSH authentication. Uses short-lived OAuth2.0-backed SSH certificates alongside Twingate's network invisibility. Guide deploys full AWS infrastructure via Pulumi.

## Key Information
- Twingate handles network access; Smallstep handles SSH credential issuance via short-lived certificates
- Open-source Smallstep requires manual user account creation on SSH hosts (no user management)
- Infrastructure deployed to AWS but architecture works on any cloud/on-prem
- Pulumi automates: VPC, public/private subnets, 2 EC2 Twingate Connectors, Smallstep CA EC2, Route53 private hosted zone, Twingate Remote Network + Resources

## Prerequisites
- AWS CLI configured or CloudShell
- Pulumi CLI installed
- Twingate API token (Read/Write + Provision permissions)
- Git
- Twingate Client installed on local machine
- OAuth 2.0 server (guide uses Google Cloud — Desktop app credentials)
- AWS SSH Keypair (emergency fallback access)
- `step` CLI installed on client machine

## Step-by-Step

1. `git clone https://github.com/twingate/pulumi-twingate-smallstep && cd pulumi-twingate-smallstep`
2. Create GCP OAuth Desktop app credentials; note Client ID + Secret
3. `pulumi stack init dev`
4. `cp ./Pulumi.example.yaml ./Pulumi.dev.yaml`
5. Set config values (see Configuration Values below)
6. `pulumi up`
7. Grant user access to Connector Resource in `smallstep_demo` Remote Network via Admin Console
8. Install `step` CLI on client machine
9. Log in to Twingate Client
10. SSH into Connector host using keypair; create local user: `sudo adduser --quiet --disabled-password --gecos '' YOUR_USERNAME`
11. Run `./bootstrap_user.sh` to trust CA certificate on client
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
- Open-source Smallstep does **not** manage user accounts on SSH hosts — must manually `adduser` for each user
- `bootstrap_user.sh` implicitly trusts CA cert — use MDM or alternative distribution in production
- Only OAuth subjects matching `ca_oauth_allowed_domain` can connect
- Connector Resources must have explicit user access granted in Admin Console after `pulumi up`

## Related Docs
- [Smallstep managed SSH service](https://smallstep.com/ssh/) — eliminates manual user management
- Smallstep blog: *DIY Single Sign-On for SSH*
- Twingate blog: *The Many Layers of Zero Trust*
- [Twingate Connector best practices](https://www.twingate.com/docs)