# Linux Client Application – OSS Third-Party Notices

## Page Title
Linux Client Application (Open Source Components & Licenses)

## Summary
This page documents the open-source components bundled in the Twingate Linux client application and their respective licenses. It serves as the third-party notice disclosure required by each component's license terms. No installation or configuration guidance is provided.

## Key Information

### Components Included
| Component | License |
|-----------|---------|
| libssl | Apache 2.0 |
| libevent, lwip | BSD 3-Clause |
| siphash | CC0 1.0 Universal |
| libjansson, jwt-cpp, args, pubnub, quicly | MIT |
| catch2 | Boost Software License 1.0 |
| zlib, nanopb | zlib License |
| fmt | MIT-like (with optional embedding exception) |

### License Summary by Type
- **Apache 2.0** – Requires attribution, license copy on redistribution; patent termination clause applies
- **BSD 3-Clause** – Requires attribution; no endorsement using contributor names
- **CC0 1.0** – Effectively public domain; no restrictions
- **MIT** – Permissive; include copyright notice in copies
- **Boost 1.0** – Similar to MIT; copyright notice required except in binary-only distributions
- **zlib** – Cannot misrepresent origin; altered versions must be marked

## Prerequisites
- None for end users
- Redistributors must comply with each component's license terms

## Configuration Values
- None (this is a license disclosure page only)

## Gotchas
- **fmt** has an optional exception: if portions are embedded into machine-executable object code during compilation, you may redistribute without including the copyright/permission notice
- **Apache 2.0** includes a patent retaliation clause — patent licenses terminate if you file patent litigation against contributors
- **BSD 3-Clause** prohibits using contributor/project names for endorsement of derived products without permission
- **CC0** does not waive trademark or patent rights (siphash component)

## Related Docs
- Twingate Linux Client installation documentation
- Twingate OSS notices for other platforms (macOS, Windows, iOS, Android clients)