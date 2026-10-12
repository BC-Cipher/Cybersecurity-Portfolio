# Network Analysis: IP Addressing, Subnetting & Autonomous Systems

**Environment:** Kali Linux  
**Tools:** ipcalc, Linux Command Line, Hurricane Electric BGP Toolkit  
**Focus:** IPv4 Addressing, CIDR, Subnet Calculation, Autonomous Systems

## Overview

During cybersecurity competition preparation, I practiced analyzing IPv4 networks, calculating subnet ranges, identifying valid host addresses, and researching autonomous systems using command-line tools and publicly available networking resources.

These activities strengthened my understanding of how IP addressing and routing information support network administration, security analysis, and reconnaissance.

## 1. IPv4 Addressing and CIDR Notation

Reviewed how IPv4 networks are divided using subnet masks and Classless Inter-Domain Routing (CIDR) notation.

CIDR prefixes indicate how many bits of an IPv4 address identify the network portion.

For example, the subnet `192.168.10.0/24` uses 24 bits for the network prefix, leaving 8 bits for host addresses.

Key concepts practiced:

- Network and host portions of IPv4 addresses
- Subnet masks and CIDR notation
- Network and broadcast addresses
- Usable host address ranges
- Subnet boundaries

## 2. Subnet Analysis Using ipcalc

Used the `ipcalc` utility in Kali Linux to examine subnet configurations.

**Example command:**

```bash
ipcalc 192.168.10.0/24
```

This command provides information such as:

- Network address
- Subnet mask
- First usable host
- Last usable host
- Broadcast address
- Number of available host addresses

**Example subnet:**

| Property | Value |
|---|---|
| Network | 192.168.10.0/24 |
| Subnet Mask | 255.255.255.0 |
| First Usable Host | 192.168.10.1 |
| Last Usable Host | 192.168.10.254 |
| Broadcast Address | 192.168.10.255 |
| Usable Hosts | 254 |

## 3. Calculating Usable Host Addresses

Practiced determining the number of usable IPv4 host addresses in conventional subnets.

Formula:

**Usable Hosts = 2^(32 - CIDR Prefix) - 2**

For example:

A `/26` subnet has 6 host bits.

2^6 - 2 = **62 usable host addresses**

The subtraction accounts for the network and broadcast addresses. Point-to-point `/31` networks and `/32` host routes are special cases.

## 4. Identifying Subnet Boundaries

Learned that the IP address written before a CIDR prefix is not always the actual network address.

For example:

```bash
ipcalc 192.168.10.75/26
```

The actual network is `192.168.10.64/26`, with a usable host range of `192.168.10.65` through `192.168.10.126`.

Understanding subnet boundaries is important when configuring routing, access controls, firewalls, and network segmentation.

## 5. Autonomous Systems and BGP Research

Explored how Autonomous System Numbers (ASNs) identify networks participating in interdomain routing.

Used publicly available BGP information to research:

- Autonomous System Numbers
- Organizations associated with an ASN
- Advertised IPv4 prefixes
- Relationships between IP address ranges and routing information

**Research resource:**

https://bgp.he.net/

An advertised prefix can help identify which autonomous system originates a route, although routing data alone does not establish ownership of every address in the prefix.

## 6. Professional Applications

These skills are relevant to:

- Network Administration
- Firewall Configuration
- Security Operations
- Network Reconnaissance
- Vulnerability Assessment
- Incident Response
- Network Segmentation and Access Control

## Key Takeaways

Subnetting is fundamental to understanding how networks are organized and secured.

Using tools such as `ipcalc` helps validate manual calculations and reduces configuration errors. Understanding network boundaries, address ranges, and autonomous systems also supports more accurate network investigations.

## Learning Context

This documentation describes general networking skills practiced during cybersecurity competition preparation. All examples are independently written and use standard networking concepts rather than competition-specific challenge data.
