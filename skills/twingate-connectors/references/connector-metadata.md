# Connector Metadata

## Summary
Twingate Connectors support custom key-value metadata pairs set via environment variables prefixed with `TWINGATE_LABEL_`. Metadata appears in the Connector detail view in the Admin Console. Some metadata (hostname, deployed_by) is preset automatically by Twingate deployment scripts.

## Key Information
- Metadata is set as environment variables with prefix `TWINGATE_LABEL_` + custom suffix
- Displayed in Admin Console as formatted label: `TWINGATE_LABEL_DEV_ENVIRONMENT=dev1` → `Dev Environment: dev1`
- Twingate auto-sets `TWINGATE_LABEL_HOSTNAME` and `TWINGATE_LABEL_DEPLOYED_BY` in most deployment scripts
- Metadata visible on left-hand side of Connector detail page

## Configuration Values

| Environment Variable | Description | Example Value |
|---|---|---|
| `TWINGATE_LABEL_HOSTNAME` | Device hostname (auto-set) | `` `hostname` `` |
| `TWINGATE_LABEL_DEPLOYED_BY` | Deployment method (auto-set) | `docker`, `ecs` |
| `TWINGATE_LABEL_<CUSTOM_KEY>` | Any custom metadata | `custom_value_1` |

## Step-by-Step

1. Identify deployment method (Docker, ECS Fargate, etc.)
2. Add `TWINGATE_LABEL_<KEY>=<VALUE>` environment variables to deployment script
3. Run deployment command — metadata appears automatically in Admin Console

**Docker example:**
```bash
docker run -d \
  --env TWINGATE_LABEL_HOSTNAME="`hostname`" \
  --env TWINGATE_LABEL_DEPLOYED_BY="docker" \
  --env TWINGATE_LABEL_DEV_ENVIRONMENT="dev1" \
  twingate/connector:1
```

**ECS Fargate example (within `environment` array):**
```json
{"name": "TWINGATE_LABEL_DEV_ENVIRONMENT", "value": "dev1"}
```

## Gotchas
- Prefix `TWINGATE_LABEL_` is required — variables without this prefix are not treated as metadata
- Key naming: underscores in the suffix become spaces with title case in the Admin Console display
- Custom metadata does not override required Connector variables (`TWINGATE_NETWORK`, `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`)

## Related Docs
- Connector deployment methods (Docker, ECS Fargate)
- Twingate Admin Console — Connector detail view
- Connector environment variable configuration