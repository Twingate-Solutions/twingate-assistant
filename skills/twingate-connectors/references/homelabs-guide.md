---
source: https://www.twingate.com/docs/homelabs-guide
type: docs
fetched: 2026-08-14
source_version: dcbd672b2c57f42cc25c30580308ef0653bc7271b9227d9c8246542ba34ccca5
---

# Twingate Home Labs Guide

## Page Title
Home Labs – Twingate Setup Guide

## Summary
Step-by-step guide for deploying Twingate on common home lab platforms to enable remote access to self-hosted services. Eliminates the need for port forwarding, dynamic DNS, or a self-managed VPN server. Covers home server platforms, NAS devices, and troubleshooting.

## Key Information
- **Setup time**: ~15 minutes regardless of platform
- **Free Starter plan**: Up to 5 users, 10 Remote Networks — sufficient for most home labs
- **Core components**: Remote Network, Connector (deployed on home lab), Resources (services by IP:port), Client (on remote device)
- **Connector deployment**: Native add-ons/containers available per platform; Docker Compose works universally

## Prerequisites
- Twingate account (free at twingate.com)
- Home lab platform running one of the supported systems (or Docker)
- Internet access on home network with outbound port 443 open

## Step-by-Step Setup
1. Sign up for free Twingate account
2. Create a **Remote Network** in Admin Console
3. Deploy a **Connector** on home lab (platform-specific method)
4. Create **Resources** — specify each service by local IP:port (e.g., `192.168.1.50:8123`)
5. Install **Twingate Client** on remote device, sign in — Resources appear automatically

## Platform-Specific Connector Deployment

| Platform | Method |
|---|---|
| Home Assistant | Add-on Store |
| Proxmox | Helper script |
| Unraid | Community Apps store |
| ZimaOS | Platform guide |
| CasaOS | Platform guide |
| Synology (DSM 7) | Docker package |
| QNAP | Container Station |
| TrueNAS SCALE | Container |

## Configuration Values
- Resources defined as `<local-ip>:<port>` (e.g., `192.168.1.100:32400` for Plex)
- Connector requires outbound **port 443** (no inbound ports needed)

## Gotchas
- **Offline Connector**: Verify container/add-on is running; check outbound port 443 is not blocked
- **Wrong IP:port**: Confirm the Resource matches what the service actually listens on; test reachability from local network first
- **DNS issues**: Local DNS names (e.g., `nas.local`) may not resolve correctly — use IP addresses directly to avoid resolution failures
- **Slow performance**: Bottleneck is typically home network upload speed; Twingate uses peer-to-peer when possible to minimize latency

## Related Docs
- Docker Compose Connector guide (fallback for any Docker-capable host)
- Twingate Troubleshooting Guide
- Protect Your Home Lab (full walkthrough)
- Headless Client Gateway for IoT
- Self-Hosted VPN with Exit Networks