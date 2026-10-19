# Infrastructure as Code Across AWS, Azure & Google Cloud

**Cloud infrastructure | Git versioning | Template debugging | Deployment validation**

## Overview

I worked with infrastructure templates across AWS, Microsoft Azure, and Google Cloud to configure resources, fix deployment errors, and check the results. Most of the labs started with existing templates that I modified, tested, and tracked with Git.

For my final AWS assignment, I designed a multi-tier web application in CloudFormation with network separation, load balancing, Auto Scaling, and an RDS database. The template design is documented here, but the submitted records do not establish that the entire final stack passed end-to-end deployment and failover testing.

| Platform | Tools | What I worked on |
|---|---|---|
| AWS | CloudFormation, Infrastructure Composer, Git | Debugged YAML templates, verified imports, committed revisions, and developed a scalable web architecture |
| Azure | ARM, Bicep, Azure CLI | Deployed and modified ARM resources, checked an App Service endpoint, and provisioned a storage account |
| Google Cloud | Deployment Manager, Jinja, Cloud Shell | Defined and deployed a VPC and Cloud Storage bucket, then checked the created resources |

## Final AWS Architecture

The final CloudFormation assignment focused on an e-commerce application with separate web, application, and database tiers.

```mermaid
flowchart TB
  Client["Web users"] --> ALB["Public Application Load Balancer"]
  subgraph Network["AWS VPC 10.0.0.0/16 | Two Availability Zones"]
    subgraph Public["Public subnets"]
      Web["Web EC2 Auto Scaling group"]
    end
    subgraph Private["Private subnets"]
      App["Application EC2 Auto Scaling group"]
      DB[("RDS MySQL Multi-AZ")]
    end
    ALB --> Web
    Web --> App
    App --> DB
  end
  CPU["CPU target tracking: 60%"] -.-> Web
  CPU -.-> App
```

This is a diagram of the template design, not a screenshot of one fully deployed environment.

| Area | Template configuration |
|---|---|
| Network | VPC `10.0.0.0/16`, two public and two private subnets across two Availability Zones |
| Web tier | Internet-facing Application Load Balancer, HTTP listener, instance target group |
| Access control | Security groups separate load balancer, web, application, and database traffic |
| Scaling | Web and application Auto Scaling groups; minimum 2 and maximum 4 instances; 60% CPU target |
| Database | MySQL RDS instance, `db.t3.micro`, 20 GiB, Multi-AZ, not publicly accessible |
| Data protection | Encrypted RDS storage, seven-day backup retention and deletion protection |
| Instance access | EC2 instance profile with Systems Manager permissions |

### Security Review

The design limits database access to the application security group and keeps the database from being directly publicly accessible. The RDS resource also specifies encryption, backups, and deletion protection.

Before using the template in production I would:

- Use HTTPS with an ACM certificate rather than public HTTP.
- Restrict SSH and favor Systems Manager Session Manager.
- Use a managed database secret; CloudFormation `NoEcho` masks parameter display but does not replace proper secrets management.
- Avoid hard-coding a Region-specific AMI identifier.
- Review NAT availability, logging, patch management and cost.
- Test the full application, scaling, failover, and restoration before making uptime claims.

## Verified Work Versus Design

**Verified in the lab records:** successful CloudFormation template imports in Infrastructure Composer, Git pushes containing revised templates, Azure ARM deployment checks, an Azure Bicep deployment returning `Succeeded`, and deployed Google Cloud VPC and bucket resources with a passing validation.

**Documented as a design:** the complete final AWS multi-tier architecture, including its Auto Scaling groups and Multi-AZ database. The final report includes configuration screenshots, but not a complete successful stack deployment or disaster-recovery test.

## Selected Infrastructure Templates

These files are based on my course templates. Example resource names were cleaned up for publication, and the AWS reference was revised to address issues in the original draft. Local format and reference checks do not replace cloud deployment tests.

| Platform | Template | Scope |
|---|---|---|
| AWS | [Web and RDS reference](templates/aws-web-rds-reference.yaml) | Two-tier variation with ALB, EC2 Auto Scaling and a private RDS database |
| AWS | [Three-AZ VPC](../../../labs/aws-cloudformation-iac/templates/vpc-three-az.yaml) | VPC, Internet Gateway, three public subnets, routes and outputs |
| Azure | [Parameterized App Service ARM template](../../../labs/azure-arm-bicep-iac/templates/app-service-parameterized.json) | App Service plan and web app with configurable name and location |
| Google Cloud | [Deployment configuration](../../../labs/google-cloud-deployment-manager/templates/deployment.yaml) | Jinja-based network and bucket definitions |

The [AWS reference YAML](templates/aws-web-rds-reference.yaml) is a simplified two-tier revision of the coursework design. It is **not** the complete three-tier final architecture shown above, and I have not claimed it was deployed. It includes a basic web-server bootstrap for the load balancer's HTTP health checks; it does not contain a complete e-commerce application.

## Related Labs

- [AWS CloudFormation Debugging & Version Control](../../../labs/aws-cloudformation-iac/)
- [Azure ARM & Bicep Deployment](../../../labs/azure-arm-bicep-iac/)
- [Google Cloud Deployment Manager](../../../labs/google-cloud-deployment-manager/)

**Skills:** AWS CloudFormation, Azure Resource Manager, Bicep, Google Cloud Deployment Manager, Jinja, YAML, JSON, Git, GitHub, template debugging, network segmentation, cloud security, deployment testing.

*Completed in authorized cloud training environments.*
