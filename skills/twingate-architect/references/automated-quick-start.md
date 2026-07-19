# Automated Deployment - Twingate

## Summary
Twingate supports automated deployment via Infrastructure-as-Code (IaC) tools, specifically Terraform and Pulumi. Guides are available for AWS, Azure, and GCP. Intended for teams deploying across multiple environments or multi-cloud setups.

## Key Information
- Supported IaC tools: **Terraform** and **Pulumi**
- Supported cloud providers: AWS, Azure, GCP (the "big three")
- Reduces manual rollout time across multiple environments
- Multi-cloud deployments are a primary use case

## Prerequisites
- Existing Twingate account
- Familiarity with Terraform or Pulumi
- Access to target cloud provider (AWS, Azure, or GCP)

## Step-by-Step
1. Choose IaC tool (Terraform or Pulumi)
2. Choose target cloud provider
3. Follow the provider-specific guide (linked from the Twingate docs)

## Configuration Values
- None explicitly listed on this page; see individual Terraform/Pulumi provider guides for specific env vars, API tokens, and resource parameters

## Gotchas
- This page is an index/landing page only — actual configuration details are in the linked provider-specific guides
- No standalone deployment instructions are provided here

## Related Docs
- Terraform deployment guides (per cloud provider)
- Pulumi deployment guides (per cloud provider)
- [Twingate Best Practices for Secure Infrastructure-as-Code Initiatives (webinar)](https://www.twingate.com)