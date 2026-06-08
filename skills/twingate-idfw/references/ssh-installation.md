# Installing Privileged Access for SSH

## Summary
Deploy Twingate's SSH privileged access by configuring a Gateway as an SSH Certificate Authority. The recommended installation method uses the Twingate Terraform provider with cloud-specific quick-start guides. Local SSH CA is suitable for testing; HashiCorp Vault SSH secrets engine is recommended for production.

## Key Information
- Gateway acts as SSH CA, signing certificates for client access
- Two CA modes: **Local SSH CA** (Gateway holds private key) and **Vault SSH CA** (production-recommended)
- Terraform provider provides complete configs including startup scripts
- Cloud-specific guides available for AWS, DigitalOcean, and GCE

## Prerequisites
- Twingate account with administrator privileges
- An existing Remote Network configured in Twingate
- Twingate Client at minimum required version
- Terraform installed locally

## Step-by-Step

### Local SSH CA (Testing)
1. Choose cloud provider guide (AWS, DigitalOcean, or GCE)
2. Follow Terraform quick-start guide for that provider
3. Apply Terraform configuration (includes Gateway setup + SSH CA config)
4. Verify SSH Resources are accessible through the Gateway

### Vault SSH CA (Production)
1. Complete Local SSH CA setup first (or in parallel)
2. Follow the Vault integration guide to configure HashiCorp Vault SSH secrets engine
3. Configure Gateway to use Vault for certificate signing instead of local CA

## Configuration Values
- Defined per-cloud in Terraform provider examples (no universal env vars documented here)
- Full configs available in Twingate Terraform provider repository

## Gotchas
- Local SSH CA stores private key on the Gateway itself — not suitable for production (key exposure risk if Gateway is compromised)
- Minimum Client version required; verify before deployment
- Each cloud provider has its own Terraform configuration — guides are not interchangeable

## Related Docs
- [Twingate Terraform Provider](https://www.twingate.com/docs/terraform)
- Local SSH CA on AWS
- Local SSH CA on DigitalOcean
- Local SSH CA on GCE
- [Vault Integration Guide](https://www.twingate.com/docs/vault-ssh-ca)
- [Remote Development with Twingate SSH](https://www.twingate.com/docs/ssh-remote-development) (VS Code, JetBrains Gateway, Cursor)