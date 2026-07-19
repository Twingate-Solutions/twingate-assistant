# Headless Clients

## Page Title
Services Headless Clients

## Summary
Twingate clients (Linux and Windows) can operate in headless mode using a Service Key to access Service Resources without a GUI or user interaction. This enables automated and infrastructure-based access patterns.

## Key Information
- Headless mode supports **Linux** and **Windows** clients
- Requires a **Service Key** (not user credentials) for authentication
- **Userspace Networking Mode** available for Linux (no root/kernel module required)
- Intended for automated/non-interactive workloads

## Prerequisites
- A Twingate Service with at least one Resource assigned
- A valid Service Key generated for the Service
- Linux or Windows Twingate client installed

## Supported Configurations
| Mode | Platform |
|------|----------|
| Headless | Linux |
| Headless | Windows |
| Userspace Networking | Linux only |

## Step-by-Step
Detailed instructions are platform-specific — follow linked guides:
1. **Linux headless mode** → see Linux headless mode instructions
2. **Windows headless mode** → see Windows headless mode instructions
3. **Linux userspace networking** → see Linux userspace networking instructions

## Example Use Cases
- **CI/CD pipelines** — authenticate automated build/deploy agents to private Resources
- **AWS ECS** — run Twingate client as a sidecar or task in ECS configurations

## Gotchas
- Service Keys are distinct from user auth tokens — cannot be used interchangeably with interactive client sessions
- Userspace networking mode is Linux-only; Windows headless uses standard networking stack
- No GUI is present in headless mode — all configuration is CLI/file-based

## Related Docs
- Linux Headless Mode Instructions
- Windows Headless Mode Instructions
- Linux Userspace Networking Instructions
- CI/CD Configurations
- AWS ECS Configurations
- Services & Service Keys (concept docs)