## SSH Access Management with Smallstep CA

**Page Title:** How to Manage Access to SSH Resources (Twingate + Smallstep)

**Summary:** Integrates Twingate network-layer access control with Smallstep certificate authority for application-layer SSH authentication using short-lived OAuth2-issued certificates. Uses Pulumi to deploy the full stack on AWS (VPC, EC2, Route53). Smallstep handles SSH credential issuance; Twingate handles network visibility and least-privilege access.

**Key Information:**
- Twingate provides network-layer protection (resource invisibility, least-privilege); Smallstep adds application-layer auth via short-lived SSH certificates
- Pulumi example repo: `github.com/twingate/pulumi-twingate-smallstep`
- Infrastructure includes: public subnet (2 connector EC2s), private subnet (Smallstep CA EC2), Route53 private hosted zone
- OAuth2 provider (e.g., Google Cloud) gates certificate issuance — only users with matching domain can authenticate
- Open-source Smallstep does NOT manage OS user accounts — must create Linux users manually; managed Smallstep service handles this automatically

**Prerequisites:**
- AWS CLI configured
- Pulumi CLI configured
- Twingate API token with Read/Write + Provision permissions
- Twingate Client installed on end-user machine
- OAuth2 credentials (Google Cloud Desktop app shown)
- AWS SSH keypair (break-glass access)

**Step-by-Step:**
1. Clone `twingate/pulumi-twingate-smallstep`
2. Create OAuth2 credentials (GCP Desktop app)
3. `pulumi stack init dev`, copy `Pulumi.example.yaml` → `Pulumi.dev.yaml`
4. Set Pulumi config values (see below)
5. `pulumi up`
6. Grant user access to connector resource in Twingate Admin Console
7. Install `step` CLI on client machine
8. Log in to Twingate Client
9. Manually create OS user on SSH host via keypair SSH
10. Run `./bootstrap_user.sh` to trust CA cert on client
11. `step ssh login USER@DOMAIN --provisioner "Google"` → issues short-lived cert
12. `ssh USER@xxx.tgdemo.int` — authenticates via certificate

**Configuration Values:**

| Pulumi Config Key | Description |
|---|---|
| `ca_config.ca_oauth_client_id` | OAuth2 Client ID |
| `ca_config.ca_oauth_client_secret` | OAuth2 Client Secret (secret) |
| `ca_config.ca_oauth_allowed_domain` | Org domain for subject filtering |
| `ca_config.ca_email` | CA admin email |
| `data.key_name` | AWS SSH keypair name |
| `twingate:apiToken` | Twingate API token (secret) |
| `twingate:network` | Twingate account name |

**Gotchas:**
- Open-source Smallstep requires manual OS user creation per SSH host — production deployments should use managed Smallstep
- Bootstrap script (`bootstrap_user.sh`) implicitly trusts the CA cert — use MDM distribution in production
- Must grant Twingate access to the connector resource before SSH testing works

**Related Docs:**
- Twingate Pulumi provider
- Smallstep managed SSH service
- Twingate Identity Firewall (SSH PAM alternative for cert-free workflows)