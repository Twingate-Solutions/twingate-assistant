# Headless Clients

## Page Title
Services: Headless Clients

## Summary
Headless clients allow Twingate's Windows or Linux clients to operate without a GUI using a Service Key to authenticate and access Service Resources. This mode is suitable for automated and server environments where interactive login is not possible.

## Key Information
- Headless mode is available for both **Windows** and **Linux** clients
- Authentication uses a **Service Key** (not user credentials)
- **Userspace Networking Mode** available for Linux (alternative networking stack)
- Designed for non-interactive/automated environments

## Prerequisites
- A Twingate Service Key configured for the target Service
- Windows or Linux client installed
- Access to Service Resources defined in Twingate admin

## Platform-Specific Instructions
| Platform | Mode | Reference |
|----------|------|-----------|
| Linux | Headless | Linux headless mode instructions |
| Windows | Headless | Windows headless mode instructions |
| Linux | Userspace Networking | Linux userspace networking instructions |

## Example Use Cases
- **CI/CD Configurations** — Running Twingate client in pipelines to access private Resources during build/test/deploy
- **AWS ECS Configurations** — Running client as a sidecar or task in ECS to enable container access to private Resources

## Gotchas
- Headless mode requires a **Service Key**, not a standard user auth token — ensure the correct key type is provisioned
- Userspace networking mode on Linux is an alternative for environments where kernel-level networking (TUN device) is restricted (e.g., unprivileged containers)
- GUI-based auth flows will not work in headless mode; the Service Key must be pre-configured

## Related Docs
- Linux headless mode instructions
- Windows headless mode instructions
- Linux userspace networking instructions
- CI/CD Configurations
- AWS ECS Configurations
- Twingate Services (Service Key provisioning)