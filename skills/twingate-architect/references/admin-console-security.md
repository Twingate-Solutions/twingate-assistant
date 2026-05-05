## Admin Console Security

Controls what authentication is required to access the Twingate Admin Console. This is separate from Resource access policies — it applies only to admin sign-in, not to end users.

**Key Information:**
- Configured under Settings → (Admin Console Security section)
- Admins do not need to sign into the Twingate Client to access the Admin Console, so Minimum Authentication Requirements and Device Security policies do not apply here
- MFA can be set to required for Admin Console access (biometrics or security key)

**Configuring Biometrics / Security Key:**
- If MFA is required, admins are prompted to configure biometrics or a security key after first successful authentication
- "Don't ask me again" suppresses the prompt on future logins
- Biometrics configured on the Twingate Client can be reused for Admin Console sign-in
- Biometrics configured for the Admin Console cannot be used for Client authentication (one-way reuse only)
- Can configure MFA later via the account dropdown → Configure MFA

**Related Docs:**
- /docs/two-factor-authentication -- End-user MFA configuration
- /docs/authentication -- Authentication overview
- /docs/security-policies -- Resource-level security policies
