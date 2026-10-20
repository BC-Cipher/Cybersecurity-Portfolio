# Security and Production Considerations

The Windows Server assignments were completed in isolated training systems. Classroom requirements demonstrate configuration techniques but are not recommended as a production security baseline.

## Identity and access

The bulk account creation exercise used a shared demonstration password. Real identity provisioning should use approved onboarding methods, unique temporary credentials or passwordless mechanisms where appropriate, protected secrets, and suitable password-change controls.

Some lab exercises added broad memberships to Remote Desktop Users. Enterprise remote access should be restricted to authorized groups, logged, and reviewed.

## SMB and NTFS permissions

One assignment used permissive share-level permissions while configuring specific NTFS ACLs. In production, **both** share permissions and NTFS permissions require review. Use least privilege and test effective access with representative accounts.

## Delegation

OU-scoped delegation limits the need for domain-wide administrator access. Grant only the operations each role needs, maintain separate administrative accounts, and review delegated groups and ACLs periodically.

## DNS and policy changes

Restrict DNS zone transfers to approved secondaries. Audit DNS changes, monitor errors, and verify resolution after modifications. Test GPOs with a small target group or OU before wider rollout, especially software deployment and workstation controls.

## Operational verification

Before adapting any coursework command to production, confirm Windows Server version support, rollback steps, least-privilege credentials, backup/recovery expectations, and the effect on existing users and services.

[Project overview](../README.md)
