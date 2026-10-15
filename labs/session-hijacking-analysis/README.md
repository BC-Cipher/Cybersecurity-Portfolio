# Session Hijacking & Network Traffic Analysis Lab
## Overview

This lab explored how session hijacking and traffic interception can affect web communications and how network analysis tools can be used to identify suspicious activity.

The exercises were completed in an authorized training environment and included both offensive security techniques and defensive traffic analysis.

## Objectives

- Understand how session hijacking attacks work
- Analyze HTTP requests and responses
- Practice intercepting web traffic through a configured proxy
- Examine authentication-related traffic
- Identify indicators of man-in-the-middle activity
- Detect suspicious network behavior using Wireshark

## Tools Used

- Caido
- Hetty
- Wireshark
- Bettercap
- Windows 11
- Windows Server
- Linux security environment

## Lab Activities

### Web Traffic Interception with Caido

Configured a controlled proxy environment and used Caido to inspect HTTP requests traveling between a client and web server.

Observed how intercepted requests could be reviewed and modified before being forwarded to the destination.

This demonstrated why session integrity, encrypted communication, and proper certificate validation are important for protecting web applications.

### HTTP Analysis with Hetty

Used Hetty as an HTTP proxy to capture and analyze web requests.

Reviewed GET and POST traffic and examined request contents to understand how information can be exposed when applications transmit sensitive data insecurely.

### Session Hijacking Detection with Wireshark

Captured network traffic in Wireshark while simulated malicious activity occurred in the lab environment.

Analyzed ARP traffic and observed an unusually high volume of ARP requests associated with the attacking system.

This demonstrated how packet analysis can help identify indicators of man-in-the-middle and session-hijacking activity.

## Security Concepts Demonstrated

- Session hijacking
- HTTP traffic interception
- Man-in-the-middle attacks
- Proxy configuration
- Packet capture and analysis
- ARP traffic analysis
- Authentication security
- Network monitoring
- Detection of suspicious network behavior

## Key Takeaways

This lab demonstrated that session security depends on more than authentication alone. If session information or network traffic is improperly protected, an attacker may be able to intercept or manipulate communications.

From a defensive perspective, packet analysis can reveal abnormal network behavior such as excessive ARP activity that may indicate an attempted man-in-the-middle attack.

The lab reinforced the importance of encrypted communications, secure session management, network monitoring, and traffic analysis as complementary security controls.

## Ethical Use

All activities were performed in an authorized cybersecurity training environment using designated lab systems. No testing was performed against external or unauthorized systems.
