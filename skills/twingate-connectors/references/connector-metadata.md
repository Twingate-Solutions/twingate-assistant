---
source: https://www.twingate.com/docs/connector-metadata
type: docs
fetched: 2026-08-14
source_version: a20e59625e267fc710984c5e4d2d56dc0fea7bab56c9a0d7e339deba36259931
---

# Connector Metadata

## Summary
Twingate Connectors support custom key-value metadata pairs set via environment variables prefixed with `TWINGATE_LABEL_`. Metadata appears in the Connector detail view in the Admin console. Some metadata (hostname, deployed_by) is preset automatically depending on deployment method.

## Key Information
- Metadata is set as environment variables with prefix `TWINGATE_LABEL_`
- Underscore-separated suffixes display as space-separated title case labels (e.g., `DEV_ENVIRONMENT` → `Dev Environment`)
- Auto-set labels: `TWINGATE_LABEL_HOSTNAME` (local hostname) and `TWINGATE_LABEL_DEPLOYED_BY` (deployment method)
- Metadata displays on the left-hand side of the Connector detail page in Admin console
- Works across all deployment methods (Docker, ECS Fargate, etc.)

## Configuration Values

| Environment Variable | Example Value | Notes |
|---|---|---|
| `TWINGATE_LABEL_HOSTNAME` | `` `hostname` `` | Auto-set; shell command for dynamic value |
| `TWINGATE_LABEL_DEPLOYED_BY` | `docker`, `ecs` | Auto-set by deployment scripts |
| `TWINGATE_LABEL_<CUSTOM_KEY>` | `custom_value` | User-defined |

## Step-by-Step

1. Identify your deployment method (Docker, ECS Fargate, Kubernetes, etc.)
2. Add environment variables prefixed `TWINGATE_LABEL_` to the deployment script/config
3. Set suffix and value to represent desired metadata
4. Run/apply the deployment command
5. Verify metadata appears in Admin console under the Connector detail view

## Examples

**Docker:**
```bash
docker run -d \
  --env TWINGATE_LABEL_HOSTNAME="`hostname`" \
  --env TWINGATE_LABEL_DEPLOYED_BY="docker" \
  --env TWINGATE_LABEL_DEV_ENVIRONMENT="dev1" \
  twingate/connector:1
```

**ECS Fargate (JSON):**
```json
{
  "name": "TWINGATE_LABEL_CUSTOM_METADATA_1",
  "value": "custom_value_1"
}
```

## Gotchas
- The `TWINGATE_LABEL_` prefix is required — variables without it are ignored as metadata
- Key suffix formatting: underscores become spaces, displayed in title case in the UI
- Dynamic values (like hostname) require shell evaluation syntax (e.g., backticks in bash); not applicable in JSON-based configs like ECS

## Related Docs
- Connector deployment methods (Docker, ECS Fargate, Kubernetes)
- Connector configuration reference
- Admin console Connector management