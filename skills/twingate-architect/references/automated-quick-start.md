# Automated Deployment - Twingate

## Summary
Twingate supports Infrastructure-as-Code (IaC) automated deployments via Terraform and Pulumi. Guides are available for AWS, Azure, and GCP. Intended to reduce rollout time across multiple environments including multi-cloud setups.

## Key Information
- Supported IaC tools: **Terraform** and **Pulumi**
- Supported cloud providers: AWS, Azure, GCP (the "big three")
- Multi-cloud deployments are supported

## Prerequisites
- Existing Twingate account
- Familiarity with Terraform or Pulumi
- Cloud provider credentials for target environment(s)

## Step-by-Step
1. Choose IaC tool (Terraform or Pulumi)
2. Choose target cloud provider (AWS, Azure, or GCP)
3. Follow the provider-specific guide (linked from Twingate docs)

## Configuration Values
- No specific env vars, CLI flags, or API params documented on this page
- See individual Terraform/Pulumi provider guides for configuration details

## Gotchas
- This page is an index/landing page only; actual implementation details are in linked sub-guides
- No direct configuration examples provided here

## Related Docs
- Terraform deployment guides (AWS, Azure, GCP)
- Pulumi deployment guides (AWS, Azure, GCP)
- Twingate webinar: *Best Practices for Secure Infrastructure-as-Code Initiatives*