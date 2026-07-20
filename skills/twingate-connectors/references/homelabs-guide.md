# Twingate Home Labs Guide

## Page Title
Home Labs Guide – Twingate Self-Hosted Remote Access Setup

## Summary
Twingate enables remote access to home lab services without port forwarding, dynamic DNS, or a VPN server. A Connector deployed on your home lab platform creates an encrypted tunnel, and Resources define which local services are accessible. Setup takes approximately 15 minutes.

## Key Information
- **Free Starter plan**: Up to 5 users, 10 Remote Networks – sufficient for most home labs
- Connector runs as a container/add-on on most platforms; Docker Compose works universally
- Resources are defined by local IP + port (e.g., `192.168.1.50:8123`)
- No inbound firewall rules or port forwarding required; outbound port 443 must be open

## Prerequisites
- Twingate account (twingate.com, Starter plan is free)
- Home lab platform running one of the supported systems or Docker
- Internet access from home network with outbound port 443 unblocked

## Step-by-Step Setup
1. Sign up at twingate.com
2. Create a **Remote Network** in Admin Console (represents your home network)
3. Deploy a **Connector** on your platform (native add-on or Docker Compose)
4. Create **Resources** using local IP:port for each service
5. Install **Twingate Client** on remote device, sign in – Resources appear automatically

## Supported Platforms

| Platform | Deployment Method |
|----------|------------------|
| Home Assistant | Add-on Store |
| Proxmox | Helper script |
| Unraid | Community Apps store |
| ZimaOS | Native guide |
| CasaOS | Connector install |
| Synology DSM 7 | Docker package |
| QNAP | Container Station |
| TrueNAS SCALE | Container |

## Gotchas
- **Connector offline**: Verify container/add-on is running; check outbound port 443 is not blocked
- **Can't reach service**: Confirm IP:port in Resource definition matches what the service actually listens on; verify reachability from local network first
- **Slow performance**: Bottleneck is typically home network upload speed; Twingate uses peer-to-peer when possible
- **DNS issues**: Use IP addresses instead of local hostnames (e.g., `nas.local`) to avoid Connector DNS resolution failures
- **Home plan** required if you exceed 5 users or 10 Remote Networks

## Configuration Values
- Resource format: `<local-ip>:<port>` (e.g., `192.168.1.100:32400`)
- Required outbound port: `443`
- Starter plan limits: 5 users, 10 Remote Networks

## Related Docs
- Docker Compose Connector guide
- Twingate Troubleshooting Guide
- Ubiquiti Connector Guide
- Headless Client Gateway for IoT
- Self-Hosted VPN with Exit Networks
- Twingate community (Reddit)