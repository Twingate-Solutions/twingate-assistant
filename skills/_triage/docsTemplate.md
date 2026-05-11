<!-- triage: unassigned URL: https://www.twingate.com/docs/docsTemplate -->

# Twingate Docs Template Reference

## Page Title
Article Components / Docs Template

## Summary
This is Twingate's internal documentation template showcasing supported markdown and custom components for authoring docs pages. It serves as a formatting reference for contributors writing or updating documentation. No functional Twingate feature is described.

## Key Information

**Heading Structure:**
- `#` = Section header (major content chunks)
- `##` = Subsection header (step-by-step guides, sub-chunks)
- H5/H6 unsupported — render at body text size

**Supported Markdown:**
- Unordered lists, ordered lists, inline code, bold, italic
- Tables with Attribute/Description/Platform columns
- Fenced code blocks with click-to-copy

**Custom Components:**
- **Callouts** (3 types): Success, Info, Extreme — require blank line above/below body, no leading indentation
- **Tabbed sections** for organizing related content (Getting Started / Advanced / Troubleshooting pattern)
- **Images** with optional caption (max 2 lines; captions not for instructions)
- **Embedded YouTube** videos
- **Integration logo links** (Azure AD, AWS, GCP, Okta, Kubernetes, Terraform, etc.)

## Configuration Values (Example from Template)

| ENV Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | `<YOUR TWINGATE SUBDOMAIN>` |
| `TWINGATE_ACCESS_TOKEN` | JWT token string |
| `TWINGATE_REFRESH_TOKEN` | Refresh token string |

Container spec: `twingate/connector:1`, 2048MB memory, 1024 CPU, `awsvpc` network mode, FARGATE compatible.

## Step-by-Step Authoring Guide

1. **Author content** — make changes only within the `/content` folder
2. **Check formatting** — follow the Notion formatting guide (internal link referenced in template)

## Gotchas

- Images inside ordered lists cause rendering issues — avoid
- Ordered lists should only be used when every item is sequentially dependent
- Extreme callouts require blank lines above/below and no line indentation
- H5/H6 headings render as body text — use H4 or higher
- Image captions must not be used for step instructions

## Related Docs

- Internal contributor guide: `notion.so/twingate/How-to-Contribute-to-Docs-...`
- Twingate Connector CLI: `/usr/bin/twingate-notifier console`