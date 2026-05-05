## Pulumi: Twingate on Azure

End-to-end Pulumi (TypeScript) recipe for Azure: Resource Group, VNet (10.0.0.0/16) with default subnet, NSG, public IP, two VMs (test webserver + Twingate Connector), and full Twingate config.

**Setup:**
- `pulumi new typescript`
- Azure auth: `az login` then `az account set --subscription=<id>`
- Pulumi config:
  - `pulumi config set twingate:network <tenant>`
  - `pulumi config set twingate:apiToken <token> --secret`
  - `pulumi config set <project>:username tgadmin`
  - `pulumi config set <project>:password <strong-pw> --secret` (must meet Azure password requirements)
  - `pulumi config set azure-native:location uksouth` (or your region)

**npm Modules:**
```
npm install @pulumi/azure-native @pulumi/azure @twingate/pulumi-twingate
```

Two Azure providers are used: `@pulumi/azure-native` (newer, generated from ARM) and `@pulumi/azure` (Terraform-based; used for `ResourceGroup`, `PublicIp` in this guide).

**Connector VM Bootstrap (cloud-init via `userData`):**
```
const startupScript = pulumi.interpolate`
#!/bin/bash
curl "https://binaries.twingate.com/connector/setup.sh" | sudo \
  TWINGATE_ACCESS_TOKEN="${tokens.accessToken}" \
  TWINGATE_REFRESH_TOKEN="${tokens.refreshToken}" \
  TWINGATE_URL="https://${twingate.config.network}.twingate.com" bash
`;
```

VM `userData` is base64-encoded: `userData: startupScript.apply(x => Buffer.from(x).toString("base64"))`.

**Connector VM:** Ubuntu `0001-com-ubuntu-server-jammy` (22.04 LTS) on `Standard_B1ms`, attached to NIC with public IP (for outbound to Twingate) and the NSG.

**Test VM:** Ubuntu 16.04 LTS on `Standard_B1ms`, no public IP, only reachable through Twingate. Init script: `python -m SimpleHTTPServer 80` serving `Hello, World!`.

**NSG Rule:**
- Allows inbound 22, 80 from a single source IP (`88.98.90.108/32` placeholder) -- replace with your IP if you need direct admin access while testing
- Connector VM gets the NSG; test VM does **not** need the NSG since access is via Twingate

**Twingate Resource:**
```
new twingate.TwingateResource("resource", {
  name: "Azure demo server",
  address: pulumi.interpolate`${privIP}`,   // private IP via networkInterface lookup
  remoteNetworkId: network.id,
  accessGroups: [{ groupId: group.id }],
  protocols: {
    allowIcmp: true,
    tcp: { policy: "RESTRICTED", ports: ["22","80"] },
    udp: { policy: "ALLOW_ALL" }
  }
});
```

**Workflow:**
1. `pulumi preview` -> `pulumi up`
2. Add Twingate user to the new group
3. Browse the test VM private IP via Twingate Client -> see "Hello, World!"
4. `pulumi down` to tear down

**Gotchas:**
- Test VM uses Ubuntu 16.04 (very old, EOL) -- update to 22.04 for production
- `python -m SimpleHTTPServer` is Python 2 -- use `python3 -m http.server 80` on modern images
- VM passwords must satisfy Azure complexity rules; failures are non-obvious in `pulumi up` output
- Mixing `@pulumi/azure` (TF-based) and `@pulumi/azure-native` (ARM-based) in the same stack is supported but verbose -- pick one for greenfield

**Related Docs:**
- /docs/pulumi-getting-started, /docs/pulumi-aws, /docs/pulumi-gcp
- /docs/azure -- Manual Azure deployment
