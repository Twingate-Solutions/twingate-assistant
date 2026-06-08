<!-- triage: unassigned URL: https://www.twingate.com/docs/docsTemplate -->

# Twingate Docs Template – Article Component Reference

## Summary
This page is a formatting and component reference for Twingate documentation authors. It demonstrates all supported markdown and custom components used across the docs site. Not intended for end users; serves as an internal authoring guide.

## Key Information

- **Headers**: `#` for section headers, `##` for subsections; H5/H6 unsupported (render at body text size)
- **Lists**: Unordered and ordered lists supported; avoid mixing ordered lists with images (causes rendering issues)
- **Tables**: Supported with standard markdown syntax
- **Code blocks**: Rendered with click-to-copy behavior; supports inline and fenced blocks
- **Callout types**: Success, Info, Extreme — blank line required above/below callout body; no leading indentation
- **Tabbed sections**: Supported for organizing related content into tabs
- **Images**: Accept optional caption prop; captions limited to two lines maximum; do not use captions for step-by-step instructions
- **Embedded video**: YouTube embeds supported
- **Integration logos**: Pre-built set of logos (AWS, Azure, GCP, Okta, etc.); request new logos via Slack (Charles or Zach)
- **Step-by-step guides**: Use subsection (`##`) headers for each step to enable linkability and proper image sizing

## Configuration Values (Example — Connector Task Definition)

| Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | `<YOUR TWINGATE SUBDOMAIN>` |
| `TWINGATE_ACCESS_TOKEN` | JWT token string |
| `TWINGATE_REFRESH_TOKEN` | Refresh token string |
| Container memory | `2048` MB |
| Container CPU | `1024` units |
| Network mode | `awsvpc` |
| Compatibility | `FARGATE` |

## Gotchas

- Images inside ordered lists break rendering — use subsection headers for step-by-step guides instead
- Extreme callouts require a blank line above and below the body text, with no leading indentation on any line
- H5 and H6 render identically to body text — do not use them
- Image captions must not be used to convey instructional steps; two-line maximum

## Prerequisites

- Content changes scoped to `/content` folder only
- Follow internal formatting guide: [Notion – How to Contribute to Docs](https://www.notion.so/twingate/How-to-Contribute-to-Docs-21d8a9f223c14af9960c2c0bdc433a5c)

## Related Docs

- Internal Notion formatting/contribution guide (link above)
- Twingate Connector deployment (ECS/Fargate task definition referenced in code example)