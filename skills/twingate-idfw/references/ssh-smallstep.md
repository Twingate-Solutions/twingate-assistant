# SSH Access Management with Twingate + Smallstep CA

## Page Title
How to Manage Access to SSH Resources (Twingate + Smallstep Integration)

## Summary
Twingate integrates with Smallstep Certificate Authority to provide application-layer authentication for SSH servers, supplementing Twingate's network-level access controls. This guide uses Pulumi to deploy the full stack on AWS, combining Twingate for network access with Smallstep for short-lived SSH certificate issuance via OAuth 2.0.

## Key Information
- Provides dual-layer security: Twingate (network layer) + Smallstep CA (application layer)
- Short-lived SSH certificates issued via OAuth 2.0 (Google Cloud used in example)
- Works on any cloud/on-premises environment (AWS, Azure, GCP, OracleCloud)
- Open-source Smallstep does **not** manage user accounts on SSH hosts — manual user creation required
- Managed Smallstep SSH service available to avoid manual user management

## Prerequisites
- AWS CLI installed and configured
- Pulumi CLI installed and configured
- Twingate API token with Read/Write and Provision permissions
- Git
- Twingate Client installed on local machine
- OAuth 2.0 server access (Google Cloud Desktop app credentials in example)
- AWS SSH Keypair (emergency fallback access)

## Step-by-Step

1. Clone repo: `git clone https://github.com/twingate/pulumi-twingate-smallstep`
2. Create GCP OAuth Desktop App credentials; note Client ID and Secret
3. Initialize Pulumi stack: `pulumi stack init dev`
4. Copy example config: `cp ./Pulumi.example.yaml ./Pulumi.dev.yaml`
5. Set config values (see Configuration Values below)
6. Deploy: `pulumi up`
7. Grant user access to Connector Resource in Twingate Admin Console (`smallstep_demo` Remote Network)
8. Install `step` CLI on client machine
9. Log in to Twingate Client
10. Manually create user account on SSH host: `sudo adduser --quiet --disabled-password --gecos '' YOUR_USERNAME`
11. Bootstrap CA trust on client: `./bootstrap_user.sh`
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
- Open-source Smallstep requires **manual user account creation** on each SSH host
- `bootstrap_user.sh` implicitly trusts the CA cert — use MDM for production certificate distribution
- OAuth domain restriction (`ca_oauth_allowed_domain`) limits access to users with matching email domains
- Connector instances deploy to **public subnet**; Smallstep CA deploys to **private subnet**

## Related Docs
- [Twingate Connector best practices](https://www.twingate.com/docs)
- [Smallstep DIY Single Sign-On for SSH](https://smallstep.com/blog/diy-single-sign-on-for-ssh/)
- [Smallstep SSH managed service](https://smallstep.com/ssh/)
- Twingate blog: *The Many Layers of Zero Trust*