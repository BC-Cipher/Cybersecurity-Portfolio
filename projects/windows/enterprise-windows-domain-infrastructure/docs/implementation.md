# Implementation Notes

These notes summarize my CYB360 Windows Server infrastructure assignments. The individual exercises were completed in a training lab and were not necessarily maintained as one continuously running environment.

## 1. Hyper-V provisioning and networking

I configured a Windows Server 2019 Hyper-V host, storage locations, and Generation 2 server and client VMs. I created reusable base images and differencing disks, set memory and startup properties, installed Windows Server Core and Desktop Experience, and worked with virtual switches, NAT, and IP configuration.

The base-image deployment lab passed **24** automated checks; the virtual networking lab passed **17**; and the Hyper-V performance assessment passed **35**.

Evidence filenames: `01-hyperv-provisioning.png`, `02-hyperv-network-validation.png`, and `03-hyperv-performance-assessment.png`. See [screenshot index](../screenshots/).

## 2. Active Directory, DNS, and DHCP

I installed Active Directory Domain Services, created a forest, configured accounts and clients, and managed DNS name resolution. The DNS work included primary and secondary zones, NS records, forwarding, and replication-related configuration. The DHCP exercises covered server installation and authorization, scopes, address exclusions, and options.

Examples of PowerShell commands used to inspect DNS settings:

```powershell
Get-DnsServerZone
Get-DnsServerForwarder
Get-DnsServerResourceRecord -ZoneName kmw.org
```

These are instructional examples, not a complete replayable setup script. The AD DS, advanced DNS, and DHCP assessments returned **12**, **6**, and **13** passing checks respectively.

## 3. Organizational design and user provisioning

In the directory logical-design lab, organizational units represented office locations including Greenville, Richmond, Greensboro, and Columbia, along with departments such as Management, Administration, and Projects.

The exercise used a **449-record** employee training dataset containing name, location, department, and account naming fields. PowerShell-based provisioning created users and placed them into the intended OUs.

Example of the OU management approach:

```powershell
New-ADOrganizationalUnit -Name Greensboro -Path 'DC=KMW,DC=local'
Get-ADOrganizationalUnit -Filter * |
    Format-Table -AutoSize DistinguishedName, Name
```

The associated assessment passed **38** checks. The original CSV is omitted from the public project.

## 4. Security groups and resource permissions

I worked with global security groups organized by department and location, domain-local groups tied to resources, nested membership, SMB shares, and NTFS permissions. The grouping model follows the AGDLP approach: **Accounts → Global groups → Domain Local groups → Permissions**.

This makes it easier to change department membership without repeatedly editing individual folder ACLs. The directory objects and permissions exercise passed **33** checks.

## 5. Group Policy and administrative delegation

I created and linked Group Policy objects and explored user/computer settings, software assignment, software publication, and GPO processing. The software installation exercise involved Chrome, 7-Zip, and Microsoft Baseline Security Analyzer in a classroom environment.

A separate delegation exercise assigned OU-level administration to location-specific groups and password-reset responsibilities to a designated group. The corresponding checks passed **11** for software deployment and **4** for delegation.

## Limitations

The included test counts verify what the course scripts checked at the time, not a production audit. The original grading scripts and complete command history are not published. Several classroom settings would need additional security review before production use.

[Project overview](../README.md) | [Validation notes](validation.md) | [Screenshot index](../screenshots/)
