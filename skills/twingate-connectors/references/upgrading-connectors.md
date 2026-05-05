## Upgrading Connectors

Best practices and method index for updating Twingate Connectors across all deployment types.

**Universal Principles:**
- Update one Connector at a time within a redundant pair — never update all Connectors simultaneously
- Retain the same access and refresh tokens during upgrade — tokens uniquely identify each Connector; new tokens require reprovisioning
- Always maintain at least 2 Connectors per Remote Network before performing any update

**Update Paths by Deployment Type:**
- Docker (Linux, AWS ECS, Azure ACI): see /docs/docker update guide
- systemd service (Linux): see /docs/systemd-service update guide
- Helm (Kubernetes): see Helm upgrade documentation

**Notifications:**
- When a Connector update is available, all admin users receive a weekly email notification at 00:00 UTC on Mondays listing which Connectors can be updated

**Related Docs:**
- /docs/docker -- Docker/ECS/Azure container update instructions
- /docs/systemd-service -- systemd package update instructions
- /docs/connector-best-practices -- HA deployment and redundancy
