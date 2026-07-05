# Installing Privileged Access for SSH

## Summary
Deploys Twingate's SSH Gateway using Terraform provider with cloud-specific guides. Supports local SSH CA (for testing) or HashiCorp Vault SSH secrets engine (for production). Enables certificate-based SSH access through Twingate Resources.

## Key Information
- Recommended installation method: Twingate Terraform provider
- Two CA modes: local SSH CA (testing/simple) or HashiCorp Vault SSH CA (production)
- Local CA: Gateway holds private key and signs certificates directly
- Vault CA: Uses Vault's SSH secrets engine for certificate signing
- Cloud guides include full Terraform config, startup scripts, and deployment steps

## Prerequisites
- Twingate account with administrator privileges
- A configured Remote Network in Twingate
- Twingate Client at minimum required version
- Terraform installed

## Deployment Options

### Local SSH CA (Quick Start)
Available for three clouds via Terraform provider examples:
- **AWS** – Local SSH CA on AWS
- **DigitalOcean** – Local SSH CA on DigitalOcean
- **GCE** – Local SSH CA on Google Compute Engine

Each guide provides complete, runnable Terraform configuration.

### Vault as SSH CA (Production)
- Use HashiCorp Vault's SSH secrets engine instead of local CA
- Requires separate Vault integration guide setup
- Recommended for production deployments

## Step-by-Step
1. Choose deployment target (AWS, DigitalOcean, or GCE)
2. Follow cloud-specific Terraform guide from Twingate Terraform provider examples
3. Apply Terraform configuration (includes Gateway + startup scripts)
4. Verify SSH Resources are accessible through Twingate
5. (Optional) Configure IDE integration for remote development

## Gotchas
- Local SSH CA stores private key on the Gateway — not suitable for production
- Must use Vault integration for production-grade key management
- Client version must meet minimum requirements (check docs before deploying)
- Remote Network must exist before deployment

## Related Docs
- Twingate Terraform Provider (published examples)
- Vault Integration Guide (SSH secrets engine setup)
- Remote Development with Twingate SSH (VS Code, JetBrains Gateway, Cursor IDE setup)
- Twingate Client version requirements