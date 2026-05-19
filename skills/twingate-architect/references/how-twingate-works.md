# How Twingate Works

## Page Title
How Twingate Works — Architecture Overview

## Summary
Twingate uses four components (Controller, Client, Connector, Relay) to enforce zero-trust access to private resources. No single component independently authorizes traffic; decisions require confirmation across multiple components. Authentication is always delegated to a third-party Identity Provider.

## Key Information

- **Four components**: Controller (coordination), Client (user device proxy), Connector (deployed behind firewall), Relay (connection broker)
- **No single point of authorization**: Access decisions require intersection of Client ACL + Connector ACL
- **Controller is data-plane agnostic**: Only component that never touches actual data flow
- **Connector deploys behind firewall**: Maintains outbound connections to Relays; never requires inbound firewall rules
- **Relay = TURN server equivalent**: No data terminated or stored; no network-identifiable information retained
- **DNS resolution is local to remote network**: DNS queries for resources forwarded to Connector for local resolution
- **Transparent proxy**: No application configuration needed on user devices for TCP/UDP traffic
- **P2P preferred**: Twingate attempts peer-to-peer Client↔Connector first; Relay used as fallback

## Component Responsibilities

| Component | Key Role |
|-----------|----------|
| Controller | Config storage, ACL generation, Connector registration, IdP delegation |
| Client | Auth proxy, ACL enforcement, DNS proxying, TLS tunnel initiation |
| Connector | ACL verification, local DNS resolution, traffic forwarding to resources |
| Relay | Connector registration point, anonymous Client↔Connector matchmaking via hash ID |

## Authorization Flow Logic

1. Controller generates **Client ACL** (resources user can access)
2. Controller generates **Connector ACL** (resources Connector can forward to)
3. Traffic only flows to resources in the **intersection** of both ACLs
4. Client establishes **certificate-pinned TLS tunnel** to Connector via anonymous Connector ID
5. Connector verifies: TLS integrity + Client signature + Client ACL claim validity

## Gotchas

- **Connector ID is anonymized**: Only a hash-based ID is shared with Clients/Relays — no private network info exposed
- **Connectors require one-time Controller authorization** to deploy; cannot self-register
- **ACL signatures**: Client ACLs are signed by Controller and verified by Connector — tampering is detectable
- **User must authenticate before accessing any resource**: No unauthenticated access possible even with valid network path
- **FQDN resources**: DNS resolution happens at the Connector (remote network), not the Client device

## Prerequisites
- Identity Provider configured (or social identity)
- Connector deployed inside target private network
- Client installed on user devices
- Resources and access policies defined in Admin console

## Related Docs
- Connector deployment guide
- Client installation guide  
- Identity Provider configuration
- Relay architecture detail
- Connection flow walkthrough (referenced as "next article in this guide")