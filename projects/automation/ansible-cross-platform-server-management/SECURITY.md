# Security and Implementation Notes

The original work was performed in controlled training networks. These notes distinguish the completed exercises from stronger configurations that would be needed on a live business network.

## Credentials
The original labs included simple shared passwords, credential values in YAML and CSV, and a Bash routine that constructed predictable passwords. Those values are omitted here. Production account-management tasks should use an approved secret store, strong password policies, and `no_log: true` where sensitive variables could otherwise be printed. Disabling logs does not make hard-coded passwords safe.

## Account management
The original Bash helper was invoked through an Ansible `command` task; it was not a fully structured native Ansible module. In production, a supported idempotent account-management module such as `ansible.builtin.user` is preferable, along with authorization and review for account deletion.

## NTFS access controls
The recorded Windows scenario granted explicit FullControl permissions to two test users and changed inheritance on the folder. That demonstrated ACL operations, not a recommended least-privilege access model. A production design should consider group-based access, narrower rights, and administrative recovery permissions. The final ACL should be inspected rather than assuming inheritance changes remove every previously inherited entry.

## Firewall management
The training exercise temporarily disabled all Windows Firewall profiles and then restored them. Disabling the firewall broadly can expose services. Real changes should normally use narrowly scoped allow rules without disabling the host firewall.

## DHCP configuration
The classroom DHCP playbook used `0666` file permissions and shell append (`>>`) to write subnet settings. Repeated execution could duplicate entries, and the permissions were overly broad. Prefer a complete managed template, restrictive mode, configuration validation, and a handler that restarts the service only when the configuration changes. DHCP must also be deployed only on an approved network segment.

## Legacy software
One Windows exercise installed an obsolete Apache 2.2 MSI. It is excluded from the sanitized implementation. The lab also used the traditional ISC DHCP service; future builds should check package support and operating-system compatibility.

## Scope and verification
The original screenshots represent separate but related exercises, including practical assessments. They do not imply all services coexisted on one permanent host. The example files in this repository have been cleaned up and should be reviewed against the installed Ansible collections and target operating-system versions before execution. A syntax check is not a functional or security test.
