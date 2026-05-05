## Okta Configuration

How to integrate Okta with Twingate -- OIDC user authentication + SCIM user/group sync via the Twingate app in Okta.

**Plan Requirement:**
- **Business or Enterprise** Twingate plans only

### What's Delegated to Okta

- **User authentication** via OpenID Connect (OIDC)
- **User and group synchronization** via SCIM

Only users assigned to the Okta Twingate application can sign in to Twingate.

### Setup -- Two Steps + SCIM

**Step 1: Create & Configure the Twingate App in Okta Admin Console**
- See /docs/okta-app-configuration for details

**Step 2: Complete Configuration in Twingate Admin Console**
- Validate connection from Twingate side

**Step 3: Configure SCIM in Okta**
- Separate from Step 1
- See /docs/okta-scim-configuration for details

### SP-Initiated SSO Only

Twingate supports **Service Provider Initiated SSO** via OIDC -- the user starts at the Twingate Client (or Admin Console URL), Twingate redirects to Okta, Okta authenticates and redirects back.

IdP-Initiated SSO is **not** supported (Okta tile -> Twingate doesn't work).

### Without Okta Lifecycle Management Module

The **Okta Lifecycle Management Module** (paid Okta add-on) is required for direct SCIM user/group sync.

**If you don't have the LCM Module:**
- Steps to connect Okta to Twingate are the same
- But Users + Groups are NOT auto-synced
- Workaround: define which users have access to Twingate within Okta. Users only become visible in the Twingate Admin Console **after they sign in for the first time** via the Twingate Client + Okta auth.
- Users can then be manually added to Twingate Groups
- Effectively: Okta gates **who can sign in**, but Twingate Group membership is managed manually

### Authentication Policy

When activating the Okta Twingate app, set up an Authentication Policy with the credentials from the app:
- Defines which Okta sign-in policies apply when users access the Twingate Client app
- Use this to enforce MFA, device trust at the Okta layer (in addition to Twingate Resource Policies)

### Decision Notes

- For most production deployments: use Okta with the Lifecycle Management Module + SCIM -- automation is essential at scale
- Without LCM: works for small teams but becomes painful past 50-100 users (manual Group management)
- For SaaS app gating with Okta: see /docs/saas-app-gating-with-okta (uses Okta Network Zones + Sign-On Policy)
- Pair with Okta Conditional Access for finer policy enforcement at the IdP layer

### Gotchas

- SCIM token from Twingate is sensitive -- rotate periodically; treat as a credential
- IdP-Initiated SSO from the Okta tile does not work -- always use SP-Initiated flow
- Without LCM, offboarding requires Okta + Twingate side actions -- consider scripting via /docs/api-overview
- Okta sign-in policies stack with Twingate Resource Policies -- avoid duplicating MFA in both layers (extra prompts, no security benefit)

### Related Docs

- /docs/okta-app-configuration -- Step 1 detail (Twingate app in Okta)
- /docs/okta-scim-configuration -- Step 3 detail (SCIM setup)
- /docs/identity-providers -- IdP overview
- /docs/saas-app-gating-with-okta -- App gating pattern
- /docs/scim-provisioning-api -- SCIM mechanics
