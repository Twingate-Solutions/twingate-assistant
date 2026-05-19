# Installing Privileged Access for SSH

## Summary
Deploy Twingate's SSH Gateway using Terraform provider templates for AWS, DigitalOcean, or GCE. Supports local SSH CA (for testing) or HashiCorp Vault SSH secrets engine (for production). Terraform configs include full configuration, startup scripts, and deployment instructions.

## Key Information
- Recommended installation method: Twingate Terraform provider
- Two CA modes: local SSH CA (dev/test) or HashiCorp Vault SSH secrets engine (production)
- Local SSH CA: Gateway holds private key and signs certificates directly
- Vault mode: Gateway delegates signing to Vault's SSH secrets engine

## Prerequisites
- Twingate account with administrator privileges
- Existing Remote Network configured
- Twingate Client at minimum required version
- Terraform installed

## Deployment Options

### Local SSH CA (Quick Start)
| Cloud | Guide |
|-------|-------|
| AWS | Local SSH CA on AWS |
| DigitalOcean | Local SSH CA on DigitalOcean |
| GCE (Google Compute Engine) | Local SSH CA on GCE |

### Production (Vault as SSH CA)
- Use HashiCorp Vault SSH secrets engine for certificate signing
- See Vault integration guide for setup

## Step-by-Step (High Level)
1. Choose deployment target (AWS, DigitalOcean, or GCE)
2. Follow cloud-specific Terraform guide from Twingate provider examples
3. Apply Terraform config (includes Gateway setup + startup scripts)
4. Verify SSH Resources are accessible through Gateway
5. (Optional) Configure IDE integration for remote development

## Gotchas
- Local SSH CA stores private key on the Gateway — **not suitable for production**
- Must use Vault integration for production deployments to avoid key exposure on Gateway
- Client version must meet minimum requirements (check docs before deploying)

## Related Docs
- Twingate Terraform Provider (examples)
- Vault SSH Integration Guide
- Remote Development with Twingate SSH (VS Code, JetBrains Gateway, Cursor)
- Twingate Client minimum version requirements