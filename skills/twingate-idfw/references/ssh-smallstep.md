# How to Manage Access to SSH Resources (Twingate + Smallstep)

## Summary
Twingate integrates with Smallstep Certificate Authority to provide application-layer SSH authentication on top of Twingate's network-level access controls. This guide deploys the full stack on AWS using Pulumi, combining Twingate for network access with Smallstep for short-lived SSH certificate issuance via OAuth 2.0.

## Key Information
- Twingate handles **network-layer** protection; Smallstep handles **application-layer** SSH authentication
- Short-lived SSH certificates are issued via OAuth 2.0 (Google Cloud used in example)
- Open-source Smallstep does **not** manage user accounts on SSH hosts — manual user creation required
- Infrastructure includes: VPC, public/private subnets, 2 Twingate Connector EC2s, 1 Smallstep CA EC2, Route53 Private Hosted Zone

## Prerequisites
- AWS CLI installed and configured (or AWS CloudShell)
- Pulumi CLI installed and configured
- Twingate API token with **Read/Write and Provision** permissions
- Git
- Twingate Client installed
- OAuth 2.0 server access (example uses Google Cloud — create **Desktop app** credentials)
- AWS SSH Keypair (emergency fallback access)

## Step-by-Step

1. **Clone repo**: `git clone https://github.com/twingate/pulumi-twingate-smallstep && cd pulumi-twingate-smallstep`
2. **Create OAuth credentials** in GCP (Desktop app type); note Client ID and Secret
3. **Init Pulumi stack**: `pulumi stack init dev` and `cp ./Pulumi.example.yaml ./Pulumi.dev.yaml`
4. **Set config values** (see Configuration Values below)
5. **Deploy**: `pulumi up`
6. **Grant user access** in Twingate Admin Console to the connector resource in `smallstep_demo` remote network
7. **Install step CLI** on client machine
8. **Log in** to Twingate Client
9. **Create local user account** on SSH host via keypair SSH: `sudo adduser --quiet --disabled-password --gecos '' YOUR_USERNAME`
10. **Bootstrap CA trust**: run `./bootstrap_user.sh` on client machine
11. **Obtain certificate and SSH**:
    ```bash
    step ssh login YOUR_USERNAME@YOUR_DOMAIN --provisioner "Google"
    step ssh config
    step ssh hosts
    ssh YOUR_USERNAME@xxx.tgdemo.int
    ```

## Configuration Values

| Pulumi Config Key | Description |
|---|---|
| `ca_config.ca_oauth_client_id` | OAuth2 Client ID |
| `ca_config.ca_oauth_client_secret` | OAuth2 Client Secret (secret) |
| `ca_config.ca_oauth_allowed_domain` | Allowed org domain (e.g. `example.com`) |
| `twingate:apiToken` | Twingate API token (secret) |
| `twingate:network` | Twingate account name |
| `ca_config.ca_email` | Email for CA configuration |
| `data.key_name` | AWS SSH keypair name |

## Gotchas
- Open-source Smallstep requires **manual user account creation** on each SSH host — no automated user provisioning
- Root CA certificate must be distributed to clients; bootstrap script is demo-only — use MDM in production
- OAuth domain restriction limits access to users with matching email domains only
- Connector EC2s deploy to **public subnet**; Smallstep CA deploys to **private subnet**

## Related Docs
- [Smallstep SSH managed service](https://smallstep.com/ssh/) — eliminates manual user management
- [Smallstep DIY SSO for SSH blog post](https://smallstep.com/blog/diy-single-sign-on-for-ssh/)
- [Twingate Zero Trust blog post](https://www.twingate.com/blog/zero-trust)
- [step CLI installation](https://smallstep.com/docs/step-cli/installation)