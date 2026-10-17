# Network Fundamentals & Address Analysis

**Environment:** Kali Linux  
**Tools:** ipcalc, Linux Command Line, Hurricane Electric BGP Toolkit  
**Focus:** IPv4 Addressing, CIDR, Subnet Calculation, Autonomous Systems

## Overview

During cybersecurity competition preparation, I practiced analyzing IPv4 networks, calculating subnet ranges, identifying valid host addresses, and researching autonomous systems using command-line tools and publicly available networking resources.

These activities strengthened my understanding of how IP addressing and routing information support network administration, security analysis, and reconnaissance.

## 1. IPv4 Addressing and CIDR Notation

Reviewed how IPv4 networks are divided using subnet masks and Classless Inter-Domain Routing (CIDR) notation.

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

This provides the network address, subnet mask, usable host range, broadcast address, and number of available host addresses.

## 3. Calculating Usable Host Addresses

Practiced determining the number of usable IPv4 host addresses in conventional subnets.

**Usable Hosts = 2^(32 - CIDR Prefix) - 2**

For example, a `/26` subnet provides 62 conventional usable host addresses. Point-to-point `/31` networks and `/32` host routes are special cases.

## 4. Identifying Subnet Boundaries

Used `ipcalc` to validate subnet boundaries and distinguish a host address from the actual network address.

Understanding subnet boundaries is important when configuring routing, access controls, firewalls, and network segmentation.

## 5. Autonomous Systems and BGP Research

Used publicly available BGP information to research:

- Autonomous System Numbers
- Organizations associated with an ASN
- Advertised IPv4 prefixes
- Relationships between IP address ranges and routing information

Routing data can help identify which autonomous system originates a route, although routing information alone does not establish ownership of every address in a prefix.

## Professional Applications

These skills support network administration, firewall configuration, security operations, network reconnaissance, vulnerability assessment, incident response, and network segmentation.

## Lessons Learned

Subnetting is fundamental to understanding how networks are organized and secured.

Using tools such as `ipcalc` helps validate manual calculations and reduce configuration errors. Understanding network boundaries, address ranges, and autonomous systems also supports more accurate network investigations.

## Learning Context

This documentation describes general networking skills practiced during cybersecurity competition preparation. All examples are independently written and use standard networking concepts rather than competition-specific challenge data.
