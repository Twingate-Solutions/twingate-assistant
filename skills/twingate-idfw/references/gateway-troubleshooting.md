<!-- manual-reference: do-not-overwrite -->
<!--
  HAND-AUTHORED REFERENCE — not generated from a public Twingate doc page.
  Produced from extensive field testing of the actual Twingate Gateway (SSH
  and Kubernetes). There is no source URL in scripts/doc_mapping.yaml for
  this file, and the auto-update pipeline (scripts/update_references.py)
  must never overwrite or delete it — it skips any file carrying the
  "manual-reference: do-not-overwrite" marker above. Edit by hand only.
-->

<!--
Copyright (c) Twingate Inc.
SPDX-License-Identifier: Apache-2.0
-->

# Twingate Gateway Troubleshooting Guide

A field guide to diagnosing problems with the Twingate Gateway (the zero-trust L7
access gateway for SSH, Kubernetes API, and web app resources). It covers the stock
gateway as shipped from `Twingate/gateway` `master`, organized by failure type, with
the exact log messages to look for and example commands to run.

The gateway can be hosted many ways — systemd service, Docker container, Kubernetes
pod (Helm chart), VM image — so every command here is an **example**; adapt paths,
unit names, and container names to your deployment.

---

## 1. How the gateway works (the 30-second model)

Understanding where a connection can fail tells you which section to read:

```text
Twingate Client ──TLS 1.3──> Gateway :8443 ──> upstream resource
      │                          │
      │  1. TCP connect          │
      │  2. TLS handshake        │   (client verifies the gateway's TLS cert
      │                          │    against the CA registered on the controller)
      │  3. HTTP CONNECT with    │
      │     GAT (JWT) + proof-   │
      │     of-possession sig    │   (gateway verifies the JWT against the
      │                          │    controller's JWKS endpoint)
      │  4. Protocol handoff     │
      │     SSH / K8s / HTTP ────┼──> 5. upstream dial + upstream auth
```

Key facts that shape every diagnosis:

- **Identity arrives before the protocol.** The GAT (Gateway Access Token, a JWT in
  the `Proxy-Authorization` header of the CONNECT request) carries the user, device,
  and target resource. Everything after step 3 is already authenticated.
- **Two independent trust relationships exist:** the *client → gateway* TLS trust
  (the certificate/CA registered on the controller) and the *gateway → upstream*
  trust (SSH CA on target hosts, or bearer token + CA file for Kubernetes). They
  fail in different ways and are fixed in different places.
- **The gateway needs outbound HTTPS to the controller** at
  `https://<network>.twingate.com` to fetch the JWKS signing keys. Without it, the
  gateway will not start.

## 2. Where the logs go and how to read them

- The gateway writes **structured JSON to stderr** — not stdout. Container runtimes
  and journald capture both streams, so `docker logs` / `kubectl logs` /
  `journalctl` all work. But a shell redirect like `gateway > file` captures
  nothing, and log shippers configured to watch only the stdout stream (for
  example, routing on Docker's json-file `stream` tag) will miss every record,
  including session recordings and API audit events.
- Every line carries a `logger` field: `gateway` for operational logs,
  `gateway.audit` for audit records (session recordings, per-request API audit).
  Filter on it to separate the streams.
- Every line carries the `version` field — confirm the running version first; many
  issues are already fixed in newer releases.

```bash
# systemd
journalctl -u twingate-gateway -o cat --since -1h

# Docker
docker logs --since 1h <container>

# Kubernetes (Helm chart deployment)
kubectl logs -n <namespace> deploy/<release>-gateway --since=1h

# Split the streams
journalctl -u twingate-gateway -o cat | grep '"logger":"gateway.audit"'   # audit/recordings
journalctl -u twingate-gateway -o cat | grep '"levelname":"error"'        # errors only
```

## 3. Quick triage table

| Log message / symptom | Most likely cause | Section |
|---|---|---|
| `failed to perform TLS handshake` + `EOF` | Client rejected the gateway's TLS cert (stale CA binding, missing SAN) — or benign TCP-probe noise | [§5](#5-tls-certificate-and-trust-failures) |
| Gateway exits at startup, `failed to validate config` | Missing required config field | [§4](#4-startup-and-configuration-failures) |
| Gateway exits at startup, `failed to create connect listener` | Cannot reach controller JWKS endpoint | [§4](#4-startup-and-configuration-failures) |
| Gateway runs, but *every* handshake fails; `failed to load cert or key file` | Unreadable/mismatched cert or key file | [§5](#5-tls-certificate-and-trust-failures) |
| `failed to parse token with error …` (client gets 401) | Expired/invalid GAT, wrong network, clock skew | [§6](#6-connect-authentication-failures) |
| `missing identity header in CONNECT` (407) | Connection not from a Twingate client (probe/scanner), or client malfunction | [§6](#6-connect-authentication-failures) |
| `failed to verify signature` (401) | Proof-of-possession failure — usually TLS interception between client and gateway | [§6](#6-connect-authentication-failures) |
| `Failed to connect to upstream SSH server` | TCP dial failure **or** target sshd rejected the gateway's certificate (untrusted CA / unknown principal) | [§7](#7-ssh-resource-issues) |
| `host key does not match known host key` | Target host rebuilt/re-keyed since first connection (TOFU pin) | [§7](#7-ssh-resource-issues) |
| kubectl: `InternalError ("")`; gateway audit shows the request but upstream fails | Gateway dialing the API server on 443 when it listens elsewhere (e.g. k3s on 6443) | [§8](#8-kubernetes-resource-issues) |
| kubectl: `403 Forbidden` mentioning impersonation | Gateway service account lacks impersonate RBAC for a forwarded group | [§8](#8-kubernetes-resource-issues) |
| Every web app request returns 500, `API request failed` | Bad `webApp.headers` template | [§9](#9-web-app-resource-issues) |
| Sessions never marked complete in a recording consumer | Consumer not seeing the `session finished` marker (wrong stream, filtered logs) | [§10](#10-session-recording-issues) |
| New CA registered but clients still fail TLS | Gateway object still bound to the old CA on the controller | [§11](#11-controller-side-management-gotchas) |
| Long-running session drops mid-use | GAT expiry — the gateway closes the connection when the token expires (by design) | [§6](#6-connect-authentication-failures) |

## 4. Startup and configuration failures

The gateway validates its configuration when it starts and fails loudly. If the
process exits immediately, read the first error line — the causes are ordered:

1. **Config file not found / unparseable** — `failed to read config file` or
   `failed to parse config file`. The config path comes from the `--config` flag or
   the `TWINGATE_CONFIG` environment variable (the Helm chart sets
   `TWINGATE_CONFIG=/etc/gateway/config.yaml`).
2. **Validation failure** — `failed to validate config` wrapping the specific
   field, e.g.:
   - `required field is missing: twingate.network`
   - `tls config: required field is missing: certificateFile` (or `privateKeyFile`)
   - `required field is missing: at least one protocol (Kubernetes, SSH, or WebApp) must be configured`
   - `invalid port number: …` for `port` / `metricsPort` outside 0–65535
   - SSH section: missing `ssh.gateway.username`, invalid key type, negative
     certificate TTL, or conflicting CA configuration (both `manual` and `vault`)
   - Kubernetes section: an upstream missing `name`, or missing both
     `bearerToken` and `bearerTokenFile`
3. **Controller unreachable** — `failed to create connect listener` /
   `failed to create token parser`. The gateway fetches its JWT signing keys (JWKS)
   from `https://<network>.twingate.com/api/v1/jwk/ec` at startup, and **a fetch
   failure is fatal**. Check outbound HTTPS (443) egress, DNS, proxies, and that
   `twingate.network` is spelled correctly.
4. **Port already in use** — a bare bind error on the main port (default `8443`) or
   metrics port (default `9090`).

```bash
# Verify controller reachability from the gateway host (expect HTTP 200 + JSON keys)
curl -sS https://<network>.twingate.com/api/v1/jwk/ec | head -c 200

# Check the ports are free / who owns them
ss -tlnp | grep -E ':(8443|9090)'
```

One important gap to know about: **the TLS certificate *content* is not validated
at startup** — only that the path fields are set. A cert file that is unreadable,
corrupt, or mismatched with its key lets the gateway start cleanly, then every
client handshake fails (see §5).

## 5. TLS certificate and trust failures

This is the most common — and most misdiagnosed — family of gateway problems.

### 5.1 Reading `failed to perform TLS handshake`

```json
{"levelname":"error","logger":"gateway","caller":"connect/conn.go:122",
 "message":"failed to perform TLS handshake","error":"EOF"}
```

The error value tells you which side gave up:

| `error` value | Meaning |
|---|---|
| `EOF` | The peer opened TCP, then closed without completing the handshake. Either a Twingate client that **rejected the gateway's certificate** and closed silently, or a bare TCP probe (see §5.5). |
| `remote error: tls: bad certificate` / `unknown certificate authority` | The peer explicitly rejected the gateway's certificate. |
| `tls: client offered only unsupported versions` | Peer tried TLS < 1.3. The gateway is **TLS 1.3 only** — a TLS-terminating middlebox (DPI/SSL inspection) between client and gateway commonly causes this. Exempt gateway traffic from inspection. |
| `first record does not look like a TLS handshake` | Something sent plaintext to the TLS port (misconfigured probe, curl without `https://`, port scan). |

Both certificate-rejection causes below produce the repeating-`EOF` pattern in
practice, because the client tears down the connection and retries on an interval.

### 5.2 Cause A — the gateway is bound to a stale CA on the controller

Registering a new CA certificate on the controller (Settings → Certificate
Authorities) does **not** automatically re-bind existing gateways. If the gateway
object still points at the old CA, the controller keeps distributing the old trust
anchor to clients, and every handshake fails — surviving client restarts and forced
syncs, because the client is faithfully enforcing the stale CA.

Verify by comparing what the gateway *serves* against what the controller
*distributes* (see §11 for the API steps):

```bash
# What the gateway actually serves (issuer + SANs + validity)
openssl s_client -connect <gateway-address>:8443 </dev/null 2>/dev/null \
  | openssl x509 -noout -issuer -subject -dates -ext subjectAltName
```

Fix: re-bind the gateway object to the new CA via the API (§11), then **restart a
client** — clients pick up the new CA on restart, not mid-session.

### 5.3 Cause B — the certificate's SANs don't cover an address clients dial

Clients validate the gateway certificate against the address they are connecting
to. A certificate minted with SANs for the gateway's own address(es) works fine —
until a new resource address is routed through the gateway (a Kubernetes API
resource is the classic trigger), at which point connections to the *new* address
fail while existing ones keep working. That partial-failure signature (SSH fine,
kubectl fails, same gateway) is the tell.

```bash
# List the SANs and check every resource address routed through this gateway is present
openssl x509 -in /etc/gateway/tls.crt -noout -ext subjectAltName
```

### 5.4 Cause C — the quick-start self-signed leaf corner

Quick-start deployments often generate a **self-signed leaf with `CA:FALSE`** and
per-resource SANs. This works until you need to add an address (§5.3) — and then
you discover the existing certificate *cannot sign a replacement* (it isn't a CA),
so the fix is a full trust-anchor swap: mint a new cert, register it as a new CA on
the controller, re-bind the gateway (§11), and replace every pinned copy (including
any copies distributed to SSH targets). Plan the rotation once, not twice:

```bash
# Is the current cert a CA? (look for "CA:TRUE" / "CA:FALSE")
openssl x509 -in /etc/gateway/tls.crt -noout -ext basicConstraints
```

Recommendation: use a `CA:TRUE` self-signed anchor (or a real internal CA) as the
registered trust anchor from day one, so future changes are a re-issue under the
same anchor rather than a trust redistribution.

### 5.5 Benign lookalike — TCP health probes

A load balancer or monitor doing **TCP-mode** health checks opens and closes the
port every interval, producing metronomic `failed to perform TLS handshake … EOF`
lines (fixed periodicity is the giveaway). The gateway serves a real health
endpoint — `GET /healthz` **over TLS on the main port** returns `200 OK` with no
authentication (this is what the Helm chart's liveness/readiness probes use).
Switch probes to HTTPS `GET /healthz`, or accept the log noise:

```bash
curl -sk https://<gateway-address>:8443/healthz -o /dev/null -w '%{http_code}\n'   # expect 200
```

If nobody is reporting access failures and the cadence is perfectly periodic,
suspect a probe before suspecting certificates.

### 5.6 Cert files broken on disk / failed hot-reload

The gateway watches its cert and key files and hot-reloads on change. Two sharp
edges:

- **A failed reload is not fatal**: `failed to load cert or key file` is logged and
  the gateway keeps serving the *old* certificate. A botched rotation can go
  unnoticed until the old cert expires. Grep for that message after every rotation
  and confirm `reloaded cert and key files` appears instead.
- **A cert broken at startup is not fatal either** (§4): the gateway runs but has
  no certificate to serve, so all handshakes fail.

```bash
# Validate the pair matches (outputs must be identical)
openssl x509 -in /etc/gateway/tls.crt -noout -pubkey | sha256sum
openssl pkey -in /etc/gateway/tls.key -pubout | sha256sum

# Validity window
openssl x509 -in /etc/gateway/tls.crt -noout -dates
```

### 5.7 Getting the client's side of the story

The gateway only ever sees `EOF`; the **Twingate client logs the actual
verification failure** — `x509: certificate signed by unknown authority` (CA
problem, §5.2) vs `x509: certificate is valid for X, not Y` (SAN problem, §5.3).
When in doubt, pull client logs — they split the ambiguity instantly.

## 6. CONNECT authentication failures

After TLS, the client sends an HTTP CONNECT carrying the GAT. Failures here are
logged with an HTTP status code and counted in the
`twingate_gateway_client_authentication_total{code=…}` metric — a spike in non-200
codes is your early-warning signal.

| Code | Log message | Causes |
|---|---|---|
| 407 | `missing identity header in CONNECT …` | No `Proxy-Authorization` bearer — connection didn't come from a healthy Twingate client (probe, scanner, or broken client). |
| 401 | `failed to parse token with error …` | Expired GAT, wrong signing key, wrong audience (token minted for a different network), `iat` in the future (**clock skew** — check NTP on the gateway host), or unsupported algorithm. |
| 401 | `failed to verify signature` / `failed to decode client signature` | Proof-of-possession failure: the client signs material exported from the TLS session, binding the token to the connection. Verification fails if **anything terminates or re-originates TLS between client and gateway** (SSL-inspecting proxy, TLS-terminating load balancer). The gateway must be reached end-to-end; use TCP passthrough only. |
| 400 | `failed to verify CONNECT destination: …` | CONNECT target doesn't match the resource address in the token — usually a client/controller resource-definition mismatch. |
| 405 | `expected CONNECT request got …` | A plain HTTP request hit the port (probe or misconfigured tool). |

Two more behaviors worth knowing:

- **The whole authentication exchange has a 10-second deadline.** Very high latency
  or packet loss between client and gateway can fail otherwise-valid connections.
- **Connections self-terminate at GAT expiry.** The gateway arms a timer for the
  token's `exp` and closes the connection when it fires. A long-lived SSH session
  dropping at a consistent age is token expiry, not a network fault — the client
  reconnects with a fresh token.
- **JWKS is refreshed automatically at runtime**, but if the controller becomes
  unreachable after startup, token validation eventually fails once keys rotate.
  Persistent 401s plus controller egress problems go together.

Success looks like: `Authenticated connection` with `resource_type` and
`resource_address` fields, and `user` / `conn_id` attached to all subsequent lines
for that connection — use `conn_id` to trace one session end to end.

## 7. SSH resource issues

The gateway terminates the client's SSH session (identity already proven by the
GAT) and opens its *own* SSH connection to the target, authenticating with a
short-lived (default 5 min) user certificate signed by the gateway's SSH CA, with
the configured `ssh.gateway.username` as the principal.

### 7.1 `Failed to connect to upstream SSH server`

One log message, two very different causes — distinguish by the wrapped `error`:

- **TCP-level** (`connection refused`, `i/o timeout`): the gateway host cannot
  reach the target on port 22 (or the resource's port). Test from the gateway host,
  not your laptop:

  ```bash
  nc -vz -w 5 <target-address> 22
  ```

- **SSH-level** (`ssh: handshake failed: … unable to authenticate`): the target
  sshd **rejected the gateway's certificate**. There is no more specific gateway
  log for this — it is the number-one SSH sharp edge. On the target, check:

  ```bash
  # 1. sshd must trust the gateway's user CA
  sudo sshd -T | grep -i trusteduserca        # expect: trustedusercakeys /etc/ssh/gateway_ca.pub
  # and the file must contain the gateway CA public key (see gateway startup log:
  # "Using auto-generated CA for SSH authentication" / "Using manual CA…" includes ca_public_key)

  # 2. the principal must be accepted: the OS user named by ssh.gateway.username
  #    must exist on the target (or be listed via AuthorizedPrincipalsFile)
  id <gateway-username>

  # 3. watch sshd's own verdict while reproducing
  sudo journalctl -u ssh -f    # look for "certificate signature algorithm", "key not permitted", etc.
  ```

  The client experience for all of these is a generic connection failure
  (`upstream connection failed`) — the target's sshd log is where the real reason
  lives.

### 7.2 Host-key trust of the target (TOFU)

With no upstream host CA configured, the gateway pins the target's host key on
first use. If a target is rebuilt or re-keyed, subsequent connections fail with
`host key does not match known host key` (or
`address does not match known address`). The pin is held in gateway memory —
restart the gateway to re-pin after a legitimate host rebuild, and treat an
*unexplained* mismatch as a potential machine-in-the-middle before resetting it.

### 7.3 Channel and feature restrictions

The gateway deliberately rejects certain SSH features; these appear as
`SSH channel rejected` / `SSH global request rejected` warnings and are policy, not
bugs: X11 forwarding, reverse forwarding (`tcpip-forward` / `forwarded-tcpip`), and
upstream-initiated sessions. Users reporting "`-R` doesn't work through the
gateway" are hitting design, not failure.

### 7.4 Vault-backed SSH CA

If the SSH CA is Vault-backed, the gateway logs its token lifecycle. Watch for
`Failed to renew Vault token, re-attempting login` and
`Failed to login to Vault, will retry later` — while the Vault login is broken,
certificate signing fails and all new SSH sessions fail. `failed to sign
certificate with Vault` on a session means the signing role/mount is wrong or the
token lacks permissions.

## 8. Kubernetes resource issues

The gateway proxies the Kubernetes API: it authenticates to the API server with
its **own** credentials (`kubernetes.upstreams[0]` bearer token, or in-cluster
service account when no upstreams are configured) and propagates the user's
identity via impersonation headers (`Impersonate-User`, one `Impersonate-Group` per
GAT group).

### 8.1 kubectl gets `InternalError ("")` — the port-443 assumption

The gateway dials the API server at exactly the resource's address with `https://`
— meaning **port 443 when the address has no port**. The resource address field
does not accept `host:port`, and there is no gateway-side port override. Managed
clusters (EKS/GKE/AKS) serve on 443; **bare k3s/kubeadm clusters serve on 6443**
and fail with this signature: gateway TLS fine, CONNECT authenticated, then the
upstream dial fails and kubectl prints `InternalError ("")`.

Workarounds:

```bash
# (a) Quick, per-user: point kubectl at the real port
#     (a Twingate client resource re-sync will reset this)
kubectl config set-cluster <cluster-name> --server=https://<api-address>:6443

# (b) Durable, on the API server host: redirect 443 -> 6443
sudo iptables -t nat -A PREROUTING -p tcp --dport 443 -j REDIRECT --to-ports 6443
# (persist with iptables-persistent / your distro's mechanism, and open 443 in the host firewall)
```

### 8.2 Impersonation 403s

The API server rejects the **entire request** if the gateway's service account
lacks `impersonate` permission on *any* forwarded group. The GAT's group list is
resource-scoped (only groups relevant to the accessed resource) **plus** a
synthetic `twingate:authenticated`; the API server itself adds
`system:authenticated`. Your impersonation RBAC must therefore cover: every
Twingate group you map to cluster roles, `twingate:authenticated`, and
`system:authenticated` (if using a whitelist of resourceNames).

```bash
# Verify the RBAC from the cluster side (as the gateway's credentials)
kubectl auth can-i impersonate users --as=system:serviceaccount:<ns>:<sa>
# Verify what actually arrives, from a user's machine through the gateway
kubectl auth whoami    # shows Username + Groups as the API server sees them
```

### 8.3 Upstream credentials

- **Only `upstreams[0]` is consumed.** Additional entries are validated but
  ignored at runtime, and the `name` field is a label — it is never matched
  against the Twingate resource. Don't expect multi-cluster fan-out from one
  gateway config.
- Missing both `bearerToken` and `bearerTokenFile` fails validation at startup;
  a wrong `caFile` (API server presents a cert the gateway can't verify) fails at
  request time — check the gateway error log and the audit line's status code.
- Every kubectl call is audited: `API request completed` on `gateway.audit` with
  method, URL, user, and status code. This is the fastest way to see whether
  requests reach the gateway and what the upstream answered:

  ```bash
  journalctl -u twingate-gateway -o cat | grep '"gateway.audit"' | grep 'API request'
  ```

## 9. Web app resource issues

- The gateway proxies web app resources to the upstream over **plain HTTP** (the
  TLS you see is client↔gateway). Don't point it at an HTTPS-only upstream.
- Custom `webApp.headers` are templates evaluated per request with identity
  variables. **A bad template makes every request fail with HTTP 500** and an
  `API request failed` error in the audit log — if a web app breaks immediately
  after a headers change, that's the cause.

## 10. Session recording issues

Stock recording captures interactive sessions as asciicast v2 and emits them
**through the audit log stream** (`logger: gateway.audit`):

- In-progress flushes log `session recording` with the asciicast payload and an
  `asciicast_sequence_num`; the final flush logs **`session finished`**.
- Flushes happen on a size threshold (`auditLog.flushSizeThreshold`, default 1 MB)
  or interval (`auditLog.flushInterval`, default 10 min) — long-idle sessions
  produce output in bursts, not continuously.

Common failure modes:

1. **Recordings "missing"** — the pipeline is watching stdout; recordings are on
   **stderr** (§2). Fix the shipper's stream selection.
2. **Sessions never complete in a consumer** — the consumer keys completion on the
   `session finished` message; confirm it is not being filtered/truncated in the
   log pipeline. Large asciicast payloads exceeding a shipper's line-size limit
   are a classic silent killer.
3. **Durability expectations** — stock recording is exactly as durable as your log
   pipeline. If the pipeline drops lines under load, recordings are lost with
   them; treat log-pipeline reliability as part of the recording design.
4. **Kubernetes exec** — WebSocket-based `kubectl exec`/`attach` sessions are
   recorded; `kubectl cp` and `kubectl proxy` traffic is deliberately skipped.

## 11. Controller-side management gotchas

Some gateway problems can only be fixed on the controller, and (as of this
writing) **gateway management is API-only** — the admin console shows a read-only
gateway card, and CA objects are immutable (create/delete only, no update).

The one that bites during certificate rotation (§5.2): creating a new CA does not
re-bind existing gateways. The sequence that works, via the GraphQL admin API
(`https://<network>.twingate.com/api/graphql/` — **the trailing slash is
required** — with an `X-API-KEY` header):

```graphql
# 1. Find your gateway and its current CA binding
query { gateways { edges { node { id name x509CertificateAuthority { id name fingerprint } } } } }

# 2. Register the new CA (console: Settings → Certificate Authorities, or API)
mutation { x509CertificateAuthorityCreate(certificate: "<PEM>", name: "gateway-ca-2026") { ok } }

# 3. Re-bind the gateway to the new CA
mutation { gatewayUpdate(id: "<gateway-id>", x509CAId: "<new-ca-id>") { ok } }
```

Then restart a Twingate client to confirm it picked up the new anchor. Clean up
the old CA object only after all clients have rolled over.

Related: the synced kubeconfig that clients receive is controller-generated;
local edits (like the §8.1 port workaround) are reset on re-sync.

## 12. Health and metrics reference

- **Health:** `GET /healthz` over TLS on the main port (default 8443) returns
  `200 OK`, unauthenticated. Use it for LB/orchestrator probes (HTTPS mode, not
  TCP — see §5.5).
- **Metrics:** Prometheus on the metrics port (default `9090`) at `/metrics`,
  namespace `twingate_gateway_`:

| Metric | Use |
|---|---|
| `twingate_gateway_active_tcp_connections` | Current client connections |
| `twingate_gateway_tcp_connections_total{connection_category}` | Volume by category (`proxy` / `health` / `unknown` — a high `unknown` rate suggests probes/scanners) |
| `twingate_gateway_client_authentication_total{code}` | CONNECT auth outcomes — watch 401/407/400 spikes (§6) |
| `twingate_gateway_client_connection_duration_seconds{code}` | Auth latency (creeping toward 10 s = network trouble) |
| `twingate_gateway_http_requests_total{resource_type,code,…}` | Inbound K8s/web-app request outcomes |
| `twingate_gateway_api_server_requests_total{resource_type,code,…}` | **Upstream** answers — `5xx`/`code="0"` here means the problem is behind the gateway |
| `twingate_gateway_recorded_session_duration_seconds` | Recording activity |

```bash
curl -s http://localhost:9090/metrics | grep '^twingate_gateway_'
```

## 13. Command cookbook

Everything above, collected. Substitute your own addresses/paths/unit names.

```bash
## Logs (pick your platform)
journalctl -u twingate-gateway -o cat --since -1h          # systemd
docker logs --since 1h <container> 2>&1                    # docker (logs go to stderr)
kubectl logs -n <ns> deploy/<release>-gateway --since=1h   # kubernetes

## Filter
... | grep '"levelname":"error"'                           # errors
... | grep '"logger":"gateway.audit"'                      # audit + recordings
... | grep '<conn_id>'                                     # trace one session

## TLS: what the gateway serves vs what's on disk
openssl s_client -connect <gw>:8443 </dev/null 2>/dev/null | openssl x509 -noout -issuer -dates -ext subjectAltName
openssl x509 -in tls.crt -noout -text                      # full dump: SANs, CA:TRUE/FALSE, validity
openssl x509 -in tls.crt -noout -pubkey | sha256sum        # must match:
openssl pkey -in tls.key -pubout | sha256sum

## Health / controller reachability
curl -sk https://<gw>:8443/healthz -o /dev/null -w '%{http_code}\n'
curl -sS https://<network>.twingate.com/api/v1/jwk/ec | head -c 200

## SSH target checks (run on the target host)
sudo sshd -T | grep -i trusteduserca
id <gateway-username>
sudo journalctl -u ssh -f

## Kubernetes checks
kubectl auth whoami                                        # identity as seen through the gateway
kubectl auth can-i --list --as=<user> --as-group=<group>   # impersonation dry-run
nc -vz -w 5 <api-server> 6443                              # is the API server on 6443, not 443?

## Metrics
curl -s http://localhost:9090/metrics | grep '^twingate_gateway_client_authentication_total'
```
