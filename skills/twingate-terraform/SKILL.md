---
name: twingate-terraform
description: |
  Twingate Terraform provider usage, module patterns, and infrastructure as code.
  Use this skill whenever the user mentions Terraform, .tf files, infrastructure
  as code with Twingate, the Twingate Terraform provider, or wants to automate
  Twingate deployment with IaC. Also trigger when the user has existing Terraform
  code and wants to add Twingate.
---

# Twingate Terraform

## When to Use This Skill

Trigger this skill when the user:

- Mentions Terraform, `.tf` files, or infrastructure as code in the context of Twingate
- Wants to create, modify, or debug Twingate Terraform configuration
- Asks how to use the Twingate Terraform provider or what resources it supports
- Has existing Terraform code (AWS, Azure, GCP, Kubernetes) and wants to integrate Twingate
- Wants to automate Remote Network, Connector, or Resource provisioning
- Asks about the Twingate provider version, authentication, or configuration
- Needs Terraform module patterns for multi-environment or multi-cloud Twingate deployments
- Is troubleshooting a Terraform apply error involving Twingate resources
- Wants to generate service accounts or connector tokens for automation

## Quick Reference

| Resource / Data Source | Purpose |
|---|---|
| `twingate_remote_network` (resource) | Create a logical network boundary (VPC, DC, branch) |
| `twingate_connector` (resource) | Register a connector record; outputs connector ID |
| `twingate_connector_tokens` (resource) | Generate access + refresh token pair for a connector |
| `twingate_resource` (resource) | Define an access resource (FQDN, CIDR, wildcard) |
| `twingate_group` (resource) | Create a group; groups are the access control unit |
| `twingate_service_account` (resource) | Create a non-human service principal |
| `twingate_service_account_key` (resource) | Generate an API key for a service account |
| `twingate_gateway_config` (resource) | Generate Identity Firewall gateway config YAML locally |
| `twingate_remote_network` (data) | Look up an existing remote network by name |
| `twingate_group` (data) | Look up an existing group by name |
| `twingate_security_policy` (data) | Look up a security policy by name |
| `twingate_user` (data) | Look up a user by email |
| `twingate_connector` (data) | Look up a connector by name |
| `twingate_resources` (data) | List or filter existing resources |

**Provider source:** `Twingate/twingate` (Terraform registry)
**Minimum version:** `>= 3.0` — always pin
**Auth env var:** `TWINGATE_API_TOKEN` (Read + Write + Provision permissions required)

## Evergreen Knowledge

### Provider Configuration

The Twingate provider requires two inputs: the API token and the network name (your tenant slug, e.g., `acme` for `acme.twingate.com`).

Always set the API token via the `TWINGATE_API_TOKEN` environment variable. Never hardcode it in `.tf` files or pass it through a Terraform variable without marking that variable `sensitive = true`. The network name is not a secret and can appear in configuration directly.

Pin the provider version to `>= 3.0`. Versions before 3.0 have breaking schema differences and lack built-in retry logic for rate limiting.

```hcl
terraform {
  required_providers {
    twingate = {
      source  = "Twingate/twingate"
      version = ">= 3.0"
    }
  }
}

provider "twingate" {
  # api_token is read from TWINGATE_API_TOKEN env var — do not hardcode here
  network = "acme"   # your tenant slug (acme.twingate.com)
}
```

To generate the API token: Twingate admin console → Settings → API → Create Token. Grant the token Read, Write, and Provision permissions. Store it in a secret manager (AWS Secrets Manager, Azure Key Vault, HashiCorp Vault) and inject it into the environment at plan/apply time. Never commit it to version control.

### Key Resources

**`twingate_remote_network`**
Represents a logical network boundary — a VPC, data center, branch office, or any environment where Connectors run. Map one Remote Network to one real trust boundary. Connectors and Resources are both associated with a Remote Network.

**`twingate_connector`**
Creates the connector record in the Twingate control plane. This resource only creates the record — it does not deploy the connector software. The `id` output is required by `twingate_connector_tokens`. Pass the connector ID to your compute resource (EC2 user_data, Helm values, etc.) to deploy and register the actual software.

**`twingate_connector_tokens`**
Generates the `access_token` and `refresh_token` pair that the connector software uses to authenticate to the Twingate control plane. These are sensitive credentials. Always mark any Terraform output that exposes them as `sensitive = true`. The tokens cannot be retrieved after creation — if lost, destroy and re-create this resource to generate a new pair.

**`twingate_resource`**
Defines an access resource. Set `address` to an FQDN, CIDR block, or wildcard DNS pattern. Use the `protocols` block to restrict access to specific protocols and port ranges. Use the `access` block to attach groups. A resource with no group assignment is unreachable by anyone — always assign at least one group.

**`twingate_group`**
Groups are the primary access control unit. Resources are assigned to groups; users and service accounts are members of groups. Create groups in Terraform when you want group lifecycle managed as code. Use the data source (`data "twingate_group"`) when the group is managed outside Terraform (e.g., via SCIM from your IdP) and you only need a reference.

**`twingate_service_account`**
A non-human principal for headless or CI/CD access. Service accounts are members of groups, just like users. Use them for any automated process that needs to access Twingate Resources.

**`twingate_service_account_key`**
Generates an API key for a service account. Sensitive — treat like `twingate_connector_tokens`. Mark outputs sensitive. Rotate by destroying and re-creating the resource.

**`twingate_gateway_config`**
Generates the gateway configuration YAML for the Identity Firewall (SSH PAM, Kubernetes gateway) locally, without an API round-trip. The `ssh.resources[].username` field is configured here, not in the GraphQL API or any other resource. Only use this resource when implementing Identity Firewall. Do not use it for standard connector deployments — it produces YAML configuration only, not a connector.

### Key Data Sources

Use data sources to reference Twingate objects that exist but are managed outside the current Terraform workspace — for example, groups provisioned by SCIM, security policies created in the console, or remote networks managed by a different module.

```hcl
data "twingate_group" "engineering" {
  name = "Engineering"
}

data "twingate_security_policy" "strict" {
  name = "Strict"
}

data "twingate_remote_network" "production" {
  name = "Production VPC"
}
```

### Typical Deployment Sequence

Follow this sequence for a clean, dependency-correct deployment. Terraform resolves `depends_on` automatically for resource references, but explicit `depends_on` is required when the dependency is passed through an external resource (e.g., passing a token to an EC2 `user_data` template).

1. Configure the provider with `TWINGATE_API_TOKEN` and `network`
2. Create `twingate_remote_network` — establishes the network boundary
3. Create `twingate_connector` — references the remote network by ID
4. Create `twingate_connector_tokens` — references the connector by ID; mark all outputs sensitive
5. Pass tokens to your compute resource (EC2 `user_data`, Helm `values`, systemd unit, etc.) to deploy the connector software; add `depends_on = [twingate_connector_tokens.this]` to the compute resource
6. Create `twingate_resource` records for each service to protect
7. Create or reference `twingate_group` records
8. Assign groups to resources via the `access` block on `twingate_resource`

### Rate Limiting

If `terraform apply` produces 429 errors against the Twingate API, upgrade the provider to the latest `>= 3.0` release. Recent versions include built-in exponential backoff and retry logic for 429 and 5xx responses. Older provider versions surface 429 errors directly without retry.

For large deployments (many resources created in a single apply), use `-parallelism=5` or lower to reduce concurrent API calls:

```bash
terraform apply -parallelism=5
```

### Runtime Schema Inspection

The Twingate provider evolves frequently. When generating or debugging Twingate Terraform code, clone the official provider repository and inspect the schema source for current resource attributes and accepted values:

```bash
git clone https://github.com/Twingate/terraform-provider-twingate
# Resource schemas are in internal/provider/
# Example: internal/provider/resource_resource.go for twingate_resource attributes
```

Also check the Terraform registry for the latest published provider version and its full attribute documentation:
`https://registry.terraform.io/providers/Twingate/twingate/latest/docs`

Reference modules and deployment examples are available at:
`https://github.com/Twingate-Solutions/terraform-scripts`

## Common Patterns

### Pattern 1: Provider Configuration

Minimal working provider configuration using environment variable authentication.

```hcl
terraform {
  required_providers {
    twingate = {
      source  = "Twingate/twingate"
      version = ">= 3.0"
    }
  }
  required_version = ">= 1.5"
}

provider "twingate" {
  # Set TWINGATE_API_TOKEN in the environment before running plan/apply.
  # Token must have Read, Write, and Provision permissions.
  network = var.twingate_network
}

variable "twingate_network" {
  description = "Twingate tenant slug (e.g. 'acme' for acme.twingate.com)"
  type        = string
}
```

### Pattern 2: Remote Network + Connector + Tokens

The foundational trio for any Twingate deployment. Always create all three together — a connector without tokens cannot authenticate, and tokens without a connector have nothing to attach to.

```hcl
resource "twingate_remote_network" "production_vpc" {
  name = "Production VPC"
}

resource "twingate_connector" "primary" {
  remote_network_id = twingate_remote_network.production_vpc.id
  name              = "prod-connector-1"
}

resource "twingate_connector" "secondary" {
  remote_network_id = twingate_remote_network.production_vpc.id
  name              = "prod-connector-2"
}

resource "twingate_connector_tokens" "primary" {
  connector_id = twingate_connector.primary.id
}

resource "twingate_connector_tokens" "secondary" {
  connector_id = twingate_connector.secondary.id
}

# Mark token outputs sensitive — never expose them in plan output
output "connector_primary_access_token" {
  value     = twingate_connector_tokens.primary.access_token
  sensitive = true
}

output "connector_primary_refresh_token" {
  value     = twingate_connector_tokens.primary.refresh_token
  sensitive = true
}
```

Deploy two connectors per Remote Network. Twingate Clients automatically load-balance and fail over between them.

### Pattern 3: Resource with Protocol Restrictions

Define a Twingate Resource with explicit protocol and port constraints. The `protocols` block restricts which transport protocols and port ranges are accessible through this resource.

```hcl
resource "twingate_resource" "postgres" {
  name              = "postgres-prod"
  address           = "postgres.internal.corp"
  remote_network_id = twingate_remote_network.production_vpc.id

  protocols {
    allow_icmp = false

    tcp {
      policy = "RESTRICTED"
      ports  = ["5432"]
    }

    udp {
      policy = "DENY_ALL"
    }
  }

  access {
    group_ids = [twingate_group.data_team.id]
  }
}

resource "twingate_resource" "internal_app" {
  name              = "internal-app"
  address           = "app.internal.corp"
  remote_network_id = twingate_remote_network.production_vpc.id

  protocols {
    allow_icmp = false

    tcp {
      policy = "RESTRICTED"
      ports  = ["80", "443", "8080-8090"]
    }

    udp {
      policy = "DENY_ALL"
    }
  }

  access {
    group_ids = [twingate_group.engineering.id]
  }
}
```

Use `"ALLOW_ALL"` for `policy` when you want to permit all ports on a protocol. Use `"DENY_ALL"` to block a protocol entirely. Use `"RESTRICTED"` with a `ports` list to allow only specific ports or ranges.

### Pattern 4: Group-Based Access

Attach groups to resources. Groups are the access control unit — resources without a group assignment are unreachable by anyone.

```hcl
resource "twingate_group" "engineering" {
  name = "Engineering"
}

resource "twingate_group" "data_team" {
  name = "Data Team"
}

resource "twingate_resource" "gitlab" {
  name              = "gitlab"
  address           = "gitlab.internal.corp"
  remote_network_id = twingate_remote_network.production_vpc.id

  protocols {
    allow_icmp = false
    tcp {
      policy = "RESTRICTED"
      ports  = ["22", "80", "443"]
    }
    udp {
      policy = "DENY_ALL"
    }
  }

  access {
    group_ids = [
      twingate_group.engineering.id,
    ]
  }
}

# Reference an SCIM-provisioned group without managing it in Terraform
data "twingate_group" "admins" {
  name = "Admins"
}

resource "twingate_resource" "admin_console" {
  name              = "admin-console"
  address           = "admin.internal.corp"
  remote_network_id = twingate_remote_network.production_vpc.id

  protocols {
    allow_icmp = false
    tcp {
      policy = "RESTRICTED"
      ports  = ["443"]
    }
    udp {
      policy = "DENY_ALL"
    }
  }

  access {
    group_ids = [data.twingate_group.admins.id]
  }
}
```

Use `resource "twingate_group"` when the group lifecycle belongs to Terraform. Use `data "twingate_group"` when the group is managed by your IdP via SCIM — do not create a duplicate group resource, which would create a second group in Twingate.

### Pattern 5: Service Account for CI Pipelines

Create a service account with an API key for a CI/CD pipeline or automated process that needs to access Twingate Resources headlessly.

```hcl
resource "twingate_service_account" "ci_pipeline" {
  name = "ci-pipeline"
}

resource "twingate_service_account_key" "ci_pipeline" {
  name               = "ci-pipeline-key"
  service_account_id = twingate_service_account.ci_pipeline.id
}

# Grant the service account access to the resources it needs
# by adding it to a group that has those resources assigned
resource "twingate_group" "ci_access" {
  name = "CI Pipeline Access"
}

resource "twingate_resource" "build_cache" {
  name              = "build-cache"
  address           = "cache.internal.corp"
  remote_network_id = twingate_remote_network.production_vpc.id

  protocols {
    allow_icmp = false
    tcp {
      policy = "RESTRICTED"
      ports  = ["6379"]
    }
    udp {
      policy = "DENY_ALL"
    }
  }

  access {
    group_ids          = [twingate_group.ci_access.id]
    service_account_ids = [twingate_service_account.ci_pipeline.id]
  }
}

output "ci_pipeline_service_key" {
  value     = twingate_service_account_key.ci_pipeline.token
  sensitive = true
}
```

The `service_account_ids` field in the `access` block (supported in provider >= 3.0) grants direct resource access to the service account without requiring group membership. Use group membership for access that aligns with an organizational role; use direct assignment for machine-only resources.

## Anti-Patterns

**Hardcoding `api_token` in `.tf` files**
Never place the API token value directly in a `provider "twingate"` block or a Terraform variable default. Set `TWINGATE_API_TOKEN` in the environment, inject it from a secret manager at runtime, or use a Terraform variable with `sensitive = true` sourced from a secrets backend. Committing a token to version control — even a private repository — is a credential exposure incident.

**Not marking connector token outputs sensitive**
`twingate_connector_tokens.access_token` and `twingate_connector_tokens.refresh_token` are credentials. If you expose them as Terraform outputs without `sensitive = true`, Terraform will print them in plaintext during `apply` and store them unredacted in plan files. Always mark these outputs sensitive, and restrict access to your Terraform state backend.

**Creating resources without assigning a group**
A `twingate_resource` with no `access` block (or an empty `group_ids` list) is valid Terraform but unreachable by anyone. Twingate does not grant implicit access — every resource must have at least one group or service account in its access block before any user or service can connect to it. Always include the `access` block.

**Using `twingate_gateway_config` for standard connector deployments**
`twingate_gateway_config` generates the configuration YAML for the Identity Firewall gateway (SSH PAM, Kubernetes gateway). It makes no API call and does not register or deploy a connector. Do not use it in a standard Twingate deployment expecting it to create or configure a connector. Use `twingate_connector` and `twingate_connector_tokens` for that purpose.

**Forgetting `depends_on` between tokens and the compute resource**
Terraform tracks resource dependencies automatically when you reference resource attributes. However, if you pass connector tokens to an EC2 `user_data` template or similar mechanism via a `templatefile()` call or local value, Terraform may not infer the dependency correctly and may attempt to create the compute resource before the tokens exist. Add an explicit `depends_on = [twingate_connector_tokens.this]` to the compute resource block to guarantee ordering.

**Using SCIM-provisioned group names as `resource "twingate_group"` resources**
If your IdP provisions groups into Twingate via SCIM, do not also create those groups with `resource "twingate_group"`. This creates duplicate groups with identical names, which causes confusion in access policy and breaks SCIM reconciliation. Use `data "twingate_group"` to reference SCIM-provisioned groups in Terraform without managing their lifecycle.

**Pinning to a pre-3.0 provider version**
Provider versions below 3.0 have schema breaking changes relative to current documentation, lack built-in 429/5xx retry logic, and are missing resources introduced in later versions (including improved `service_account_ids` support in the `access` block). Always require `>= 3.0`. Prefer pinning to the latest published minor version and updating deliberately.

## Current Documentation

Reference files in `./references/` are auto-generated by the update pipeline and contain summaries of current Twingate documentation. Read them for up-to-date attribute names, provider changelog notes, and registry examples.

If a reference file is missing or appears outdated, fetch canonical sources directly:

```bash
# Terraform registry provider docs
curl -s https://registry.terraform.io/providers/Twingate/twingate/latest/docs

# Official provider source for full resource schemas
git clone https://github.com/Twingate/terraform-provider-twingate
# Inspect internal/provider/ for current resource schema definitions

# Reference modules and deployment examples
git clone https://github.com/Twingate-Solutions/terraform-scripts
```

Key Twingate doc slugs relevant to this skill:
- `automated-deployment` — IaC and scripted deployment overview
- `terraform` — Terraform provider quick start
- `quick-start` — manual deployment steps (useful for understanding the model before translating to Terraform)

## Related Skills

- **twingate-architect** — architecture background; understand Remote Networks, Resources, and Groups before writing Terraform for them
- **twingate-connectors** — connector deployment detail across platforms (Docker, Linux service, cloud marketplace); use alongside this skill when passing connector tokens to a compute resource
- **twingate-idfw** — Identity Firewall implementation; the `twingate_gateway_config` resource is only relevant in this context
- **twingate-kubernetes** — Helm-based connector deployment; use when passing connector tokens to a Helm release via Terraform's `helm_release` resource
- **twingate-api** — GraphQL API for data sources and automation; useful when Terraform data sources don't expose the field needed and a direct API call is required
