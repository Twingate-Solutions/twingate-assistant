---
source: https://www.twingate.com/docs/ubuntu-18-04-eol
type: docs
fetched: 2026-08-14
source_version: be6f51ae8f55f1f66f7d065ecf262e6bcef77ec0482131a763c6c123f7dd6d16
---

# Ubuntu 18.04 End of Life

## Summary
Ubuntu 18.04 LTS reached end of life on May 31, 2023. Twingate dropped support for Connectors and Clients running on Ubuntu 18.04 after that date. Users must migrate to a supported Ubuntu version to receive future updates and support.

## Key Information
- **EOL Date:** May 31, 2023
- **Support cutoff:** No support for Connectors or Clients on Ubuntu 18.04 after May 31, 2023
- **Migration support window:** Business and Enterprise plan users received migration support until July 31, 2023
- **Existing installations:** Continue functioning but will eventually be deprecated
- **Future versions:** May not be compatible with Ubuntu 18.04 at all

## Prerequisites
- Access to machines running Ubuntu 18.04
- Business or Enterprise plan (if migration support was needed, within the window)

## Required Action
Upgrade all machines running Ubuntu 18.04 to:
- **Ubuntu 20.04 LTS** (recommended)
- **Ubuntu 22.04 LTS** (recommended)

## Gotchas
- Running future Connector versions on Ubuntu 18.04 is unsupported — Twingate will not debug issues
- Existing Connector/Client versions will keep working temporarily but face eventual deprecation — don't assume current functionality indicates ongoing compatibility
- No exceptions noted for any plan tier after July 31, 2023 migration support window closed

## Related Docs
- [Canonical Ubuntu 18.04 EOL information](https://ubuntu.com/blog/ubuntu-18-04-eol)
- Twingate Connector installation docs (for supported OS versions)