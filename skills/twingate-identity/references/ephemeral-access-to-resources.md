---
source: https://www.twingate.com/docs/ephemeral-access-to-resources
type: docs
fetched: 2026-11-13
source_version: 2931ad2b657b8c27aad23098bcb12cde592cc564e8bdcee0b03d3d29f099afac
trust: official
---

# Ephemeral Access

## Summary
Ephemeral Access grants a Group temporary access to a Resource until an expiration time you set. When the time is reached, the Group is automatically removed from the Resource and its users lose access. It is configured in the Admin Console via the **Set Expiration** option.

## Key Information
- Expiration applies to a specific Group's access to a specific Resource.
- Expiration can be set from one hour to one year from the current date.
- Can be configured from either a Resource page or a Group detail page.
- Groups or Resources with an active expiration display an **Expires [date]** pill.
- At expiration, the Group is removed from the Resource automatically.
- Changes to expiration times are recorded in the **Access** category of the Admin Console audit logs.
- Typical uses: projects with a defined end date, fixed-duration contractor engagements, and "break glass" access to sensitive Resources.

## Prerequisites
- Admin Console access with permission to manage Resource access (the page does not state specific roles).
- An existing Group and Resource.

## Step-by-Step

**From a Resource page (new Group):**
1. Add a Group to the Resource.
2. Click **Set Expiration** in the access configuration to open the date picker.
3. Choose a date and time, then click **Set Expiration Time**.
4. Click **Grant Access**.

**From a Resource page (existing Group):**
1. Open the options menu on the Group's row.
2. Select **Set Expiration**.
3. Choose a date/time and apply. To clear it, use **Remove Expiration** in the date picker (access is kept).

**From a Group page:**
- Adding a new Resource: click **Set Expiration** in the access configuration.
- Existing Resource: use the options menu on the Resource row and select **Set Expiration**.

## Configuration Values
- No env vars, CLI flags, or API parameters are documented on this page. Configuration is through the Admin Console UI only.
- Expiration range: minimum 1 hour, maximum 1 year from now.

## Gotchas
- **Remove Expiration** clears the expiration only; it does not remove the Group's access.
- Expiration is per Group-Resource pairing, not global to the Group.
- Users lose access via that Group when it expires. The page does not say how other Group memberships or overlapping access are affected, so verify if users have access through multiple Groups.
- The page does not describe API or Terraform support for expiration; check the API/provider docs before automating.

## Related Docs
- Admin Console audit logs (Access category)
- Groups and Resource access management documentation