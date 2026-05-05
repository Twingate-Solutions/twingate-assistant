## Pulumi: Twingate on AWS

End-to-end Pulumi (TypeScript) recipe for AWS: VPC, subnet, internet gateway, route table, two EC2 instances (Connector + demo server using the Twingate AMI), and full Twingate config.

**Setup:**
- `pulumi new typescript` -- scaffold the project
- AWS auth via env vars: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`
- `pulumi config set twingate:apiToken <token> --secret`
- `pulumi config set twingate:network <tenant>`
- `cat ~/.ssh/aws_id_rsa.pub | pulumi config set publicKey` -- store SSH public key in config

**npm Modules:**
```
npm install @pulumi/aws @twingate/pulumi-twingate
```

**Twingate AMI:**
- Filter: `name = "twingate/images/hvm-ssd/twingate-amd64-*"`, owner `617935088040`
- Pre-installed Connector + dependencies; configure via cloud-init `userData`

**Connector Bootstrap (cloud-init via `pulumi.all().apply()`):**
The `userData` script writes `/etc/twingate/connector.conf` with:
- `TWINGATE_URL=https://${twingate.config.network}.twingate.com`
- `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN` from `TwingateConnectorTokens`
- `TWINGATE_LOG_ANALYTICS=v1` (enable analytics logs)
- `TWINGATE_LABEL_HOSTNAME=$HOSTNAME_LOOKUP` (from EC2 metadata)
- `TWINGATE_LABEL_EGRESSIP=$EGRESS_IP` (from `checkip.amazonaws.com`)
- `TWINGATE_LABEL_DEPLOYEDBY=tg-pulumi-aws-ec2`

Then `systemctl enable --now twingate-connector`.

**Access Group Pattern (note: differs from Terraform):**
```
const tgresource = new twingate.TwingateResource("resource", {
  name: "aws demo server",
  address: webserver.privateIp,
  remoteNetworkId: network.id,
  accessGroups: [{ groupId: group.id }],   // <-- accessGroups (camelCase, object form)
  protocols: {
    allowIcmp: true,
    tcp: { policy: "RESTRICTED", ports: ["22","80"] },
    udp: { policy: "ALLOW_ALL" }
  }
});
```

The Pulumi provider uses `accessGroups: [{ groupId }]` instead of Terraform's `group_ids = [...]`.

**EC2 Instances:**
- Demo server (`Demo Server`): `associatePublicIpAddress: false`, no public IP
- Connector (`Twingate-Connector`): `associatePublicIpAddress: true` (needed for outbound to Twingate without NAT)

**Workflow:**
1. `pulumi preview` -- non-destructive plan
2. `pulumi up` -- approve to create resources
3. Add Twingate user to the new group (Admin Console)
4. Test SSH: `ssh -i ~/.ssh/aws_id_rsa ubuntu@10.0.1.X` (private IP) via Twingate Client
5. `pulumi down` to tear down

**Gotchas:**
- Pulumi state with `--secret` values is encrypted at rest in the Pulumi service; still avoid committing `Pulumi.<stack>.yaml`
- `twingate.config.network` references the configured `twingate:network` -- works inside `pulumi.interpolate` / `apply()`
- Pulumi provider is community-maintained: file issues at the GitHub repo

**Related Docs:**
- /docs/pulumi-getting-started -- Pulumi setup overview
- /docs/pulumi-azure, /docs/pulumi-gcp -- Other clouds
- /docs/aws -- Manual AWS deployment
