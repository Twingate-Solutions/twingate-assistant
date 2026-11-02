<!-- manual-reference: do-not-overwrite -->
# Intake: read-only discovery commands

When the admin has no clean diagram or export, offer short **read-only** commands they (or Claude,
with their approval, in Claude Code / Cowork) can run. Output lands in the state file as
`sourced`. Rules:

- Read-only only. Never offer a command that changes infrastructure during discovery.
- Show the command and say what it reads before anyone runs it. Claude runs a command only
  after the admin approves that specific command.
- Prefer the admin's existing CLI auth (`aws`, `az`, `gcloud`, `kubectl`). Never ask for cloud
  credentials in chat.
- Trim output to what's needed (names, CIDRs, IDs). Never store secrets or keys.
- Adapt to `meta.scripting`: bash/zsh by default; PowerShell equivalents only if the admin chose
  PowerShell.

The commands below are generic cloud-CLI shapes. Check flags against the CLI's own help if a
command errors — CLIs change.

## Cloud networks → Remote Network candidates

```bash
# AWS — VPCs, subnets, security groups (per region)
aws ec2 describe-vpcs --query 'Vpcs[].{id:VpcId,cidr:CidrBlock,name:Tags[?Key==`Name`]|[0].Value}' --output table
aws ec2 describe-subnets --query 'Subnets[].{id:SubnetId,vpc:VpcId,cidr:CidrBlock,az:AvailabilityZone,public:MapPublicIpOnLaunch}' --output table
aws ec2 describe-instances --query 'Reservations[].Instances[].{id:InstanceId,name:Tags[?Key==`Name`]|[0].Value,ip:PrivateIpAddress,dns:PrivateDnsName,vpc:VpcId}' --output table
aws route53 list-hosted-zones --query 'HostedZones[?Config.PrivateZone].Name'

# Azure — VNets, subnets, private DNS zones
az network vnet list --query '[].{name:name,rg:resourceGroup,cidr:addressSpace.addressPrefixes}' -o table
az network vnet subnet list --vnet-name <vnet> -g <rg> --query '[].{name:name,cidr:addressPrefix}' -o table
az network private-dns zone list --query '[].name' -o tsv

# GCP — VPCs, subnets, instances
gcloud compute networks list
gcloud compute networks subnets list --format='table(name,network,region,ipCidrRange)'
gcloud compute instances list --format='table(name,zone,networkInterfaces[0].networkIP)'

# Kubernetes — clusters/services that may become Resources
kubectl get svc -A -o wide
```

Each VPC/VNet is usually one Remote Network candidate — confirm boundary guidance with the
twingate-architect skill.

## On-prem

```bash
# DNS: resolve a list of hostnames (one per line in hosts.txt)
while read h; do printf '%s ' "$h"; dig +short "$h" | head -1; done < hosts.txt
# Reverse lookups for a subnet's known IPs
while read ip; do printf '%s ' "$ip"; dig +short -x "$ip"; done < ips.txt
```

Ask for IPAM, DNS zone, or CMDB exports when they exist — they beat ad-hoc scans. Do not
suggest network scanning (nmap sweeps) unless the admin raises it and owns the authorisation.

## IdP directory (Phase 2 suggestions)

- If a read-only IdP connector (Okta, Entra, Google) is available in the session, list groups and
  member counts through it and propose which to provision. The admin does the assignment.
- Otherwise ask for an export, or e.g. `az ad group list --query '[].{name:displayName,id:id}' -o table`
  for Entra. Record group names only, never member emails beyond what's needed.

## Connector-host preflight (Phase 6, run on the candidate host)

Run *on the host that will run the connector*, before deploying it:

1. **Name resolution** of every in-scope Resource address from that host
   (`getent hosts <fqdn>` or `dig +short <fqdn>`).
2. **Reachability** of each Resource port from that host (`nc -zv -w 3 <host> <port>`;
   PowerShell: `Test-NetConnection <host> -Port <port>`).
3. **Egress to Twingate** — load the twingate-connectors skill and grep its references for
   "outbound" / "egress" / "ports" to get the current required destinations and ports, then
   test each (`nc -zv`, `curl -sv https://<destination>`). Never use ports from memory.
4. **TLS interception** — `openssl s_client -connect <twingate-destination>:443 -servername <name> </dev/null 2>/dev/null | openssl x509 -noout -issuer`.
   An issuer belonging to the organisation's proxy or firewall vendor means traffic is inspected;
   check the twingate-connectors and twingate-troubleshoot skills for the impact and the bypass
   guidance.

Record results per remote network in `connector_hosts`, and failures as tasks with evidence.
