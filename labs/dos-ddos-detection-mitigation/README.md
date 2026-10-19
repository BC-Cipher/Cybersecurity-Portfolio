# DoS/DDoS Detection & Mitigation Lab

**Traffic Monitoring | Resource Impact Analysis | DDoS Detection | Source Blocking**

## Overview

I examined denial-of-service traffic in a controlled lab and used monitoring tools to investigate its impact on a Windows system.

I used traffic monitoring and Windows Resource Monitor to investigate suspicious connections, resource usage, and the effects of high-volume traffic.

## Tools & Technologies

- Anti DDoS Guardian
- Windows Resource Monitor
- TCP/IP
- Network Flow Analysis
- Windows 11
- Windows Server

---

## 1. DDoS Traffic Monitoring

Anti DDoS Guardian was used on the protected Windows host to monitor incoming and outgoing network connections in real time.

The interface provided source and destination information, ports, protocols, and traffic-volume data that could be used to identify unusually high-volume sessions.

![Anti DDoS Guardian traffic monitoring](screenshots/anti-ddos-guardian-monitoring.png)

*Anti DDoS Guardian monitoring network flows during the authorized denial-of-service exercise.*

### Security Takeaway

Effective DoS/DDoS defense depends on identifying abnormal traffic patterns quickly and correlating volume, source, destination, protocol, and connection-rate information.

---

## 2. System Resource Impact Analysis

Windows Resource Monitor was used to observe system behavior while controlled high-volume traffic was generated in the lab.

The captured evidence shows elevated CPU, memory, and network activity, demonstrating how availability attacks can consume system resources even when the host remains operational.

![Windows Resource Monitor under load](screenshots/windows-resource-monitor-dos-impact.png)

*Windows Resource Monitor used to observe system impact during controlled high-volume traffic generation.*

---

## 3. Mitigation Workflow

The associated defensive workflow included reviewing high-volume sessions in Anti DDoS Guardian and using its blocking controls to stop suspicious source addresses.

### Defensive Takeaway

Source blocking can be useful during a contained incident, but production DDoS resilience normally requires layered controls such as upstream filtering, rate limiting, connection limits, load balancing, CDN or scrubbing services, and continuous monitoring.

---

## Skills Demonstrated

- DoS/DDoS traffic analysis
- Network flow monitoring
- Resource utilization analysis
- Availability-impact assessment
- Source and port analysis
- Defensive traffic filtering
- Incident mitigation concepts
- Security monitoring
- Technical documentation

---

## Lessons Learned

This project reinforced that availability attacks are best understood through both network telemetry and host-level resource monitoring.

High-volume traffic can degrade system performance without immediately taking a system offline. Correlating flow data with CPU, memory, and network utilization provides stronger evidence for detection and response.

## Ethical Use

All denial-of-service testing documented in this project was performed in an authorized, isolated cybersecurity training environment against designated lab systems.
