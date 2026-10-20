# Validation and Evidence

The results below come from the original completed lab submissions and their course-provided PowerShell/Pester checks. Each filename is reserved in the [screenshot folder](../screenshots/) for the corresponding original screenshot.

| Assignment | Verified result | Screenshot filename |
|---|---|---|
| 2.3, VMs from base images | 24 passed, 0 failed | `01-hyperv-provisioning.png` |
| 2.4, virtual networking | 17 passed, 0 failed | `02-hyperv-network-validation.png` |
| 2.7, Hyper-V performance assessment | 35 passed, 0 failed | `03-hyperv-performance-assessment.png` |
| 3.7, Active Directory forest | 12 passed, 0 failed | `04-active-directory-forest.png` |
| 3.5, advanced DNS | 6 passed, 0 failed | `05-dns-secondary-zones.png` |
| 3.8, DHCP | 13 passed, 0 failed | `06-dhcp-role-scopes.png` |
| 4.4, OU design and user import | 38 passed, 0 failed | `07-bulk-user-provisioning.png` |
| 4.5, security groups and permissions | 33 passed, 0 failed | `08-security-groups-ntfs.png` |
| 4.6, Group Policy creation | 3 passed, 0 failed | `09-gpo-creation.png` |
| 4.8, Group Policy software deployment | 11 passed, 0 failed | `10-gpo-software-deployment.png` |
| 4.9, delegated AD control | 4 passed, 0 failed | `11-delegated-administration.png` |

## How to interpret the evidence

These counts represent individual checks written for the course, not a comprehensive security audit. Passing an OU-import test does not by itself demonstrate a manual inspection of all 449 user accounts. Screenshots of test output do not establish full command history, continuous uptime, or independent security validation.

### Excluded or partially verified work

**4.7, Group Policy processing:** One automated check failed even though additional screenshots demonstrated membership in the intended exception group. The submission showed a mismatch between `JoeTaylor` and `Joe Taylor`. It is not represented as a fully passing exercise.

**4.11, performance assessment:** The submitted documentation showed a script/container error. Without a successful full validation result, that assessment is not counted among the passing tests.

## Image upload status

Original screenshots are being added separately. Files use the exact names in the [screenshot checklist](../screenshots/) so the evidence can be reviewed alongside these notes.

[Project overview](../README.md)
