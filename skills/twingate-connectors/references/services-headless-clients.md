---
source: https://www.twingate.com/docs/services-headless-clients
type: docs
fetched: 2026-08-14
source_version: 052c52be5dd32e6337d925d2d4e93a5fc77c1b697e53387de0ddb438832ce7c2
---

# Headless Clients

## Page Title
Headless Clients (Twingate Services)

## Summary
Twingate clients (Linux and Windows) can operate in headless mode using a Service Key to access Service Resources without a GUI or user authentication. This enables automated/non-interactive workloads to connect to Twingate-protected resources.

## Key Information
- Headless mode is available for both **Windows** and **Linux** Twingate clients
- Requires a **Service Key** (not user credentials) for authentication
- **Userspace Networking Mode** available for Linux (useful in environments without root/kernel module access)
- Designed for automated workloads, not interactive user sessions

## Prerequisites
- A Twingate Service and Service Key configured in the admin console
- Twingate Linux or Windows client installed
- Resources assigned to the Service

## Available Modes
| Mode | Platform | Use Case |
|------|----------|----------|
| Headless | Linux | Automated Linux workloads |
| Headless | Windows | Automated Windows workloads |
| Userspace Networking | Linux | Environments without kernel module access |

## Step-by-Step
Refer to platform-specific documentation:
1. **Linux headless**: See Linux headless mode instructions
2. **Windows headless**: See Windows headless mode instructions
3. **Linux userspace networking**: See Linux userspace networking instructions

## Example Use Cases
- **CI/CD Configurations** — Running Twingate client in pipeline environments (GitHub Actions, GitLab CI, etc.)
- **AWS ECS Configurations** — Running Twingate client as a sidecar or task in ECS

## Gotchas
- Service Keys are distinct from user credentials — must be generated specifically for Services in the admin console
- Userspace networking mode exists specifically for environments where the standard kernel-level networking isn't available (e.g., containers without elevated privileges)

## Related Docs
- Linux headless mode instructions
- Windows headless mode instructions
- Linux userspace networking instructions
- CI/CD Configurations
- AWS ECS Configurations
- Twingate Services (Service Key generation)