## Installing Privileged Access for SSH

**URL:** https://www.twingate.com/docs/ssh-installation

### Summary
Deploys the Twingate Identity Firewall Gateway for SSH access using the Terraform provider. The provider publishes complete, runnable examples for AWS, DigitalOcean, and GCE. Production deployments should use HashiCorp Vault as the SSH CA instead of a local CA.

### Key Information
- Terraform provider is the recommended (and only documented) installation method
- Two CA modes: local SSH CA (dev/test) and HashiCorp Vault SSH secrets engine (production)
- Local CA: Gateway holds the private key and signs certificates directly
- Vault CA: Gateway delegates signing to Vault's SSH secrets engine
- After deployment, SSH Resources are accessible through the Twingate Client

### Prerequisites
- Twingate account with administrator privileges
- A Remote Network already configured
- Twingate Client at minimum version (check docs for current requirement)
- Terraform installed locally

### Step-by-Step
1. Choose deployment target: AWS, DigitalOcean, or GCE
2. Follow the corresponding Terraform quick-start guide from the provider examples
3. Each guide includes: full Terraform config, startup scripts, and deployment instructions
4. For production: configure Vault SSH secrets engine integration instead of local CA
5. After Gateway is running, configure SSH Resources and test Client connectivity
6. Optionally configure remote IDE access (VS Code, JetBrains Gateway, Cursor)

### Configuration Values
| Setting | Notes |
|---|---|
| CA mode | `local` (default for quick-start) or `vault` (production) |
| Cloud targets | AWS, DigitalOcean, GCE (separate Terraform examples per cloud) |

### Gotchas
- Local SSH CA is explicitly for testing only — do not use in production (private key on Gateway is a single point of compromise)
- No manual installation path documented — use Terraform; manual setup is unsupported
- Client version minimum must be met before SSH access works; check version requirements before deploying

### Related Docs
- Twingate Terraform provider (published examples)
- Vault integration guide (SSH secrets engine CA setup)
- Remote development with Twingate SSH (VS Code, JetBrains Gateway, Cursor IDE setup)
- Twingate Client minimum version requirements