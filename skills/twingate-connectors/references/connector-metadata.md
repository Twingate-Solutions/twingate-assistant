# Connector Metadata

## Summary
Twingate Connectors support custom key-value metadata set via environment variables prefixed with `TWINGATE_LABEL_`. Metadata appears in the Connector detail view in the Admin Console. Some labels (hostname, deployed_by) are preset automatically by Twingate deployment scripts.

## Key Information
- Metadata is set as environment variables with prefix `TWINGATE_LABEL_`
- Suffix becomes the display label (underscores converted to spaces, title-cased)
- Values display on the left-hand side of the Connector detail page
- Twingate auto-sets `TWINGATE_LABEL_HOSTNAME` and `TWINGATE_LABEL_DEPLOYED_BY` in most deployment scripts
- Works across all deployment methods (Docker, ECS Fargate, etc.)

## Configuration Values

| Environment Variable | Example Value | Notes |
|---|---|---|
| `TWINGATE_LABEL_<SUFFIX>` | `custom_value` | User-defined metadata |
| `TWINGATE_LABEL_HOSTNAME` | `` `hostname` `` | Auto-set by Twingate scripts |
| `TWINGATE_LABEL_DEPLOYED_BY` | `docker`, `ecs` | Auto-set by Twingate scripts |

## Step-by-Step

1. Identify your deployment method (Docker, ECS, systemd, etc.)
2. Add environment variables prefixed with `TWINGATE_LABEL_` to the deployment script
3. Run the deployment command
4. Verify metadata appears in Admin Console → Connector detail view

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
{"name": "TWINGATE_LABEL_CUSTOM_METADATA_1", "value": "custom_value_1"}
```

## Gotchas
- Label suffix format matters: `DEV_ENVIRONMENT` displays as `Dev Environment` — underscores become spaces
- Custom metadata added manually may be overwritten if regenerating deployment scripts from the Admin Console
- No validation on metadata values — incorrect prefixes will be silently ignored

## Related Docs
- Connector deployment methods (Docker, ECS Fargate, systemd)
- Twingate Admin Console – Connector detail view