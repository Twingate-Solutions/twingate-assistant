# Twingate Home Labs Guide

## Page Title
Home Labs - Twingate Setup for Self-Hosted Services

## Summary
Guide for deploying Twingate on home lab platforms to enable remote access to self-hosted services without port forwarding, dynamic DNS, or a VPN server. Covers major home server platforms and NAS devices with platform-specific connector deployment methods. Setup takes approximately 15 minutes.

## Key Information
- **Free Starter plan**: Up to 5 users, 10 Remote Networks — sufficient for most home labs
- Connector runs as a container/add-on on the home lab host
- Resources are defined by local IP:port (e.g., `192.168.1.50:8123`)
- Peer-to-peer connections used when possible to minimize latency
- Home upload speed is typically the performance bottleneck

## Prerequisites
- Twingate account (free at twingate.com)
- Home lab platform running one of: Home Assistant, Proxmox, Unraid, ZimaOS, CasaOS, Synology DSM 7, QNAP, TrueNAS SCALE, or any Docker-capable host
- Outbound internet access on port 443

## Step-by-Step Setup
1. Sign up at twingate.com (Starter plan)
2. Create a **Remote Network** in Admin Console representing your home network
3. Deploy a **Connector** on your home lab (platform-specific add-on, or Docker Compose)
4. Create **Resources** for each service (local IP:port)
5. Install **Twingate Client** on remote device, sign in — Resources appear automatically

## Platform-Specific Connector Deployment

| Platform | Method |
|----------|--------|
| Home Assistant | Add-on Store |
| Proxmox | Helper script |
| Unraid | Community Apps store |
| ZimaOS | Native guide |
| CasaOS | Native guide |
| Synology (DSM 7) | Docker package |
| QNAP | Container Station |
| TrueNAS SCALE | Container |
| Generic | Docker Compose |

## Gotchas
- **DNS**: Use IP addresses directly instead of local DNS names (e.g., `nas.local`) to avoid resolution failures through the Connector
- **Connector offline**: Check outbound port 443 is not blocked; verify container/add-on is actually running
- **Resource unreachable**: Confirm IP:port matches what the service actually listens on — test from local network first
- **Performance**: Home upload bandwidth is the limiting factor, not Twingate itself

## Related Docs
- Docker Compose Connector guide (fallback for any Docker host)
- Twingate Troubleshooting Guide
- Protect Your Home Lab (Full Walkthrough)
- Headless Client Gateway for IoT
- Self-Hosted VPN with Exit Networks