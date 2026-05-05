## Pulumi: Twingate on GCP

End-to-end Pulumi (TypeScript) recipe for GCP: VPC, subnet, firewall, two Compute Engine instances (Connector + Nginx demo server), and full Twingate config.

**Setup:**
- `pulumi new typescript`
- GCP auth: `gcloud auth application-default login`
- Pulumi config:
  - `pulumi config set gcp:project <gcp-project-id>`
  - `pulumi config set gcp:region europe-west2`
  - `pulumi config set gcp:zone europe-west2-c`
  - `pulumi config set twingate:apiToken <token> --secret`
  - `pulumi config set twingate:network <tenant>`

**npm Modules:**
```
npm install @pulumi/gcp @twingate/pulumi-twingate
```

**Connector Bootstrap (via `metadataStartupScript` + `pulumi.interpolate`):**
```
const startupScript = pulumi.interpolate`
#!/bin/bash
curl "https://binaries.twingate.com/connector/setup.sh" | sudo \
  TWINGATE_ACCESS_TOKEN="${tokens.accessToken}" \
  TWINGATE_REFRESH_TOKEN="${tokens.refreshToken}" \
  TWINGATE_URL="https://${twingate.config.network}.twingate.com" bash
`;
```

Both VMs use Ubuntu 22.04 (`ubuntu-os-cloud/ubuntu-2204-lts`) on `e2-micro`.

**Networking:**
- VPC: `autoCreateSubnetworks: false`
- Subnet: `172.16.0.0/24` in `europe-west2`
- Firewall: ICMP + TCP/80 from instances tagged `demo` (`sourceTags: ["demo"]`)
- VM `accessConfigs: [{}]` (empty block) -- ephemeral public IP for outbound

**Twingate Resource:**
```
new twingate.TwingateResource("resource", {
  name: "gcp demo server",
  address: webserver.networkInterfaces[0].networkIp,   // private IP
  remoteNetworkId: network.id,
  accessGroups: [{ groupId: group.id }],
  protocols: {
    allowIcmp: true,
    tcp: { policy: "RESTRICTED", ports: ["80"] },
    udp: { policy: "ALLOW_ALL" }
  }
});
```

**Webserver Init:**
- `apt-get install nginx`
- Custom `/var/www/html/index.html` with simple branding
- `service nginx start`

**Workflow:**
1. `pulumi preview` -> `pulumi up`
2. Add Twingate user to the new group (Admin Console)
3. Browse the test VM `network_ip` via Twingate Client -> see Nginx demo page
4. `pulumi down` to tear down

**Gotchas:**
- Both VMs get ephemeral public IPs in this demo -- in production, use Cloud NAT and remove `accessConfigs` on the test VM (it never needs to be reachable from the internet)
- Connector VM service account scope is `cloud-platform` (very broad) -- restrict in production
- Manual user-to-group assignment in Admin Console is intentional in the demo; production should drive via IdP/SCIM

**Related Docs:**
- /docs/pulumi-getting-started, /docs/pulumi-aws, /docs/pulumi-azure
- /docs/gcp -- Manual GCP deployment
