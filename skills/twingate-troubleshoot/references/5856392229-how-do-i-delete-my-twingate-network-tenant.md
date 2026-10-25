---
source: https://help.twingate.com/articles/5856392229-how-do-i-delete-my-twingate-network-tenant
type: help
fetched: 2026-10-25
source_version: b14bda47af1772fd489ca606ff69c01231b5f64afdb535b127e3eb0870ed15f2
trust: official
---

# How to Delete a Twingate Network/Tenant

## Summary
Describes the process for permanently deleting a Twingate network tenant via the Admin Console. Requires downgrading any active paid subscription to Starter before deletion becomes available.

## Key Information
- Only applicable to **Starter**, **Teams**, and **Business** plan admins
- **Enterprise/invoice accounts** must contact their Twingate representative directly
- **End-users** cannot delete the network — only admins can; end-users should contact their admin to be removed

## Prerequisites
- Admin access to the Twingate Admin Console
- Subscription must be on the **Starter (free)** plan — paid plans must be downgraded first
- Subscription downgrade takes effect at the **end of the current billing period**

## Step-by-Step

### Step 1: Downgrade Subscription (if on Teams or Business)
1. Downgrade to the free Starter plan (see *Downgrade your subscription* docs)
2. Wait until the next billing period for the downgrade to take effect
3. Verify the scheduled change via *How do I check that my subscription will downgrade?*

### Step 2: Delete the Network
1. Sign into the **Admin Console**
2. Click **Settings**
3. Click **Billing**
4. Scroll to the bottom — locate **Delete Network Account** section
5. Click **Delete**
6. Follow the confirmation prompts

## Gotchas
- The **Delete Network Account** option is hidden while any active paid subscription exists — it only appears after the subscription has fully lapsed to Starter
- Downgrade is not immediate; you must wait until the end of the billing period before deletion becomes available
- This process deletes the **entire network/tenant**, not an individual user account

## Related Docs
- Downgrade your subscription
- How do I check that my subscription will downgrade?