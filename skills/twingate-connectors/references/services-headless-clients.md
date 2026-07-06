# Headless Clients

## Page Title
Headless Clients (Twingate Services)

## Summary
Headless clients allow Twingate Service Keys to access Service Resources without a GUI, using either Windows or Linux clients in headless mode. This enables automated/non-interactive workloads to authenticate via Service Accounts rather than user credentials.

## Key Information
- Supported platforms: Windows and Linux
- Authentication method: Service Key (not user credentials)
- Linux supports an additional **Userspace Networking Mode**
- Intended for automated workloads, not interactive users

## Prerequisites
- A configured Twingate Service Account with a Service Key
- Access to Windows or Linux client binaries
- Resources assigned to the Service in Twingate Admin Console

## Step-by-Step
This page is an index/overview — see linked pages for detailed instructions:
1. **Linux headless mode** → Follow Linux headless mode instructions
2. **Windows headless mode** → Follow Windows headless mode instructions
3. **Linux userspace networking** → Alternative networking mode for Linux (no kernel module required)

## Configuration Values
Not specified on this page — see platform-specific pages for flags/env vars.

## Example Use Cases
- **CI/CD Configurations** — Running Twingate client in pipelines (e.g., GitHub Actions, GitLab CI)
- **AWS ECS Configurations** — Running headless client as a sidecar or task in ECS

## Gotchas
- Headless mode requires a **Service Key**, not a user token — ensure correct credential type is used
- Linux userspace networking mode is a distinct configuration from standard headless mode (useful in environments where kernel-level networking is restricted, e.g., containers)

## Related Docs
- Linux Headless Mode Instructions
- Windows Headless Mode Instructions
- Linux Userspace Networking Instructions
- CI/CD Configurations
- AWS ECS Configurations
- Twingate Services / Service Accounts (parent concept)