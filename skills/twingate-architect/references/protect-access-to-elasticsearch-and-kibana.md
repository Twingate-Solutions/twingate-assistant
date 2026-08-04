# Protect Access to Elasticsearch and Kibana with Twingate

## Summary
Twingate adds SSO and MFA to Elasticsearch and Kibana without modifying the applications or requiring paid Elastic security tiers. Access is controlled through your identity provider, and servers can be hidden from the public internet entirely.

## Key Information
- Elasticsearch and Kibana have no built-in authentication/authorization on free/lower tiers
- Elastic SSO/auth features require higher-cost paid plans
- Twingate enforces identity provider SSO and MFA at the network layer, not the application layer
- No changes required to Elasticsearch or Kibana configurations
- Users provisioned/deprovisioned centrally via identity provider — no separate Elastic user accounts needed
- Servers can be fully hidden from public internet (not just access-restricted)

## Prerequisites
- Twingate account with admin access
- Existing identity provider (IdP) configured in Twingate
- Elasticsearch/Kibana deployed on-premise or in a private network
- Twingate Connector deployed in the same network as Elastic instances

## Step-by-Step
1. Deploy a Twingate Connector in the network hosting Elasticsearch/Kibana
2. In the Twingate admin console, add the Elasticsearch and Kibana servers as Resources
3. Assign appropriate Groups/access policies to those Resources
4. Configure MFA enforcement via your identity provider's policy if required
5. Users access Elasticsearch/Kibana only through the Twingate client — no direct internet exposure

## Configuration Values
- No specific env vars, CLI flags, or API parameters documented on this page
- Resource configuration: use server hostname/IP and relevant ports (Elasticsearch default: `9200`, Kibana default: `5601`)

## Gotchas
- Authentication is enforced at the Twingate/IdP layer only — Elasticsearch itself remains unauthenticated internally; ensure network segmentation prevents bypass
- Misconfiguration of Elasticsearch security (even with Twingate) can still expose data if the server is reachable via other network paths
- MFA enforcement depends on IdP configuration, not Twingate alone

## Related Docs
- [Add Resources in Twingate Admin Console](https://www.twingate.com/docs/resources) (referenced as "add the relevant servers as resources")
- Step-by-step resource setup instructions (linked inline on source page)
- Twingate Connector deployment documentation