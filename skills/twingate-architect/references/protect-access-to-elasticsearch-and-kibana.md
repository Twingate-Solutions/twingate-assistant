# Protect Access to Elasticsearch and Kibana

## Summary
Twingate secures Elasticsearch and Kibana by layering SSO and MFA from your identity provider without modifying the Elastic applications or requiring a paid Elastic security tier. Resources are added through the Twingate admin console, hiding servers from the public internet entirely.

## Key Information
- Elastic's authentication/SSO features require higher-tier paid plans; Twingate provides these capabilities at the network layer regardless of Elastic plan
- MFA enforcement is handled by your existing identity provider via Twingate access policies
- User provisioning/deprovisioning managed centrally through your identity provider—no separate Elastic user accounts needed
- Elasticsearch/Kibana servers can be fully hidden from the public internet within a private network

## Prerequisites
- Twingate account with admin console access
- Identity provider configured with Twingate (for SSO/MFA enforcement)
- Twingate Connector deployed in the same network as Elasticsearch/Kibana servers

## Step-by-Step
1. Add Elasticsearch and/or Kibana servers as **Resources** in the Twingate admin console
2. Configure access policies on those resources to enforce MFA via your identity provider
3. Assign user groups to the resources
4. Users access Elasticsearch/Kibana through the Twingate client—no direct internet exposure

*Full step-by-step instructions linked from the doc: [Add resources guide](https://www.twingate.com/docs/)*

## Configuration Values
- No Elastic-side configuration changes required
- No specific environment variables or CLI flags documented on this page
- Access policy settings configured in Twingate admin console UI

## Gotchas
- No native authentication changes are made to Elasticsearch/Kibana—security is entirely at the network/access layer
- Misconfiguring Elasticsearch security (if exposed directly) has historically caused massive data breaches; Twingate mitigates this by removing public exposure entirely
- SSO/MFA only applies when users connect via Twingate client; ensure direct network paths to Elastic servers are blocked at the firewall level

## Related Docs
- [Adding Resources](https://www.twingate.com/docs/resources) — step-by-step for adding servers as resources
- Identity Provider / SSO configuration guides
- Twingate Connector deployment documentation
- Access Policy configuration