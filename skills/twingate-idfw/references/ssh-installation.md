---
source: https://www.twingate.com/docs/ssh-installation
type: docs
fetched: 2026-08-14
source_version: 415e1171eeec42d644722062f43de46a5aff1a7b72dfc16730965b2a6ef5ea1c
---

# Installing Privileged Access for SSH

## Summary
Deploys Twingate's SSH Gateway using Terraform provider with cloud-specific guides. Supports local SSH CA (dev/test) or HashiCorp Vault SSH secrets engine (production). Enables certificate-based SSH access through Twingate Resources.

## Key Information
- Recommended installation method is via Twingate Terraform provider
- Two CA modes: local SSH CA (simple, Gateway holds private key) or Vault SSH secrets engine (production)
- Cloud guides include full Terraform config, startup scripts, and deployment steps
- After setup, supports remote IDE development (VS Code, JetBrains Gateway, Cursor)

## Prerequisites
- Twingate account with administrator privileges
- An existing Remote Network configured in Twingate
- Twingate Client at minimum required version
- Terraform installed locally

## Step-by-Step

### Local SSH CA Deployment
1. Choose cloud provider guide (AWS, DigitalOcean, or GCE)
2. Follow Terraform provider example for target cloud
3. Apply Terraform config (includes Gateway + SSH CA setup)
4. Configure SSH Resources in Twingate pointing to target hosts
5. Connect via Twingate Client

### Production (Vault CA) Deployment
1. Complete local CA setup as baseline
2. Follow Vault integration guide to configure Vault SSH secrets engine
3. Reconfigure Gateway to use Vault for certificate signing instead of local CA key

## Configuration Values
| Option | Details |
|--------|---------|
| CA Mode | `local` (Gateway signs certs) or `vault` (HashiCorp Vault signs certs) |
| Cloud Targets | AWS, DigitalOcean, Google Compute Engine |
| Terraform Provider | Twingate official Terraform provider |

## Gotchas
- Local SSH CA stores private key on the Gateway — not suitable for production; use Vault instead
- Twingate Client must meet minimum version requirements before SSH access works
- Remote Network must exist before deploying the Gateway via Terraform

## Related Docs
- [Twingate Terraform Provider](https://www.twingate.com/docs/terraform) — provider reference
- Local SSH CA on AWS — Terraform example
- Local SSH CA on DigitalOcean — Terraform example  
- Local SSH CA on GCE — Terraform example
- Vault Integration Guide — production CA setup
- [Remote Development with Twingate SSH](https://www.twingate.com/docs/ssh-remote-development) — IDE configuration (VS Code, JetBrains Gateway, Cursor)