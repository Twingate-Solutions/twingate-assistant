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
Managed FQDNs should return `100.95.x.x` when the client is connected. If resolving to
the real backend IP, the client is not intercepting. If returning `100.95.x.x` but still
timing out, the DNS layer is healthy — the problem is downstream (Connector or policy).

**Step 4 — Is the Connector ALIVE?**
Check admin console → Remote Networks → Connectors. `DEAD_NO_RELAYS` always means outbound
443 to `*.twingate.com` is blocked or a DPI appliance is intercepting the TLS connection.

**Step 5 — Can the Connector reach the Resource?**
Test from the Connector host, not the user's machine. The user's machine cannot directly
reach the backend resource — that is the point of ZTNA.

**Step 6 — Is the Security Policy satisfied?**
Check: device trust enrollment, MFA completion, session expiry, geoblocking, and JIT
approval status.

---

Additional guidelines:

- **Both Connectors DEAD emergency:** Deploy a new Connector from any machine with outbound
  internet access. Connectors only need outbound 443 to `*.twingate.com` to register — you
  do not need an existing working Connector to deploy a replacement.
- **Platform-specific first steps:** macOS — verify the Network Extension is approved in
  System Settings → Privacy & Security. Windows — verify the TAP adapter is present in
  Device Manager. Linux headless — verify the service is running and the config file is
  correctly populated.
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

## Routing

- **→ twingate-connectors**: for Connector deployment, upgrade, or token questions
- **→ twingate-identity**: for security policy configuration, device trust setup, or SCIM
  provisioning questions
- **→ twingate-architect**: when the failure suggests an architectural problem (wrong Remote
  Network topology, Resource defined incorrectly)
- **→ twingate-idfw**: for SSH certificate validation failures, PAM module errors, or
  gateway connectivity issues

## References

See [`references/`](./references/) for current doc summaries.

Key references:

- `troubleshooting-overview.md` — platform-specific diagnostic steps and error message reference
