# Connector Metadata

## Summary
Twingate Connectors support custom key-value metadata pairs set via environment variables prefixed with `TWINGATE_LABEL_`. Metadata appears in the Connector detail view in the Admin Console. Twingate presets `hostname` and `deployed_by` labels automatically for most deployment methods.

## Key Information
- Metadata is displayed in the Admin Console on the Connector detail page (left-hand side)
- Environment variable naming: `TWINGATE_LABEL_<SUFFIX>=<value>`
- Underscores in suffix are converted to spaces with title case in UI (e.g., `DEV_ENVIRONMENT` → `Dev Environment`)
- Twingate auto-sets `TWINGATE_LABEL_HOSTNAME` and `TWINGATE_LABEL_DEPLOYED_BY` in most deployment scripts

## Configuration Values

| Environment Variable | Description | Example |
|---|---|---|
| `TWINGATE_LABEL_HOSTNAME` | Device hostname (auto-set) | `` `hostname` `` |
| `TWINGATE_LABEL_DEPLOYED_BY` | Deployment method (auto-set) | `docker`, `ecs` |
| `TWINGATE_LABEL_<CUSTOM>` | Any custom metadata | `TWINGATE_LABEL_DEV_ENVIRONMENT=dev1` |

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
- Prefix `TWINGATE_LABEL_` is required exactly — no variation supported
- Custom metadata must be added at deploy time via the deployment script; no indication of runtime updating via API
- ECS Fargate requires each label as a separate object in the `environment` array (JSON format), not simple `--env` flags

## Related Docs
- Connector deployment methods (Docker, ECS Fargate, etc.)
- Twingate Admin Console — Connector detail view