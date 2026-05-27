# Headless Clients

## Summary
Twingate clients (Windows and Linux) can operate in headless mode using a Service Key to access Service Resources without a GUI. This enables automated/non-interactive environments to authenticate and connect to protected resources.

## Key Information
- Headless mode uses **Service Keys** (not user credentials) for authentication
- Both **Windows** and **Linux** clients support headless mode
- Linux client also supports **userspace networking mode** (alternative to kernel-level networking)
- Designed for automated environments: CI/CD pipelines, containers, servers

## Prerequisites
- A Service Key generated from the Twingate Admin Console
- A configured Service with associated Resources
- Twingate Windows or Linux client installed

## Platform-Specific Instructions
| Platform | Mode | Reference |
|----------|------|-----------|
| Linux | Headless | Linux headless mode instructions |
| Windows | Headless | Windows headless mode instructions |
| Linux | Userspace networking | Linux userspace networking instructions |

## Example Use Cases
- **CI/CD Configurations** – Running Twingate client in pipeline environments (GitHub Actions, GitLab CI, etc.)
- **AWS ECS Configurations** – Running client as a sidecar or task in containerized AWS workloads

## Gotchas
- Headless mode requires a **Service Key**, not a user login token — ensure the correct credential type is provisioned
- Userspace networking mode (Linux) is an alternative when kernel/TUN device access is restricted (e.g., unprivileged containers)
- Service Keys must be associated with a Service that has explicit Resource access configured in the Admin Console

## Related Docs
- Linux headless mode instructions
- Windows headless mode instructions
- Linux userspace networking instructions
- CI/CD Configurations
- AWS ECS Configurations
- Twingate Services (Admin Console configuration)