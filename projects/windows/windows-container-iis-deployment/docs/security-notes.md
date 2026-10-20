# Container Security Considerations

This work used Windows Server 2019 and Windows Server Core 1809, which reflect the classroom environment rather than a recommended present-day production baseline.

**Supported base images:** Before a real deployment, verify that the host OS, container image, and runtime versions are compatible and supported. Prefer an approved, patched base image and rebuild after applicable security updates.

**Application lifecycle:** The instructional Dockerfile used an interactive PowerShell command. A production IIS container needs an appropriate runtime process and functional health checks; an active container alone does not prove an application is serving traffic.

**Host storage:** Bind mounts may expose sensitive host files. Mount only required directories, limit permissions, and establish backup and recovery processes. Named volumes are not a replacement for backups.

**Exposed ports:** Restrict published ports and verify firewall configuration and expected client reachability. Avoid placing management interfaces or unused services on publicly reachable interfaces.

**Credentials and metadata:** Do not commit secrets, access tokens, or personal account information to Dockerfiles or embed them in image layers. Crop or redact identifying information in screenshots before publication.

**Verification:** For enterprise use, add image vulnerability scanning, HTTP/service tests, logging, runtime monitoring, and rollback procedures. Those controls are not claimed as completed in the original assignments.

[Project overview](../README.md)
