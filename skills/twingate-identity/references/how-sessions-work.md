# How Sessions Work

## Summary
Twingate controls authentication frequency via two independent timers: Sign In Policy (global) and Resource Policy (per-resource). Re-authentication leverages a stored IdP session copy to minimize user interruption. Understanding timer interactions and IdP session alignment is key to balancing security and UX.

## Key Information
- **Sign In Policy timer**: Global session gate; expiry signs user out of Twingate Client entirely
- **Resource Policy timer**: Per-resource; expiry requires re-auth before accessing that resource
- **Rolling window**: Successful Resource Policy re-auth resets the Sign In Policy timer
- **Device-only policies do NOT reset the Sign In Policy timer**
- Stored IdP session is internal—admins cannot configure it in Twingate; lifetime set by IdP
- Social IdPs (Google, Microsoft, LinkedIn, GitHub): session lifetimes not configurable by org

## Re-authentication Flow
1. Timer expires → Twingate checks stored IdP session
2. **IdP session valid** → Silent browser redirect, auto re-authenticated, no user action needed (unless MFA required)
3. **IdP session expired** → User redirected to IdP to sign in; all Twingate timers reset after success

## Configuration Values

| Control | Recommended Value | Notes |
|---|---|---|
| Sign In Policy | Up to 30 days | Acts as baseline, not primary control |
| Resource Policy (RDP/SSH) | 12–16 hours | Prevents mid-session disconnects |
| Resource Policy (web apps) | 12–16 hours | Adjust down for high-sensitivity resources |
| Resource Policy (device-only) | N/A | No auth check; stays accessible while Sign In Policy valid |

## Offboarding / Access Revocation

**Target: revoke within 5 minutes**

| User Type | Steps |
|---|---|
| Enterprise IdP | (1) Block devices in Twingate (≤5 min) + (2) Suspend in IdP and revoke sessions (up to 1 hour) |
| Social IdP | (1) Block devices in Twingate + (2) Disable user in Twingate (≤5 min avg) |

- **Deactivate, don't delete** in enterprise IdPs—preserves audit logs, same access revocation effect
- Do both steps for enterprise IdPs: covers SCIM sync delays

## Gotchas
- Resource Policy re-auth only resets Sign In Policy if authentication is enabled (device-only policies don't count)
- Other SSO applications accessed through Twingate manage their own sessions independently—Twingate does not influence their session state
- SCIM sync delays (up to 1 hour) mean device block is the reliable fast-revocation mechanism
- Social IdP session lifetimes are provider-controlled; no org-level configuration possible

## Prerequisites
- Admin access to Twingate Admin Console
- Enterprise IdP configured if session lifetime alignment is needed
- SCIM provisioning configured for enterprise IdP sync (for offboarding)

## Related Docs
- Session Evaluation Walkthrough (linked inline)
- How to Offboard Users
- Device-only Resource Policies
- Sign In Policy configuration
- Resource Policy configuration