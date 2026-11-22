---
source: https://www.twingate.com/docs/ssh-smallstep
type: docs
fetched: 2026-11-22
source_version: 2ed172bdd58e6acc4bc9c3fb612051860d3099be0102f889492f28b80cb59c4e
trust: official
---

# How to Manage Access to SSH Resources (Twingate + Smallstep)

## Summary
Twingate can be paired with a Certificate Authority such as Smallstep to add application-layer authentication (SSH certificates) on top of Twingate's network-level access control. The guide uses Pulumi to deploy an AWS environment (VPC, Twingate Connectors, Smallstep CA, Route53 private zone, Twingate Remote Network) and then tests SSH login with short-lived certificates issued via OAuth 2.0.

## Key Information
- Works for SSH servers, web apps, and databases (PostgreSQL, MySQL, MongoDB); the guide covers SSH only.
- Uses open source Smallstep; not limited to AWS (also Azure, GCP, OracleCloud, on-prem).
- Pulumi deploys:
  - VPC with internet gateway, public subnet, private subnet
  - 2 EC2 instances running Twingate Connectors (public subnet)
  - Smallstep CA on EC2 (private subnet)
  - Route53 Private Hosted Zone
  - Twingate Remote Network `smallstep_demo` with Resources for the Connectors and the Smallstep CA
- Example hostnames take the form `XXX.tgdemo.int`.

## Prerequisites
- AWS CLI (or AWS CloudShell) configured
- Pulumi CLI configured
- Twingate API token with Read/Write and Provision permissions
- Git
- Twingate Client installed
- OAuth 2.0 server (example uses Google Cloud)
- AWS SSH keypair for break-glass access

## Step-by-Step
1. Clone the example repo: `git clone https://github.com/twingate/pulumi-twingate-smallstep`, then `cd pulumi-twingate-smallstep`.
2. Create OAuth credentials (for GCP: Desktop app type); note the Client ID and Secret.
3. `pulumi stack init dev`, then `cp ./Pulumi.example.yaml ./Pulumi.dev.yaml`.
4. Set the config values (below), then run `pulumi up`.
5. In the Twingate Admin Console, grant your user access to the Connector Resource (`XXX.tgdemo.int`) in the `smallstep_demo` Remote Network.
6. Install the step CLI (`brew install step`, a `.deb` package on Ubuntu, or `winget install Smallstep.step` on Windows).
7. Log in to the Twingate Client.
8. SSH to the Connector host with the AWS keypair (`ssh -i ./path/to/your/keypair.pem ubuntu@XXX.tgdemo.int`) and create your user: `sudo adduser --quiet --disabled-password --gecos '' YOUR_USERNAME`.
9. On the client machine, inspect and run `./bootstrap_user.sh` to trust the CA root certificate (demo only).
10. Run `step ssh login YOUR_USERNAME@YOUR_DOMAIN --provisioner "Google"`, then `step ssh config` and `step ssh hosts`.
11. Connect with `ssh YOUR_USERNAME@xxx.tgdemo.int`.

## Configuration Values (Pulumi)
- `ca_config.ca_oauth_client_id`
- `ca_config.ca_oauth_client_secret` (use `--secret`)
- `ca_config.ca_oauth_allowed_domain`: only users in this domain can connect
- `ca_config.ca_email`
- `data.key_name`: AWS SSH keypair name
- `twingate:apiToken` (use `--secret`)
- `twingate:network`: Twingate account name

## Gotchas
- Open source Smallstep does not manage host user accounts. The local part of the email (e.g. `charles` from `charles@example.com`) must be created manually on each SSH host.
- `bootstrap_user.sh` implicitly trusts the CA; in production, distribute the root certificate via MDM or similar.
- Your user needs Twingate access to the Resource, and the Twingate Client must be running, before SSH will work.
- Certificates are short-lived, so re-run `step ssh login` when they expire.

## Related Docs
- The Many Layers of Zero Trust (https://www.twingate.com/blog/smallstep-integration)
- DIY Single Sign-On for SSH (https://smallstep.com/blog/diy-single-sign-on-for-ssh/)
- Smallstep SSH, a managed service that removes the need to run your own CA or add users manually (https://smallstep.com/solutions/smallstep-ssh/)
- step CLI installation (https://smallstep.com/docs/step-cli/installation/)