# SSH Access Management with Twingate + Smallstep

## Page Title
How to Manage Access to SSH Resources (Twingate + Smallstep Integration)

## Summary
Twingate integrates with Smallstep Certificate Authority to provide application-layer authentication for SSH servers, augmenting Twingate's network-level protections. This guide deploys the combination in AWS using Pulumi, with Smallstep issuing short-lived SSH certificates via OAuth 2.0. The result is zero-trust SSH access: Twingate controls network visibility, Smallstep controls identity verification.

## Key Information
- Twingate handles network-layer access (resource invisibility, least privilege)
- Smallstep handles application-layer authentication (short-lived SSH certificates via OAuth2)
- Infrastructure-as-code via Pulumi; not AWS-specific (works on Azure, GCP, OracleCloud, on-prem)
- Open-source Smallstep does **not** manage user accounts on SSH hosts — manual account creation required
- Smallstep managed service (`Smallstep SSH`) eliminates manual user management

## Prerequisites
- AWS CLI installed and configured (or AWS CloudShell)
- Pulumi CLI installed and configured
- Twingate API token with **Read/Write and Provision** permissions
- Git
- Twingate Client installed on local machine
- OAuth 2.0 server access (guide uses Google Cloud — Desktop app credentials)
- AWS SSH Keypair (fallback access)

## Step-by-Step

1. Clone repo: `git clone https://github.com/twingate/pulumi-twingate-smallstep`
2. Create OAuth credentials (GCP: Desktop app type); note Client ID and Secret
3. Init Pulumi stack: `pulumi stack init dev`
4. Copy config: `cp ./Pulumi.example.yaml ./Pulumi.dev.yaml`
5. Set configuration values (see below)
6. Deploy: `pulumi up`
7. Grant user access to Connector Resource in `smallstep_demo` Remote Network via Twingate Admin Console
8. Install `step` CLI on client machine
9. Log in to Twingate Client
10. Manually create SSH user on host: `sudo adduser --quiet --disabled-password --gecos '' YOUR_USERNAME`
11. Bootstrap CA trust on client: `./bootstrap_user.sh`
12. Obtain certificate and connect:
    ```bash
    step ssh login YOUR_USERNAME@YOUR_DOMAIN --provisioner "Google"
    step ssh config
    step ssh hosts
    ssh YOUR_USERNAME@xxx.tgdemo.int
    ```

## Configuration Values

| Config Key | Description |
|---|---|
| `ca_config.ca_oauth_client_id` | OAuth2 Client ID |
| `ca_config.ca_oauth_client_secret` | OAuth2 Client Secret (secret) |
| `ca_config.ca_oauth_allowed_domain` | Allowed OAuth domain (org domain) |
| `twingate:apiToken` | Twingate API token (secret) |
| `twingate:network` | Twingate account name |
| `ca_config.ca_email` | Email for Certificate Authority |
| `data.key_name` | AWS SSH keypair name |

## Gotchas
- Open-source Smallstep requires **manual user account creation** on each SSH host — no automated user provisioning
- Root CA certificate must be distributed to clients; `bootstrap_user.sh` is demo-only — use MDM in production
- Must grant explicit user access in Twingate Admin Console after `pulumi up` completes

## Related Docs
- [Twingate Blog: The Many Layers of Zero Trust](https://www.twingate.com/blog)
- [Smallstep Blog: DIY Single Sign-On for SSH](https://smallstep.com/blog)
- [Smallstep SSH managed service](https://smallstep.com/ssh/)
- Twingate Connector deployment best practices