<!-- triage: unassigned URL: https://www.twingate.com/docs/docsTemplate -->

# Twingate Docs Template Reference

## Page Title
Docs Template — Article Components

## Summary
This is Twingate's internal documentation template showcasing supported markdown and custom components for authoring docs pages. It serves as a formatting reference for contributors writing or updating documentation.

## Key Information

- **Headers**: `#` for section headers, `##` for subsections; H5/H6 unsupported (render as body text)
- **Lists**: Unordered and ordered lists supported; ordered lists only when every item is sequential — do not embed images in ordered lists
- **Inline formatting**: Bold, italic, inline code all supported
- **Tables**: Standard markdown tables with Attribute/Description/Platform columns supported
- **Code blocks**: Rendered with click-to-copy behavior; supports shell and JSON
- **Callouts**: Three severity levels — Success, Info, Extreme; Extreme callouts require blank lines above/below body and no line indentation
- **Images**: Accept optional caption prop; captions limited to two lines maximum; do not use captions for step-by-step instructions
- **Tabbed sections**: Supported for organizing related content into tabs (e.g., Getting Started / Advanced / Troubleshooting)
- **YouTube embeds**: Supported via embedded component
- **Integration logos**: Pre-built logo components available (AWS, Azure, GCP, Okta, Kubernetes, etc.)

## Configuration Values (Example from Template)

| Environment Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Your Twingate subdomain |
| `TWINGATE_ACCESS_TOKEN` | Connector access token |
| `TWINGATE_REFRESH_TOKEN` | Connector refresh token |

Example context: Fargate/ECS task definition with `twingate/connector:1`, 2048MB memory, 1024 CPU, `awsvpc` network mode.

## Gotchas

- Images inside ordered lists cause rendering issues — avoid
- Extreme callouts **require** a blank line above and below the body text with no leading indentation
- H5 and H6 render at body text size — use H4 or above for visible hierarchy
- Image captions must not be used as instructional steps
- Content changes should be limited to the `/content` folder

## Step-by-Step Authoring Guide

1. Author content using supported markdown components within `/content` folder
2. Follow the internal formatting guide: [Notion: How to Contribute to Docs](https://www.notion.so/twingate/How-to-Contribute-to-Docs-21d8a9f223c14af9960c2c0bdc433a5c)

## Related Docs

- Internal contributor guide: Notion link above
- Contact Charles or Zach on Slack for new integration logo requests