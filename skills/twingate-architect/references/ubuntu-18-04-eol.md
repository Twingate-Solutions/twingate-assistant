# Ubuntu 18.04 End of Life

## Summary
Ubuntu 18.04 LTS reached end of life on May 31, 2023. Twingate dropped support for Connectors and Clients running on Ubuntu 18.04 after that date. Users must migrate to a supported Ubuntu version to continue receiving updates and support.

## Key Information
- **EOL Date**: May 31, 2023
- **Support cutoff**: No Connector or Client support on Ubuntu 18.04 after May 31, 2023
- **Migration support window**: Business and Enterprise plan users received migration assistance until July 31, 2023
- Existing Connector/Client versions continue functioning but will eventually be deprecated
- Future Connector versions may not run on Ubuntu 18.04

## Prerequisites
- Active Twingate deployment using Ubuntu 18.04

## Required Action
Upgrade all machines running Ubuntu 18.04 to:
- **Ubuntu 20.04 LTS** (recommended), or
- **Ubuntu 22.04 LTS** (recommended)

## Gotchas
- Running future Connector versions on Ubuntu 18.04 is unsupported — Twingate will not assist with issues
- Existing installed versions will keep working temporarily but face eventual deprecation — no defined end date given
- Migration support window (until July 31, 2023) has already passed; no extended support available

## Related Docs
- [Canonical Ubuntu 18.04 EOL information](https://ubuntu.com/blog/18-04-end-of-life)
- Twingate Connector installation documentation (for Ubuntu 20.04/22.04)