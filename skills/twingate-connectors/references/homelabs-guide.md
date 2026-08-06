---
source: https://www.twingate.com/docs/homelabs-guide
type: docs
fetched: 2026-08-05
source_version: 6e96c424159bd9fb3e6649afe98e5fa940b1034776af4d8da927a57938e44336
---

# Twingate Home Labs Guide

## Page Title
Home Labs – Twingate Setup for Self-Hosted Services

## Summary
Twingate enables remote access to home lab services without port forwarding, dynamic DNS, or a VPN server. A Connector deployed on your home network creates a secure tunnel, and Resources are defined by local IP/port. Setup takes approximately 15 minutes on any supported platform.

## Key Information
- **Free Starter plan**: Up to 5 users, 10 Remote Networks — sufficient for most home labs
- **Connector deployment**: Native add-ons available for major platforms; Docker Compose works universally
- **Resources**: Defined by local IP + port (e.g., `192.168.1.50:8123`)
- **Client**: Install on phone/laptop/tablet; Resources appear automatically after sign-in
- **Peer-to-peer connections** used when possible to minimize latency

## Prerequisites
- Twingate account (free at twingate.com)
- Home lab platform running one of the supported systems or Docker
- Internet access on the home network (outbound port 443 must be open)

## Step-by-Step Setup
1. Sign up at twingate.com (Starter plan)
2. Create a **Remote Network** in the Admin Console
3. Deploy a **Connector** on your platform (see platform-specific guides below)
4. Create **Resources** using local IP:port for each service
5. Install **Twingate Client** on remote devices, sign in

## Supported Platforms

| Platform | Deployment Method |
|---|---|
| Home Assistant | Add-on Store |
| Proxmox | Helper script |
| Unraid | Community Apps store |
| ZimaOS | Native guide |
| CasaOS | Native guide |
| Synology DSM 7 | Docker package |
| QNAP | Container Station |
| TrueNAS SCALE | Container |

**Fallback**: Docker Compose guide works on any Docker-capable host.

## Configuration Values
- Resource format: `<local-ip>:<port>` (e.g., `192.168.1.100:32400`)
- Outbound port required: **443**

## Gotchas
- **Connector offline**: Check container/add-on is running; verify outbound port 443 is not blocked
- **Can't reach service**: Confirm IP/port match what the service actually listens on; validate local reachability first
- **DNS issues**: Local hostnames (`.local`) may fail to resolve through the Connector — use IP addresses directly to avoid resolution problems
- **Slow performance**: Bottleneck is typically home network **upload speed**, not Twingate overhead

## Related Docs
- [Docker Compose Connector Guide](https://www.twingate.com/docs/)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/)
- Protect Your Home Lab (Full Walkthrough)
- Ubiquiti Connector Guide
- Headless Client Gateway for IoT
- Self-Hosted VPN with Exit Networks
- [Twingate Reddit Community](https://reddit.com/r/twingate)