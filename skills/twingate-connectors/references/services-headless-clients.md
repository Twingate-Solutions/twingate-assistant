# Headless Clients

## Summary
Twingate clients (Windows and Linux) can operate in headless mode using a Service Key to access Service Resources without a GUI or user interaction. This enables automated/non-interactive deployments such as CI/CD pipelines and containerized environments.

## Key Information
- Headless mode uses **Service Keys** (not user credentials) for authentication
- Both **Windows** and **Linux** clients support headless mode
- Linux supports an additional **userspace networking mode**
- Designed for automated, non-interactive workloads

## Prerequisites
- A configured Twingate Service with an associated Service Key
- Twingate Windows or Linux client installed
- Service Key credentials available to the deployment environment

## Platform-Specific Instructions
- **Linux headless mode**: See Linux headless mode instructions
- **Windows headless mode**: See Windows headless mode instructions
- **Linux userspace networking**: Alternative networking mode for Linux (see linked docs)

## Example Use Cases
- **CI/CD Configurations**: Automated pipeline access to protected Resources
- **AWS ECS Configurations**: Containerized task access to internal Resources

## Gotchas
- Service Keys are distinct from user credentials — ensure the correct key type is used
- Userspace networking mode is Linux-only; not available on Windows headless deployments
- Service must be pre-configured with appropriate Resource access before deploying headless clients

## Related Docs
- Linux Headless Mode Instructions
- Windows Headless Mode Instructions
- Linux Userspace Networking Instructions
- CI/CD Configurations
- AWS ECS Configurations
- Twingate Services (Service Key generation)