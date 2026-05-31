<!-- triage: unassigned URL: https://www.twingate.com/docs/docsTemplate -->

# Twingate Docs Template

## Summary
This is a documentation component reference/style guide for Twingate documentation authors. It demonstrates all supported markdown and custom components available when authoring Twingate docs. Not intended for end-user implementation.

## Key Information

### Supported Markdown Components
- Unordered lists, ordered lists, inline `code`, **bold**, *italic*
- Tables with Attribute/Description/Platform columns
- Code blocks with click-to-copy behavior
- Headers: H1 (`#`), H2 (`##`), H3 (`###`), H4 (`####`) — H5/H6 unsupported (render as body text)

### Custom Components
- **Callouts** (3 severity levels): Success, Info, Extreme
  - Extreme callouts require blank line above and below body; no leading indentation
- **Tabbed sections** for organizing related content (Getting Started / Advanced / Troubleshooting pattern)
- **Integration logo links** (AWS, Azure AD, GCP, Okta, Kubernetes, Terraform, etc.)
- **Image component** with optional caption prop (max 2 lines; do not use captions for instructions)
- **Embedded YouTube videos**

### Step-by-Step Guide Formatting
- Use subsection headers (`##`) for each numbered step
- Provides linkability and prevents image stretching
- Do **not** place images inside ordered lists — causes rendering issues

## Configuration Values (Example from Template)
```json
TWINGATE_NETWORK: "<YOUR TWINGATE SUBDOMAIN>"
TWINGATE_ACCESS_TOKEN: "eyJ0eXAiOiJEQVQiLCJh..."
TWINGATE_REFRESH_TOKEN: "suoodqhy0niwjzpY_ki8..."
```
Container: `twingate/connector:1`, Memory: `2048`, CPU: `1024`, Network mode: `awsvpc`

## Gotchas
- Images inside ordered lists cause rendering issues — avoid
- H5/H6 headings render at body text size — unsupported, avoid use
- Extreme callouts break without blank lines surrounding body content and no line indentation
- Image captions must not be used for step instructions; max 2 lines
- All content changes should stay within the `/content` folder

## Prerequisites
- Access to Twingate docs repo
- Formatting guide: [Notion internal link](https://www.notion.so/twingate/How-to-Contribute-to-Docs-21d8a9f223c14af9960c2c0bdc433a5c) (internal)
- New integration logos: contact Charles or Zach on Slack

## Related Docs
- Twingate internal contribution/formatting guide (Notion)
- Individual integration pages (AWS, Azure, GCP, Okta, Kubernetes, Terraform, etc.)