# Cross-Platform Infrastructure Automation & Configuration Management

**Ansible · AlmaLinux · Ubuntu · Windows Server 2019 · Python · Bash · PowerShell · SSH · YAML**

Managing one server is straightforward. Managing several servers consistently, especially when they run different operating systems, takes a different approach. I used Ansible from an AlmaLinux workstation to configure and manage Ubuntu and Windows Server 2019, then verified the changes directly on the target systems.

This project combines my work on secure remote administration, service deployments, Windows access controls, custom automation, and reusable Ansible roles. The emphasis is on what I configured, why it mattered, how I checked the results, and what I would change before using similar configurations in production.

## Project overview

| Focus | Work demonstrated |
| --- | --- |
| Centralized administration | Ansible inventory groups and YAML playbooks targeting Linux and Windows |
| Secure remote access | OpenSSH, public-key authentication, remote logins, `ping`, and `win_ping` |
| Application services | Apache and MySQL on Ubuntu, IIS on Windows Server |
| Identity management | Windows local groups and accounts; Linux user creation, checks, and removal |
| Access control | NTFS folder permissions, explicit access control entries, and inheritance changes |
| Network and host controls | Windows Firewall management, Linux DHCP deployment, and lease verification |
| Automation development | Python modules, Bash scripts, CSV input, loops, and conditional tasks |
| Reusability | Ansible Galaxy roles and separate installation and service tasks |

**Scope:** I worked in a controlled virtual training environment. Related exercises and practical assessments sometimes used different lab instances. The project describes the complete body of work and does not suggest that every service was deployed simultaneously in one permanent environment.

## Architecture

```text
                       AlmaLinux control workstation
                         Ansible / Python / YAML
                                  |
                       SSH + organized inventory
                       /                       \
                      /                         \
               Ubuntu Linux               Windows Server 2019
               192.168.1.3                    192.168.1.2
               Apache / MySQL                 IIS web server
               DHCP service                   Local users and groups
               Linux account checks           NTFS permissions
                                              Windows Firewall
```

The AlmaLinux machine was the central administration workstation. The Ubuntu and Windows systems were managed targets. The example IP addresses are private addresses from the lab.

Some inventory groups, including `webserver` and `dbserver`, pointed to the same Ubuntu host. The names separated functions logically; they did not represent separate physical application and database servers.

**Why this matters:** A business might need to configure several servers, deploy a new service, provision employees, or correct access permissions. Ansible makes those actions repeatable and easier to review, rather than relying on separate manual changes to every machine.

## 1. Remote access and connectivity

I began with the foundations: user accounts, network addressing, and secure remote communication.

I installed and enabled OpenSSH on Ubuntu, verified the service status, and connected from the AlmaLinux machine. I created a test file on Ubuntu and confirmed it was visible from the remote SSH session, demonstrating that the connection reached the intended host.

I then configured an Ansible inventory to identify the managed machines. For Linux, I generated an SSH key pair and copied the public key to the Ubuntu account. That allowed the control workstation to establish SSH connections without repeatedly supplying the account password.

For Windows Server, I worked with OpenSSH support already prepared in the training environment. I configured its inventory entry to use an SSH transport and PowerShell shell type.

I checked communication using the appropriate Ansible modules:

- **Linux `ping`** confirmed that Ansible could execute a module on Ubuntu.
- **Windows `win_ping`** confirmed that Ansible could communicate with Windows Server.

Both produced successful responses in the completed reports. These module checks are not simply ordinary network ICMP pings; they test Ansible's remote execution path.

**Outcome:** I could target two different operating systems from one control workstation.

## 2. Automated web and database deployments

### Apache and a custom page on Ubuntu

I wrote an Ansible playbook to install the Apache web server and used another playbook to deploy an HTML page to Ubuntu's web directory. I checked Apache with `systemctl` and accessed the resulting page through a browser.

In the final practical exercise, I repeated the Apache setup and retrieved the HTML over the network with `curl`. That check provided client-side evidence of the server's response, beyond the successful Ansible recap.

### MySQL on Ubuntu

I used a separate inventory group and playbook to install MySQL and ensure the service was started and enabled. The documented `systemctl` output showed the MySQL service active.

Because the application and database inventory groups referenced one Ubuntu machine, this was a combined lab host rather than a segmented production application architecture.

### IIS on Windows Server

I created an `iisserver` target group and used a Windows-specific Ansible playbook to install the IIS Web Server role.

I verified that the default IIS page could be reached from AlmaLinux. I then used a playbook to stop the default site, prepared an HTML page, transferred the content to the IIS document directory, and restarted the site.

The captured browser displayed the custom IIS test page. The final exercise also showed an **HTTP 200 OK** response from the Windows web server, indicating a successful HTTP request.

**Outcome:** I deployed and tested application services on both operating systems using Ansible, service inspection, browsers, and command-line verification.

## 3. Windows user administration and file permissions

This phase moved beyond application installation into identity and access management.

I created Windows local users and groups using Ansible modules. In a later practical scenario, I brought several related tasks together into one playbook:

1. Created the `ECPIgroup` local security group.
2. Created two local user accounts, `ECPIadmin` and `ECPIuser`.
3. Added the accounts to the group.
4. Created the `C:\ECPI` directory.
5. Granted explicit NTFS access rights to the two users.
6. Changed the directory's permission inheritance settings.
7. Checked the resulting users, group, folder, and access controls in Windows management tools and PowerShell.

An access control list, or **ACL**, defines which accounts may use a resource and which operations those accounts may perform. This matters because the wrong permissions on a shared folder can expose or compromise business data.

The recorded exercise granted **FullControl** to the test accounts. That accurately demonstrates ACL administration, but it is broader than a typical least-privilege policy. In a production environment I would review the business need, prefer appropriately scoped group-based access, and inspect the effective permissions after modifying inheritance. Disabling inheritance alone does not guarantee the removal of all entries that were previously inherited.

**Outcome:** Successful playbook output was supported by Windows user, group membership, folder security, and PowerShell verification.

## 4. Windows Firewall and DHCP management

### Windows Firewall

I used Ansible playbooks to disable the Domain, Private, and Public Windows Firewall profiles in the controlled lab, inspected the changed status, and then ran a separate playbook to turn the firewall profiles back on.

The exercise demonstrated that host firewall settings could be managed remotely. It was **not** a recommended permanent configuration. For a real system, I would keep the firewall enabled and define narrow rules for required traffic.

### DHCP on Ubuntu

I used Ansible to install and start the ISC DHCP service, transfer subnet information, and configure address assignment on Ubuntu. The configuration included a subnet, an address pool, default gateway, and DNS server.

I inspected the `dhcpd.leases` file on Ubuntu. The captured lease record showed the Windows client receiving an address from the lab pool, connecting the server configuration to observable network behavior.

I also identified two limitations in the training playbook: it used permissive file permissions and appended subnet configuration using a shell command. A repeated append can duplicate entries, so a managed template with restricted permissions would be a safer and more repeatable production method.

**Outcome:** I demonstrated automated host and network-service configuration, backed by status and DHCP lease records.

## 5. Custom Python and Bash automation

### Python account verification

I developed a custom Python module for Ansible to check whether specified Linux accounts existed. The module used the local system account database and was invoked from a YAML playbook. I expanded the playbook from individual checks to a loop through several usernames.

During implementation I troubleshot Python interpreter-path and indentation errors. My work also showed how a missing account was reported. The original module treated a missing user as a failed Ansible task; that was the module's designed behavior, not necessarily a failure to contact the machine.

The [sanitized Python module](examples/library/check_user.py) in this repository is an **adapted reference**: it returns an explicit `exists` value for each user and does not fail on an ordinary negative lookup.

### CSV-driven Linux account lifecycle

I created a Bash helper and Ansible playbook that read CSV records and created multiple Linux accounts. I checked the account database afterward and worked through authentication and script-formatting problems.

In the midterm practical work I also used a Bash helper and another Ansible playbook to remove the test users, then examined `/etc/passwd` to verify the results.

These tasks went beyond one-off administration: they combined structured input, scripting, repeated operations, account verification, and eventual account removal.

The training scripts used plaintext and predictable passwords. I have **not** republished that credential-handling approach. A production workflow should use `ansible.builtin.user` where appropriate, an approved secret store, audit logging, and explicit authorization for account removal.

**Outcome:** Practical work with Python, Bash, YAML, CSV input, Ansible loops, account administration, and troubleshooting.

## 6. Reusable Ansible roles

I used Ansible Galaxy to create a standard Apache role directory. Instead of keeping every action in one large playbook, I separated package installation and service management into distinct task files and included them through the role's `main.yml`.

The recorded role-based run completed with **no unnecessary changes** on an already configured Ubuntu host.

That illustrates **idempotency**, a central idea in configuration management: when a system already matches the desired configuration, reapplying the task should not change it.

Roles make it easier to maintain and reuse known configuration procedures across multiple machines or projects.

## Verification and troubleshooting

| Configuration area | Evidence from completed work |
| --- | --- |
| Remote connectivity | SSH sessions, Linux `ping` and Windows `win_ping` returning success |
| Apache | Playbook recaps, Apache service status, page retrieval in browser and terminal |
| MySQL | Installation recap and active MySQL service |
| IIS | IIS role configuration, browser-visible test site, HTTP 200 response |
| Windows identities | Created users and group shown in Computer Management |
| Folder access | Explicit NTFS permissions displayed in Windows and PowerShell |
| Windows Firewall | Changed profile states and subsequent enabled-state verification |
| DHCP | Deployment output and a Windows client's lease in `dhcpd.leases` |
| Custom scripts | Executed playbooks, account database checks, and recorded debugging |
| Apache role | Successful execution with no changes required on a configured host |

I used both the control workstation's results and the target systems to validate changes. A syntax check alone can identify formatting problems, but it does not demonstrate that the actual remote service works.

Errors were also part of the work. I corrected YAML indentation problems, Python script errors, variable naming mistakes, and account authentication issues. The goal was to determine why an operation failed and verify the corrected behavior, not simply to hide unsuccessful first attempts.

## Selected technical examples

The files linked below are **credential-free references adapted from the completed work**. They are not presented as exact historical source files or as newly executed deployments.

- [Ansible inventory](examples/inventory.ini)
- [Apache deployment on Ubuntu](examples/linux_apache.yml)
- [IIS configuration on Windows](examples/windows_iis.yml)
- [Windows group and folder access](examples/windows_access.yml)
- [Windows Firewall enabled-state playbook](examples/windows_firewall_enabled.yml)
- [Custom Python account-check module](examples/library/check_user.py)
- [Account-check playbook](examples/check_linux_users.yml)
- [Reusable Apache role](examples/roles/apache/tasks/main.yml)

See [Security and Implementation Notes](SECURITY.md) for production considerations and the limitations of the original exercise configurations.

## What I took from the project

The strongest lesson was the importance of combining automation with verification. A successful task recap is useful, but it is not enough by itself. I still needed to confirm account membership, inspect folder permissions, review firewall state, examine DHCP leases, and request web pages from a client.

The work also made clear that a functional lab configuration is not automatically secure or suitable for production. Protecting secrets, controlling access, preserving host firewalls, and making repeated deployments predictable are as important as making the initial deployment succeed.

This project demonstrates skills directly applicable to systems administration, infrastructure security, operations engineering, and cloud automation.

[All projects](../../) | [Portfolio home](../../../)
