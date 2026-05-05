## Troubleshooting Peer-to-Peer Connections

Diagnostic playbook for when peer-to-peer (P2P) Twingate connections fail to establish, forcing fallback to **Relay** transport. Diagnoses NAT traversal issues.

### Background

Twingate has two transport mechanisms:
- **Peer-to-peer**: direct Client <-> Connector via NAT traversal -- preferred for performance
- **Relay**: indirect via Twingate Relay servers -- fallback when P2P fails

Neither requires inbound firewall rules. P2P specifically uses **NAT traversal** (UDP/QUIC), which can be blocked by various network conditions.

### Four Common Causes of P2P Failure

1. **UDP or QUIC blocked** (either side)
2. **Outbound IP/port restrictions** (either side)
3. **Double NAT** (Client side, typically)
4. **Incompatible NAT type** (endpoint-dependent)

### Diagnostic Order

#### 1. Verify UDP & QUIC Are Not Blocked

Twingate uses **QUIC over UDP** for NAT traversal. Some firewalls block QUIC by default.

**Test**: visit `https://quic.nginx.org/` from the Connector host (and Client host). Successful connection = QUIC works.

**Most common offender**: Connector-side firewalls. Client-side QUIC blocking is rare.

#### 2. Verify Outbound Rules

Both Client and Connector must be able to send UDP packets to **any IP and any port** (NAT devices map random ports).

Reference: /docs/firewalls-and-twingate has the full prerequisite list. Verify:
- No outbound UDP block on the Connector side
- No outbound UDP block on the Client side
- No port-range filtering preventing high random ports

#### 3. Check for Double NAT (Client Side)

**Double NAT** = two NAT devices on the path (e.g., ISP router + your own router behind it).

UDP is stateless; double NAT introduces brittle multi-hop port mappings that break P2P.

**Resolution**: bridge mode on one of the NAT devices, or remove the second device.

#### 4. Check NAT Types

P2P requires **endpoint-independent NAT** on both ends. Endpoint-dependent NAT assigns different ports per destination -- breaks NAT traversal because the Client doesn't know which port the Connector is using for it.

**Connector NAT type**: Admin Console -> Connector detail page -> **STUN Discovery** should be **Available**.

**Client NAT type**: Client logs -- search for `stun_nat_type`:
```
[INFO] [libsdwan] stun_nat_type: endpoint-independent
```

If `endpoint-dependent`, P2P will not work for that Client.

### Connector Behind Incompatible NAT

**Known incompatible**: AWS NAT Gateway -- breaks NAT traversal.

**Workarounds:**
- Use a **third-party NAT solution**: Cohesive Cloud NAT, fck-nat, alterNAT
- Build a custom NAT gateway (EC2 with `iptables MASQUERADE`)

**For enterprise firewalls** (Sonicwall, Palo Alto, OPNsense, etc.):
- Sonicwall: configure **Consistent NAT**
- Palo Alto: implement **Persistent NAT**
- OPNsense: add an **Outbound NAT rule** with port preservation
- Other firewalls: contact Twingate Support

### Decision Notes

- P2P failure is functional but degrades performance/latency -- diagnose and fix for production
- Always check **STUN Discovery: Available** in the Connector detail page first -- it's a quick yes/no
- AWS NAT Gateway is the most common Connector-side issue for cloud deployments -- plan around it

### Gotchas

- Some "fixes" (like opening firewall ports) don't actually help if the NAT type itself is wrong -- always check NAT type before chasing firewall rules
- Client-side double NAT is invisible to admins -- need to ask the user to check their home network setup
- Endpoint-dependent NAT can be inherent to ISP equipment -- only fix is bridge mode or different network

### Related Docs

- /docs/how-nat-traversal-works -- Deep dive on NAT traversal
- /docs/peer-to-peer-communication-in-twingate -- P2P fundamentals
- /docs/firewalls-and-twingate -- Firewall coexistence + outbound prerequisites
- /docs/firewall-failures -- Sibling: when firewalls block P2P entirely
- /docs/connector-best-practices -- Connector network requirements
