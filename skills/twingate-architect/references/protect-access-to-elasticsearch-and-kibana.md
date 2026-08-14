---
source: https://www.twingate.com/docs/protect-access-to-elasticsearch-and-kibana
type: docs
fetched: 2026-08-14
source_version: a067d9d54ead8879ee5ea504a27c06f33c356addd8c12142dcdda26f7795eb6a
---

# Protect Access to Elasticsearch and Kibana

## Summary
Twingate adds SSO and MFA to Elasticsearch and Kibana without modifying the applications or requiring paid Elastic security tiers. Resources are added through the Twingate admin console, leveraging your existing identity provider for authentication and authorization.

## Key Information
- Elasticsearch and Kibana lack built-in authentication/authorization on free/lower tiers
- Twingate wraps SSO and MFA around Elastic without application-level changes
- No separate Elastic user accounts needed — provisioning/deprovisioning handled via identity provider
- Elastic servers can be hidden from the public internet within a private network
- Works with any Twingate-supported identity provider

## Prerequisites
- Twingate account with admin access
- Existing identity provider (IdP) configured in Twingate
- Elasticsearch/Kibana deployed (on-premise or private network)
- Twingate Connector deployed on the same network as Elastic instances

## Step-by-Step
1. Deploy a Twingate Connector on the network hosting Elasticsearch/Kibana
2. In the Twingate admin console, add Elasticsearch server(s) as Resources
3. Add Kibana server(s) as separate Resources if applicable
4. Assign access policies to Resources (enable MFA requirement via IdP policy)
5. Grant user/group access to Resources through the admin console
6. Users access Elastic via Twingate Client — no direct internet exposure

## Configuration Values
- No Elastic-side configuration required
- Resource definition: hostname/IP and port of Elasticsearch (default: `9200`) and Kibana (default: `5601`)
- Access policies: configured per Resource in Twingate admin console

## Gotchas
- Elastic's SSO/auth features are **not** being used — Twingate handles auth at the network layer, so Elastic itself remains unauthenticated internally
- Ensure Connectors are placed such that Elastic ports are not publicly exposed (firewall rules should block direct internet access)
- Multiple Elastic instances across environments each need their own Resource definitions
- Deprovisioning in IdP removes Twingate access but does not affect any local Elastic accounts if they exist

## Related Docs
- [Add Resources (Twingate admin console)](https://www.twingate.com/docs/resources)
- [Deploy a Connector](https://www.twingate.com/docs/connectors)
- [Configure Identity Provider](https://www.twingate.com/docs/identity-providers)
- [Access Policies / MFA](https://www.twingate.com/docs/access-policies)