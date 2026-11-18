<!-- manual-reference: do-not-overwrite -->
<!--
  HAND-AUTHORED REFERENCE — SE field notes for SCIM sync failures. It carries no
  `source:` frontmatter, so the auto-update pipeline does not own it. Where a
  generated summary shows a SCIM endpoint host without a shard (e.g. the generic
  `<tenant>.twingate.com` form in `identity-provider-setup.md`), this file governs
  for shard-based tenants.
-->
# SCIM Sync Troubleshooting — SE Notes

## Okta: users and groups are created, but memberships never apply

**Symptom**
- Okta SCIM creates users and groups in Twingate, but group memberships never apply.
- Or profile updates fail with `User not found`.
- Okta reports `SUCCESS` for the push in both cases.

**Log signature**
Twingate logs show Okta's `GET` requests at push time with no following `PATCH`.

**Cause**
The SCIM base URL is missing the region shard. The reads reach Twingate; the writes do
not survive the redirect.

**Fix**
Use the full `<slug>.<shard>.twingate.com` host, copied from the Admin Console URL —
`acme.us1.twingate.com`, not `acme.twingate.com`.

- **Okta catalog app:** the SCIM endpoint is pre-configured from the app's **Subdomain**
  field, so that field must hold `<slug>.<shard>` (e.g. `acme.us1`). See
  `okta-app-configuration.md`.
- **Custom SCIM app or another IdP:** paste the SCIM endpoint exactly as the Admin Console
  shows it. Do not rebuild it from the tenant name.

After correcting the URL, re-push the affected groups from Okta and confirm the member
counts in Twingate's Groups page match the IdP.

**Self-check (admin, no support ticket needed)**
1. Note the host in the browser address bar while signed in to the Twingate Admin Console.
2. Compare it with the host in the IdP's SCIM base URL (Okta: the Twingate app's
   Subdomain field).
3. If the console host has two labels before `.twingate.com` (`acme.us1`) and the IdP has
   one (`acme`), the shard is missing and this is the cause.
