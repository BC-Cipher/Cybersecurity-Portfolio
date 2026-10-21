# Project Portfolio

Larger projects that bring infrastructure, security, configuration, and analysis together.

Focused exercises are organized separately under [Technical Labs](../labs/).

## Infrastructure Automation & Configuration Management

### [Cross-Platform Infrastructure Automation & Configuration Management](automation/ansible-cross-platform-server-management/)

Managed Ubuntu and Windows Server 2019 from AlmaLinux with Ansible. Documented service deployments, Windows accounts and ACLs, DHCP, Windows Firewall, custom Python/Bash workflows, and reusable roles, with original test evidence and sanitized code examples.

[Browse automation projects](automation/)

## Network Infrastructure and Security

### [Secure Network Design, VLAN Segmentation, IoT Integration & Routing](networking/secure-network-design-vlan-iot-routing/)

A five-VLAN Cisco Packet Tracer network with DHCP, four managed IoT devices, simulated ISP connectivity, cable-to-fiber transition, MAC port-security testing, and RIPv2/OSPF routing.

### [Enterprise Network Integration, Segmentation & Security](networking/enterprise-network-integration-segmentation-security/)
Designed a simulated multi-location network in Cisco Packet Tracer. Configured routing, VLANs, DHCP, centralized authentication, and perimeter controls at the primary site, then reviewed remote-site exposure and single points of failure.

### [Switch Port Security and Access Control Validation](networking/switch-port-security-validation/)
Configured and tested MAC-based port restrictions in Packet Tracer, including shutdown and restrict actions, DHCP failure for unauthorized replacement devices, and recovery of an affected port.

### [Routing, Device Administration, IPv6 Security and Site-to-Site VPNs](networking/)
Cisco Packet Tracer case studies covering OSPF/BGP routing, TACACS+/RADIUS, SSH administration, ASA firewall configuration, OSPFv3, IPv6 access controls, and IPsec VPN/QoS testing. Includes original console screenshots and clear verification limits.

[Browse networking projects](networking/)

## Windows Infrastructure and Identity

### [Enterprise Windows Infrastructure, Active Directory and Container Services](windows/rsi-enterprise-infrastructure-capstone/)
Five-stage Windows infrastructure case study connecting Hyper-V deployment, a parent and child Active Directory domain, DHCP hot-standby failover, workstation policies, departmental file shares, and Docker-based IIS services. Includes original configuration screenshots and a security review.

### [Windows Server Infrastructure and Active Directory Administration](windows/enterprise-windows-domain-infrastructure/)
Hyper-V virtualization, Active Directory, DNS, DHCP, group permissions, CSV-based user provisioning, Group Policy, and delegated administration.

### [Windows Containers, Docker Networking, and IIS Deployment](windows/windows-container-iis-deployment/)
Windows Server Core containers, persistent storage, NAT networking, and a custom IIS image built with a Dockerfile.

[Browse Windows infrastructure projects](windows/)

## Linux Infrastructure and Security

### [Linux Infrastructure, Service Deployment & Security Operations](linux/linux-infrastructure-services-security/)

Multi-phase Linux case study covering QEMU/KVM guests, shared storage and Samba/Rsync, Nginx and Redis containers, LAMP/HTTPS, firewall policies, centralized Rsyslog, monitoring, and Bash/systemd automation. Includes test evidence and a review of production security considerations.

[Browse Linux projects](linux/)

## Incident Investigation and Machine Learning

### [Container Incident Investigation & Isolation Forest](ai-assisted-incident-investigation/)
Investigated persistent HTTP probing across a four-container lab, traced it to a background Bash script, and checked Isolation Forest anomalies against packet and process evidence. Includes an analysis of benign mDNS outliers and a [separate synthetic MitM model comparison](ai-assisted-incident-investigation/mitm-model-comparison.md).

## Cloud Infrastructure and Security

### [AWS Secure & Scalable Web Architecture](cloud/aws-secure-scalable-web-architecture/)
Built AWS network, compute, and database components across training labs, then documented how they fit into a scalable web architecture.

### [Infrastructure as Code Across AWS, Azure & Google Cloud](cloud/multicloud-infrastructure-as-code/)
Used CloudFormation, ARM, Bicep, and Deployment Manager to work with cloud resources across AWS, Azure, and Google Cloud. Includes the final AWS architecture design and linked template files.

[Browse the Cloud Portfolio](cloud/)

## Security Data and Database Design

### [Security Log Analysis & Relational Database Design](security-log-analysis-database-design/)
Cleaned and analyzed security log data in Excel, then developed an Access relational database with staging tables, saved queries, lookup relationships, and management reports.
