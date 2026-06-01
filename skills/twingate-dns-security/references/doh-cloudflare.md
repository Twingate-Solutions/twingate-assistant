# How to Configure Cloudflare DoH and DNS Filtering with Twingate

## Summary
Integrates Cloudflare Zero Trust DNS-over-HTTPS (DoH) and optional DNS filtering with Twingate. Requires retrieving a custom DoH URL from Cloudflare and configuring it as a custom DoH provider in Twingate's Admin Console.

## Key Information
- Cloudflare Zero Trust provides both DoH encryption and DNS filtering (policy-based)
- DNS filtering policies are optional — DoH can be used without them
- Twingate consumes the Cloudflare DoH endpoint as a custom DoH resolver

## Prerequisites
- Valid Cloudflare Zero Trust account (trial account sufficient)
- Access to Twingate Admin Console
- Familiarity with Twingate custom DoH resolver configuration

## Step-by-Step

1. **Add DNS Location in Cloudflare**
   - Navigate to Cloudflare Zero Trust Dashboard → **Gateway** → **DNS Locations**
   - Create a new DNS location
   - Save and close

2. **Retrieve Custom DoH URL**
   - Return to **Gateway** → **DNS Locations**
   - Click the newly created location
   - Copy the **DNS over HTTPS** URL

3. **Configure DNS Filtering Policies (Optional)**
   - Navigate to **Policies** in Cloudflare Zero Trust Dashboard
   - Create desired filtering rules

4. **Configure Twingate with Cloudflare DoH URL**
   - In Twingate Admin Console, add the copied Cloudflare DoH URL as a custom DoH provider
   - Follow Twingate's "Configure a Custom DoH resolver" documentation

## Configuration Values
| Parameter | Value |
|-----------|-------|
| DoH URL Source | Cloudflare Zero Trust → Gateway → DNS Locations → [location] → DNS over HTTPS field |
| Twingate setting | Custom DoH Provider URL in Admin Console |

## Gotchas
- The Cloudflare DoH URL is location-specific — ensure you copy from the correct DNS location
- DNS filtering policies must be set up in Cloudflare separately; Twingate only passes DNS queries through the DoH endpoint
- No mention of split DNS behavior — verify interaction with Twingate's private resource DNS resolution

## Related Docs
- [Configure a Custom DoH resolver in Twingate](https://www.twingate.com/docs/custom-doh) *(referenced but URL inferred)*
- Cloudflare Zero Trust Gateway documentation (DNS Locations, Policies)