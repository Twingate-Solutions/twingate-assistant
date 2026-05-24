# Connector Metadata

## Summary
Twingate Connectors support custom key-value metadata via environment variables prefixed with `TWINGATE_LABEL_`. Metadata appears in the Connector detail view in the Admin Console. Twingate auto-populates some labels (hostname, deployed_by) depending on the deployment method.

## Key Information
- Metadata is set via environment variables with the `TWINGATE_LABEL_` prefix
- The suffix becomes the display label (underscores converted to spaces, title-cased)
- Displayed on the left-hand side of the Connector page in Admin Console
- Pre-set labels added by Twingate: `TWINGATE_LABEL_HOSTNAME`, `TWINGATE_LABEL_DEPLOYED_BY`
- Works with any deployment method that supports environment variables

## Configuration Values

| Environment Variable | Example Value | Notes |
|---|---|---|
| `TWINGATE_LABEL_HOSTNAME` | `` `hostname` `` | Auto-set; local device hostname |
| `TWINGATE_LABEL_DEPLOYED_BY` | `docker`, `ecs` | Auto-set; deployment method |
| `TWINGATE_LABEL_<CUSTOM_KEY>` | `custom_value` | User-defined; any suffix |

**Display format:** `TWINGATE_LABEL_DEV_ENVIRONMENT=dev1` → displays as `Dev Environment: dev1`

## Step-by-Step

1. Identify your deployment method (Docker, ECS Fargate, etc.)
2. Add environment variables prefixed with `TWINGATE_LABEL_` to the deployment script
3. Run the deployment command
4. Verify metadata appears in Admin Console → Connector detail view

**Docker example:**
```bash
docker run -d \
  --env TWINGATE_NETWORK="<network>" \
  --env TWINGATE_ACCESS_TOKEN="" \
  --env TWINGATE_REFRESH_TOKEN="" \
  --env TWINGATE_LABEL_HOSTNAME="`hostname`" \
  --env TWINGATE_LABEL_DEPLOYED_BY="docker" \
  --env TWINGATE_LABEL_CUSTOM_METADATA_1="custom_value_1" \
  twingate/connector:1
```

**ECS Fargate** — add to the `environment` array in the task definition JSON:
```json
{"name": "TWINGATE_LABEL_CUSTOM_METADATA_1", "value": "custom_value_1"}
```

## Gotchas
- Metadata can only be set at deploy time via environment variables; no runtime update mechanism is documented
- Label suffix format affects display name — underscores become spaces in the Admin Console
- Pre-set `TWINGATE_LABEL_HOSTNAME` and `TWINGATE_LABEL_DEPLOYED_BY` may be overwritten if you redefine them

## Related Docs
- Connector deployment methods (Docker, ECS Fargate, etc.)
- Connector configuration (`TWINGATE_NETWORK`, `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`)