# Installing Privileged Access for SSH

## Summary
Deploys Twingate's SSH Gateway using Terraform provider with cloud-specific guides. Supports local SSH CA (for testing) or HashiCorp Vault SSH secrets engine (for production). Enables certificate-based SSH access through Twingate Resources.

## Key Information
- Recommended installation method: Twingate Terraform provider
- Two CA modes: local SSH CA (testing) or HashiCorp Vault SSH secrets engine (production)
- Local CA: Gateway holds private key and signs certificates directly
- Cloud guides include full Terraform config, startup scripts, and deployment instructions

## Prerequisites
- Twingate account with administrator privileges
- A configured Remote Network
- Twingate Client (minimum version requirements apply)
- Terraform installed

## Deployment Options

### Local SSH CA (Quick Start)
| Cloud | Guide |
|-------|-------|
| AWS | Local SSH CA on AWS |
| DigitalOcean | Local SSH CA on DigitalOcean |
| Google Compute Engine | Local SSH CA on GCE |

### Vault SSH CA (Production)
- Use HashiCorp Vault's SSH secrets engine to sign certificates
- Gateway delegates signing to Vault instead of holding CA key locally
- See Vault integration guide for setup

## Gotchas
- Local SSH CA stores private key on the Gateway — not suitable for production
- Must use Terraform provider examples as the authoritative source; configs include startup scripts that are not documented inline
- Client version must meet minimum requirements (check compatibility before deploying)

## Next Steps
- After Gateway deployment, configure SSH Resources as accessible Twingate Resources
- For IDE integration (VS Code, JetBrains Gateway, Cursor): see "Remote development with Twingate SSH" guide

## Related Docs
- Twingate Terraform provider (example configurations)
- Vault integration guide (production CA setup)
- Remote development with Twingate SSH (IDE setup)
- Twingate Client minimum version requirements