## SaaS App Gating with AWS Exit Nodes

Pattern for using IP allowlist on SaaS apps that natively support it -- by routing user traffic through Twingate Connectors with **fixed AWS Elastic IPs**, the SaaS app sees a known source IP and grants access.

### Use Case

Some SaaS apps (Salesforce, Zoom, etc.) support **IP allowlisting** as their app-layer access control. This pattern uses Twingate Connectors as **exit nodes** with stable IPs:

1. Deploy Twingate Connectors on AWS EC2 with **Elastic IPs**
2. Authorize the EIP(s) in the SaaS app's allowlist
3. Twingate users authenticated to the relevant Resources route through these Connectors -> appear from the EIP -> SaaS app authorizes

### Setup

**Step 1: Deploy EC2 Connectors as Exit Nodes**

- Linux EC2 instance(s) -- recommended Ubuntu 22.04 (any Docker-supporting Linux works)
- Instance size: `t3a.micro` is sufficient; size up for high traffic
- **Multiple instances recommended** for redundancy
- Outbound internet: required (Connectors talk to Twingate Cloud + SaaS apps)
- Inbound internet: **never required** -- block all inbound (only allow SSH temporarily during setup)

**Step 2: Verify Public IP Path**

The "public IP" the SaaS app sees depends on AWS network setup:
- **Direct IGW egress**: instance's Elastic IP is the public IP
- **NAT Gateway egress**: NAT Gateway's IP is the public IP (instance EIP is masked)

Test egress to confirm: `curl https://checkip.amazonaws.com` from the instance.

**Whatever IP shows up here is what you'll allowlist in the SaaS app.**

**Step 3: Install Twingate Connector**

- Follow /docs/connectors-on-linux for Connector deployment on Ubuntu/Linux
- Generate Connector tokens in Twingate Admin Console -> Add Connector

**Step 4: Create Twingate Resource for the SaaS App**

In Twingate Admin Console:
- Create a Resource with the SaaS app's FQDN (e.g., `acme.salesforce.com`)
- Twingate intercepts requests to that FQDN; user traffic routes through the AWS Connector

**Step 5: Authorize Users**

- Create a Group (or use existing) for users who need this app
- Assign the Resource to the Group
- Add users to the Group

### Result

Users connected to Twingate accessing `acme.salesforce.com`:
1. Twingate Client intercepts the FQDN
2. Routes through the AWS Connector via Twingate's tunnel
3. Connector exits to SaaS app from the EIP
4. SaaS app sees the EIP -> matches its allowlist -> grants access

Users NOT on Twingate get denied at the SaaS app's allowlist check.

### Decision Notes

- For SaaS apps without native IP allowlist: use the **SaaS App Gating with IdP** pattern instead (per /docs/saas-app-gating, /docs/saas-app-gating-with-okta, etc.)
- Multiple EIPs (multiple Connectors) require multiple allowlist entries in the SaaS app -- prefer a NAT Gateway with a single static IP if managing one IP is simpler
- Use `terraform-aws` provisioning for repeatability if you have multiple regions or environments

### Gotchas

- Forgetting to **block all inbound** on the EC2 instance is a security mistake -- the Connector needs ZERO inbound; verify the security group is locked down
- EIPs vs. NAT Gateway egress IP differs subtly -- always test which IP egresses before allowlisting
- SaaS app's allowlist may have IP-CIDR limits; for many Connectors, NAT consolidates to one entry
- Failover: if you have only one Connector and it dies, all users lose access until restored -- always run 2+

### Related Docs

- /docs/whitelisting-traffic-to-public-services -- General whitelisting context
- /docs/saas-app-gating -- IdP-based SaaS gating (alternative)
- /docs/connector-best-practices, /docs/connectors-on-linux -- Connector setup
- /docs/aws -- AWS Connector deployment overview
- /docs/aws-vpn-replacement, /docs/aws-how-to-setup-subnets -- AWS networking patterns
