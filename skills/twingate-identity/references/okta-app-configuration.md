## Twingate Okta Application Configuration

How to add and configure the official Twingate gallery app in Okta -- step 1 of the Okta integration. Step 2 (SCIM sync) is covered separately in /docs/okta-scim-configuration.

### Add the Twingate App in Okta

1. Okta Admin -> **Applications** -> **Browse App Catalog**
2. Search for **Twingate**, select it
3. Click **Add**
4. Enter your **Twingate subdomain** (the `mycorp` part of `mycorp.twingate.com`)
5. **Recommended**: check both **Application Visibility** boxes to **hide** Twingate from users' Okta dashboards
   - Reason: users authenticate by starting at the Twingate Client, not by clicking the Okta tile (Twingate doesn't support IdP-Initiated SSO)
   - Showing the tile invites confused user behavior

### Assign Users / Groups

- Assign the Twingate Okta app to the users / groups who should access Twingate
- **Always assign yourself first** -- needed to validate the integration

**Suggested Pattern:**
- Create a dedicated Okta group like **"Twingate-Admins"** that includes yourself
- Assign that group to the Twingate app
- **Avoid** using a different group that includes you. If you remove that group later, your access disappears
- For non-admin users, use a separate group like **"Twingate-Users"**

### Complete the Integration in Twingate Admin Console

In Twingate Admin Console -> Identity Provider -> Okta:

| Field | Where to Get It |
|---|---|
| **Okta Domain** | Global header, upper-right of Okta dashboard |
| **Client ID** | Sign On tab of the Twingate Okta app |
| **Client Secret** | Sign On tab of the Twingate Okta app |

After entering, Twingate prompts you to sign in with Okta to validate.

### Decision Notes

- Hide Twingate in users' portals -- always: prevents confusion since Okta tile click doesn't work
- Use a dedicated Okta group for Twingate access -- not Default -- for cleaner future delegation
- Assign yourself before saving -- otherwise you'll be locked out

### Gotchas

- IdP-Initiated SSO from Okta tile does **not** work -- always SP-Initiated (start at Twingate Client)
- If you initially assign the integration via "Default" Okta group and later try to scope tighter, ensure your user remains in an assigned group throughout
- Client Secret is sensitive -- treat as a credential

### Related Docs

- /docs/okta-configuration -- Overall Okta integration overview (step 0)
- /docs/okta-scim-configuration -- Step 2: SCIM user/group sync
- /docs/identity-providers -- IdP overview
- /docs/saas-app-gating-with-okta -- App gating pattern
