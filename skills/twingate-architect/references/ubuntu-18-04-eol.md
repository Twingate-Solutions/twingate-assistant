# Ubuntu 18.04 End of Life

## Summary
Ubuntu 18.04 LTS reached end of life on May 31, 2023. Twingate dropped support for Connectors and Clients on Ubuntu 18.04 after that date. Users must migrate to a supported Ubuntu version to receive future updates and support.

## Key Information
- **EOL date**: May 31, 2023
- **Migration support window**: Business and Enterprise plans received migration support until July 31, 2023
- **Impact**: No support for Connectors or Clients on Ubuntu 18.04 after EOL; future versions may not run on Ubuntu 18.04
- **Existing installations**: Continue working but will eventually be deprecated

## Prerequisites
- Active Twingate Business or Enterprise plan (for migration support during transition window)

## Required Action
Upgrade all machines running Ubuntu 18.04 to a supported version:
- **Ubuntu 20.04 LTS** (recommended)
- **Ubuntu 22.04 LTS** (recommended)

## Gotchas
- Future Connector versions **may not run** on Ubuntu 18.04 — no workaround supported
- Existing pinned Connector/Client versions continue functioning temporarily but will be deprecated
- Migration support window (to July 31, 2023) has now passed; no extended support available
- Free/Teams plan users did not qualify for the extended migration support window

## Related Docs
- [Twingate Connector installation](https://www.twingate.com/docs/connectors)
- [Ubuntu 18.04 EOL — Canonical official notice](https://ubuntu.com/blog/ubuntu-18-04-eol)