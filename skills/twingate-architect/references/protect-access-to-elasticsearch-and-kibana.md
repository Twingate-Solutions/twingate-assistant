## Protecting Elasticsearch and Kibana Access with Twingate

Elasticsearch and Kibana's basic/free tiers lack authentication, user management, and SSO -- security features are gated behind expensive paid plans. Twingate adds IdP-based SSO and MFA enforcement to Elasticsearch and Kibana at the network layer, requiring zero application changes and no Elastic plan upgrade.

**Key Information**
- Elastic's authentication/SSO features require paid tiers -- cost-prohibitive for many orgs running multiple instances
- Twingate adds SSO + MFA via Security Policy at network level; the Elastic application itself is unchanged
- Implementation: add Elasticsearch/Kibana hosts as Twingate Resources; assign to appropriate Groups; apply Security Policy requiring MFA
- Deprovisioning: disable the user in the IdP -- no Elastic-specific cleanup required
- The Elastic servers are hidden from the public internet; no public endpoint exposure

**Prerequisites**
- Twingate Remote Network and Connector deployed in the same network as Elasticsearch/Kibana
- Identity Provider (Okta, Azure AD, Google, etc.) configured in Twingate

**Step-by-Step**
1. Add Elasticsearch server (and Kibana server if separate) as Twingate Resources with appropriate ports (9200 for ES, 5601 for Kibana)
2. Assign Resources to the Group(s) that should have access
3. Apply a Security Policy requiring MFA to those Groups
4. Remove any existing public firewall rules exposing Elasticsearch/Kibana

**Gotchas**
- Twingate MFA enforcement does not add application-level authentication to Elastic -- it gates network access; Elastic itself still has no built-in auth on free tier, so Connector-level network restriction is the full auth layer
- Historical Elastic data breaches often resulted from misconfigured public endpoints; Twingate eliminates the public endpoint entirely

**Related Docs**
- /docs/security-policies
- /docs/resources
- /docs/protect-legacy-apps-with-multi-factor-authentication
