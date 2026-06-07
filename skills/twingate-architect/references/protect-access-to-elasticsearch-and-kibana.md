# Protect Access to Elasticsearch and Kibana

## Summary
Twingate secures Elasticsearch and Kibana by layering SSO and MFA from your identity provider without modifying the applications or requiring paid Elastic security tiers. It hides the servers from public internet access and centralizes user provisioning/deprovisioning through your IdP.

## Key Information
- Elasticsearch and Kibana lack built-in authentication/authorization on free/lower tiers
- Twingate adds SSO and MFA without any application-level changes
- No Elastic paid plan required for SSO functionality when using Twingate
- Servers are hidden within private network — not publicly accessible or discoverable
- User provisioning and deprovisioning managed centrally via identity provider

## Prerequisites
- Twingate account with admin console access
- Identity provider configured with Twingate (for SSO/MFA enforcement)
- Elasticsearch/Kibana deployed on-premise or in private network
- Twingate Connector deployed in the same network as Elastic instances

## Step-by-Step
1. Add Elasticsearch and Kibana servers as **Resources** in the Twingate admin console
2. Configure access policy to enforce MFA via your identity provider
3. Assign users or groups to the resource
4. Users access Elasticsearch/Kibana through Twingate client (SSO + MFA enforced automatically)

> Full step-by-step instructions linked from the Twingate admin console resource creation flow.

## Configuration Values
- No application-level config changes required on Elasticsearch or Kibana
- Resource definition: hostname/IP and port of Elasticsearch (default: 9200) and Kibana (default: 5601)

## Gotchas
- SSO and MFA are enforced at the **network access layer**, not within Elasticsearch/Kibana itself — application-level auth is separate
- Misconfigured Elasticsearch security settings (even with Twingate) can still expose data; Twingate controls network access only
- Multiple Elasticsearch instances across environments each need to be added as separate Resources

## Related Docs
- [Add Resources in Twingate Admin Console](https://www.twingate.com/docs/resources)
- [Step-by-step resource setup instructions](https://www.twingate.com/docs/step-by-step)
- [Identity Provider / SSO Configuration](https://www.twingate.com/docs/identity-providers)
- [MFA Access Policies](https://www.twingate.com/docs/access-policies)