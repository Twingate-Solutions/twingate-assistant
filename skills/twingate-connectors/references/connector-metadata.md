# Connector Metadata

## Summary
Twingate Connectors support custom key-value metadata via environment variables prefixed with `TWINGATE_LABEL_`. Metadata appears in the Connector detail view in the Admin Console. Twingate auto-sets `hostname` and `deployed_by` labels for most deployment methods.

## Key Information
- Metadata displays in Admin Console on the Connector detail page (left-hand side)
- Key format: `TWINGATE_LABEL_<SUFFIX>=<value>`
- Underscores in suffix are converted to spaces with title case display (e.g., `DEV_ENVIRONMENT` → `Dev Environment`)
- Pre-set labels by Twingate: `TWINGATE_LABEL_HOSTNAME`, `TWINGATE_LABEL_DEPLOYED_BY`

## Configuration Values

| Environment Variable | Example Value | Notes |
|---|---|---|
| `TWINGATE_LABEL_HOSTNAME` | `` `hostname` `` | Auto-set by Twingate scripts |
| `TWINGATE_LABEL_DEPLOYED_BY` | `docker`, `ecs` | Auto-set by Twingate scripts |
| `TWINGATE_LABEL_<CUSTOM>` | `custom_value` | User-defined |

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
```json
"environment": [
  {"name": "TWINGATE_LABEL_DEPLOYED_BY", "value": "ecs"},
  {"name": "TWINGATE_LABEL_CUSTOM_METADATA_1", "value": "custom_value_1"}
]
```

## Gotchas
- Metadata is set at **deploy time** via environment variables — no runtime API to update labels without redeploying
- No validation on custom suffix values; naming conflicts with Twingate's reserved labels (`HOSTNAME`, `DEPLOYED_BY`) will overwrite auto-set values
- ECS and other non-shell deployments require JSON-style env var format rather than shell `--env` flags

## Related Docs
- Connector deployment methods (Docker, ECS Fargate, others)
- Twingate Admin Console — Connector detail view