---
source: https://www.twingate.com/docs/pci-compliance
type: docs
fetched: 2026-08-14
source_version: c38003f78ade1f7bec32b3c0156abbeca764befc536fc32b3ce8263269d55e19
---

# PCI Compliance with Twingate

## Page Title
PCI Compliance — Twingate for Companies Requiring PCI DSS Compliance

## Summary
Twingate is not validated as PCI DSS compliant but can be used by organizations that must comply with PCI DSS. When used to secure a cardholder data environment (CDE), Twingate is classified as a third-party service provider under PCI DSS Requirement 12.8. Organizations must understand which PCI requirements Twingate fulfills and verify Twingate meets those specific controls.

## Key Information
- Twingate **is not** PCI DSS validated, but PCI DSS does **not require** third-party service providers to be validated
- When securing a CDE, Twingate is considered "in scope" as a third-party service provider
- Relevant standard: **PCI DSS Requirement 12.8** (managing third-party service providers)
- Twingate can help satisfy **Requirement 7.3** — access control system for managing access to in-scope system components
- If Twingate fails to meet applicable PCI requirements it's being used for, the organization's compliance is impacted

## Prerequisites
- Organization must identify which specific PCI DSS requirements they intend to fulfill using Twingate
- Organization must verify Twingate's implementation meets those specific controls
- Twingate must be actively used to secure CDE access (not just generally deployed)

## Configuration Considerations
- Scope Twingate specifically to CDE components to limit compliance surface area
- Document Twingate's role as a service provider per Requirement 12.8 obligations (vendor agreements, monitoring, compliance reviews)

## Gotchas
- "In scope" ≠ "must be fully PCI DSS validated" — these are distinct concepts
- If Twingate is managing a function (e.g., access control) and fails to meet the related PCI requirement, **the merchant's compliance fails** for that requirement
- Organizations bear responsibility for understanding and verifying how Twingate satisfies each PCI requirement claimed
- PCI DSS compliance is the **organization's responsibility** — Twingate does not provide a compliance guarantee

## Related Docs
- PCI Security Standards Council guidance on Requirement 12.8
- Twingate access control documentation (Requirement 7.3 use case)
- Contact Twingate directly for compliance-specific questions: twingate.com/docs/pci-compliance → "contact us" link