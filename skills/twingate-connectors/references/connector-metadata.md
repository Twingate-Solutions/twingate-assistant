## Connector Metadata

How to add custom key-value metadata labels to Twingate Connectors at deployment time. Labels appear in the Admin Console Connector detail view.

**Mechanism:**
- Set environment variables prefixed with `TWINGATE_LABEL_` followed by your label key and value
- Label key is converted for display: `TWINGATE_LABEL_DEV_ENVIRONMENT=dev1` displays as "Dev Environment: dev1"

**Built-in Labels (pre-set by Twingate deployment scripts):**
- `TWINGATE_LABEL_HOSTNAME` -- set to the deploying machine's hostname
- `TWINGATE_LABEL_DEPLOYED_BY` -- set to the deployment method (e.g., `docker`, `ecs`)

**Adding Custom Labels (Docker example):**
```
--env TWINGATE_LABEL_CUSTOM_METADATA_1="custom_value_1"
--env TWINGATE_LABEL_CUSTOM_METADATA_2="custom_value_2"
```

**Adding Custom Labels (ECS Fargate task definition):**
Add additional `{"name": "TWINGATE_LABEL_...", "value": "..."}` objects to the `environment` array in the task definition JSON.

**Use Cases:**
- Tag Connectors with environment (dev/staging/prod), region, team, or cost center
- Useful for identifying Connectors across large deployments in the Admin Console

**Related Docs:**
- /docs/advanced-connector-management -- Advanced Connector features index
- /docs/connector-details -- Other Connector metadata reported by the Controller
