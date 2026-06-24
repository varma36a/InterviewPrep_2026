"""Additional AWS interview topics — expands aws section to 50+."""

from data.interview_content import InterviewItem

MARKET_ITEMS: dict[tuple[str, str], list[InterviewItem]] = {
    ("aws", "foundation"): [
        InterviewItem(
            "aws-ec2",
            "When should you choose Amazon EC2 for an application?",
            "EC2 gives full OS-level control, flexible sizing, and custom runtime setup for IaaS workloads.",
            "",
        ),
        InterviewItem(
            "aws-s3",
            "What is Amazon S3 and what are common use cases?",
            "S3 is durable object storage for backups, static assets, logs, and data lake workloads.",
            "",
        ),
        InterviewItem(
            "aws-iam",
            "How does AWS IAM secure access to cloud resources?",
            "IAM manages identities, authentication, and fine-grained authorization through policies.",
            "",
        ),
        InterviewItem(
            "aws-vpc",
            "What is an Amazon VPC in AWS networking?",
            "A VPC is an isolated virtual network where you define IP ranges, subnets, and routing.",
            "",
        ),
        InterviewItem(
            "aws-rds",
            "Why use Amazon RDS instead of self-managed databases on EC2?",
            "RDS automates backups, patching, failover, and scaling for managed relational databases.",
            "",
        ),
        InterviewItem(
            "aws-route53",
            "What role does Amazon Route 53 play in AWS architecture?",
            "Route 53 provides highly available DNS with health checks and routing policies.",
            "",
        ),
        InterviewItem(
            "aws-elb",
            "What does Elastic Load Balancing do for application traffic?",
            "ELB distributes incoming traffic across healthy targets to improve availability and scale.",
            "",
        ),
        InterviewItem(
            "aws-auto-scaling",
            "How does Auto Scaling improve resilience and cost?",
            "Auto Scaling adjusts capacity based on demand, keeping performance stable while minimizing waste.",
            "",
        ),
        InterviewItem(
            "aws-cloudwatch",
            "What capabilities does Amazon CloudWatch provide?",
            "CloudWatch collects metrics, logs, and events for monitoring, alerting, and operational visibility.",
            "",
        ),
        InterviewItem(
            "aws-shared-responsibility",
            "Explain the AWS Shared Responsibility Model.",
            "AWS secures the cloud infrastructure while customers secure their workloads, data, and configurations.",
            "",
        ),
        InterviewItem(
            "aws-regions-az",
            "What are Regions and Availability Zones in AWS?",
            "Regions are geographic locations; AZs are isolated datacenters for fault-tolerant design.",
            "",
        ),
        InterviewItem(
            "aws-ebs-volumes",
            "What are EBS volumes and how are they used?",
            "EBS provides persistent block storage for EC2 instances with SSD and HDD options.",
            "",
        ),
        InterviewItem(
            "aws-security-groups",
            "How do Security Groups protect AWS resources?",
            "Security Groups act as stateful virtual firewalls controlling inbound and outbound traffic rules.",
            "",
        ),
        InterviewItem(
            "aws-s3-storage-classes",
            "Why does S3 offer multiple storage classes?",
            "S3 storage classes optimize cost and retrieval characteristics based on access patterns.",
            "",
        ),
        InterviewItem(
            "aws-iam-roles-policies",
            "What is the difference between IAM roles and IAM policies?",
            "Policies define permissions; roles are assumable identities that receive those permissions.",
            "",
        ),
        InterviewItem(
            "aws-vpc-subnets-routing",
            "How do subnets and route tables work inside a VPC?",
            "Subnets segment network tiers while route tables direct traffic to gateways and endpoints.",
            "",
        ),
        InterviewItem(
            "aws-ec2-instance-types",
            "How do you choose the right EC2 instance type?",
            "Select families by workload profile: compute, memory, storage, or GPU optimization.",
            "",
        ),
        InterviewItem(
            "aws-cloudwatch-logs-alarms",
            "How are CloudWatch Logs and Alarms used together?",
            "Logs capture runtime events and alarms trigger notifications when metrics breach thresholds.",
            "",
        ),
    ],
    ("aws", "intermediate"): [
        InterviewItem(
            "aws-lambda",
            "What is AWS Lambda and when is it a good fit?",
            "Lambda runs event-driven serverless code without managing servers, ideal for bursty workloads.",
            "",
        ),
        InterviewItem(
            "aws-api-gateway",
            "What does Amazon API Gateway provide for APIs?",
            "API Gateway handles routing, auth, throttling, and monitoring for REST and HTTP APIs.",
            "",
        ),
        InterviewItem(
            "aws-sqs",
            "How does Amazon SQS decouple distributed systems?",
            "SQS queues messages between producers and consumers for reliable asynchronous processing.",
            "",
        ),
        InterviewItem(
            "aws-sns",
            "When do you use Amazon SNS?",
            "SNS is pub/sub messaging for fan-out notifications to queues, email, SMS, or Lambda.",
            "",
        ),
        InterviewItem(
            "aws-dynamodb",
            "What are the core design principles of DynamoDB?",
            "DynamoDB is a serverless key-value/document database optimized for predictable low latency.",
            "",
        ),
        InterviewItem(
            "aws-ecs",
            "What is Amazon ECS and how is it deployed?",
            "ECS orchestrates containers using EC2 or Fargate with integrated AWS networking and IAM.",
            "",
        ),
        InterviewItem(
            "aws-eks",
            "Why choose Amazon EKS for Kubernetes workloads?",
            "EKS provides managed Kubernetes control plane with AWS integrations for production clusters.",
            "",
        ),
        InterviewItem(
            "aws-cloudfront",
            "How does CloudFront improve web application delivery?",
            "CloudFront caches content at edge locations to reduce latency and offload origins.",
            "",
        ),
        InterviewItem(
            "aws-cognito",
            "What problem does Amazon Cognito solve?",
            "Cognito manages user sign-up, sign-in, federation, and token issuance for applications.",
            "",
        ),
        InterviewItem(
            "aws-waf",
            "How does AWS WAF protect public endpoints?",
            "WAF filters malicious HTTP requests using managed and custom rules before traffic reaches apps.",
            "",
        ),
        InterviewItem(
            "aws-step-functions",
            "When should Step Functions be used in serverless design?",
            "Step Functions orchestrates multi-step workflows with retries, branching, and state tracking.",
            "",
        ),
        InterviewItem(
            "aws-eventbridge",
            "What is Amazon EventBridge used for?",
            "EventBridge routes events between AWS services and applications for event-driven integration.",
            "",
        ),
        InterviewItem(
            "aws-secrets-manager",
            "Why is AWS Secrets Manager preferred over hardcoded credentials?",
            "Secrets Manager securely stores, rotates, and retrieves application secrets and database credentials.",
            "",
        ),
        InterviewItem(
            "aws-kms",
            "What is AWS KMS and how does envelope encryption work?",
            "KMS centrally manages encryption keys and integrates with AWS services for secure data protection.",
            "",
        ),
        InterviewItem(
            "aws-cloudformation",
            "What value does CloudFormation provide for infrastructure?",
            "CloudFormation enables repeatable infrastructure-as-code stacks with versioned templates.",
            "",
        ),
        InterviewItem(
            "aws-multi-az",
            "What does Multi-AZ deployment mean in AWS?",
            "Multi-AZ places redundant components across Availability Zones to improve fault tolerance.",
            "",
        ),
        InterviewItem(
            "aws-disaster-recovery",
            "What disaster recovery strategies are common on AWS?",
            "AWS DR patterns include backup/restore, pilot light, warm standby, and multi-site active-active.",
            "",
        ),
        InterviewItem(
            "aws-cost-optimization",
            "How do you optimize cloud spend in AWS?",
            "Use rightsizing, commitment discounts, storage lifecycle policies, and observability to control costs.",
            "",
        ),
        InterviewItem(
            "aws-serverless-patterns",
            "What are common AWS serverless architecture patterns?",
            "Patterns combine Lambda, API Gateway, SQS, SNS, and DynamoDB for scalable event-driven systems.",
            "",
        ),
        InterviewItem(
            "aws-security-best-practices",
            "What are practical AWS security best practices?",
            "Use least privilege IAM, encryption, logging, network segmentation, and continuous posture checks.",
            "",
        ),
        InterviewItem(
            "aws-vpc-endpoints",
            "Why are VPC endpoints important for private networking?",
            "VPC endpoints allow private access to AWS services without traversing the public internet.",
            "",
        ),
    ],
    ("aws", "advanced"): [
        InterviewItem(
            "aws-terraform",
            "How does Terraform fit into AWS platform engineering?",
            "Terraform codifies AWS infrastructure declaratively and supports reusable modules and automation.",
            "",
        ),
        InterviewItem(
            "aws-well-architected",
            "What is the AWS Well-Architected Framework?",
            "It is a design framework for reliability, security, performance, cost, and operational excellence.",
            "",
        ),
        InterviewItem(
            "aws-organizations",
            "How does AWS Organizations support governance at scale?",
            "Organizations manages multi-account structures, policies, and centralized billing.",
            "",
        ),
        InterviewItem(
            "aws-transit-gateway",
            "When should you introduce AWS Transit Gateway?",
            "Transit Gateway provides centralized hub-and-spoke routing across VPCs and on-prem networks.",
            "",
        ),
        InterviewItem(
            "aws-direct-connect",
            "What are key benefits of AWS Direct Connect?",
            "Direct Connect offers private, consistent, lower-latency connectivity from datacenters to AWS.",
            "",
        ),
        InterviewItem(
            "aws-site-to-site-vpn",
            "How does AWS Site-to-Site VPN work?",
            "Site-to-Site VPN creates encrypted IPsec tunnels between on-premises gateways and AWS.",
            "",
        ),
        InterviewItem(
            "aws-hybrid-connectivity",
            "How do you design robust hybrid connectivity in AWS?",
            "Hybrid designs combine Transit Gateway, VPN, and Direct Connect with BGP-based failover.",
            "",
        ),
        InterviewItem(
            "aws-control-tower",
            "What does AWS Control Tower automate?",
            "Control Tower automates landing zone setup with guardrails, account vending, and governance.",
            "",
        ),
        InterviewItem(
            "aws-guardduty-security-hub",
            "How do GuardDuty and Security Hub complement each other?",
            "GuardDuty detects threats while Security Hub aggregates findings and compliance posture.",
            "",
        ),
        InterviewItem(
            "aws-landing-zone",
            "What is an AWS landing zone and why is it critical?",
            "A landing zone is a governed multi-account baseline for secure, scalable cloud adoption.",
            "",
        ),
        InterviewItem(
            "aws-advanced-dr-patterns",
            "What advanced disaster recovery patterns are used on AWS?",
            "Advanced DR uses cross-region replication and automated failover for strict RTO/RPO requirements.",
            "",
        ),
    ],
}

MARKET_DETAILED: dict[str, dict] = {
    "aws-ec2": {
        "explanation": (
            "**Amazon EC2** is AWS compute infrastructure where you control the **operating system**, runtime, patch "
            "strategy, and host-level configuration. It is ideal for **lift-and-shift**, legacy dependencies, or "
            "software requiring custom kernel modules. In interviews, contrast EC2 with managed services by highlighting "
            "the trade-off between **control** and **operational overhead**."
        ),
        "code": """# Launch an EC2 instance
aws ec2 run-instances \\
  --image-id ami-0f58b397bc5c1f2e8 \\
  --instance-type t3.medium \\
  --key-name prod-key \\
  --security-group-ids sg-0123456789abcdef0 \\
  --subnet-id subnet-0123456789abcdef0 \\
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=api-ec2-01}]'""",
        "language": "bash",
        "key_points": [
            "Provides full OS and runtime control",
            "Supports broad workload compatibility",
            "Requires patching and capacity planning",
            "Best when managed platforms cannot fit",
        ],
    },
    "aws-s3": {
        "explanation": (
            "**Amazon S3** is highly durable **object storage** designed for virtually unlimited scale. It is commonly "
            "used for static web assets, backups, archives, and analytical datasets. Strong interview answers mention "
            "**11 nines durability**, lifecycle policies, and access controls via bucket policies and IAM."
        ),
        "code": """# Create bucket and enable versioning
aws s3api create-bucket --bucket interviewprep-data-prod --region ap-south-1 \\
  --create-bucket-configuration LocationConstraint=ap-south-1
aws s3api put-bucket-versioning --bucket interviewprep-data-prod \\
  --versioning-configuration Status=Enabled""",
        "language": "bash",
        "key_points": [
            "Object storage with very high durability",
            "Supports lifecycle and archival transitions",
            "Integrates with encryption and IAM",
            "Core service for backups and static content",
        ],
    },
    "aws-iam": {
        "explanation": (
            "**AWS IAM** controls authentication and authorization using users, groups, roles, and policies. The best "
            "practice is **least privilege** with short-lived credentials and role assumption. Strong answers explain "
            "that IAM policy evaluation includes explicit deny precedence over allow."
        ),
        "code": """{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject"],
      "Resource": "arn:aws:s3:::interviewprep-data-prod/*"
    }
  ]
}""",
        "language": "json",
        "key_points": [
            "Identity and access management core service",
            "Policies define permissions explicitly",
            "Roles enable temporary credentials",
            "Explicit deny always wins evaluation",
        ],
    },
    "aws-vpc": {
        "explanation": (
            "**Amazon VPC** gives you isolated network boundaries with configurable CIDRs, subnets, routing, and "
            "security controls. Interview-ready designs separate public and private tiers and route internet traffic "
            "through gateways. Mentioning **NAT Gateway**, route tables, and NACL/SG differences shows depth."
        ),
        "code": """# Create VPC with DNS support
aws ec2 create-vpc --cidr-block 10.20.0.0/16 --tag-specifications \\
  'ResourceType=vpc,Tags=[{Key=Name,Value=core-vpc}]'
aws ec2 modify-vpc-attribute --vpc-id vpc-0123456789abcdef0 --enable-dns-support
aws ec2 modify-vpc-attribute --vpc-id vpc-0123456789abcdef0 --enable-dns-hostnames""",
        "language": "bash",
        "key_points": [
            "Defines private network isolation in AWS",
            "Supports subnet and route segmentation",
            "Enables secure multi-tier architecture",
            "Works with NAT, IGW, and endpoints",
        ],
    },
    "aws-rds": {
        "explanation": (
            "**Amazon RDS** provides managed relational engines such as PostgreSQL, MySQL, and SQL Server. It reduces "
            "operational burden through automated backups, patching, and built-in high availability options. Great "
            "answers compare RDS with self-managed databases by focusing on **operability** and SLA."
        ),
        "code": """# Create PostgreSQL RDS instance
aws rds create-db-instance \\
  --db-instance-identifier orders-db-prod \\
  --engine postgres \\
  --db-instance-class db.m6g.large \\
  --allocated-storage 100 \\
  --master-username adminuser \\
  --master-user-password 'ChangeMeStrong123!' \\
  --multi-az \\
  --backup-retention-period 7""",
        "language": "bash",
        "key_points": [
            "Managed relational database service",
            "Automates backup and patching workflows",
            "Supports Multi-AZ for failover resilience",
            "Reduces toil versus self-managed databases",
        ],
    },
    "aws-route53": {
        "explanation": (
            "**Amazon Route 53** is a highly available DNS service with health checks and policy-based routing. It can "
            "perform weighted, latency-based, geolocation, and failover routing. Interview explanations should connect "
            "DNS decisions to business goals like **global performance** and **resilience**."
        ),
        "code": """{
  "Comment": "Weighted record set for blue/green",
  "Changes": [
    {
      "Action": "UPSERT",
      "ResourceRecordSet": {
        "Name": "api.example.com",
        "Type": "A",
        "SetIdentifier": "blue",
        "Weight": 80,
        "AliasTarget": {
          "HostedZoneId": "Z35SXDOTRQ7X7K",
          "DNSName": "dualstack.alb-123.ap-south-1.elb.amazonaws.com",
          "EvaluateTargetHealth": true
        }
      }
    }
  ]
}""",
        "language": "json",
        "key_points": [
            "Authoritative DNS with high availability",
            "Supports advanced routing policies",
            "Integrates health checks for failover",
            "Critical for global traffic management",
        ],
    },
    "aws-elb": {
        "explanation": (
            "**Elastic Load Balancing** distributes traffic to healthy targets across one or more AZs. In interviews, "
            "differentiate **ALB** (Layer 7), **NLB** (Layer 4), and **GWLB** (appliance insertion). Strong candidates "
            "also explain health checks, target groups, and TLS termination decisions."
        ),
        "code": """# Create an Application Load Balancer
aws elbv2 create-load-balancer \\
  --name web-alb \\
  --type application \\
  --subnets subnet-a1 subnet-b1 \\
  --security-groups sg-0abc123def4567890""",
        "language": "bash",
        "key_points": [
            "Distributes traffic across healthy targets",
            "ALB supports host and path routing",
            "NLB optimized for high-performance TCP",
            "Improves availability across AZs",
        ],
    },
    "aws-auto-scaling": {
        "explanation": (
            "**Auto Scaling** increases or decreases compute capacity based on demand signals like CPU, requests, or "
            "custom CloudWatch metrics. It improves performance consistency and avoids overprovisioning. Interview "
            "answers should mention minimum, desired, and maximum capacities with policy cooldown behavior."
        ),
        "code": """# Target tracking policy for ASG
aws autoscaling put-scaling-policy \\
  --auto-scaling-group-name api-asg \\
  --policy-name cpu-target-60 \\
  --policy-type TargetTrackingScaling \\
  --target-tracking-configuration '{
    "PredefinedMetricSpecification": {"PredefinedMetricType":"ASGAverageCPUUtilization"},
    "TargetValue": 60.0
  }'""",
        "language": "bash",
        "key_points": [
            "Scales capacity automatically with demand",
            "Balances cost and performance objectives",
            "Uses target tracking or step policies",
            "Depends on quality of metrics and thresholds",
        ],
    },
    "aws-cloudwatch": {
        "explanation": (
            "**Amazon CloudWatch** is the core AWS observability platform for metrics, logs, alarms, and events. "
            "Effective answers include metric namespaces, dimensions, custom metrics, and dashboarding. Mentioning "
            "composite alarms and anomaly detection demonstrates practical operations experience."
        ),
        "code": """# Put a custom application metric
aws cloudwatch put-metric-data \\
  --namespace "InterviewPrep/App" \\
  --metric-data '[
    {
      "MetricName":"CheckoutLatencyMs",
      "Dimensions":[{"Name":"Environment","Value":"prod"}],
      "Value":142,
      "Unit":"Milliseconds"
    }
  ]'""",
        "language": "bash",
        "key_points": [
            "Central service for metrics and alarms",
            "Supports custom and service metrics",
            "Enables operational dashboards and alerting",
            "Feeds automation through event integrations",
        ],
    },
    "aws-shared-responsibility": {
        "explanation": (
            "The **Shared Responsibility Model** splits security obligations between AWS and customers. AWS manages "
            "security **of the cloud** (datacenters, hardware, managed service internals), while customers manage "
            "security **in the cloud** (identity, data, network rules, patching where applicable). Interviewers expect "
            "you to show how responsibility changes across IaaS, containers, and serverless."
        ),
        "code": """shared_responsibility:
  aws:
    - physical_security
    - network_infrastructure
    - managed_service_platform
  customer:
    - iam_configuration
    - data_classification_and_encryption
    - operating_system_patching_for_ec2
    - application_security_testing""",
        "language": "yaml",
        "key_points": [
            "Boundary depends on service abstraction level",
            "Customers always own data and identity controls",
            "IaaS has more customer operational duties",
            "Model must map into compliance evidence",
        ],
    },
    "aws-regions-az": {
        "explanation": (
            "**Regions** are separate geographic areas, while **Availability Zones** are isolated datacenter groups "
            "within a region. Resilient architectures spread workloads across multiple AZs to tolerate localized failure. "
            "Interview responses should discuss latency, data residency, and cost trade-offs for multi-region design."
        ),
        "code": """# List Availability Zones in a region
aws ec2 describe-availability-zones \\
  --region ap-south-1 \\
  --query 'AvailabilityZones[].ZoneName' \\
  --output text""",
        "language": "bash",
        "key_points": [
            "Regions meet geography and compliance needs",
            "AZs provide fault-isolated deployment zones",
            "Multi-AZ improves availability within region",
            "Multi-region adds disaster recovery capability",
        ],
    },
    "aws-ebs-volumes": {
        "explanation": (
            "**Amazon EBS** provides persistent block storage for EC2 with performance tiers like gp3, io2, and st1. "
            "Use EBS snapshots for backup and point-in-time restore workflows. Interview-quality answers compare EBS "
            "with instance store and EFS based on persistence, latency, and sharing requirements."
        ),
        "code": """# Create a gp3 volume and attach to an instance
aws ec2 create-volume \\
  --availability-zone ap-south-1a \\
  --size 100 \\
  --volume-type gp3 \\
  --iops 3000 \\
  --throughput 125
aws ec2 attach-volume --volume-id vol-0123456789abcdef0 --instance-id i-0123456789abcdef0 --device /dev/xvdf""",
        "language": "bash",
        "key_points": [
            "Persistent block storage for EC2",
            "Multiple volume classes for workload profiles",
            "Snapshots support backup and DR workflows",
            "AZ-scoped unless restored in another zone",
        ],
    },
    "aws-security-groups": {
        "explanation": (
            "**Security Groups** are stateful virtual firewalls attached to ENIs, EC2, and other services. You define "
            "allow rules for inbound and outbound traffic; return traffic is automatically permitted. Strong interview "
            "answers compare Security Groups with stateless NACLs and emphasize least-open network posture."
        ),
        "code": """# Allow HTTPS ingress from internet
aws ec2 authorize-security-group-ingress \\
  --group-id sg-0123456789abcdef0 \\
  --protocol tcp \\
  --port 443 \\
  --cidr 0.0.0.0/0""",
        "language": "bash",
        "key_points": [
            "Stateful firewall at resource level",
            "Only allow rules are configured",
            "Inbound and outbound controlled independently",
            "Works with NACLs for layered defense",
        ],
    },
    "aws-s3-storage-classes": {
        "explanation": (
            "S3 storage classes balance **cost**, **retrieval time**, and **availability** for different data access "
            "patterns. Frequently accessed data fits Standard, while archive data moves to Glacier classes. Interviews "
            "often test if you can justify lifecycle transitions using real access frequency."
        ),
        "code": """{
  "Rules": [
    {
      "ID": "logs-lifecycle",
      "Status": "Enabled",
      "Filter": {"Prefix": "logs/"},
      "Transitions": [
        {"Days": 30, "StorageClass": "STANDARD_IA"},
        {"Days": 120, "StorageClass": "GLACIER_IR"},
        {"Days": 365, "StorageClass": "DEEP_ARCHIVE"}
      ]
    }
  ]
}""",
        "language": "json",
        "key_points": [
            "Choose class based on access pattern",
            "Lifecycle rules automate class transitions",
            "Archive classes reduce long-term storage cost",
            "Retrieval latency varies by class",
        ],
    },
    "aws-iam-roles-policies": {
        "explanation": (
            "**IAM policies** describe permissions, while **IAM roles** provide temporary identities that can assume "
            "those permissions. Roles are preferred for workloads because they avoid static long-lived credentials. "
            "In interviews, explain trust policy vs permission policy clearly."
        ),
        "code": """{
  "RoleName": "app-ec2-role",
  "AssumeRolePolicyDocument": {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {"Service": "ec2.amazonaws.com"},
        "Action": "sts:AssumeRole"
      }
    ]
  }
}""",
        "language": "json",
        "key_points": [
            "Policies define what actions are allowed",
            "Roles define who can assume identity",
            "Temporary credentials improve security posture",
            "Trust and permission policies are distinct",
        ],
    },
    "aws-vpc-subnets-routing": {
        "explanation": (
            "VPC designs use **subnets** to separate application tiers and **route tables** to control traffic paths. "
            "Public subnets route to an internet gateway, while private subnets route outbound via NAT or endpoints. "
            "Strong answers include deterministic routing and explicit egress strategy."
        ),
        "code": """# Associate private route table to private subnet
aws ec2 create-route \\
  --route-table-id rtb-0123456789abcdef0 \\
  --destination-cidr-block 0.0.0.0/0 \\
  --nat-gateway-id nat-0123456789abcdef0
aws ec2 associate-route-table \\
  --subnet-id subnet-0a1b2c3d4e5f6a7b8 \\
  --route-table-id rtb-0123456789abcdef0""",
        "language": "bash",
        "key_points": [
            "Subnets segment network tiers securely",
            "Routes determine packet destinations",
            "Private egress commonly uses NAT gateways",
            "Design should minimize unnecessary internet exposure",
        ],
    },
    "aws-ec2-instance-types": {
        "explanation": (
            "EC2 instance families are optimized for different workload profiles such as compute, memory, storage, or "
            "accelerated processing. Interviewers expect rational sizing based on CPU, RAM, network, and cost goals. "
            "Explain right-sizing with real telemetry instead of guessing."
        ),
        "code": """instance_selection:
  general_purpose: ["t3", "m7g"]
  compute_optimized: ["c7g", "c6i"]
  memory_optimized: ["r7g", "x2idn"]
  storage_optimized: ["i4i", "im4gn"]
  accelerated: ["g5", "p5"]""",
        "language": "yaml",
        "key_points": [
            "Choose family by workload bottleneck",
            "Use monitoring data for right-sizing",
            "Consider networking and EBS throughput limits",
            "Balance performance with pricing model",
        ],
    },
    "aws-cloudwatch-logs-alarms": {
        "explanation": (
            "**CloudWatch Logs** stores runtime logs and enables queries via Logs Insights, while **CloudWatch Alarms** "
            "trigger actions when metrics cross thresholds. Combined, they provide detection and response loops for "
            "incidents. Interview answers should include alarms wired to SNS, autoscaling, or incident tooling."
        ),
        "code": """# Create an alarm for high 5xx errors on ALB
aws cloudwatch put-metric-alarm \\
  --alarm-name alb-5xx-high \\
  --metric-name HTTPCode_Target_5XX_Count \\
  --namespace AWS/ApplicationELB \\
  --statistic Sum \\
  --period 60 \\
  --threshold 20 \\
  --comparison-operator GreaterThanThreshold \\
  --evaluation-periods 3 \\
  --alarm-actions arn:aws:sns:ap-south-1:123456789012:ops-alerts""",
        "language": "bash",
        "key_points": [
            "Logs provide detail for troubleshooting",
            "Alarms provide proactive alerting",
            "Integration enables automated incident response",
            "Queries and dashboards improve MTTR",
        ],
    },
    "aws-lambda": {
        "explanation": (
            "**AWS Lambda** runs code in response to events without provisioning servers. It scales automatically and "
            "bills per request and execution time, making it ideal for variable traffic. Strong interview coverage "
            "includes cold starts, idempotency, and concurrency controls."
        ),
        "code": """# Deploy Lambda function package
aws lambda create-function \\
  --function-name process-orders \\
  --runtime python3.12 \\
  --handler app.handler \\
  --role arn:aws:iam::123456789012:role/lambda-exec-role \\
  --zip-file fileb://function.zip \\
  --timeout 30 \\
  --memory-size 512""",
        "language": "bash",
        "key_points": [
            "Serverless compute with event triggers",
            "Scales automatically with demand",
            "Needs idempotent processing design",
            "Tune memory, timeout, and concurrency",
        ],
    },
    "aws-api-gateway": {
        "explanation": (
            "**Amazon API Gateway** provides managed API front doors with auth, throttling, caching, and observability. "
            "It integrates naturally with Lambda, ECS, and HTTP backends. Interviewers often check whether you can "
            "explain route design, request validation, and stages."
        ),
        "code": """openapi: 3.0.1
info:
  title: Orders API
  version: "1.0"
paths:
  /orders:
    get:
      x-amazon-apigateway-integration:
        type: aws_proxy
        httpMethod: POST
        uri: arn:aws:apigateway:ap-south-1:lambda:path/2015-03-31/functions/arn:aws:lambda:ap-south-1:123456789012:function:get-orders/invocations""",
        "language": "yaml",
        "key_points": [
            "Managed API lifecycle and security controls",
            "Supports REST and HTTP API patterns",
            "Integrates tightly with Lambda authorization",
            "Offers throttling and usage plan governance",
        ],
    },
    "aws-sqs": {
        "explanation": (
            "**Amazon SQS** is a durable queue that decouples producers from consumers in distributed systems. It helps "
            "absorb traffic spikes and improve reliability with retries and dead-letter queues. Interview answers should "
            "differentiate Standard vs FIFO and visibility timeout behavior."
        ),
        "code": """# Create queue and dead-letter policy
aws sqs create-queue --queue-name orders-main
aws sqs create-queue --queue-name orders-dlq
aws sqs set-queue-attributes \\
  --queue-url https://sqs.ap-south-1.amazonaws.com/123456789012/orders-main \\
  --attributes '{"RedrivePolicy":"{\\"deadLetterTargetArn\\":\\"arn:aws:sqs:ap-south-1:123456789012:orders-dlq\\",\\"maxReceiveCount\\":\\"5\\"}"}'""",
        "language": "bash",
        "key_points": [
            "Enables asynchronous workload decoupling",
            "DLQ captures repeatedly failed messages",
            "Visibility timeout controls processing lease",
            "FIFO supports ordering and deduplication",
        ],
    },
    "aws-sns": {
        "explanation": (
            "**Amazon SNS** is a pub/sub messaging service used for fan-out to SQS, Lambda, HTTP endpoints, and user "
            "notifications. It supports filtering policies to reduce unnecessary downstream processing. Strong interview "
            "examples include event notifications, incident alerts, and cross-service broadcasts."
        ),
        "code": """# Publish message to topic
aws sns publish \\
  --topic-arn arn:aws:sns:ap-south-1:123456789012:order-events \\
  --message '{"event":"OrderCreated","orderId":"A123"}' \\
  --message-attributes '{"eventType":{"DataType":"String","StringValue":"OrderCreated"}}'""",
        "language": "bash",
        "key_points": [
            "Fan-out messaging across multiple subscribers",
            "Supports delivery to SQS, Lambda, HTTP, email",
            "Filter policies reduce consumer noise",
            "Useful for notifications and event propagation",
        ],
    },
    "aws-dynamodb": {
        "explanation": (
            "**Amazon DynamoDB** is a serverless NoSQL database optimized for low-latency key-value and document access. "
            "Data modeling centers on access patterns using partition and sort keys. Interviewers expect discussion of "
            "GSIs, capacity modes, and hot partition mitigation."
        ),
        "code": """{
  "TableName": "orders",
  "BillingMode": "PAY_PER_REQUEST",
  "AttributeDefinitions": [
    {"AttributeName": "pk", "AttributeType": "S"},
    {"AttributeName": "sk", "AttributeType": "S"}
  ],
  "KeySchema": [
    {"AttributeName": "pk", "KeyType": "HASH"},
    {"AttributeName": "sk", "KeyType": "RANGE"}
  ]
}""",
        "language": "json",
        "key_points": [
            "Single-digit millisecond performance at scale",
            "Model schema around query access patterns",
            "Use GSIs for alternate query dimensions",
            "On-demand mode simplifies capacity planning",
        ],
    },
    "aws-ecs": {
        "explanation": (
            "**Amazon ECS** orchestrates containers with deep AWS integration for IAM, networking, and autoscaling. "
            "Teams can run tasks on EC2 for control or Fargate for serverless operations. Interview-ready answers cover "
            "task definitions, services, and deployment strategies."
        ),
        "code": """# Register ECS task definition
aws ecs register-task-definition \\
  --family orders-api \\
  --network-mode awsvpc \\
  --requires-compatibilities FARGATE \\
  --cpu 512 \\
  --memory 1024 \\
  --container-definitions '[{"name":"api","image":"123456789012.dkr.ecr.ap-south-1.amazonaws.com/orders:latest","portMappings":[{"containerPort":8080}]}]'""",
        "language": "bash",
        "key_points": [
            "Managed container orchestration on AWS",
            "Fargate removes host management tasks",
            "Task definitions declare container runtime config",
            "Integrates with ALB and CloudWatch natively",
        ],
    },
    "aws-eks": {
        "explanation": (
            "**Amazon EKS** offers a managed Kubernetes control plane while preserving upstream Kubernetes APIs. It suits "
            "teams requiring portability and ecosystem tooling with AWS networking/security integration. Strong interview "
            "responses compare EKS to ECS in terms of complexity and flexibility."
        ),
        "code": """# Create EKS cluster config snippet
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig
metadata:
  name: platform-eks
  region: ap-south-1
managedNodeGroups:
  - name: ng-general
    instanceType: m6i.large
    desiredCapacity: 3""",
        "language": "yaml",
        "key_points": [
            "Managed Kubernetes control plane by AWS",
            "Supports standard Kubernetes workloads",
            "Requires cluster operations maturity",
            "Best for complex microservice orchestration needs",
        ],
    },
    "aws-cloudfront": {
        "explanation": (
            "**Amazon CloudFront** is a global CDN that caches content near users to reduce latency and origin load. "
            "It supports dynamic acceleration, edge security, and signed URL access controls. Interview answers should "
            "mention cache behaviors, invalidations, and origin failover."
        ),
        "code": """# Create CloudFront invalidation after deployment
aws cloudfront create-invalidation \\
  --distribution-id E12ABC34DEF56G \\
  --paths "/*" """,
        "language": "bash",
        "key_points": [
            "Edge caching improves global response time",
            "Reduces origin traffic and infrastructure load",
            "Integrates with WAF and TLS at edge",
            "Supports fine-grained cache behavior policies",
        ],
    },
    "aws-cognito": {
        "explanation": (
            "**Amazon Cognito** handles user authentication, user directories, federation, and token issuance for apps. "
            "It supports OAuth2/OIDC flows and social/enterprise identity providers. Interview-quality responses explain "
            "User Pools vs Identity Pools and token-based authorization."
        ),
        "code": """# Create a Cognito user pool
aws cognito-idp create-user-pool \\
  --pool-name interviewprep-users \\
  --policies '{"PasswordPolicy":{"MinimumLength":12,"RequireUppercase":true,"RequireLowercase":true,"RequireNumbers":true,"RequireSymbols":true}}'""",
        "language": "bash",
        "key_points": [
            "Managed user sign-up and sign-in service",
            "Supports OIDC and SAML federation",
            "Issues JWTs for API authorization",
            "Separates authentication from application logic",
        ],
    },
    "aws-waf": {
        "explanation": (
            "**AWS WAF** protects HTTP applications from common web exploits and bot abuse. It can attach to CloudFront, "
            "ALB, and API Gateway with managed rule groups plus custom rules. Interview responses are stronger when they "
            "include tuning to reduce false positives."
        ),
        "code": """{
  "Name": "BlockSQLiRule",
  "Priority": 10,
  "Statement": {
    "SqliMatchStatement": {
      "FieldToMatch": {"Body": {}},
      "TextTransformations": [{"Type": "URL_DECODE", "Priority": 0}]
    }
  },
  "Action": {"Block": {}},
  "VisibilityConfig": {
    "SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true,
    "MetricName": "BlockSQLiRule"
  }
}""",
        "language": "json",
        "key_points": [
            "Protects against OWASP-style web attacks",
            "Supports managed and custom rule sets",
            "Deploys at edge or regional entry points",
            "Requires ongoing tuning for application behavior",
        ],
    },
    "aws-step-functions": {
        "explanation": (
            "**AWS Step Functions** orchestrates distributed workflows using visual state machines and JSON definitions. "
            "It provides retries, branching, parallelism, and execution history for reliability. Interviewers look for "
            "clear understanding of Standard vs Express workflow trade-offs."
        ),
        "code": """{
  "Comment": "Order workflow",
  "StartAt": "ValidateOrder",
  "States": {
    "ValidateOrder": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Next": "ChargePayment"
    },
    "ChargePayment": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "End": true
    }
  }
}""",
        "language": "json",
        "key_points": [
            "Coordinates multi-step service workflows",
            "Built-in retries and error handling",
            "Execution history aids observability",
            "Ideal for long-running business processes",
        ],
    },
    "aws-eventbridge": {
        "explanation": (
            "**Amazon EventBridge** is an event bus for loosely coupled integration between AWS services, SaaS sources, "
            "and custom applications. Rules match event patterns and route to targets like Lambda, SQS, or Step Functions. "
            "Strong interview answers include schema registry and event replay benefits."
        ),
        "code": """{
  "Source": ["com.interviewprep.orders"],
  "DetailType": ["OrderCreated"],
  "Detail": {
    "environment": ["prod"]
  }
}""",
        "language": "json",
        "key_points": [
            "Central event bus for decoupled architecture",
            "Pattern-based routing to multiple targets",
            "Supports SaaS and custom event producers",
            "Improves extensibility of microservice systems",
        ],
    },
    "aws-secrets-manager": {
        "explanation": (
            "**AWS Secrets Manager** stores sensitive values such as DB credentials and API keys with encryption and "
            "access control. It supports automated rotation using Lambda and native integrations. Interview responses "
            "should emphasize avoiding secrets in source code or plaintext config."
        ),
        "code": """# Store a JSON secret
aws secretsmanager create-secret \\
  --name prod/orders/db \\
  --secret-string '{"username":"appuser","password":"StrongP@ssw0rd!"}'""",
        "language": "bash",
        "key_points": [
            "Secure secret storage with KMS encryption",
            "Supports secret rotation automation",
            "Integrates with IAM for access control",
            "Eliminates hardcoded credentials risk",
        ],
    },
    "aws-kms": {
        "explanation": (
            "**AWS KMS** manages cryptographic keys and is central to encryption across AWS services. It supports "
            "customer-managed keys, key policies, and audit trails through CloudTrail. Interview-ready explanations "
            "cover **envelope encryption** and separation of key management from data storage."
        ),
        "code": """# Create a customer managed key
aws kms create-key \\
  --description "CMK for payment service data encryption" \\
  --key-usage ENCRYPT_DECRYPT \\
  --origin AWS_KMS""",
        "language": "bash",
        "key_points": [
            "Centralized key management service",
            "Enables encryption across AWS services",
            "Supports granular key policies and grants",
            "Provides auditable key usage trails",
        ],
    },
    "aws-cloudformation": {
        "explanation": (
            "**AWS CloudFormation** provisions infrastructure declaratively using version-controlled templates. It "
            "supports repeatable deployments, drift detection, and change sets for safer releases. Interviewers often "
            "evaluate whether candidates understand stack lifecycle and rollback behavior."
        ),
        "code": """AWSTemplateFormatVersion: "2010-09-09"
Description: "Simple S3 bucket stack"
Resources:
  AppBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: interviewprep-app-assets-prod
      VersioningConfiguration:
        Status: Enabled""",
        "language": "yaml",
        "key_points": [
            "Infrastructure-as-code with AWS-native templates",
            "Enables consistent environment provisioning",
            "Supports stack rollback and change previews",
            "Integrates with CI/CD release automation",
        ],
    },
    "aws-multi-az": {
        "explanation": (
            "**Multi-AZ** architecture deploys redundant components across Availability Zones to tolerate zone-level "
            "outages. It is a key reliability pattern for databases, load balancers, and compute tiers. Strong interview "
            "answers differentiate Multi-AZ (HA) from Multi-Region (DR)."
        ),
        "code": """high_availability_pattern:
  load_balancer:
    azs: [ap-south-1a, ap-south-1b]
  app_tier:
    asg_spread_across_azs: true
  database:
    rds_multi_az: true""",
        "language": "yaml",
        "key_points": [
            "Protects against single-AZ failures",
            "Common baseline for production reliability",
            "Often required for SLA commitments",
            "Different objective than cross-region DR",
        ],
    },
    "aws-disaster-recovery": {
        "explanation": (
            "AWS disaster recovery strategies map to target **RTO/RPO** goals and budget constraints. Typical patterns "
            "include backup/restore, pilot light, warm standby, and active-active multi-site. Interview responses should "
            "explain trade-offs between recovery speed, complexity, and operating cost."
        ),
        "code": """dr_strategies:
  backup_restore:
    rto: "hours to days"
    rpo: "hours"
  pilot_light:
    rto: "tens of minutes"
    rpo: "minutes"
  warm_standby:
    rto: "minutes"
    rpo: "near-zero"
  active_active:
    rto: "near-zero"
    rpo: "near-zero" """,
        "language": "yaml",
        "key_points": [
            "Choose strategy based on RTO and RPO",
            "Higher resilience usually increases cost",
            "Automation is critical for predictable recovery",
            "Frequent DR drills validate real readiness",
        ],
    },
    "aws-cost-optimization": {
        "explanation": (
            "Cost optimization on AWS requires continuous visibility, rightsizing, and architecture decisions. Strong "
            "interview answers mention Savings Plans, Reserved Instances, spot usage, and storage lifecycle policies. "
            "It is important to tie optimization to business outcomes, not only lower spend."
        ),
        "code": """# AWS CLI Cost Explorer query example
aws ce get-cost-and-usage \\
  --time-period Start=2026-06-01,End=2026-06-24 \\
  --granularity DAILY \\
  --metrics UnblendedCost \\
  --group-by Type=DIMENSION,Key=SERVICE""",
        "language": "bash",
        "key_points": [
            "Use telemetry to drive rightsizing decisions",
            "Apply commitment discounts for steady workloads",
            "Automate storage and idle resource cleanup",
            "Track unit economics alongside raw spend",
        ],
    },
    "aws-serverless-patterns": {
        "explanation": (
            "Common AWS serverless patterns combine **API Gateway + Lambda + DynamoDB**, event fan-out with SNS/SQS, "
            "and orchestration with Step Functions. Good interview answers show asynchronous boundaries, retries, and "
            "idempotency keys for robustness. Mentioning observability and dead-letter handling strengthens credibility."
        ),
        "code": """serverless_reference_architecture:
  ingestion:
    - API Gateway
    - Lambda
  async_processing:
    - EventBridge
    - SQS
    - Lambda consumers
  persistence:
    - DynamoDB
  orchestration:
    - Step Functions""",
        "language": "yaml",
        "key_points": [
            "Build loosely coupled event-driven systems",
            "Use queues for backpressure and retries",
            "Design handlers to be idempotent",
            "Instrument latency and failure paths deeply",
        ],
    },
    "aws-security-best-practices": {
        "explanation": (
            "AWS security best practices include **least privilege IAM**, encryption in transit/at rest, centralized "
            "logging, and continuous posture assessment. Mature teams automate guardrails with Organizations, SCPs, and "
            "policy checks. Interviewers value practical examples of prevention and detection working together."
        ),
        "code": """security_baseline:
  identity:
    - enforce_mfa_for_human_users
    - use_roles_instead_of_access_keys
  data:
    - enable_kms_encryption
    - enforce_tls_everywhere
  detection:
    - cloudtrail_all_regions
    - guardduty_enabled
  governance:
    - scp_restrict_root_usage""",
        "language": "yaml",
        "key_points": [
            "Identity controls are first security boundary",
            "Encrypt sensitive data by default",
            "Centralized logs enable threat detection",
            "Automated guardrails reduce configuration drift",
        ],
    },
    "aws-vpc-endpoints": {
        "explanation": (
            "**VPC endpoints** allow private connectivity from VPC resources to AWS services without internet gateways, "
            "NAT, or public IP exposure. Gateway endpoints are used for S3/DynamoDB, while interface endpoints use ENIs "
            "for many services. Interview answers should mention tighter security and predictable egress cost."
        ),
        "code": """# Create interface endpoint for Secrets Manager
aws ec2 create-vpc-endpoint \\
  --vpc-id vpc-0123456789abcdef0 \\
  --service-name com.amazonaws.ap-south-1.secretsmanager \\
  --vpc-endpoint-type Interface \\
  --subnet-ids subnet-0a1b2c3d4e5f6a7b8 subnet-0123abcd4567efgh8 \\
  --security-group-ids sg-0123456789abcdef0""",
        "language": "bash",
        "key_points": [
            "Private service access without public internet",
            "Gateway and interface endpoint models differ",
            "Improves network security posture significantly",
            "Can reduce NAT gateway dependency and cost",
        ],
    },
    "aws-terraform": {
        "explanation": (
            "**Terraform** is widely used to provision AWS resources through declarative modules and state management. "
            "It enables reusable platform patterns, peer reviews, and automated provisioning pipelines. Interview-ready "
            "discussion should include remote state locking and plan/apply workflow discipline."
        ),
        "code": """provider "aws" {
  region = "ap-south-1"
}

resource "aws_s3_bucket" "stateful_assets" {
  bucket = "interviewprep-platform-assets-prod"
}
""",
        "language": "yaml",
        "key_points": [
            "Declarative multi-service infrastructure provisioning",
            "Modules improve reuse and standardization",
            "Remote state with locking prevents conflicts",
            "Plan review improves deployment safety",
        ],
    },
    "aws-well-architected": {
        "explanation": (
            "The **AWS Well-Architected Framework** helps teams evaluate workloads across six pillars: operational "
            "excellence, security, reliability, performance efficiency, cost optimization, and sustainability. In "
            "interviews, discuss it as a continuous improvement process, not a one-time checklist."
        ),
        "code": """well_architected_review:
  workload: payments-api
  pillars:
    - operational_excellence
    - security
    - reliability
    - performance_efficiency
    - cost_optimization
    - sustainability""",
        "language": "yaml",
        "key_points": [
            "Structured framework for architecture trade-offs",
            "Covers six pillars of cloud excellence",
            "Used repeatedly as systems evolve",
            "Findings should drive prioritized remediation",
        ],
    },
    "aws-organizations": {
        "explanation": (
            "**AWS Organizations** enables centralized governance for multi-account environments. You can apply Service "
            "Control Policies, consolidate billing, and automate account provisioning. Interview responses should connect "
            "organizations to blast-radius reduction and delegated administration models."
        ),
        "code": """{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": ["ec2:RunInstances"],
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:RequestedRegion": ["ap-south-1", "us-east-1"]
        }
      }
    }
  ]
}""",
        "language": "json",
        "key_points": [
            "Central governance for multi-account estates",
            "SCPs define permission boundaries globally",
            "Consolidated billing improves financial visibility",
            "Supports secure account lifecycle management",
        ],
    },
    "aws-transit-gateway": {
        "explanation": (
            "**AWS Transit Gateway** simplifies network topology by acting as a central routing hub for VPCs, VPNs, and "
            "Direct Connect gateways. It removes the operational complexity of full-mesh peering. Interviewers often ask "
            "about route domain segmentation and inspection patterns."
        ),
        "code": """# Create Transit Gateway
aws ec2 create-transit-gateway \\
  --description "Central network hub" \\
  --options AmazonSideAsn=64512,AutoAcceptSharedAttachments=enable,DefaultRouteTableAssociation=enable""",
        "language": "bash",
        "key_points": [
            "Hub-and-spoke architecture for large networks",
            "Reduces VPC peering complexity dramatically",
            "Supports hybrid attachments and routing domains",
            "Improves centralized network governance controls",
        ],
    },
    "aws-direct-connect": {
        "explanation": (
            "**AWS Direct Connect** provides private, dedicated connectivity from on-premises sites to AWS. It improves "
            "consistency, throughput, and often cost for predictable high-volume transfer. In interviews, compare it with "
            "VPN on latency, reliability, and operational setup requirements."
        ),
        "code": """hybrid_connectivity:
  primary:
    type: direct_connect
    bandwidth: 1Gbps
    routing: bgp
  backup:
    type: site_to_site_vpn
    failover: automatic""",
        "language": "yaml",
        "key_points": [
            "Private link avoids internet variability",
            "Suitable for predictable high-throughput traffic",
            "Uses BGP for dynamic route exchange",
            "Commonly paired with VPN for resilience",
        ],
    },
    "aws-site-to-site-vpn": {
        "explanation": (
            "**Site-to-Site VPN** establishes encrypted IPsec tunnels between customer gateways and AWS VPN gateways. "
            "It is quick to provision and cost-effective for many hybrid use cases. Interviewers expect knowledge of "
            "redundant tunnels and route propagation behavior."
        ),
        "code": """# Create customer gateway and VPN connection
aws ec2 create-customer-gateway \\
  --type ipsec.1 \\
  --public-ip 203.0.113.10 \\
  --bgp-asn 65010
aws ec2 create-vpn-connection \\
  --type ipsec.1 \\
  --customer-gateway-id cgw-0123456789abcdef0 \\
  --vpn-gateway-id vgw-0123456789abcdef0""",
        "language": "bash",
        "key_points": [
            "Encrypted tunnels for hybrid connectivity",
            "Fast deployment compared to private circuits",
            "Supports dynamic routing with BGP",
            "Includes redundant tunnels for availability",
        ],
    },
    "aws-hybrid-connectivity": {
        "explanation": (
            "Hybrid connectivity architecture blends Direct Connect, VPN, Transit Gateway, and route controls for secure "
            "integration across cloud and datacenters. High-quality interview answers describe active/active or active/"
            "passive routing with failover automation and observability."
        ),
        "code": """hybrid_design:
  core_hub: transit_gateway
  on_prem_primary: direct_connect
  on_prem_backup: site_to_site_vpn
  routing:
    - bgp_communities
    - route_preference_controls
  monitoring:
    - cloudwatch_vpn_tunnel_state
    - dx_connection_metrics""",
        "language": "yaml",
        "key_points": [
            "Combines multiple connectivity options strategically",
            "BGP policies control preferred traffic paths",
            "Requires redundancy and failure testing",
            "Monitoring validates end-to-end network health",
        ],
    },
    "aws-control-tower": {
        "explanation": (
            "**AWS Control Tower** automates landing zone setup using best-practice guardrails, account factory, and "
            "centralized governance integrations. It accelerates secure multi-account adoption with consistent baselines. "
            "Interviewers value understanding of preventive vs detective guardrails."
        ),
        "code": """control_tower_baseline:
  ou_structure:
    - Security
    - Sandbox
    - Workloads
  guardrails:
    preventive:
      - disallow_public_s3_buckets
    detective:
      - detect_unencrypted_ebs""",
        "language": "yaml",
        "key_points": [
            "Automates enterprise landing zone deployment",
            "Applies governance guardrails consistently",
            "Supports managed account vending workflows",
            "Improves speed and compliance for cloud adoption",
        ],
    },
    "aws-guardduty-security-hub": {
        "explanation": (
            "**Amazon GuardDuty** detects threats using log and DNS analysis, while **AWS Security Hub** aggregates "
            "security findings and compliance posture into a unified view. Together they provide detection and governance "
            "at scale. Strong interview answers include automated remediation workflows."
        ),
        "code": """{
  "Findings": {
    "GuardDuty": {
      "type": "UnauthorizedAccess:IAMUser/ConsoleLogin",
      "severity": 8.0
    },
    "SecurityHub": {
      "control": "S3.8",
      "status": "FAILED"
    }
  }
}""",
        "language": "json",
        "key_points": [
            "GuardDuty specializes in threat detection telemetry",
            "Security Hub centralizes and normalizes findings",
            "Combined view improves response prioritization",
            "Automations can trigger tickets or remediation",
        ],
    },
    "aws-landing-zone": {
        "explanation": (
            "An **AWS landing zone** is a pre-configured multi-account foundation with identity, logging, networking, "
            "and security baselines. It enables teams to onboard workloads quickly without re-solving governance each time. "
            "Interview-level depth includes account boundaries, shared services, and policy inheritance."
        ),
        "code": """landing_zone_components:
  identity:
    - aws_sso_center
  security:
    - centralized_cloudtrail
    - guardduty
    - security_hub
  networking:
    - transit_gateway
    - inspection_vpc
  governance:
    - organizations
    - service_control_policies""",
        "language": "yaml",
        "key_points": [
            "Establishes secure, scalable cloud foundation",
            "Defines account structure and guardrails early",
            "Centralizes shared security and logging services",
            "Speeds compliant workload onboarding significantly",
        ],
    },
    "aws-advanced-dr-patterns": {
        "explanation": (
            "Advanced DR on AWS targets strict continuity needs using cross-region replication, immutable backups, and "
            "automated failover orchestration. Patterns include active-active APIs, Aurora global databases, and Route 53 "
            "health-based routing. Interview answers should tie architecture choices directly to **RTO/RPO objectives**."
        ),
        "code": """advanced_dr:
  data:
    - aurora_global_database
    - s3_cross_region_replication
  compute:
    - multi_region_active_active
    - immutable_amis_in_secondary_region
  traffic_management:
    - route53_health_checks
    - failover_routing_policy
  automation:
    - runbooks_in_step_functions
    - periodic_game_days""",
        "language": "yaml",
        "key_points": [
            "Targets near-zero downtime disaster recovery",
            "Requires cross-region data replication strategy",
            "Failover must be automated and tested regularly",
            "Architecture must match explicit business RTO/RPO",
        ],
    },
}
