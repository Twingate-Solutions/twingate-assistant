# AWS Connector Deployment Patterns

Reference for the `twingate-connectors` skill. Contains complete Terraform modules
for deploying Twingate connectors on AWS (ECS Fargate, EC2, EKS).

---

## Twingate Resources (All AWS Deployment Types)

```hcl
resource "twingate_remote_network" "aws_vpc" {
  name     = "AWS Production VPC"
  location = "AWS"
}

resource "twingate_connector" "connector_1" {
  remote_network_id = twingate_remote_network.aws_vpc.id
  name              = "aws-connector-1"
}

resource "twingate_connector_tokens" "connector_1" {
  connector_id = twingate_connector.connector_1.id
}

resource "twingate_connector" "connector_2" {
  remote_network_id = twingate_remote_network.aws_vpc.id
  name              = "aws-connector-2"
}

resource "twingate_connector_tokens" "connector_2" {
  connector_id = twingate_connector.connector_2.id
}
```

---

## ECS Fargate Module

```hcl
resource "aws_secretsmanager_secret" "connector_1_access" {
  name = "twingate/connector-1/access-token"
}

resource "aws_secretsmanager_secret_version" "connector_1_access" {
  secret_id     = aws_secretsmanager_secret.connector_1_access.id
  secret_string = twingate_connector_tokens.connector_1.access_token
}

# (repeat for refresh token and connector 2)

resource "aws_security_group" "twingate_connector" {
  name   = "twingate-connector"
  vpc_id = var.vpc_id

  egress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 443
    to_port     = 443
    protocol    = "udp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_ecs_task_definition" "connector_1" {
  family                   = "twingate-connector-1"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"
  task_role_arn            = aws_iam_role.connector_task.arn
  execution_role_arn       = aws_iam_role.connector_execution.arn

  container_definitions = jsonencode([{
    name  = "twingate-connector"
    image = "twingate/connector:1"
    secrets = [
      {
        name      = "TWINGATE_ACCESS_TOKEN"
        valueFrom = aws_secretsmanager_secret.connector_1_access.arn
      },
      {
        name      = "TWINGATE_REFRESH_TOKEN"
        valueFrom = aws_secretsmanager_secret.connector_1_refresh.arn
      }
    ]
    environment = [
      { name = "TWINGATE_NETWORK", value = var.twingate_network },
      { name = "TWINGATE_TIMESTAMP_FORMAT", value = "2" },
      { name = "TWINGATE_LABEL_DEPLOYED_BY", value = "terraform" }
    ]
  }])
}

resource "aws_ecs_service" "connector_1" {
  name            = "twingate-connector-1"
  cluster         = var.ecs_cluster_id
  task_definition = aws_ecs_task_definition.connector_1.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = [var.private_subnet_az1_id]
    security_groups  = [aws_security_group.twingate_connector.id]
    assign_public_ip = false
  }
}

# Deploy connector_2 in a second AZ (var.private_subnet_az2_id)
```

---

## IAM — ECS Task Role

```json
{
  "Effect": "Allow",
  "Action": "secretsmanager:GetSecretValue",
  "Resource": [
    "arn:aws:secretsmanager:<region>:<account>:secret:twingate/connector-1/*",
    "arn:aws:secretsmanager:<region>:<account>:secret:twingate/connector-2/*"
  ]
}
```

Scope to specific secret ARNs — do not use `Resource: "*"` or broad `secretsmanager:*`.
For EC2 deployments, attach the same policy to the EC2 instance profile.

---

## EC2 / systemd Alternative

For customers without ECS, run the connector via Docker on EC2. Use a user data script
to fetch tokens from Secrets Manager at launch:

```bash
#!/bin/bash
ACCESS_TOKEN=$(aws secretsmanager get-secret-value \
  --secret-id twingate/connector-1/access-token \
  --query SecretString --output text)
REFRESH_TOKEN=$(aws secretsmanager get-secret-value \
  --secret-id twingate/connector-1/refresh-token \
  --query SecretString --output text)

docker run -d \
  --name twingate-connector \
  -e TWINGATE_NETWORK="<tenant>" \
  -e TWINGATE_ACCESS_TOKEN="$ACCESS_TOKEN" \
  -e TWINGATE_REFRESH_TOKEN="$REFRESH_TOKEN" \
  -e TWINGATE_TIMESTAMP_FORMAT=2 \
  -e TWINGATE_LABEL_DEPLOYED_BY=ec2-userdata \
  --restart unless-stopped \
  twingate/connector:1
```

Deploy two instances in different AZs. Each instance needs its own token pair and a
dedicated Security Group with no inbound rules.

---

## EKS Helm Alternative

```bash
helm repo add twingate https://twingate.github.io/helm-charts
helm repo update

helm install twingate-connector-1 twingate/connector \
  --set connector.network="<tenant>" \
  --set connector.accessToken="<access-token>" \
  --set connector.refreshToken="<refresh-token>"
```

For production: use the External Secrets Operator to sync tokens from Secrets Manager
into Kubernetes Secrets. Deploy two Helm releases with separate token pairs and configure
pod anti-affinity to spread across nodes in different AZs
(`topology.kubernetes.io/zone`).
