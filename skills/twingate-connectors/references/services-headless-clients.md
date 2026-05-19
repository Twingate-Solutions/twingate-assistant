# Headless Clients

## Summary
Twingate clients (Windows and Linux) can operate in headless mode using a Service Key to access Service Resources without user interaction. This enables automated and non-interactive environments to authenticate with Twingate.

## Key Information
- Headless mode uses **Service Keys** (not user credentials) for authentication
- Both **Windows** and **Linux** clients support headless mode
- Linux supports an additional **userspace networking mode**
- Designed for automated/non-interactive workloads (CI/CD, containers, etc.)

## Prerequisites
- A configured Twingate Service with an associated Service Key
- Windows or Linux Twingate client installed
- Access to Service Resources configured in Twingate admin

## Platform-Specific Instructions

| Platform | Mode | Reference |
|----------|------|-----------|
| Linux | Headless | Linux headless mode instructions |
| Windows | Headless | Windows headless mode instructions |
| Linux | Userspace networking | Linux userspace networking instructions |

## Example Use Cases
- **CI/CD pipelines** — run client headlessly in pipeline steps to access private resources
- **AWS ECS** — run client as sidecar or task to enable container access to Twingate Resources

## Gotchas
- Service Keys are distinct from user credentials — ensure the Service is granted access to the required Resources in the admin console before deploying
- Userspace networking mode (Linux only) — relevant when the client cannot use kernel-level networking (e.g., unprivileged containers)
- No mention of macOS headless support — appears limited to Windows and Linux

## Related Docs
- Linux headless mode instructions
- Windows headless mode instructions
- Linux userspace networking instructions
- CI/CD Configurations
- AWS ECS Configurations
- Twingate Services (Service Key generation)