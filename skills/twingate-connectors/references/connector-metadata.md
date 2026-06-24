# Connector Metadata

## Summary
Twingate Connectors support custom key-value metadata pairs set via environment variables prefixed with `TWINGATE_LABEL_`. Metadata appears in the Connector detail view in the Admin Console. Some labels (hostname, deployed_by) are preset automatically by Twingate deployment scripts.

## Key Information
- Metadata displays in Admin Console on the Connector detail page (left-hand side)
- Environment variable names are transformed for display: `TWINGATE_LABEL_DEV_ENVIRONMENT` → `Dev Environment: dev1`
- Works with any deployment method that supports environment variables
- Twingate auto-sets `TWINGATE_LABEL_HOSTNAME` and `TWINGATE_LABEL_DEPLOYED_BY` in many deployment scripts

## Configuration Values

| Environment Variable | Format | Example |
|---|---|---|
| `TWINGATE_LABEL_<SUFFIX>` | `TWINGATE_LABEL_` + custom key | `TWINGATE_LABEL_DEV_ENVIRONMENT=dev1` |
| `TWINGATE_LABEL_HOSTNAME` | Auto-set | `` `hostname` `` |
| `TWINGATE_LABEL_DEPLOYED_BY` | Auto-set | `docker`, `ecs` |

## Step-by-Step

1. Identify deployment method (Docker, ECS Fargate, etc.)
2. Add environment variables prefixed with `TWINGATE_LABEL_` to deployment script
3. Run/deploy the Connector
4. Verify metadata appears in Admin Console → Connector detail view

## Examples

**Docker:**
```bash
docker run -d \
  --env TWINGATE_LABEL_CUSTOM_METADATA_1="custom_value_1" \
  --env TWINGATE_LABEL_CUSTOM_METADATA_2="custom_value_2" \
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
- Variable suffix becomes the display label (underscores → spaces, title-cased)
- Must add metadata at deploy time via environment variables — no runtime injection method documented
- Preset labels (`HOSTNAME`, `DEPLOYED_BY`) may be overwritten if you redefine them manually

## Related Docs
- Connector deployment methods (Docker, ECS Fargate, etc.)
- Twingate Admin Console Connector management