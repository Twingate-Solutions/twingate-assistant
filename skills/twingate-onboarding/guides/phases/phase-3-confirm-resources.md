<!-- manual-reference: do-not-overwrite -->
# Phase 3 — Confirm resources

**Goal:** turn the inferred catalog into a buildable one: address, ports, environment,
sensitivity, owner — each `stated`, `sourced`, or `confirmed`.

**Load:** twingate-architect (resource definition: FQDN vs CIDR vs wildcard, aliases, overlapping
resources, DNS behaviour — grep its references for "alias", "wildcard", "overlap").

## Steps

1. List in-scope resources still `inferred` (`status.py` names them). Ask about the lowest-
   confidence first, framed as confirming a guess (`question-bank.md`); round size follows the
   admin's path and assist level.
2. Prefer FQDN addresses; IPs/CIDRs only where no name exists, and as narrow as possible. Flag
   broad CIDRs.
3. Ports: confirm app and admin ports separately. `["*"]` only when the admin explicitly wants all
   ports — note the trade-off.
4. Record owner and sensitivity; sensitivity drives the policy tier in Phase 4.
5. Mark anything the admin defers as `in_scope: false` with a note rather than leaving it inferred.

## Exit gate

Every in-scope resource has buildable provenance and at least one TCP or UDP port entry.

## Notes

- An admin correction makes the value `stated`; plain acceptance of a guess makes it `confirmed`.
- Never batch-confirm ("all looks fine") without showing the table being confirmed.
