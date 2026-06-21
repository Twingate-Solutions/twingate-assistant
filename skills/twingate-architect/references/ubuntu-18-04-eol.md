# Ubuntu 18.04 End of Life

## Summary
Ubuntu 18.04 LTS reached end of life on May 31, 2023. Twingate dropped support for Connectors and Clients on Ubuntu 18.04 after that date. Users must migrate to a supported Ubuntu version to receive future updates and support.

## Key Information
- **EOL date**: May 31, 2023
- **Migration support window**: Business and Enterprise plans received migration support until July 31, 2023
- **Impact**: No support for Connectors or Clients on Ubuntu 18.04; future versions may not run on 18.04
- **Existing installs**: Continue working but will eventually be deprecated

## Prerequisites
- Active Twingate Business or Enterprise plan (for migration support, now expired)

## Required Action
Upgrade all machines running Ubuntu 18.04 to:
- **Ubuntu 20.04 LTS** (recommended)
- **Ubuntu 22.04 LTS** (recommended)

## Gotchas
- Future Connector versions **may silently fail** on Ubuntu 18.04 — no guarantee of error messaging
- Twingate will provide **zero support** for issues on Ubuntu 18.04 post-EOL
- Existing Connector/Client versions continue functioning temporarily but have no defined deprecation timeline
- Migration support window (to July 31, 2023) has now passed — no extended support available

## Related Docs
- [Canonical Ubuntu 18.04 EOL information](https://ubuntu.com)
- Twingate Connector installation docs (for supported OS versions)
- Twingate Client installation docs