<!-- triage: unassigned URL: https://www.twingate.com/docs/docsTemplate -->

# Twingate Docs Template / Component Reference

## Summary
This is Twingate's internal documentation template page demonstrating supported markdown and custom components for doc authoring. It serves as a formatting reference for contributors writing or updating Twingate documentation articles.

## Key Information

- **Heading levels**: `#` for section headers, `##` for subsections; H5/H6 unsupported (render as body text)
- **Lists**: Unordered and ordered lists supported; only use ordered lists when every item is a text step (no images inline)
- **Callout types**: Success, Info, Extreme — callout body requires blank line above and below, no leading indentation
- **Code blocks**: Supported with click-to-copy; inline code also supported
- **Images**: Accept caption prop; captions max two lines; not to be used for instructions
- **Tabbed sections**: Supported for organizing related content into tabs
- **Integration logos**: Pre-built set of partner/platform logos available (AWS, Azure, GCP, Okta, etc.)
- **YouTube embeds**: Supported via embed component

## Configuration Values (Example from Template)

| Environment Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Your Twingate subdomain |
| `TWINGATE_ACCESS_TOKEN` | Connector access token |
| `TWINGATE_REFRESH_TOKEN` | Connector refresh token |

Example container spec: `twingate/connector:1`, memory `2048`, cpu `1024`, network mode `awsvpc`

## Gotchas

- Images inside ordered lists cause rendering issues — avoid
- Callouts **require** a blank line above and below the body text
- No indentation at the start of callout body lines
- H5/H6 headings render at body text size — effectively unsupported
- Image captions must not be used for step-by-step instructions
- Content changes should be limited to the `/content` folder

## Step-by-Step Authoring Guide

1. Author content using supported markdown components within `/content` folder
2. Follow formatting guide: [Twingate Notion Contributor Guide](https://www.notion.so/twingate/How-to-Contribute-to-Docs-21d8a9f223c14af9960c2c0bdc433a5c)

## Related Docs

- Twingate Connector deployment (ECS/Fargate task definition pattern shown in template)
- Twingate Notion contributor guide (internal)
- Contact Charles or Zach on Slack for new integration logo requests