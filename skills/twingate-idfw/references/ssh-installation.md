# Installing Privileged Access for SSH

## Summary
Deploy Twingate's SSH Gateway using the Terraform provider across AWS, DigitalOcean, or GCE. The Gateway acts as an SSH certificate authority (CA), signing certificates for access control. Production deployments should use HashiCorp Vault as the CA instead of a local CA.

## Key Information
- Primary deployment method is Twingate Terraform provider with cloud-specific example configurations
- Two CA modes: **Local SSH CA** (Gateway holds private key, signs directly) and **Vault SSH CA** (production-recommended)
- Terraform guides include full configuration, startup scripts, and deployment instructions
- After deployment, supports remote IDE development via VS Code, JetBrains Gateway, and Cursor

## Prerequisites
- Twingate account with administrator privileges
- A configured Remote Network in Twingate
- Twingate Client at minimum required version
- Terraform installed

## Deployment Options

### Local SSH CA (Quick-Start)
| Cloud | Guide |
|-------|-------|
| AWS | Local SSH CA on AWS |
| DigitalOcean | Local SSH CA on DigitalOcean |
| Google Compute Engine | Local SSH CA on GCE |

### Vault SSH CA (Production)
- Use HashiCorp Vault's SSH secrets engine for certificate signing
- Requires separate Vault integration setup

## Step-by-Step (General Flow)
1. Ensure prerequisites are met (admin account, Remote Network, Terraform)
2. Select cloud provider and follow corresponding Terraform guide
3. Apply Terraform configuration (includes Gateway setup + startup scripts)
4. Configure SSH Resources accessible through the Gateway
5. Optionally configure IDE integration for remote development

## Gotchas
- Local SSH CA stores the private key on the Gateway itself — not suitable for production use
- Vault CA integration requires additional setup steps documented separately
- Twingate Client must meet **minimum version requirements** (check docs for specific version)

## Related Docs
- Twingate Terraform Provider
- Vault Integration Guide (SSH CA)
- Remote Development with Twingate SSH (VS Code, JetBrains, Cursor)
- Twingate Client minimum version requirements