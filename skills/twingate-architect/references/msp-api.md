---
source: https://www.twingate.com/docs/msp-api
type: docs
fetched: 2026-11-13
source_version: ae48d7a518781cd09017bb2432ff5afe0d004ca33429c41f7852cffab98ae599
trust: official
---

# MSP Partner API

## Summary
The MSP Partner API is a GraphQL API for Twingate resellers and MSPs. It operates across all networks under a Partner. It can list MSP Networks (Portals) and Customer Networks, read plan and license counts, and create new MSP Portals. It cannot update or delete anything, and it cannot create Customer Networks (use the MSP Portal for that).

## Key Information
- Operations: queries `partner`, `networks(filter, first, after, last, before)`, `network(id)`; mutation `mspNetworkCreate(networkSlug, networkName, adminEmail)`.
- Not the Admin API. It does not manage Resources, Users, Groups, Connectors, or Policies. Use each network's own Admin API for those.
- `networks` returns a union of `MspNetwork` and `CustomerNetwork`. Use inline fragments and `__typename`. It excludes disabled networks; `network(id)` includes them.
- `licenses` = active users + active Service Accounts − active admins, minimum 1.
- `subscription` can be `null` shortly after a Customer Network is created. Treat it as pending.
- Plan types: `TEAMS`, `BUSINESS`, `BUSINESS_AND_DNSF`, `ENTERPRISE`.
- IDs are opaque. Store them as returned, match on ID rather than name, and never decode or construct them.
- Pagination is Relay cursor style. Loop on `pageInfo.hasNextPage` using `endCursor`; the server caps page size. For all customers, use flat `networks` filtered to `CUSTOMER_NETWORK`.
- New MSP Networks are on the Business plan with social sign-in. The admin gets a welcome email and an invitation.

## Prerequisites
- Partner ID and API key, issued by partnersupport@twingate.com. The key is shown once.
- Server-side code only (no CORS; a browser exposes the key).

## Step-by-Step: Provision an MSP Network
1. Convert the slug locally: strip all non-alphanumerics, lowercase.
2. List MSP Networks and confirm no `url` starts with `https://<slug>.`.
3. Have a person confirm (it creates a live network and sends email).
4. Call `mspNetworkCreate` once.
5. Check `ok`; if false, show `error`.
6. Verify the `entity.url` subdomain matches your slug.
7. Save `entity.id` and `entity.url`.

## Configuration Values
- Endpoint: issued with credentials, e.g. `https://api.us2.twingate.com/partners`
- Headers: `X-PARTNER-ID`, `X-API-KEY`, `Content-Type: application/json`; `User-Agent` is recommended (e.g. `acme-psa-sync/2.1.0`).
- Every request must be a `POST` with a JSON body.
- Health check: `{"query":"{ partner { id name } }"}`
- Limits: 1,000 networks per Partner (MSP and Customer combined), query depth 20, no published rate limit, 30s request timeout suggested.

## Gotchas
- API keys have no scopes and grant full access. Use a secrets manager and a separate key per system.
- `mspNetworkCreate` is not idempotent. Never auto-retry it. After a timeout, search for the converted slug before retrying.
- The slug is silently altered (`Acme-MSP_01` becomes `acmemsp01`) and cannot be changed later.
- Validation errors return HTTP 200 with `ok: false`. Always check `errors` too, since 200 does not mean every field resolved.
- Error statuses: `GET` returns 400; methods other than GET, POST, or OPTIONS return 405; bad credentials return 401.
- Retry queries on 429/502/503/504 with exponential backoff.
- `aggregatedSubscriptions` can fail for the whole MSP list if a customer is on an unreportable plan. Contact support.
- Admin email must be a real mailbox that can sign in via Google, Microsoft, GitHub, or LinkedIn.
- To rotate a key: request a new one, deploy it, then ask Twingate to revoke the old one (permanent).
- No change history is available. Snapshot exports keyed by ID to detect changes.

## Related Docs
- Managed Service Providers
- MSP Billing
- Customer Networks
- Per-network Admin API