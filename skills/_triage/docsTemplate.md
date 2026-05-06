<!-- triage: unassigned URL: https://www.twingate.com/docs/docsTemplate -->

# Twingate Docs Template

## Summary
This is Twingate's internal documentation template page demonstrating available markdown components and formatting conventions for doc authors. It serves as a reference for supported content types, styling rules, and component usage. Not intended as end-user documentation.

## Key Information

- **Headers**: `#` for section headers, `##` for subsection headers; H5/H6 unsupported (render as body text)
- **Lists**: Unordered lists for general content; ordered lists only when every item is sequentially followed by another list item (no images inside ordered lists)
- **Code blocks**: Support click-to-copy behavior; available for both shell commands and JSON
- **Callout types**: Success, Info, Extreme (use Extreme sparingly); requires blank line above/below body, no leading indentation
- **Tabbed sections**: Supported for organizing related content into tabs
- **Images**: Accept caption prop; captions max two lines; do not use captions for step-by-step instructions
- **Integration logos**: Pre-built set including AWS, Azure AD, GCP, Kubernetes, Okta, Terraform, Jamf, and others
- **YouTube embeds**: Supported inline

## Configuration Values (Example from Template)

| Environment Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Your Twingate subdomain |
| `TWINGATE_ACCESS_TOKEN` | Access token for connector auth |
| `TWINGATE_REFRESH_TOKEN` | Refresh token for connector auth |

Example container spec targets **Fargate**, `memory: 2048`, `cpu: 1024`, image: `twingate/connector:1`, network mode: `awsvpc`.

## Gotchas

- Images inside ordered lists cause rendering issues — avoid
- Extreme callouts **require** a blank line above and below the body text
- No leading indentation allowed in callout body lines
- H5/H6 headings render at body text size — effectively unsupported
- Captions must not be used as instructional text in step-by-step guides

## Step-by-Step Authoring Guide

1. Author content using supported markdown components within the `/content` folder only
2. Follow the formatting guide: [Twingate Internal Notion Doc](https://www.notion.so/twingate/How-to-Contribute-to-Docs-21d8a9f223c14af9960c2c0bdc433a5c)

## Device Attribute Reference (Example Table)

| Attribute | Description | Platforms |
|---|---|---|
| Name | User-set friendly name | Windows, macOS, iOS |
| Hostname | DNS hostname (often based on device name) | Windows, macOS, Linux |
| Make | Device manufacturer | macOS, Linux, iOS |

## Related Docs

- Twingate Internal Contribution Guide (Notion — internal access required)
- Connector deployment documentation (ECS/Fargate)