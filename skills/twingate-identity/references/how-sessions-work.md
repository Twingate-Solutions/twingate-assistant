# How Sessions Work

## Summary
Twingate controls authentication frequency through two independent timers: Sign In Policy (global session) and Resource Policy (per-resource session). Re-authentication leverages a stored IdP session copy to minimize user friction when possible. Understanding timer interactions and IdP session alignment is essential for policy design.

## Key Information
- **Sign In Policy session**: Global timer; expiry signs user out of Twingate Client entirely
- **Resource Policy session**: Per-resource timer; expiry requires re-auth before accessing that resource
- **Rolling window**: Successful Resource Policy re-auth resets the Sign In Policy timer to full duration
- **Device-only policies** do NOT reset the Sign In Policy timer
- Twingate stores a copy of the user's IdP session internally (not admin-configurable)
- If stored IdP session is valid → silent re-auth via Twingate-hosted page (no user action)
- If stored IdP session expired → user redirected to IdP to sign in again
- Enterprise IdPs (Okta, Entra ID, Google Workspace, JumpCloud, OneLogin): IdP session lifetime is admin-configurable
- Social IdPs (Google, Microsoft, LinkedIn, GitHub): session lifetime set by provider, not configurable

## Configuration Values
| Control | Recommended Value | Notes |
|---|---|---|
| Sign In Policy | Up to 30 days | Acts as baseline gate only |
| Resource Policy (RDP/SSH) | 12–16 hours | Avoids mid-session disconnects |
| Resource Policy (web apps) | 12–16 hours | Adjust down for high sensitivity |
| Resource Policy (critical) | Shorter per risk tolerance | — |

## Offboarding (Access Revocation)

**To revoke within 5 minutes:**

1. **Block devices in Twingate** (Admin Console or API) — enforced within 5 minutes; works for all IdP types
2. **Enterprise IdP users**: Suspend user in IdP + revoke sessions — syncs to Twingate (up to ~1 hour via SCIM)
3. **Social IdP users**: Disable user in Twingate (Admin Console or API) — revokes existing sessions within ~5 minutes

**Notes:**
- Do both steps (1+2) for enterprise IdPs to cover SCIM sync delays
- Deactivate/suspend rather than delete in enterprise IdPs — preserves audit logs, same access effect
- SCIM not available for social IdPs

## Policy Design Best Practices
- Set Sign In Policy long (30 days); rely on Resource Policies for per-resource security
- Long-lived connections (RDP/SSH): 12–16 hour Resource Policy
- Short-lived connections (web apps): 12–16 hours or shorter based on sensitivity
- High-sensitivity resources: shorter intervals per risk tolerance
- Device-only policies: use for services/monitoring needing pre-login connectivity

## Gotchas
- Resource Policy re-auth only resets Sign In Policy timer if authentication is required — device-only policies do not qualify
- Other SSO apps accessed through Twingate manage their own sessions independently; Twingate does not influence their session state
- SCIM sync delay can be up to 1 hour — always block devices as primary revocation for time-sensitive offboarding
- Stored IdP session is an internal mechanism; admins cannot configure it in Twingate

## Related Docs
- Session Evaluation Walkthrough
- How to Offboard Users
- Device-only Resource Policies
- Sign In Policy configuration
- Resource Policy configuration