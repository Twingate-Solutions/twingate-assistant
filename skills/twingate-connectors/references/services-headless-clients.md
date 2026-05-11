# Headless Clients

## Summary
Twingate clients (Windows and Linux) can operate in headless mode using a Service Key to access Service Resources without a GUI. This enables automated and server-side use cases such as CI/CD pipelines and container deployments.

## Key Information
- Headless mode uses **Service Keys** (not user credentials) for authentication
- Both **Windows** and **Linux** clients support headless mode
- Linux client also supports **userspace networking mode** (alternative to kernel networking)
- Designed for automated/non-interactive environments

## Prerequisites
- A configured Twingate Service with an associated Service Key
- Windows or Linux Twingate client installed
- Access to Service Key credentials

## Platform-Specific Instructions
| Platform | Mode | Reference |
|----------|------|-----------|
| Linux | Headless | Linux headless mode instructions |
| Windows | Headless | Windows headless mode instructions |
| Linux | Userspace networking | Linux userspace networking instructions |

## Example Use Cases
- **CI/CD pipelines** — automated build/deploy systems accessing private Resources
- **AWS ECS** — containerized workloads using Service Keys for Resource access

## Gotchas
- Service Keys are required; standard user auth tokens do not apply in this context
- Userspace networking mode is Linux-only — use when kernel-level networking is unavailable (e.g., unprivileged containers)
- No GUI is presented; all configuration is done via CLI flags or config files

## Related Docs
- Linux headless mode instructions
- Windows headless mode instructions
- Linux userspace networking instructions
- CI/CD Configurations
- AWS ECS Configurations
- Twingate Services (Service Key generation)