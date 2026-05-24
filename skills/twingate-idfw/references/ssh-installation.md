# Installing Privileged Access for SSH

## Summary
Deploys Twingate's SSH privileged access by setting up a Gateway that acts as an SSH certificate authority. Uses Terraform provider for deployment across cloud providers. Supports both local CA (testing) and HashiCorp Vault (production) as certificate signers.

## Key Information
- Terraform is the recommended (and primary documented) installation method
- Gateway acts as SSH CA, signing certificates for client access
- Two CA modes: local SSH CA (simple/testing) and HashiCorp Vault SSH secrets engine (production)
- Cloud-specific Terraform examples include full configs, startup scripts, and deployment steps

## Prerequisites
- Twingate account with administrator privileges
- Existing Remote Network configured in Twingate
- Twingate Client at minimum required version for SSH support
- Terraform installed locally

## Deployment Options

### Local SSH CA (Testing/Simple)
Gateway holds CA private key and signs certificates directly.

| Cloud | Guide |
|-------|-------|
| AWS | Local SSH CA on AWS |
| DigitalOcean | Local SSH CA on DigitalOcean |
| Google Compute Engine | Local SSH CA on GCE |

### Vault as SSH CA (Production)
- Gateway integrates with HashiCorp Vault's SSH secrets engine
- Vault signs certificates instead of local key on Gateway
- See Vault integration guide for setup

## Step-by-Step (General Flow)
1. Ensure prerequisites are met (admin account, Remote Network, compatible Client)
2. Install Terraform
3. Select appropriate cloud guide from Twingate Terraform provider examples
4. Apply Terraform configuration (includes Gateway deployment + SSH resource setup)
5. Run startup scripts as provided in cloud-specific guide
6. Verify SSH Resources are accessible through Twingate Client

## Gotchas
- Local SSH CA keeps private key on the Gateway — not suitable for production (key exposure risk if Gateway is compromised)
- Must use Vault SSH secrets engine for production deployments
- Twingate Client must meet **minimum version requirements** specific to SSH access — verify before deployment
- Each cloud guide is self-contained; don't mix configurations across guides

## Related Docs
- Twingate Terraform Provider (external, publishes runnable examples)
- Vault Integration Guide (HashiCorp Vault SSH CA setup)
- Remote Development with Twingate SSH (VS Code, JetBrains Gateway, Cursor IDE setup)
- Minimum Client Version Requirements for SSH