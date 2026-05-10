# Twingate in GitHub Codespaces

## Summary
Twingate can be run inside GitHub Codespaces to allow cloud-based development environments to access Twingate-protected resources. The integration is maintained as an open source project.

## Key Information
- Enables access to Twingate-secured resources from within GitHub Codespaces environments
- Works via both browser-based Codespaces and VS Code desktop client
- Implementation details and scripts are in Twingate's open source repository

## Prerequisites
- GitHub Codespaces access
- Twingate account with appropriate network/resource configuration
- VS Code (optional, for desktop-based Codespaces)

## Implementation
Refer to the [Twingate Open Source Repository](https://github.com/Twingate) for:
- Devcontainer configuration files
- Setup scripts
- Feature definitions for Codespaces integration

## Gotchas
- Documentation is sparse on this page — primary implementation guidance lives in the external OSS repo, not the docs page
- Twingate client must be configured within the Codespace environment (not the host machine)

## Related Docs
- GitHub Codespaces official documentation
- Twingate Open Source Repository (linked from docs page)
- Twingate network/resource configuration docs

---
*Note: This documentation page has minimal content — full implementation details require consulting the linked open source repository directly.*