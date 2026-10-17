# AWS VPC and EC2 Web Infrastructure

Configured a two-Availability-Zone Amazon VPC with public and private subnets, route tables, an Internet Gateway, NAT Gateway, security groups, and an Amazon Linux EC2 web server.

## Network design

| Component | CIDR |
|---|---|
| VPC | 10.0.0.0/16 |
| Public subnet A | 10.0.0.0/24 |
| Private subnet A | 10.0.1.0/24 |
| Public subnet B | 10.0.2.0/24 |
| Private subnet B | 10.0.3.0/24 |

## Work performed

Configured routes for the public and private subnets, deployed an EC2 web server in a public subnet and validated browser access. Used a security group to control HTTP traffic.

## Security analysis

Private subnets used NAT for outbound access. Security groups controlled inbound connections. A production internet-facing application should use HTTPS and restricted administration.

*AWS Academy training environment.*
