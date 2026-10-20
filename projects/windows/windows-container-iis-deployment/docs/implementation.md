# Technical Implementation Notes

These notes describe the Windows Server 2019 container exercises in CYB360. Commands are representative of the learning workflow, not an original command history or a production deployment script.

## Container installation and management

The first exercises installed Docker and verified a locally available hello-world image. I then worked with Windows Server Core and Nano Server images and practiced container creation, startup, attachment, inspection, and removal.

Useful commands from the labs included:

```powershell
docker images
docker container ls -a
docker inspect nat
```

The installation lab passed **4** checks, and the container operations lab passed **9**.

## Storage persistence

The storage assignments explored a container's ephemeral filesystem and two persistence methods:

- **Bind mounts** mapped a host folder such as `D:\WebData` into a container.
- **Named volumes** used a Docker-managed volume called `WebSite`.

The revised submission for the storage lab passed **9** checks. This confirms the conditions tested by the assignment, not a production backup or disaster-recovery capability.

## Network configuration

The network exercises involved inspecting Docker NAT configuration, testing connectivity, creating a NAT-backed network, connecting and disconnecting containers, and publishing ports.

An example from the lab instructions:

```powershell
docker network create --driver nat --subnet 192.168.128.0/17 Test-Nat
```

The networking submission passed **11** automated checks.

## Dockerfile-based IIS build

For the Dockerfile assignment I created an image based on `mcr.microsoft.com/windows/servercore:1809`, installed the Web Server role, and copied website files to the IIS content directory. I built a versioned image tagged `iis-websvr:v2`.

The submitted screenshot includes Docker image history and a running container named `V2-Test` with host port **1234** mapped to container port **80**.

The original standalone Dockerfile and site assets were not provided as source files. Their contents are documented through the original VS Code screenshot. The evidence does not independently demonstrate an HTTP response or application monitoring.

[Project overview](../README.md) | [Validation](validation.md) | [Screenshot index](../screenshots/)
