# AWS IAM Access Control & Policy Validation

## Overview

This hands-on AWS lab focused on identity and access management, permission design, and authorization testing. I worked with IAM users, groups, AWS managed policies, and an inline policy to assign access based on job function and verify that each identity could perform only the intended actions.

**Environment:** AWS Identity and Access Management, Amazon S3, Amazon EC2  
**Focus:** least privilege, group-based permissions, policy analysis, access validation

## Scenario

Three users required different levels of AWS access:

| User | IAM group | Intended access |
|---|---|---|
| user-1 | S3-Support | Read-only access to Amazon S3 |
| user-2 | EC2-Support | Read-only access to Amazon EC2 |
| user-3 | EC2-Admin | View, start, and stop EC2 instances |

Rather than assigning permissions directly to individual users, access was granted through IAM groups aligned to each support or administration function.

## What I Implemented

- Reviewed existing IAM users and group membership
- Inspected the AWS managed policy `AmazonEC2ReadOnlyAccess`
- Inspected the AWS managed policy `AmazonS3ReadOnlyAccess`
- Reviewed an EC2 administration inline policy that allowed instance viewing, starting, and stopping
- Mapped users to groups according to job responsibilities
- Used separate IAM user sessions to validate effective permissions
- Confirmed both successful access and expected authorization failures

## Permission Validation

The lab included positive and negative authorization testing rather than only checking that a policy was attached.

| Test | Expected result | Validation |
|---|---|---|
| user-1 lists S3 resources | Allowed | S3 read access available |
| user-1 accesses EC2 | Denied | No EC2 permission assigned |
| user-2 views EC2 instances | Allowed | Read-only EC2 access available |
| user-2 stops an EC2 instance | Denied | Read-only policy blocked modification |
| user-2 lists S3 buckets | Denied | No S3 permission assigned |
| user-3 stops an EC2 instance | Allowed | EC2 administration policy permitted the action |

## Security Principles Demonstrated

**Least privilege:** Each user received only the access required for the assigned role.

**Group-based access control:** Permissions were inherited through IAM groups, which is easier to manage consistently than assigning one-off permissions to every user.

**Policy interpretation:** I reviewed policy effects, actions, and resources to understand what each policy permitted.

**Authorization testing:** I verified controls from the user perspective, including intentionally testing actions that should fail.

**Separation of duties:** Storage support, compute support, and compute administration were assigned different capabilities.

## Production Hardening

For a production AWS environment, I would strengthen this design by:

- Requiring multi-factor authentication for privileged access
- Favoring federated access and temporary credentials through AWS IAM Identity Center or assumable roles
- Avoiding long-lived access keys unless a workload specifically requires them
- Reviewing permissions regularly and removing unused access
- Using AWS CloudTrail for audit visibility
- Using IAM Access Analyzer to identify unintended external or cross-account access

## Skills Demonstrated

AWS IAM, users and groups, managed policies, inline policies, least privilege, authorization testing, Amazon S3 permissions, Amazon EC2 permissions, access-control troubleshooting, cloud security fundamentals

## Related Project

See [AWS Secure & Scalable Web Architecture](../../projects/cloud/aws-secure-scalable-web-architecture/) for the broader cloud infrastructure project.

> This lab was completed in an AWS training environment. Credentials, account identifiers, and restricted course materials are not included in this public portfolio.
