# Protect Access to Elasticsearch and Kibana

## Summary
Twingate secures Elasticsearch and Kibana by adding SSO and MFA without modifying the applications or requiring paid Elastic security tiers. It hides Elastic servers from the public internet and centralizes user provisioning through your identity provider.

## Key Information
- Elasticsearch/Kibana lack built-in authentication by default; security features require higher-cost Elastic paid plans
- Twingate adds SSO/MFA at the network access layer — no application-level changes required
- Works with any Elastic deployment tier (no Elastic security subscription needed)
- Servers are hidden within private network, not publicly accessible or discoverable
- User provisioning/deprovisioning managed centrally via identity provider — no separate Elastic user accounts needed

## Prerequisites
- Twingate account with admin console access
- Elasticsearch/Kibana deployed on-premise or in private network
- Identity provider configured with Twingate (for SSO/MFA enforcement)
- Twingate Connector deployed in the same network as Elastic servers

## Step-by-Step
1. Deploy a Twingate Connector in the network hosting your Elasticsearch/Kibana servers
2. Add Elasticsearch server(s) as Resources in the Twingate admin console
3. Add Kibana server(s) as Resources in the Twingate admin console
4. Configure access policies on those Resources to enforce MFA via your identity provider
5. Assign user groups to the Resources

> Full resource setup instructions: See [Add Resources documentation](https://www.twingate.com/docs/adding-access-to-resources)

## Configuration Values
- No specific env vars or CLI flags documented on this page
- Resource configuration done via Twingate Admin Console UI
- MFA enforcement set via Access Policy on each Resource

## Gotchas
- Elastic's native security features (SSO, user auth) are **not** included in free/basic tiers — Twingate bypasses this requirement entirely
- Misconfiguring Elastic security directly has historically caused major data exposures; Twingate approach avoids touching Elastic security config
- Must remember to deprovision users at the identity provider level (Twingate reflects IdP state, but Elastic has no native deprovisioning hook)

## Related Docs
- [Adding Resources](https://www.twingate.com/docs/adding-access-to-resources)
- Twingate Identity Provider / SSO setup documentation
- Twingate Access Policies documentation