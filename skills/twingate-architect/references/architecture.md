## Page Title
Twingate Architecture Overview

## Summary
Twingate implements Zero Trust Networking — every access attempt is authenticated and authorized regardless of whether the user is on a public or private network. The architecture relies on four components: Controller, Clients, Connectors, and Relay infrastructure. Users never gain broad network access; only specific authorized resources are reachable.

## Key Information
- **Zero Trust model**: network is assumed untrusted; every resource access is verified per-request
- **Four components**:
  - **Controller** — cloud-hosted control plane; manages auth, policy, and session orchestration
  - **Client** — end-user software (desktop/mobile); intercepts DNS and routes resource traffic
  - **Connector** — lightweight process deployed in the private network; proxies traffic to resources
  - **Relay** — Twingate-hosted fallback infrastructure when peer-to-peer is unavailable
- **DNS interception**: Client transparently intercepts DNS queries for Twingate resources; private DNS addresses resolve without exposing the DNS resolver
- **Peer-to-peer by default**: direct Client↔Connector connections without open inbound ports; relay used only as fallback
- **No network-level access**: users reach only the specific resources they are authorized for, not the broader network

## Prerequisites
- Twingate account (Controller is SaaS — no self-hosting required)
- Connector deployed in target private network
- Client installed on end-user device

## Step-by-Step
Not applicable — this is a concept/orientation page. See `/docs/how-twingate-works` for the detailed component walkthrough.

## Configuration Values
None on this page — see individual component docs for deployment parameters.

## Gotchas
- This page is an architecture index, not a deployment guide — it links to sub-documents rather than providing step-by-step instructions
- Peer-to-peer communication requires no extra configuration; it is on by default for all customers
- "Zero trust" here refers to the network access model, not a vendor product category

## Related Docs

- `/docs/how-twingate-works` — detailed component communication flow
- `/docs/how-dns-works-with-twingate` — DNS interception deep dive
- `/docs/peer-to-peer-communication-in-twingate` — peer-to-peer connection mechanics
- `/docs/how-nat-traversal-works` — relay fallback behavior
