# How to Configure Cloudflare DoH and DNS Filtering with Twingate

## Page Title
How to Configure Cloudflare DoH and DNS Filtering

## Summary
This guide explains how to integrate Cloudflare's DNS-over-HTTPS (DoH) and DNS filtering capabilities with Twingate. The process involves creating a DNS location in Cloudflare Zero Trust, retrieving the custom DoH URL, and adding it to Twingate's Admin Console.

## Key Information
- Enables Cloudflare DNS filtering on top of DoH protection when used with Twingate
- Cloudflare DNS filtering policies are optional but available if needed
- Integration is completed on the Twingate side by adding a custom DoH provider

## Prerequisites
- Valid Cloudflare Zero Trust account (trial account is sufficient)
- Access to Twingate Admin Console

## Step-by-Step

1. **Add a DNS Location in Cloudflare**
   - Navigate to Cloudflare Zero Trust dashboard
   - Go to **Gateway → DNS Locations**
   - Create a new DNS location
   - Save and close the location

2. **Retrieve the Custom DoH URL**
   - Return to **Gateway → DNS Locations**
   - Click on the newly created location
   - Copy the **DNS over HTTPS** URL

3. **Set Up DNS Filtering Rules (Optional)**
   - Navigate to **Policies** in Cloudflare Zero Trust
   - Create filtering policies as needed

4. **Configure Twingate with Cloudflare's DoH URL**
   - Add the copied DoH URL as a custom DoH provider in the Twingate Admin Console
   - Follow Twingate's "Configure a Custom DoH resolver" documentation

## Configuration Values
- **DoH URL**: Retrieved from Cloudflare Zero Trust → Gateway → DNS Locations → [your location] → DNS over HTTPS field
- **Twingate setting**: Custom DoH provider (configured in Twingate Admin Console)

## Gotchas
- The Cloudflare DoH URL is location-specific — must be copied from your specific DNS location, not a generic endpoint
- DNS filtering policies must be configured in Cloudflare separately; they are not automatically applied

## Related Docs
- [Configure a Custom DoH Resolver in Twingate](https://www.twingate.com/docs/custom-doh) *(referenced but URL not provided on this page)*
- Cloudflare Zero Trust Gateway documentation (external)