<!-- initial seed — to be refreshed by pipeline -->

## Page Title
Identity Firewall (IDFW) Overview

## Summary
Twingate Identity Firewall (IDFW) extends Zero Trust enforcement to the host level — attributing every session to a specific authenticated identity, device, and Twingate policy at the point of access rather than only at the network layer. It replaces bastion hosts and privileged jump servers with auditable, policy-gated access that logs who accessed what resource, when, and from which device.

## Key Information
- **What IDFW is**: attribute-based access control enforced at the host or service level; standard Twingate controls which users can reach a resource's IP/port, while IDFW adds identity attribution *inside the host* — the SSH daemon or K8s API server sees the verified Twingate identity, not just a source IP
- **SSH PAM module**: a Linux PAM (Pluggable Authentication Module) installed on target hosts; intercepts every SSH connection and validates the session against the Twingate Controller before allowing shell access; rejected sessions never reach a shell
- **Kubernetes gateway**: a sidecar or gateway component deployed in a K8s cluster; enforces identity-aware access to the Kubernetes API server and cluster services; kubectl and API calls are validated against Twingate policy
- **Session recording**: IDFW-gated SSH sessions can be recorded end-to-end (terminal I/O capture); recordings are stored and retrievable for audit, compliance, and incident response
- **Ansible role**: an official Twingate Ansible role automates SSH PAM module installation and configuration across fleets of Linux hosts; supports variable-driven target configuration
- **Terraform module**: an IDFW-specific Terraform module provisions the Twingate resource and policy objects that back IDFW enforcement; ensures IaC parity between Twingate access policy and host-level PAM configuration
- **Relationship to standard access**: standard Twingate resource access controls network reachability (Client ↔ Connector); IDFW adds a second enforcement layer *at the host* — even a user with network access to the SSH port is blocked unless their Twingate session is valid and authorized by IDFW policy

## Prerequisites
- Twingate IDFW license/feature enabled on the account
- Target Linux hosts (SSH PAM): systemd-based Linux distribution; PAM available (`libpam-modules`); Connector reachable from host for policy validation callbacks
- Kubernetes gateway: Kubernetes 1.24+; Helm 3; cluster admin privileges for sidecar injection or gateway deployment
- Session recording: object storage destination configured (e.g., S3 or GCS bucket) with write permissions
- Ansible role: Ansible 2.12+ on the control node; SSH access to target hosts for initial role application
- Terraform module: Terraform 1.3+; Twingate Terraform provider configured with API key

## Step-by-Step
1. Enable IDFW in the Twingate Admin Console (requires account-level feature flag — contact Twingate support if not visible)
2. **SSH PAM path**: on each target host, install the Twingate PAM module package → edit `/etc/pam.d/sshd` to include the Twingate PAM entry → configure `/etc/twingate/idfw.conf` with the tenant URL and resource token → restart `sshd`
3. **Ansible path**: add the `twingate.idfw` Ansible role to your playbook → set `twingate_tenant`, `twingate_resource_token`, and optional `session_recording_enabled` variables → run playbook against target hosts
4. **Kubernetes gateway path**: add the Twingate Helm repository → install the IDFW gateway chart into the target namespace → annotate target namespaces or deployments to route API traffic through the gateway → verify gateway pod is Running
5. In the Twingate Admin Console, create an IDFW-enabled Resource (toggle "Identity Firewall" on the resource) and assign it to the appropriate Group(s)
6. (Optional) Enable session recording on the Resource: configure storage backend credentials in Admin Console → Sessions → Recording Storage
7. Test access: authenticate with the Twingate Client, SSH to the target host, verify the session appears in Admin Console → Sessions with identity attribution; attempt access without an active Twingate session to confirm it is blocked

## Configuration Values
- PAM config file: `/etc/twingate/idfw.conf`
- Key PAM config fields: `tenant_url`, `resource_token`, `session_recording = true|false`
- Helm chart repo: `https://charts.twingate.com`
- IDFW Helm chart name: `twingate/idfw-gateway`
- Ansible Galaxy role: `twingate.idfw`
- Terraform module source: `twingate/idfw/twingate` (Terraform Registry)

## Gotchas
- The PAM module must be configured *before* disabling password auth or removing other PAM entries — a misconfigured PAM stack can lock all SSH access to the host; always test with a second open session before closing the first
- IDFW resource tokens are per-resource, not per-host — if multiple hosts serve the same logical resource, they share the same token; do not reuse tokens across logically distinct resources
- Session recording generates significant storage volume for interactive sessions — size the storage bucket appropriately and set lifecycle policies to expire old recordings per retention policy
- The Kubernetes gateway does not replace network policy — it adds identity enforcement on top of existing K8s network controls; both layers should be configured
- Ansible role idempotency: re-running the role on an already-configured host is safe, but changes to `idfw.conf` require an `sshd` restart which briefly interrupts active SSH sessions
- Terraform module manages Twingate-side objects (resource, policy, token) only — it does not install the PAM module on hosts; pair with Ansible or user_data/cloud-init for full automation

## Related Docs
- `/docs/identity-firewall` — IDFW feature overview and architecture
- `/docs/ssh-pam-module` — SSH PAM module installation and configuration reference
- `/docs/kubernetes-gateway` — IDFW Kubernetes gateway deployment guide
- `/docs/session-recording` — session recording setup and retrieval
- `/docs/idfw-ansible` — Ansible role reference and variable documentation
- `/docs/idfw-terraform` — Terraform module usage and examples
- `/docs/replacing-bastion-hosts` — migration guide from bastion/jump server to IDFW
