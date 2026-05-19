# Connector Metadata

## Summary
Twingate Connectors support custom key-value metadata pairs set via environment variables prefixed with `TWINGATE_LABEL_`. Metadata appears in the Connector detail view in the Admin Console. Some labels (hostname, deployed_by) are preset automatically depending on deployment method.

## Key Information
- Metadata displays in Admin Console on the Connector detail page (left-hand side)
- Environment variable names are transformed for display: `TWINGATE_LABEL_DEV_ENVIRONMENT` → `Dev Environment: dev1`
- Twingate auto-sets `TWINGATE_LABEL_HOSTNAME` (local hostname) and `TWINGATE_LABEL_DEPLOYED_BY` on many deployment methods
- Works across all deployment types (Docker, ECS Fargate, etc.)

## Configuration Values

| Environment Variable Pattern | Example | Display Output |
|---|---|---|
| `TWINGATE_LABEL_<KEY>=<VALUE>` | `TWINGATE_LABEL_DEV_ENVIRONMENT=dev1` | `Dev Environment: dev1` |
| `TWINGATE_LABEL_HOSTNAME` | `` `hostname` `` | Auto-set by Twingate |
| `TWINGATE_LABEL_DEPLOYED_BY` | `docker` | Auto-set by Twingate |

## Docker Example
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

## ECS Fargate Example
Add to `environment` array in task definition JSON:
```json
{
  "name": "TWINGATE_LABEL_CUSTOM_METADATA_1",
  "value": "custom_value_1"
}
```

## Gotchas
- No documented limit on number of metadata pairs, but keep keys descriptive
- Underscores in the key suffix become spaces in display (e.g., `CUSTOM_METADATA` → `Custom Metadata`)
- Metadata is display-only; it has no functional effect on Connector behavior
- Must be set at deploy time via environment variables — no runtime API to update labels noted in this doc

## Related Docs
- Connector deployment methods (Docker, ECS Fargate, etc.)
- Twingate Admin Console: Connector detail view