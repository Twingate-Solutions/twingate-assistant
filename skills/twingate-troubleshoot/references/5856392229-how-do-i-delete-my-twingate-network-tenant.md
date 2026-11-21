---
source: https://help.twingate.com/articles/5856392229-how-do-i-delete-my-twingate-network-tenant
type: help
fetched: 2026-11-19
source_version: 660029a679703926c99c4743eec52c9d0a56e7f68a1efdef2ff237dcaf557db5
trust: official
---

# How do I delete my Twingate Network/tenant?

## Summary
This page explains how to permanently delete a Twingate Network (tenant) from the Admin Console. Paid Teams or Business subscriptions must first be downgraded to the free Starter plan, and the delete option only appears once no subscription is active.

## Key Information
- Deletion is done by an admin in the Admin Console under Settings > Billing.
- The **Delete Network Account** option is hidden while a paid subscription is active.
- A downgrade takes effect at the next billing period, not immediately.
- This process deletes the whole Network/tenant, not an individual user account.
- Enterprise or invoice accounts: work directly with your Twingate representative instead of using this process.
- End-users: this is not how to remove yourself from a Network. Contact your Twingate Admin to be removed.

## Prerequisites
- Admin access to the Twingate Admin Console.
- Network is on the free Starter plan (downgrade any Teams or Business subscription first).
- Not an Enterprise or invoice account (those go through a Twingate representative).

## Step-by-Step
1. **Downgrade active subscriptions (if applicable).** Downgrade Teams or Business to Starter using the "Downgrade your subscription" article.
2. Verify the scheduled change using "How do I check that my subscription will downgrade?". The downgrade applies at the next billing period.
3. Once on Starter, sign into the Admin Console.
4. Click **Settings**.
5. Click **Billing**.
6. Scroll to the **Delete Network Account** section.
7. Click **Delete**.
8. Follow the prompts to confirm deletion.

## Configuration Values
None. No env vars, CLI flags, or API parameters are documented. This is a UI-only process.

## Gotchas
- If you don't see **Delete Network Account**, an active subscription still exists. Wait until the subscription period ends and the plan reverts to Starter.
- Downgrading is not immediate, so deletion may be delayed until the end of the current billing period.
- Don't use this flow to remove a single user. It deletes the entire Network.
- Enterprise and invoice-billed customers cannot self-serve deletion.

## Related Docs
- Downgrade your subscription
- How do I check that my subscription will downgrade?
- Source: https://help.twingate.com/articles/5856392229-how-do-i-delete-my-twingate-network-tenant