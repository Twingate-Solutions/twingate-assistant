<!-- triage: unassigned URL: https://www.twingate.com/docs/docsTemplate -->

# Twingate Docs Template

## Summary
This is a documentation component showcase/template page demonstrating all supported markdown and custom components available for Twingate documentation authoring. It serves as a reference for content contributors when formatting articles.

## Key Information

- **Headers**: `#` for section headers, `##` for subsection headers; H5/H6 unsupported (render as body text)
- **Lists**: Unordered and ordered lists supported; only use ordered lists when every item is sequential (no images inside ordered lists)
- **Inline formatting**: Bold, italic, inline code supported
- **Tables**: Supported with Attribute/Description/Platform columns as shown
- **Code blocks**: Include click-to-copy functionality; support shell and JSON syntax
- **Callout types**: Success, Info, Extreme (use Extreme sparingly)
- **Tabbed sections**: Supported for organizing related content into tabs
- **Images**: Accept caption prop; captions max two lines; do not use captions for step-by-step instructions
- **Video**: Embedded YouTube supported
- **Integration logos**: Pre-built set of integration link icons available (Azure AD, AWS, GCP, Okta, Kubernetes, etc.)

## Prerequisites

- Content changes must be within the `/content` folder only
- Review formatting guide at Notion before contributing: `https://www.notion.so/twingate/How-to-Contribute-to-Docs-21d8a9f223c14af9960c2c0bdc433a5c`

## Configuration Values

Callout formatting requirements:
- Blank line **above and below** callout body in markdown
- No indentation at beginning of any line in callout body

## Gotchas

- Images inside ordered lists will cause rendering issues — avoid
- H5 and H6 headers are unsupported and render at body text size
- Extreme callouts require blank lines above and below body content (no exceptions)
- Image captions must not be used for instructions; max two lines
- New integration logos require contacting Charles or Zach on Slack before authoring

## Related Docs

- Twingate contributor/formatting guide (internal Notion): `https://www.notion.so/twingate/How-to-Contribute-to-Docs-21d8a9f223c14af9960c2c0bdc433a5c`