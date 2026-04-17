# Azure Connector Deployment Patterns

Reference for the `twingate-connectors` skill. Contains complete Terraform modules
for deploying Twingate connectors on Azure (ACI, Azure VMs, AKS).

---

## Twingate Resources (All Azure Deployment Types)

```hcl
resource "twingate_remote_network" "azure_vnet" {
  name     = "Azure Production VNet"
  location = "AZURE"
}

resource "twingate_connector" "connector_1" {
  remote_network_id = twingate_remote_network.azure_vnet.id
  name              = "azure-connector-1"
}

resource "twingate_connector_tokens" "connector_1" {
  connector_id = twingate_connector.connector_1.id
}

resource "twingate_connector" "connector_2" {
  remote_network_id = twingate_remote_network.azure_vnet.id
  name              = "azure-connector-2"
}

resource "twingate_connector_tokens" "connector_2" {
  connector_id = twingate_connector.connector_2.id
}
```

---

## ACI Module (Single Direct-Injection Pattern)

Tokens are passed directly as `secure_environment_variables`, sourced from the
`twingate_connector_tokens` resource. This is the primary ACI deployment pattern.

```hcl
resource "azurerm_resource_group" "twingate" {
  name     = "rg-twingate-connectors"
  location = var.location
}

resource "azurerm_container_group" "connector_1" {
  name                = "twingate-connector-1"
  location            = azurerm_resource_group.twingate.location
  resource_group_name = azurerm_resource_group.twingate.name
  os_type             = "Linux"
  restart_policy      = "Always"

  container {
    name   = "twingate-connector"
    image  = "twingate/connector:1"
    cpu    = "0.5"
    memory = "0.5"

    environment_variables = {
      TWINGATE_NETWORK          = var.twingate_network
      TWINGATE_TIMESTAMP_FORMAT = "2"
      TWINGATE_LABEL_DEPLOYED_BY = "terraform"
    }

    secure_environment_variables = {
      TWINGATE_ACCESS_TOKEN  = twingate_connector_tokens.connector_1.access_token
      TWINGATE_REFRESH_TOKEN = twingate_connector_tokens.connector_1.refresh_token
    }
  }
}

# Deploy connector_2 as a second azurerm_container_group in a different region or zone
```

**Key Vault token storage** is an optional additive step if you want tokens stored for
audit or rotation tracking, but the ACI container group always injects them directly
via `secure_environment_variables` — the two approaches are not mutually exclusive.

**VNet integration note:** ACI VNet integration requires a subnet delegated to
`Microsoft.ContainerInstance/containerGroups`. Without VNet integration, ACI uses
public egress, which is acceptable for outbound-only connectors but less secure than
private placement.

---

## Azure VM Alternative

For customers who prefer full VM control or have compliance requirements around
container orchestration. Assign a system-assigned Managed Identity with
`Key Vault Secrets User` on the Key Vault containing connector tokens, then use
a cloud-init or custom script extension to fetch tokens at boot:

```bash
#!/bin/bash
ACCESS_TOKEN=$(az keyvault secret show \
  --vault-name <vault-name> \
  --name twingate-connector-1-access-token \
  --query value -o tsv)
REFRESH_TOKEN=$(az keyvault secret show \
  --vault-name <vault-name> \
  --name twingate-connector-1-refresh-token \
  --query value -o tsv)

docker run -d \
  --name twingate-connector \
  -e TWINGATE_NETWORK="<tenant>" \
  -e TWINGATE_ACCESS_TOKEN="$ACCESS_TOKEN" \
  -e TWINGATE_REFRESH_TOKEN="$REFRESH_TOKEN" \
  -e TWINGATE_TIMESTAMP_FORMAT=2 \
  -e TWINGATE_LABEL_DEPLOYED_BY=azure-vm \
  --restart unless-stopped \
  twingate/connector:1
```

Deploy two VMs in different Availability Zones (`zones = ["1"]` and `zones = ["2"]`),
each with its own Managed Identity and token pair.

---

## AKS Helm Alternative

```bash
helm repo add twingate https://twingate.github.io/helm-charts
helm repo update

helm install twingate-connector-1 twingate/connector \
  --set connector.network="<tenant>" \
  --set connector.accessToken="<access-token>" \
  --set connector.refreshToken="<refresh-token>"
```

For production: use the External Secrets Operator to sync tokens from Azure Key Vault
into Kubernetes Secrets. Deploy two Helm releases with separate token pairs and configure
pod anti-affinity to spread across nodes in different zones
(`topology.kubernetes.io/zone`).

---

## Entra ID Integration Notes

**SSO (SAML):** Create a new Enterprise Application in Entra ID for Twingate. Configure
SAML SSO using the Twingate SAML metadata or the manual ACS URL / Entity ID from the
Twingate admin console. Assign users and groups to the Enterprise Application.

**SCIM Provisioning:** In the same Enterprise Application, enable Provisioning (Automatic
mode). Use the Twingate SCIM endpoint and a Twingate API key as the tenant URL and secret
token. Entra ID security groups sync to Twingate Groups via SCIM.

This is the recommended pattern for Entra ID customers. See the `twingate-identity` skill
for full IdP configuration steps.
