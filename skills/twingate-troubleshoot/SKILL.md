---
name: twingate-troubleshoot
description: >
  Use when the user reports connectivity issues, access failures, DNS resolution
  problems, or any error with Twingate. Activate for: "can't connect", "not working",
  "resource not found", "access denied", DEAD connector, DNS not resolving, device
  trust blocking access, security policy issues, P2P failure, or any Twingate
  troubleshooting or diagnostic request.
---

## Role

Twingate diagnostics specialist. Owns the six-step decision tree for isolating failures
across the full connection chain: Client → DNS → Controller Auth → Connector → Resource.
When a user reports that something isn't working, this skill finds the broken link
systematically.

## Decisions & Guidelines

Walk the decision tree in order. Stop at the first step that reveals the failure.

**Step 1 — Is the Twingate Client running and authenticated?**
The client must be installed, running, and the user signed in via the IdP. Installation
alone is insufficient. If the client is installed but not signed in, resources will not
appear and DNS will not be intercepted.

**Step 2 — Is the resource visible in the user's resource list?**
If absent: check group membership and device trust policy.
**Device trust failures are silent — the resource disappears with no error message.**

**Step 3 — Is DNS resolving correctly?**
Managed FQDNs should resolve to a Twingate-internal address (the Client uses a
CGNAT-style range — current address space documented in
`references/troubleshooting-overview.md` and `references/dns-failures.md`).
If the response is the real backend IP, the client is not intercepting. If
the response is the Twingate-internal address but the connection still times
out, the DNS layer is healthy — the problem is downstream (Connector or policy).

**Step 4 — Is the Connector ALIVE?**
Check admin console → Remote Networks → Connectors. `DEAD_NO_RELAYS` always
means the connector cannot reach Twingate's control/relay infrastructure —
typically DPI/SSL inspection on `*.twingate.com`, or one of the required
outbound ports being blocked. Read
`skills/twingate-connectors/references/connector-best-practices.md` for the
full network requirements before declaring a root cause.

**Step 5 — Can the Connector reach the Resource?**
Test from the Connector host, not the user's machine. The user's machine cannot directly
reach the backend resource — that is the point of ZTNA.

**Step 6 — Is the Security Policy satisfied?**
Check: device trust enrollment, MFA completion, session expiry, geoblocking, and JIT
approval status.

---

Additional guidelines:

- **Both Connectors DEAD emergency:** Deploy a new Connector from any machine
  with outbound internet access that meets the connector network requirements
  in `skills/twingate-connectors/references/connector-best-practices.md`. You
  do not need an existing working Connector to deploy a replacement.
- **Platform-specific first steps:** Each OS has its own first-line check
  (network extension approval on macOS, virtual adapter on Windows, service
  status on Linux). Current per-platform diagnostic steps and component names
  are in `references/troubleshooting-overview.md` — open that file before
  walking a user through OS-specific commands.
- **Always test Connector → Resource connectivity from the Connector host.** Never from the
  user's machine.
- **Never probe inbound ports on a Connector.** Connectors have no inbound ports. Check
  outbound connectivity instead.
- **Check Connector logs before running network diagnostics.** Logs contain the exact
  failure reason — expired token, relay unreachable, TLS handshake failure.
- **`DEAD_NO_RELAYS` often means DPI, not just a blocked port.** If outbound 443 is
  nominally permitted but the Connector cannot reach Twingate Relays, check for a DPI
  appliance terminating TLS. Add a bypass rule for `*.twingate.com`.
- **Relay fallback is a latency concern, not a security concern.** Both P2P and Relay paths
  are encrypted. Never treat Relay fallback as a security incident.

## When to Verify

This skill body contains the diagnostic decision tree, not every error
signature or platform-specific command. **Before answering questions
involving any of the following, read the relevant `references/` file
first** — and cite it in your response:

- Specific IP ranges, port numbers, or DNS responses
- Error message text or exact admin-console state names
- Platform-specific diagnostic commands (macOS, Windows, Linux)
- Connector log signatures and what they indicate
- Firewall, P2P, NAT traversal, or split-tunnel failure modes

Do not answer these from training-data memory or this skill body alone.

## Routing

- **→ twingate-connectors**: for Connector deployment, upgrade, or token questions
- **→ twingate-identity**: for security policy configuration, device trust setup, or SCIM
  provisioning questions
- **→ twingate-architect**: when the failure suggests an architectural problem (wrong Remote
  Network topology, Resource defined incorrectly)
- **→ twingate-idfw**: for SSH certificate validation failures, PAM module errors, or
  gateway connectivity issues

## References

`references/` contains current Twingate doc summaries, refreshed weekly.
**Consult these before answering fact-shaped questions** — your loaded context
may be incomplete or stale.

| If the user asks about… | Read first |
|---|---|
| General diagnostic walkthrough, platform-specific first steps, error messages | `troubleshooting-overview.md`, `how-to-troubleshoot.md`, `troubleshooting.md` |
| DNS resolution failures, internal-IP responses, split-DNS misbehaviour | `dns-failures.md` |
| `DEAD` Connector states, Connector reachability | `connector-failures.md` (also `skills/twingate-connectors/references/connector-best-practices.md` for network requirements) |
| Firewall rules, egress policy, DPI / SSL inspection issues | `firewalls-and-twingate.md`, `firewall-failures.md` |
| P2P establishment failures, NAT traversal, Relay fallback | `troubleshooting-p2p.md` |
| Split-tunnel routing, traffic not flowing through Twingate | `split-tunnel-failures.md` |

For comprehensive coverage, see [`references/`](./references/) for the full
set of doc summaries. **Default to checking** — do not answer error-message
or platform-command questions from memory.
