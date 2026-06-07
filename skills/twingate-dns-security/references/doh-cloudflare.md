# How to Configure Cloudflare DoH and DNS Filtering with Twingate

## Summary
Integrates Cloudflare Zero Trust DNS-over-HTTPS (DoH) and DNS filtering with Twingate. Involves creating a DNS location in Cloudflare, retrieving the custom DoH URL, and registering it in the Twingate Admin Console.

## Key Information
- Enables Cloudflare DNS filtering policies alongside DoH encryption
- Cloudflare provides a unique per-location DoH endpoint URL
- DNS filtering rules are optional; DoH protection works independently

## Prerequisites
- Valid Cloudflare Zero Trust account (trial sufficient)
- Access to Twingate Admin Console
- Twingate custom DoH resolver feature enabled

## Step-by-Step

1. **Create DNS Location in Cloudflare**
   - Navigate to Cloudflare Zero Trust dashboard → **Gateway** → **DNS Locations**
   - Add a new DNS location
   - Save and close

2. **Retrieve Custom DoH URL**
   - Return to **Gateway** → **DNS Locations**
   - Click the newly created location
   - Copy the **DNS over HTTPS** URL

3. **Configure DNS Filtering (Optional)**
   - Navigate to **Policies** in Cloudflare Zero Trust
   - Create desired filtering policies

4. **Register DoH URL in Twingate**
   - Add the copied Cloudflare DoH URL as a custom DoH provider in the Twingate Admin Console
   - Follow Twingate's "Configure a Custom DoH resolver" documentation

## Configuration Values
| Parameter | Value |
|-----------|-------|
| DoH URL source | Cloudflare Zero Trust → Gateway → DNS Locations → [location] → DNS over HTTPS field |

## Gotchas
- DNS filtering policies are separate from DoH setup — DoH URL must still be configured in Twingate even if no filtering policies are created
- Each Cloudflare DNS location generates a unique DoH URL; ensure you copy from the correct location

## Related Docs
- [Configure a Custom DoH Resolver in Twingate](https://www.twingate.com/docs/custom-doh) (referenced but not shown)
- Twingate Admin Console custom DoH provider settings