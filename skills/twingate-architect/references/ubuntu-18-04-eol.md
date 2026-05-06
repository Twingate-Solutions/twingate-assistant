# Ubuntu 18.04 End of Life

## Summary
Ubuntu 18.04 LTS reached end of life on May 31, 2023. Twingate dropped support for Connectors and Clients running on Ubuntu 18.04 after that date. Users must migrate to a supported Ubuntu version to receive future updates and support.

## Key Information
- **EOL Date**: May 31, 2023
- Post-EOL: No support for Connectors or Clients on Ubuntu 18.04
- Future Connector/Client versions may not be compatible with Ubuntu 18.04
- Migration support window: Business and Enterprise plans had until July 31, 2023
- Existing (older) Connector and Client versions continue to function but will eventually be deprecated

## Prerequisites
- Active Twingate Business or Enterprise plan (for migration support, within window)
- Access to machines running Ubuntu 18.04

## Required Action
Upgrade all machines running Ubuntu 18.04 to a supported version:
- **Ubuntu 20.04 LTS** (recommended)
- **Ubuntu 22.04 LTS** (recommended)

## Gotchas
- Running future Connector versions on Ubuntu 18.04 is unsupported — Twingate will not debug issues
- Existing installed Connector/Client versions will keep working temporarily, but no new versions are guaranteed to install or run
- Migration support from Twingate (Business/Enterprise) expired July 31, 2023 — no extended support window remains

## Related Docs
- [Canonical Ubuntu 18.04 EOL announcement](https://ubuntu.com/blog/18-04-end-of-life)
- Twingate Connector installation docs (for Ubuntu 20.04/22.04)