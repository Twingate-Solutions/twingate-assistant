---
source: https://www.twingate.com/docs/connector-metadata
type: docs
fetched: 2026-11-13
source_version: 987d352206899496dd8ffe813740afdf4253bb8c18eb50b938f945aedc8830ae
trust: official
---

# Connector Metadata

## Summary
Twingate lets you attach custom key-value metadata to Connectors at deploy time. Metadata is set through environment variables prefixed `TWINGATE_LABEL_` and appears in the Connector detail view in the Admin Console. The deployment scripts from the Admin Console already preset some labels, such as `hostname` and `deployed_by`.

## Key Information
- Metadata is added as extra configuration options (environment variables) in the deployment script or config for the chosen deployment method.
- Naming format: `TWINGATE_LABEL_<SUFFIX>=<value>`.
- Display: `TWINGATE_LABEL_DEV_ENVIRONMENT=dev1` shows in the Admin Console as `Dev Environment: dev1`. Additional metadata appears below it on the left side of the Connector page.
- Twingate presets `hostname` (local hostname of the host device) for many deployment methods. This helps identify where a Connector runs.
- Twingate presets `deployed_by` in many cases, indicating the deployment method (e.g. `docker`, `ecs`).

## Prerequisites
- A Connector deployment script or config from the Admin Console (Docker, ECS Fargate, etc.).
- Valid `TWINGATE_NETWORK`, `TWINGATE_ACCESS_TOKEN`, and `TWINGATE_REFRESH_TOKEN` values from the Connector's token generation.

## Step-by-Step
1. Generate the Connector deployment script in the Admin Console for your deployment method.
2. Add one `TWINGATE_LABEL_<NAME>` variable per metadata item, using the same mechanism the script uses for other environment variables.
3. Run or apply the deployment.
4. Check the Connector detail view in the Admin Console for the labels.

## Configuration Values
**Docker** (`--env` flags):
```
--env TWINGATE_LABEL_HOSTNAME="`hostname`" \
--env TWINGATE_LABEL_DEPLOYED_BY="docker" \
--env TWINGATE_LABEL_CUSTOM_METADATA_1="custom_value_1" \
--env TWINGATE_LABEL_CUSTOM_METADATA_2="custom_value_2" \
```

**ECS Fargate** (entries in the `environment` array of `containerDefinitions` in `aws ecs register-task-definition`):
```
{"name":"TWINGATE_LABEL_CUSTOM_METADATA_1","value":"custom_value_1"}
```

Existing variables in the same scripts: `TWINGATE_NETWORK`, `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`. The Docker image is `twingate/connector:1`.

## Gotchas
- The syntax differs by deployment method. Docker uses `--env`, while ECS uses `{name, value}` objects in JSON. Add labels in the form your method expects.
- Labels are set at deploy time, so changing them means redeploying or updating the Connector's configuration.
- The ECS Fargate default script includes only `deployed_by`, not `hostname`, because Fargate has no meaningful local hostname to preset.
- Keep the `TWINGATE_LABEL_` prefix exact. Variables without it are not shown as metadata.

## Related Docs
- Connector deployment guides (Docker, ECS, Kubernetes, Linux, etc.)
- Connector configuration and environment variable reference
- Admin Console Connector detail view