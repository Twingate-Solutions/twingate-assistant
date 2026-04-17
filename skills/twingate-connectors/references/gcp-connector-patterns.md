# GCP Connector Deployment Patterns

Reference for the `twingate-connectors` skill. Contains complete Terraform modules
for deploying Twingate connectors on GCP (GCE, GKE, Managed Instance Groups).

---

## Twingate Resources (All GCP Deployment Types)

```hcl
resource "twingate_remote_network" "gcp_vpc" {
  name     = "GCP Production VPC"
  location = "GOOGLE_CLOUD"
}

resource "twingate_connector" "connector_1" {
  remote_network_id = twingate_remote_network.gcp_vpc.id
  name              = "gcp-connector-1"
}

resource "twingate_connector_tokens" "connector_1" {
  connector_id = twingate_connector.connector_1.id
}

resource "twingate_connector" "connector_2" {
  remote_network_id = twingate_remote_network.gcp_vpc.id
  name              = "gcp-connector-2"
}

resource "twingate_connector_tokens" "connector_2" {
  connector_id = twingate_connector.connector_2.id
}
```

---

## IAM and Secret Manager

### Service Account

Create a dedicated service account — do not reuse the default Compute Engine service
account or any service account with broad permissions.

```hcl
resource "google_service_account" "twingate_connector" {
  account_id   = "twingate-connector"
  display_name = "Twingate Connector Service Account"
}
```

### Secret Manager Access

Scope the binding to the specific secrets — not a project-wide binding.

```hcl
resource "google_secret_manager_secret_iam_member" "connector_1_access" {
  secret_id = google_secret_manager_secret.connector_1_access.id
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${google_service_account.twingate_connector.email}"
}
```

---

## GCE Module

```hcl
resource "google_service_account" "twingate_connector" {
  account_id   = "twingate-connector"
  display_name = "Twingate Connector"
  project      = var.project_id
}

resource "google_secret_manager_secret" "connector_1_access" {
  secret_id = "twingate-connector-1-access-token"
  project   = var.project_id
  replication {
    auto {}
  }
}

resource "google_secret_manager_secret_version" "connector_1_access" {
  secret      = google_secret_manager_secret.connector_1_access.id
  secret_data = twingate_connector_tokens.connector_1.access_token
}

resource "google_secret_manager_secret_iam_member" "connector_1_access" {
  secret_id = google_secret_manager_secret.connector_1_access.id
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${google_service_account.twingate_connector.email}"
}

# (repeat secret resources for connector_1 refresh token and all connector_2 secrets)

resource "google_compute_instance" "connector_1" {
  name         = "twingate-connector-1"
  machine_type = "e2-small"
  zone         = "${var.region}-a"
  project      = var.project_id

  tags = ["twingate-connector"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-12"
    }
  }

  network_interface {
    subnetwork = var.subnetwork_self_link
    # No access_config block = no external IP; relies on Cloud NAT
  }

  service_account {
    email  = google_service_account.twingate_connector.email
    scopes = ["cloud-platform"]
  }

  metadata_startup_script = <<-EOT
    #!/bin/bash
    apt-get update && apt-get install -y docker.io google-cloud-cli
    ACCESS_TOKEN=$(gcloud secrets versions access latest \
      --secret="twingate-connector-1-access-token" --project="${var.project_id}")
    REFRESH_TOKEN=$(gcloud secrets versions access latest \
      --secret="twingate-connector-1-refresh-token" --project="${var.project_id}")
    docker run -d \
      --name twingate-connector \
      -e TWINGATE_NETWORK="${var.twingate_network}" \
      -e TWINGATE_ACCESS_TOKEN="$ACCESS_TOKEN" \
      -e TWINGATE_REFRESH_TOKEN="$REFRESH_TOKEN" \
      -e TWINGATE_TIMESTAMP_FORMAT=2 \
      -e TWINGATE_LABEL_DEPLOYED_BY=terraform \
      --restart unless-stopped \
      twingate/connector:1
  EOT
}

# Deploy connector_2 in zone "${var.region}-b" with its own secrets
```

GCE instances without external IPs require Cloud NAT for outbound access to
`*.twingate.com:443`. Verify a Cloud NAT gateway is configured on the subnet's router
before deployment.

---

## GKE Helm Alternative

```bash
helm repo add twingate https://twingate.github.io/helm-charts
helm repo update

helm install twingate-connector-1 twingate/connector \
  --set connector.network="<tenant>" \
  --set connector.accessToken="<access-token>" \
  --set connector.refreshToken="<refresh-token>"
```

For production clusters: use the External Secrets Operator with Workload Identity to
sync tokens from Secret Manager into Kubernetes Secrets. Deploy two Helm releases with
separate token pairs and configure pod anti-affinity to spread across nodes in different
zones (`topology.kubernetes.io/zone`).

---

## Google Workspace Integration Notes

**SSO (SAML):** In the Google Workspace Admin Console, go to Apps → Web and mobile apps
and create a new SAML app for Twingate. Configure SAML SSO using the Twingate SAML
metadata or the manual ACS URL and Entity ID from the Twingate admin console. Assign the
app to the organizational units or groups that should have Twingate access.

**SCIM Provisioning:** In the Twingate SAML app settings in Google Workspace, enable
automatic provisioning. Use the Twingate SCIM endpoint and a Twingate API key as the
tenant URL and secret token. Google Workspace Groups sync to Twingate Groups via SCIM.

See the `twingate-identity` skill for full IdP configuration steps.
