---
name: twingate-troubleshoot
description: |
  Twingate troubleshooting and diagnostics. Use this skill when the user reports
  connectivity issues, access problems, DNS resolution failures, or any error with
  Twingate. Also trigger on 'not connecting', 'can't access', 'troubleshoot',
  'debug', 'diagnose', error messages, or specific Twingate failures.
---

# Twingate Troubleshooting

## When to Use This Skill

- User reports they cannot reach a resource protected by Twingate
- User sees "resource not found", "access denied", or a connection timeout
- User asks to troubleshoot, debug, or diagnose a Twingate issue
- DNS resolution is returning unexpected results for a managed resource
- A connector shows DEAD or unhealthy in the admin console
- Users are randomly losing access mid-session
- A newly added resource is not appearing in the client
- Device trust or security policy is suspected of blocking access
- Any Twingate error message or unexplained connectivity failure

## Quick Reference

- The connection chain is: **Client → DNS → Controller Auth → Connector → Resource**
- Managed resource FQDNs resolve to `100.95.x.x` when the client is connected
- Connector states: `ALIVE`, `DEAD_NO_HEARTBEAT`, `DEAD_HEARTBEAT_TOO_OLD`, `DEAD_NO_RELAYS`
- `DEAD_NO_RELAYS` always means the connector cannot reach Twingate Relays — check outbound 443 to `*.twingate.com`
- Device trust failures are **silent**: the resource simply disappears from the client's resource list
- Both P2P and Relay paths are encrypted — falling back to Relay is a performance concern, not a security concern
- The connector requires **no inbound ports** — do not attempt to probe or scan it

## Evergreen Knowledge

### The Connection Chain

Every Twingate connection traverses a discrete, testable chain:

```
Client → DNS → Controller Auth → Connector → Resource
```

When something breaks, find the broken link. ZTNA troubleshooting differs fundamentally from traditional networking: there are no inbound ports to probe, no VPN concentrator to ping. Instead, interrogate each component in order. The chain model eliminates guesswork — if you know where the chain breaks, you know exactly what to fix.

### The Six-Step Decision Tree

Walk through these steps in order. Stop at the first step that reveals the failure.

**Step 1 — Is the Twingate Client running and authenticated?**

The client must be installed, running, and the user must be signed in via the IdP. Installation alone is not sufficient.

- Check: the client tray icon or app shows "Connected" and an authenticated identity
- If the client is installed but the user is not signed in, resources will not appear and DNS will not be intercepted
- Fix: install the client if missing; have the user sign in; verify the SSO/IdP configuration is correct

**Step 2 — Is the resource visible in the user's resource list?**

Open the Twingate Client and check the Resources tab. If the resource is absent from the list, the connection attempt will fail before any network traffic is involved.

- If absent: the user's Groups do not include this resource, or a device trust policy is hiding it
- Fix: check group membership in the admin console; check the resource's group assignments; check whether a security policy is filtering resources based on device state
- Note: device trust failures are silent — the resource disappears rather than showing an error

**Step 3 — Is DNS resolving correctly?**

For FQDN and wildcard resources, the Twingate Client intercepts DNS queries and returns a synthetic address in the `100.95.x.x` range.

- Test: `nslookup <resource-fqdn>` — should return a `100.95.x.x` address
- If resolving to the real backend IP: the client is not intercepting — client is not connected, or the resource definition is incorrect
- If resolving to `100.95.x.x` but the connection still fails: the DNS layer is healthy; the problem is downstream (connector or policy)
- If another DNS resolver is intercepting the query first: split DNS conflict; check for competing resolvers or VPN clients

**Step 4 — Is the Connector alive?**

Navigate to the admin console → Remote Networks → select the network → Connectors. Check the connector status.

- `ALIVE`: connector is healthy and reachable
- `DEAD_NO_HEARTBEAT`: connector process is not running — restart the container or service
- `DEAD_HEARTBEAT_TOO_OLD`: connector was alive but missed recent heartbeats — restart and check for resource exhaustion on the host
- `DEAD_NO_RELAYS`: connector cannot reach Twingate Relays — outbound port 443 to `*.twingate.com` is blocked

Fix for `DEAD_NO_RELAYS`: verify the connector host can reach `*.twingate.com:443`. Check host-level firewall rules, security group egress rules (AWS/GCP/Azure), and corporate proxy settings. Deep-packet inspection (DPI) appliances that terminate TLS will break the connector's relay connection.

**Step 5 — Can the Connector reach the Resource?**

The connector must have network-level routing to the backend resource. This is the most commonly missed step.

- Test from the connector host (not from the user's machine):
  ```bash
  curl -v http://<resource-ip>:<port>
  telnet <resource-ip> <port>
  ```
- Common causes of failure: the connector is in a VPC or subnet that lacks a route to the resource; a security group or firewall rule blocks connector → resource traffic; the resource IP in Twingate does not match the actual resource IP
- Fix: add the required security group rule, firewall rule, or route; verify the resource definition uses the correct IP or CIDR

**Step 6 — Is the Security Policy satisfied?**

If the resource is visible and the connector is alive but access is still denied, the security policy is the likely cause.

- Device trust: is the device enrolled in the required MDM or EDR solution?
- MFA: did the user complete the required MFA challenge for this session?
- Session duration: has the session expired and the user needs to re-authenticate?
- Geoblocking: is the user connecting from a region that is blocked by policy?
- JIT access: was a just-in-time access request submitted and approved?

Fix: verify the device is enrolled and the enrollment status is syncing to Twingate; have the user re-authenticate; adjust the security policy if the settings are misconfigured.

### Common Failure Categories

**Device / Client layer**

- Client not installed or not running
- User not signed in to the client
- Client version is below the minimum supported version (upgrade required)
- Device trust policy blocking the device from seeing resources

**DNS layer**

- Resource FQDN not resolving to `100.95.x.x` (client not intercepting)
- Split DNS conflict: a competing DNS resolver intercepts the query before Twingate
- VPN conflict: another VPN client captures routes or DNS queries that Twingate should handle
- Stale DNS cache: resource was recently redefined; old record is cached on the client

**Connector layer**

- Connector container or process has crashed — restart it
- `DEAD_NO_RELAYS`: outbound 443 to `*.twingate.com` is blocked
- Connector token has expired or been invalidated — rotate tokens and redeploy
- Connector host has insufficient CPU or memory, causing missed heartbeats

**Firewall / Network layer**

- Outbound HTTPS (443) from the connector host to `*.twingate.com` is blocked
- DPI appliance terminating TLS connections from the connector
- VPN on the user's machine capturing traffic that should be handled by Twingate
- Missing route or security group rule between connector and resource

**Policy / Authorization layer**

- User is not a member of the group that has access to the resource
- Security policy requires device trust but the device is not enrolled
- Session has expired; user must re-authenticate
- JIT access request not yet approved
- Geoblocking rule matches the user's current location

### Key Diagnostic Commands

```bash
# Check DNS resolution for a managed resource
# Should return 100.95.x.x when the Twingate client is connected
nslookup <resource-fqdn>

# Check connectivity from the connector host to the resource
curl -v http://<resource-ip>:<port>
telnet <resource-ip> <port>

# Check connector container logs (Docker deployment)
docker logs twingate-connector --tail 100

# Check connector service logs (systemd deployment)
journalctl -u twingate-connector -n 100

# Test outbound relay connectivity from the connector host
curl -v https://<tenant>.twingate.com/api/graphql

# Query connector status via GraphQL API
# POST to https://<tenant>.twingate.com/api/graphql
# Header: X-API-KEY: <api-key>
# Body: { "query": "{ connectors { edges { node { id name state } } } }" }
```

## Current Documentation

For current troubleshooting steps, error message reference, and platform-specific guidance, read the reference files in this skill's `references/` directory.

If a reference file seems outdated or missing, fetch the doc directly:

```bash
curl -s https://www.twingate.com/docs/troubleshooting
curl -s https://www.twingate.com/docs/troubleshoot-p2p
curl -s https://www.twingate.com/docs/troubleshoot-connector
curl -s https://www.twingate.com/docs/troubleshoot-nat
```

Key doc slugs:

- `troubleshooting` — main troubleshooting guide and overview
- `troubleshoot-p2p` — P2P connection issues
- `troubleshoot-connector` — connector-specific failures
- `troubleshoot-nat` — NAT traversal failures

## Common Patterns

**"I can't access the resource"**

Start at Step 1 of the decision tree. Confirm client is running, user is authenticated, and the resource appears in the client's resource list before investigating the network layer.

**Connector shows DEAD after an upgrade**

Likely a token issue. Connector tokens can be invalidated during certain upgrade paths. Check the connector logs for authentication errors, generate new tokens in the admin console, and redeploy the connector with the new tokens.

**Resource resolves to `100.95.x.x` but the connection times out**

DNS is working correctly. The connector is the next link to check. Confirm the connector is ALIVE, then test connectivity from the connector host to the resource IP and port. The most common cause is a missing security group egress rule between the connector and the resource.

**Users randomly losing access mid-session**

Security policy session duration has been exceeded. The user's session expired and Twingate terminated the connection. Adjust the session duration in the security policy, or train users to expect periodic re-authentication prompts.

**Newly added resource not appearing in the client**

Two likely causes: (1) DNS cache — have the user disconnect and reconnect the Twingate client to force a resource list refresh; (2) the resource was just added and the client has not yet synced. Disconnect/reconnect resolves both.

**VPN conflict causing intermittent failures**

If the user has another VPN client running alongside Twingate, routes and DNS queries can conflict. Check whether the other VPN is capturing `100.95.x.x` routes or overriding the DNS resolver. In most cases, Twingate should be used instead of the conflicting VPN, not alongside it.

## Anti-Patterns and Gotchas

**Probing inbound ports on the connector.**
Twingate connectors have no inbound ports. Attempting to port-scan or probe the connector host will reveal nothing useful. The connector initiates all connections outbound. If the connector is unreachable from the admin console, check the connector host's outbound connectivity to `*.twingate.com`, not inbound accessibility.

**Testing connectivity from the user's machine instead of the connector host.**
The user's machine cannot directly reach the backend resource — that is the point of ZTNA. Always test the connector → resource path by running diagnostic commands on the connector host itself.

**Ignoring connector logs.**
Connector logs frequently contain the exact failure reason: expired token, relay unreachable, TLS handshake failure. Check the logs before spending time on network diagnostics.

**Treating Relay fallback as a security problem.**
When P2P cannot be established (e.g., due to symmetric NAT), Twingate falls back to a Relay path. Both paths use the same encryption. Relay fallback is a latency concern and should be investigated as a performance issue, not a security incident.

**Not checking device trust state when a resource disappears.**
Device trust failures are intentionally silent: the resource simply stops appearing in the client's list. This is a common source of "it was working yesterday" reports. Always ask whether device trust is configured and whether the user's device is enrolled and compliant.

**Assuming a token rotation is unnecessary after infrastructure changes.**
Connector tokens are long-lived but can be invalidated by certain admin actions (tenant resets, explicit revocation). After any significant infrastructure change, verify the connector is ALIVE and check its logs for authentication errors.

**Overlooking DPI as the cause of `DEAD_NO_RELAYS`.**
Corporate firewalls with deep-packet inspection can intercept and terminate TLS connections that appear to be going to allowed destinations. If outbound 443 is nominally permitted but the connector cannot reach Twingate Relays, DPI termination is a strong candidate. Check whether the firewall has a TLS inspection bypass rule for `*.twingate.com`.

## Related Skills

- [twingate-architect](../twingate-architect/SKILL.md) — connection chain architecture, P2P vs. Relay, encryption model
- [twingate-connectors](../twingate-connectors/SKILL.md) — connector deployment, token management, upgrade procedures, HA
- [twingate-identity](../twingate-identity/SKILL.md) — security policy configuration, device trust, group access, session duration
- [twingate-dns-security](../twingate-dns-security/SKILL.md) — DNS filtering and split DNS configurations that may conflict with Twingate's DNS interception
