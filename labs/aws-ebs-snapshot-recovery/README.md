# Amazon EBS Storage, Snapshots & Volume Recovery

## Overview
I worked with Amazon Elastic Block Store (EBS) volumes attached to EC2 instances, reviewed volume properties, accessed Linux storage through the terminal, created a snapshot, and restored storage from a snapshot in an AWS training environment.

**Services:** Amazon EC2, EBS, EBS snapshots  
**Focus:** Persistent block storage, disaster recovery, Linux storage operations

## Work Completed
- Reviewed EBS volume type, size, attachment, and availability-zone information.
- Used Linux terminal commands to investigate mounted storage and files.
- Created and verified an EBS snapshot.
- Created a replacement volume from a snapshot.
- Verified the restored volume appeared in the EC2 storage inventory.
- Checked file visibility in Linux as part of the recovery procedure.

A separate EBS resize exercise covered extending volume capacity and Linux partition/filesystem resizing. The uploaded file for that exercise contains the lab **instructions**, not a completed student report, so I have not represented its screenshots as verified execution evidence here.

## Evidence to Add
Save under [screenshots/](screenshots/):
- `ebs-snapshot.png`: snapshot entry marked completed.
- `ebs-restored-volumes.png`: restored volumes shown in the AWS console.

## Security & Operational Considerations
Snapshots are useful for recovery but require appropriate IAM permissions, encryption, retention controls, and documented restoration tests. Recovery planning should also account for whether data is application-consistent, not just whether a volume was successfully recreated.

## Key Takeaway
Creating a snapshot is only one part of recovery. Recreating storage and verifying accessible content are equally important.
