# Connector Metadata

## Summary
Twingate Connectors support custom key-value metadata pairs set via environment variables prefixed with `TWINGATE_LABEL_`. Metadata is visible in the Admin Console on the Connector detail page. Some metadata (hostname, deployed_by) is preset automatically depending on deployment method.

## Key Information
- Metadata displays in Admin Console as human-readable labels (e.g., `DEV_ENVIRONMENT` → `Dev Environment`)
- All custom metadata env vars must use prefix: `TWINGATE_LABEL_`
- Built-in auto-populated labels: `TWINGATE_LABEL_HOSTNAME`, `TWINGATE_LABEL_DEPLOYED_BY`
- Works across all deployment methods (Docker, ECS Fargate, etc.)

## Prerequisites
- Existing Connector deployment script from Admin Console
- Access to modify environment variables in deployment configuration

## Configuration Values

| Environment Variable | Format | Example |
|---|---|---|
| `TWINGATE_LABEL_<SUFFIX>` | `TWINGATE_LABEL_KEY=value` | `TWINGATE_LABEL_DEV_ENVIRONMENT=dev1` |
| `TWINGATE_LABEL_HOSTNAME` | Auto-set | `` `hostname` `` |
| `TWINGATE_LABEL_DEPLOYED_BY` | Auto-set | `docker`, `ecs` |

## Step-by-Step

**Docker:**
```bash
docker run -d \
  --env TWINGATE_LABEL_CUSTOM_METADATA_1="custom_value_1" \
  --env TWINGATE_LABEL_CUSTOM_METADATA_2="custom_value_2" \
  # ... other flags
```

**ECS Fargate** (add to `environment` array in task definition JSON):
```json
{
  "name": "TWINGATE_LABEL_CUSTOM_METADATA_1",
  "value": "custom_value_1"
}
```

## Gotchas
- Underscores in suffix convert to spaces in UI display (`DEV_ENVIRONMENT` → `Dev Environment`)
- Must add metadata at deploy time by modifying the provided script — no indication of post-deploy editing support
- ECS requires metadata inside the `environment` array within the JSON task definition, not as top-level CLI flags

## Related Docs
- Connector deployment methods (Docker, ECS Fargate)
- Twingate Admin Console Connector detail view