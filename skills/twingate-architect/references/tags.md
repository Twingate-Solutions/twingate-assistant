## Resource Tags

Key-value metadata attached to Resources for organization and filtering. Tags do not affect access control or routing; they are used for search, reporting, and operational organization.

**Key Information:**
- Each tag is a key-value pair (e.g., `environment: production`)
- Max 64 tags per Resource; one tag per key per Resource
- Both keys and values are case-sensitive UTF-8; leading/trailing whitespace is auto-stripped
- Keys cannot start with `tg` (reserved prefix); key length 1-128 chars; value length 1-256 chars
- Tags are filterable in Admin Console: Network → Resources → Tags filter (include/exclude by key-value)
- Managed via Admin Console or Twingate API; Terraform/Pulumi/K8s operator support planned

**Common Tag Keys:**
- `owner` -- team or person responsible (e.g., `devops`, `alex@autoco.example`)
- `managed_by` -- provisioning tool (e.g., `terraform`, `k8s_operator`)
- `application` -- workload name (e.g., `prometheus`, `kafka`)
- `environment` -- lifecycle stage (e.g., `production`, `staging`)
- `location` / `region` -- physical or cloud region (e.g., `us-west-2`)

**Best Practices:**
- Use consistent, standardized keys across all Resources -- avoid mixing synonyms like `owner` and `owner-team`
- Tag all Resources; partial tagging reduces filter usefulness

**Gotchas:**
- Tags are purely metadata and do not affect routing or access control
- Keys starting with `tg` are reserved and will be rejected

**Related Docs:**
- /docs/resources -- Resource configuration
- /docs/graphql-api -- Managing tags via API
