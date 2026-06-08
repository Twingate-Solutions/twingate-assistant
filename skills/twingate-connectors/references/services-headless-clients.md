# Headless Clients

## Summary
Twingate clients (Linux and Windows) can operate in headless mode using a Service Key to access Service Resources without a GUI. This enables automated/non-interactive environments to authenticate and connect to protected resources.

## Key Information
- Headless mode supports both Windows and Linux Twingate clients
- Requires a Service Key (not user credentials) for authentication
- Linux client supports an additional Userspace Networking Mode
- Designed for automated environments (CI/CD pipelines, containers, etc.)

## Prerequisites
- A configured Twingate Service with an associated Service Key
- Windows or Linux Twingate client installed
- Access to Service Resources defined in Twingate admin

## Available Modes

| Mode | Platform |
|------|----------|
| Standard headless | Linux, Windows |
| Userspace networking | Linux only |

## Use Cases
- CI/CD pipeline configurations (automated builds/deployments needing private resource access)
- AWS ECS container configurations
- Any non-interactive/automated workload requiring access to Twingate-protected resources

## Related Docs
- Linux headless mode instructions
- Windows headless mode instructions
- Linux userspace networking instructions
- CI/CD Configurations
- AWS ECS Configurations

## Gotchas
- Service Keys are distinct from user credentials — ensure the correct key type is provisioned
- Userspace networking mode is Linux-only; not available on Windows headless deployments
- Headless mode is tied to Services, not individual user accounts — permissions are scoped to what the Service is granted access to