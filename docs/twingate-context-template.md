# Twingate Context

<!-- Maintained by twingate-se. Commit this file to your repo. Read by Twingate skills
     to orient without re-asking. Update after any topology change. -->

> **Last updated:** {YYYY-MM-DD}

## Deployment

| Setting | Value |
|---|---|
| Tenant subdomain | {name} (access at {name}.twingate.com) |
| IaC tooling | Terraform / Pulumi / Kubernetes operator / manual |
| IaC root path | {path in repo, e.g., `infra/twingate/`} |
| Identity provider | {Okta / Entra ID / Google Workspace / other} |
| SCIM provisioning | Configured / Not configured |
| Terraform provider version | {e.g., `~> 3.0`} |

## Remote Networks

| Name | Terraform Resource | Cloud | Location | Environments Covered |
|---|---|---|---|---|
| {e.g., prod-us-east} | `twingate_remote_network.prod_us_east` | AWS | us-east-1 | production |

## Connectors

| Name | Terraform Resource | Remote Network | Platform | HA Status |
|---|---|---|---|---|
| {e.g., prod-connector-1} | `twingate_connector.prod_1` | prod-us-east | ECS Fargate | 2 instances, 2 AZs |

## Resources

| Name | Terraform Resource | Type | Address | Remote Network | Access Groups |
|---|---|---|---|---|---|
| {e.g., prod-db} | `twingate_resource.prod_db` | FQDN | db.internal.corp | prod-us-east | engineering |

## Groups

| Name | Terraform Resource | IdP Source | SCIM Status | Resources |
|---|---|---|---|---|
| {e.g., engineering} | `twingate_group.engineering` | Okta | Synced | prod-db, staging-api |

## IdP Group Mapping

| IdP Group | Twingate Group | SCIM Managed | Notes |
|---|---|---|---|
| {e.g., eng-all@corp.com} | engineering | Yes | |

## IaC Structure

{Brief description of how Twingate resources are organized in the repo. Example:}

infra/twingate/
  networks.tf       — twingate_remote_network + twingate_connector resources
  resources.tf      — twingate_resource definitions
  groups.tf         — twingate_group + twingate_resource_access
  variables.tf      — tenant name, API token reference
  outputs.tf        — connector tokens (sensitive)

Provider block in: infra/providers.tf
State backend: {S3 / Terraform Cloud / local}

## Security Policies

| Policy Name | Terraform Resource | Groups | Session Duration | MFA | Device Trust |
|---|---|---|---|---|---|
| {e.g., employees-standard} | `twingate_security_policy.standard` | engineering, ops | 8h | Required | Recommended |

## Open Items

- [ ] {e.g., SCIM not yet configured — manual group management in place}
- [ ] {e.g., Connector upgrade to v3 pending}

## Change Log

- {YYYY-MM-DD}: {What changed and why}
