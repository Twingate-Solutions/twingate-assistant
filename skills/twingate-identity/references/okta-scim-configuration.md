## Okta SCIM User & Group Sync Configuration

How to enable SCIM user/group sync from Okta to Twingate -- step 2 of the Okta integration. Requires the Twingate Okta app already installed (per /docs/okta-app-configuration).

**Plan Requirement:**
- **Business or Enterprise** Twingate plans
- **Okta Lifecycle Management Module** required for SCIM sync (paid Okta add-on)

### Supported SCIM Operations

- Create users in Twingate from Okta
- Update user attributes
- Deactivate users (deactivated in Okta or removed from Twingate Okta app)
- Group push (Okta group -> Twingate Group with members)

### Configuration

**Step 1: Configure API Integration in Okta**
- Twingate Okta app -> **Provisioning** tab
- Click **Configure API Integration**

**Step 2: Get the SCIM Token from Twingate**
- Twingate Admin Console -> SCIM Token
- Note: SCIM endpoint is auto-configured at app install time -- you don't need to re-enter it

**Step 3: Enable API Integration in Okta**
- Tick **Enable API Integration**
- Paste the SCIM Token
- **Test API Credentials** -> should succeed

**Step 4: Enable Provisioning Options**
- Provisioning tab -> enable all 3:
  - Create Users
  - Update User Attributes
  - Deactivate Users
- **Save**
- **Do not modify SCIM Attribute Mappings** -- defaults are correct

Users previously assigned to the Okta Twingate app sync immediately.

### Group Push (Push Groups Tab)

To sync Okta groups to Twingate:

1. Push Groups tab -> **Push Groups** -> **Find groups by name**
2. Search for the group name, select, **Save**

Group members sync only if they're already assigned to the Twingate Okta app.

**Recommended Pattern**: Assign the **Okta group itself** to the Twingate app (not just individual users). Then all members sync automatically.

### Troubleshooting

**"Group is set up to push, but users are not syncing":**
- The users must also be assigned to the Twingate Okta app (via the group or individually)
- Group push by itself doesn't sync members; group must also be app-assigned

**"User removed from Okta group is still in Twingate":**
- If the user was assigned to the Twingate app individually (not via the group), removing them from the group doesn't remove them from the app
- Either: remove them from the Twingate app directly, OR assign only groups (not individuals) to the app from the start

### Decision Notes

- Always assign **groups** (not individuals) to the Twingate Okta app -- cleaner lifecycle, simpler offboarding
- For complex scoping: SCIM Attribute Mappings are configurable but generally shouldn't be touched
- Use Okta Lifecycle Management features (workflows, password policies) on the upstream Okta app -- they'll flow through SCIM

### Gotchas

- LCM Module is **paid** -- without it, SCIM sync isn't available (manual user management required, see /docs/okta-configuration)
- Removing a user from a synced group doesn't always offboard them -- depends on whether they were assigned individually
- Default SCIM Username mapping uses Okta `userName` (typically email) -- if your Okta uses something else, sync issues result; verify before mass rollout

### Related Docs

- /docs/okta-app-configuration -- Step 1 (must precede SCIM setup)
- /docs/okta-configuration -- Overview
- /docs/scim-provisioning-api -- Underlying SCIM 2.0 API reference
- /docs/groups -- Synced Group behavior
- /docs/users -- User management
