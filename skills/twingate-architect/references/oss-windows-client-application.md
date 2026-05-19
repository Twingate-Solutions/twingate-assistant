# Windows Client Application - OSS Third Party Notices

## Page Title
Twingate Windows Client Application – Open Source Component Licenses

## Summary
This page lists all third-party open source components bundled in the Twingate Windows client application, along with their respective license texts. It serves as the legal third-party notice disclosure required by the included licenses. No implementation guidance is provided.

## Key Information

- **Total components**: 19 third-party libraries used in the Windows client
- **License types used**:
  - Apache 2.0: `libssl`
  - BSD 3-Clause: `libevent`, `lwip`, `nlog`
  - CC0 1.0 Universal: `siphash`
  - MIT: `libjansson`, `jwt-cpp`, `args`, `ModernWpf`, `MVVMLight`, `Newtonsoft JSON.NET`, `Sentry`, `pubnub`, `quicly`
  - Boost Software License 1.0: `catch2`
  - zlib License: `zlib`, `nanopb`
  - Code Project Open License: `wpf-notifyicon`
  - Microsoft Public License: `CommonServiceLocator`
  - MIT-variant: `fmt`

## Component Inventory

| Component | License | Primary Use |
|-----------|---------|-------------|
| libssl | Apache 2.0 | TLS/cryptography |
| libevent | BSD 3-Clause | Event notification |
| lwip | BSD 3-Clause | Lightweight TCP/IP |
| nlog | BSD 3-Clause | Logging (.NET) |
| jwt-cpp | MIT | JWT handling |
| quicly | MIT | QUIC protocol |
| pubnub | MIT | Real-time messaging |
| nanopb | zlib | Protocol Buffers |
| Sentry | MIT | Error reporting |
| wpf-notifyicon | CPOL | System tray UI |

## Prerequisites
- N/A — This is a legal disclosure page, not a setup guide.

## Step-by-Step
- N/A

## Configuration Values
- N/A

## Gotchas
- **`wpf-notifyicon` (CPOL)**: Has redistribution restrictions — cannot be sold standalone; accompanying articles cannot be redistributed without author consent.
- **`fmt`**: Uses MIT with an optional exception allowing embedded object-form redistribution without copyright notices.
- **`CommonServiceLocator`**: Under Microsoft Public License — patent claims against contributors automatically terminate your patent license.
- **CC0 (`siphash`)**: Trademark and patent rights are explicitly *not* waived under CC0.

## Related Docs
- [Twingate OSS notices for other platforms] (Linux/macOS equivalents would follow similar structure)
- Twingate Windows Client installation documentation