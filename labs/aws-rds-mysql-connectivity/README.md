# Amazon RDS MySQL Provisioning & Connectivity

## Overview
These RDS exercises covered database instance configuration, subnet-group selection, access control, and connecting a MySQL client to an AWS-hosted relational database.

**Services:** Amazon RDS for MySQL, Amazon VPC, security groups  
**Client:** MySQL Workbench

## Work Completed
- Created or inspected database security-group settings in a training VPC.
- Configured a DB subnet group spanning subnets in multiple Availability Zones.
- Inspected database connectivity and endpoint settings.
- Worked with an RDS MySQL database instance.
- Used MySQL Workbench to configure a client connection and documented a successful connection test in the introductory RDS exercise.

## Troubleshooting Record
A separate “Build a Database Server” report explicitly records that the exercise's web-server address did not load in the browser. I investigated the console-side configuration, but I have not claimed that the address-book web application worked in that attempt. This distinction matters when interpreting the evidence.

## Evidence to Add
Save under [screenshots/](screenshots/):
- `rds-db-subnet-group.png`: subnets across multiple Availability Zones.
- `rds-connectivity.png`: RDS connectivity and endpoint configuration.
- `mysql-connection-success.png`: successful MySQL Workbench connection test from the separate introductory RDS exercise.

## Security & Production Hardening
- Keep databases in private subnets with no unnecessary public endpoint.
- Permit MySQL TCP/3306 only from designated application/client security groups.
- Enable encryption, backups, monitoring, and suitable retention policies.
- Store passwords in Secrets Manager rather than code or screenshots.
- Use Multi-AZ where availability requirements justify the cost.

## Key Takeaway
Database access involves more than a running RDS instance. Network routing, security-group permissions, endpoints, authentication, and client connectivity all need validation.
