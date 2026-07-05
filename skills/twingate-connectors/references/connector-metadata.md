# Connector Metadata

## Summary
Twingate Connectors support custom key-value metadata added at deployment time via environment variables. Metadata is displayed in the Connector detail view in the Admin console. Twingate automatically presets some metadata values like `hostname` and `deployed_by` depending on deployment method.

## Key Information
- Metadata is set via environment variables prefixed with `TWINGATE_LABEL_`
- Key suffix is converted to display name (e.g., `DEV_ENVIRONMENT` → "Dev Environment")
- Displayed on left-hand side of Connector detail page in Admin console
- Works across all deployment methods (Docker, ECS Fargate, etc.)
- Twingate auto-populates `TWINGATE_LABEL_HOSTNAME` and `TWINGATE_LABEL_DEPLOYED_BY` in most deployment scripts

## Configuration Values

| Environment Variable | Description | Example |
|---|---|---|
| `TWINGATE_LABEL_HOSTNAME` | Auto-set to local hostname | `` `hostname` `` |
| `TWINGATE_LABEL_DEPLOYED_BY` | Auto-set to deployment method | `docker`, `ecs` |
| `TWINGATE_LABEL_<SUFFIX>` | Custom metadata | `TWINGATE_LABEL_DEV_ENVIRONMENT=dev1` |

## Step-by-Step

1. Identify your deployment method (Docker, ECS Fargate, Kubernetes, etc.)
2. Add environment variables prefixed with `TWINGATE_LABEL_` to your deployment script/config
3. Set the value for each label
4. Run the deployment command
5. Verify metadata appears in Admin console → Connector detail view

## Examples

**Docker:**
```bash
docker run -d \
  --env TWINGATE_LABEL_HOSTNAME="`hostname`" \
  --env TWINGATE_LABEL_DEPLOYED_BY="docker" \
  --env TWINGATE_LABEL_DEV_ENVIRONMENT="dev1" \
  twingate/connector:1
```

**ECS Fargate (JSON task definition):**
```json
{
  "name": "TWINGATE_LABEL_DEV_ENVIRONMENT",
  "value": "dev1"
}
```

## Gotchas
- Underscore-separated suffixes are converted to title case with spaces in the UI (`CUSTOM_METADATA_1` → "Custom Metadata 1")
- No validation on label values — ensure values don't contain characters that break your shell or JSON syntax
- Auto-preset labels (`HOSTNAME`, `DEPLOYED_BY`) may already exist in Twingate-generated scripts; avoid duplicating them

## Related Docs
- Connector deployment methods (Docker, ECS Fargate, Kubernetes)
- Twingate Admin Console — Connector detail view