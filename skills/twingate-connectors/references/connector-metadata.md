# Connector Metadata

## Summary
Twingate Connectors support custom key-value metadata added as environment variables at deploy time. Metadata appears in the Connector detail view in the Admin Console. Twingate auto-sets some metadata (hostname, deployed_by) depending on deployment method.

## Key Information
- Metadata is set via environment variables prefixed with `TWINGATE_LABEL_`
- Key format: `TWINGATE_LABEL_<SUFFIX>=<value>` → displays as `Suffix: value` in Admin Console
- Underscore in suffix converts to space in display (e.g., `DEV_ENVIRONMENT` → `Dev Environment`)
- Displayed on left-hand side of Connector detail page
- Works across all deployment methods (Docker, ECS Fargate, etc.)

## Prerequisites
- An existing Connector deployment script or configuration
- Access to Twingate Admin Console

## Configuration Values

| Environment Variable | Description | Example |
|---|---|---|
| `TWINGATE_LABEL_HOSTNAME` | Auto-set: device hostname | `` `hostname` `` |
| `TWINGATE_LABEL_DEPLOYED_BY` | Auto-set: deployment method | `docker`, `ecs` |
| `TWINGATE_LABEL_<CUSTOM>` | User-defined metadata | `TWINGATE_LABEL_ENV=prod` |

## Step-by-Step

**Docker:**
```bash
docker run -d \
  --env TWINGATE_NETWORK="<network>" \
  --env TWINGATE_ACCESS_TOKEN="" \
  --env TWINGATE_REFRESH_TOKEN="" \
  --env TWINGATE_LABEL_HOSTNAME="`hostname`" \
  --env TWINGATE_LABEL_DEPLOYED_BY="docker" \
  --env TWINGATE_LABEL_CUSTOM_KEY="custom_value" \
  twingate/connector:1
```

**ECS Fargate** — add to `environment` array in task definition JSON:
```json
{
  "name": "TWINGATE_LABEL_CUSTOM_KEY",
  "value": "custom_value"
}
```

## Gotchas
- Metadata is set at **deploy time only** — changing it requires redeployment with updated env vars
- Prefix `TWINGATE_LABEL_` is required; variables without this prefix are ignored as metadata
- Auto-populated fields (`hostname`, `deployed_by`) vary by deployment method — not all methods set both

## Related Docs
- Connector deployment methods (Docker, ECS Fargate, etc.)
- Connector detail view in Admin Console