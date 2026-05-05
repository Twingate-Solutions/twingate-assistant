## OneLogin Configuration

How to integrate OneLogin with Twingate -- OIDC user authentication + SCIM user/group sync via the Twingate OneLogin application.

**Plan Requirement:**
- **Business or Enterprise** Twingate plans
- **SCIM sync requires OneLogin's Unlimited Plan**

### What's Delegated to OneLogin

- **User authentication** via OpenID Connect (OIDC)
- **User and group synchronization** via SCIM

Only users assigned to the OneLogin Twingate application can sign in to Twingate.

### Supported Features

- **SP-Initiated SSO** via OIDC (start at the Twingate Client)
- IdP-Initiated SSO is **not** supported

### Setup -- Two Stages + SCIM

**Stage 1: Add the Twingate App in OneLogin**

1. OneLogin Admin -> **Applications** -> **Add App** (top-right)
2. Search for **Twingate**, select it
3. **Disable "Visible in portal"** (recommended) -- hides Twingate from users' OneLogin portal since IdP-Initiated SSO doesn't work
4. **Save**

**Known Issue**: After Save, OneLogin may show "SCIM Base URL cannot be blank" error. Workaround:
- Navigate to **Configuration** tab
- Enter `https://twingate.com` (placeholder; SCIM is configured properly later)
- **Save** to silence the validation error

**Stage 2: Assign OneLogin Roles to the Twingate App**

OneLogin uses **Roles** for app assignment, not Groups directly.

**Suggested Pattern:**
- Create a OneLogin role like **"Twingate-Admins"** that you belong to
- Assign that role to the Twingate app (in addition to or instead of "Default")
- Avoid assigning **only** the "Default" role to the app -- if you later remove Default, all access vanishes including yours

**Stage 3: Complete in Twingate Admin Console**

| Field | Where to Get It |
|---|---|
| **OneLogin Subdomain** | Inspect your OneLogin Admin URL, OR check **Settings > Branding -> Brand** in OneLogin |
| **Client ID** | SSO tab of the Twingate OneLogin app |
| **Client Secret** | SSO tab of the Twingate OneLogin app |

Twingate prompts you to sign in with OneLogin to validate.

**Stage 4: Configure SCIM**
- See /docs/onelogin-configuration-scim for the SCIM setup walkthrough

### Decision Notes

- For SaaS app gating: see /docs/saas-app-gating-with-onelogin (uses OneLogin App Policies)
- Use a dedicated OneLogin role (not Default) for Twingate access -- enables granular delegation later
- Hide Twingate in OneLogin portal: required for clean UX since IdP-Initiated SSO doesn't work

### Gotchas

- "SCIM Base URL cannot be blank" error on Save is a **known UI bug** -- use the placeholder workaround
- IdP-Initiated SSO doesn't work -- always start at the Twingate Client
- SCIM requires OneLogin Unlimited Plan -- check before assuming SCIM will work
- Always assign yourself via a non-removable role; otherwise you'll lose access on cleanup

### Related Docs

- /docs/onelogin-configuration-scim -- Step-by-step SCIM setup
- /docs/identity-providers -- IdP overview
- /docs/saas-app-gating-with-onelogin -- App gating pattern
- /docs/scim-provisioning-api -- Underlying SCIM API
