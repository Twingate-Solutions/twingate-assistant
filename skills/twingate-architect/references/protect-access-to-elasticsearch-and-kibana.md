# Protect Access to Elasticsearch and Kibana

## Summary
Twingate secures Elasticsearch and Kibana by adding SSO and MFA via your identity provider without modifying the applications or requiring paid Elastic security tiers. It hides Elastic servers within a private network, making them invisible to the public internet.

## Key Information
- Elasticsearch and Kibana have no built-in authentication/authorization on free/lower tiers
- Twingate adds SSO and MFA enforcement without any changes to Elastic applications
- Works regardless of Elastic subscription tier
- Centralized user provisioning/deprovisioning through your identity provider
- No separate user accounts needed in Elasticsearch or Kibana
- Servers are hidden from public internet — not just access-controlled

## Prerequisites
- Twingate account with admin console access
- Identity provider configured with Twingate (for SSO/MFA enforcement)
- Elasticsearch/Kibana deployed on-premise or in private network
- Twingate Connector deployed in the same network as Elastic servers

## Step-by-Step
1. Add Elasticsearch and Kibana servers as **Resources** in the Twingate admin console
2. Configure access policies on those resources to enforce MFA via your identity provider
3. Assign user groups to the resources
4. Users access Elastic only through the Twingate client — direct internet access is blocked

> See [Add Resources](https://www.twingate.com/docs) for detailed instructions.

## Configuration Values
- No application-level config changes required in Elasticsearch or Kibana
- Access control configured entirely in Twingate admin console via Resource and Policy settings

## Gotchas
- Elastic security features (SSO, user management) on paid plans can conflict or overlap — Twingate approach bypasses Elastic's own security layer entirely at the network level
- Misconfiguring Elasticsearch security (even with paid plans) has historically caused massive data exposure — Twingate mitigates this by blocking network-level access
- Deprovisioning must happen at the identity provider level; no separate Elastic account cleanup needed, but only if users never had direct Elastic credentials

## Related Docs
- [Adding Resources to Twingate](https://www.twingate.com/docs/resources)
- [Identity Provider / SSO Configuration](https://www.twingate.com/docs/identity-providers)
- [Deploying Connectors](https://www.twingate.com/docs/connectors)
- [Access Policies and MFA](https://www.twingate.com/docs/access-policies)