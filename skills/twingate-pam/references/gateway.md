---
source: https://www.twingate.com/docs/gateway
type: docs
fetched: 2026-11-22
source_version: ddd9c321ecac06166f5c23e76bb936097817432359decc85a1edc9f94728ce94
trust: official
---

# Twingate Gateway

## Summary
The Twingate Gateway is an open-source Layer 7 reverse proxy behind every Privileged Access Management (PAM) Resource. It sits between protocol clients (`kubectl`, `ssh`, browsers) and the upstream service, authenticates the Twingate user via a Gateway Access Token (GAT), and signs in to the upstream service on the user's behalf. This page covers behavior shared across protocols.

## Key Information
- A PAM Resource has two addresses: **Address** (upstream service as reached by the Gateway, e.g. `10.0.0.1`) and **Gateway address** (Gateway as reached by the Connector, e.g. `gateway.int`).
- With the Twingate Operator, the Gateway address resolves from the Gateway's `Service`: the load balancer address for `LoadBalancer` services, otherwise the in-cluster DNS name.
- **Connection flow:**
  1. The protocol client opens TCP to the Resource address; the Twingate Client tunnels it to the Connector.
  2. The Connector sees the Resource has a Gateway and forwards to the Gateway address.
  3. The Twingate Client opens outer TLS to the Gateway.
  4. The Client sends HTTP `CONNECT` with a GAT; the Gateway validates it.
  5. Depending on protocol, an inner secure layer (TLS or SSH) opens inside the same TCP connection.
  6. The Gateway forwards requests upstream and returns responses.
- **GAT:** a signed JWT scoped to user, device, and Resource, issued by the Controller after all Security Policies are satisfied (MFA, device trust, location, JIT access).
- **Upstream authentication:**
  - Kubernetes: service account token plus impersonation headers carrying the user's identity.
  - SSH: short-lived SSH certificate signed by an SSH CA.
  - Web App: identity headers injected per request (e.g. the signed token).
- The user's device holds no upstream credentials.
- **Synced client trust config** (contains no tokens, keys, or passwords):
  - Kubernetes: `~/.kube/config` with context and CA cert per cluster.
  - SSH: `~/.ssh/known_hosts` with the Gateway's SSH host CA.
  - Web App: none.
- **Deployment:** in a Kubernetes cluster (Twingate Kubernetes Operator or Gateway Helm chart), or on a VM as a Docker container or release binary.
- Each Gateway belongs to one Remote Network and can serve multiple Resources in it.
- The Gateway's only outbound connection to Twingate is fetching public keys to verify GATs. Audit logs and session recordings stay in your environment.

## Prerequisites
- A PAM Resource and a Remote Network with Connectors.
- An X.509 CA-signed certificate for the Gateway covering every Resource address and alias it serves.

## Configuration Values
- `twingateOperator.gateway.address`: available from Gateway 2.1; set it when Connectors reach the Gateway by another route than the Service-derived address.

## Gotchas
- Every Connector in the Remote Network must be able to reach the Gateway address, since any can carry a connection.
- The Client validates the Gateway certificate against both the registered X.509 CA and the dialed hostname, so missing aliases cause failures.

## Related Docs
- Privileged Access Management (https://www.twingate.com/docs/privileged-access-management)
- Privileged Access for Kubernetes (https://www.twingate.com/docs/kubernetes-access)
- Privileged Access for SSH (https://www.twingate.com/docs/ssh-privileged-access-overview)
- Privileged Access for Web Apps (https://www.twingate.com/docs/web-app-access)
- Gateway TLS Certificates (https://www.twingate.com/docs/gateway-tls-certificates)
- Session Recordings (https://www.twingate.com/docs/gateway-session-recordings)
- Gateway Monitoring (https://www.twingate.com/docs/gateway-monitoring)
- Upgrading the Gateway (https://www.twingate.com/docs/gateway-upgrades)
- Twingate Kubernetes Operator (https://github.com/Twingate/kubernetes-operator)
- Gateway Helm chart (https://github.com/Twingate/gateway/pkgs/container/helmcharts%2Fgateway)
- Gateway release binaries (https://github.com/Twingate/gateway/releases)