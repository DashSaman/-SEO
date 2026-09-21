# Phase 1 — Install Docker Engine + Docker Compose on Ubuntu 24.04 in WSL2

This guide assumes the operator is new to Docker. The selected architecture installs the official Docker Engine inside Ubuntu 24.04. **Docker Desktop on Windows is not used.**

![Docker install flow](assets/docker-install-flow.svg)

## Why Docker?

Docker lets Growth OS run services in isolated containers instead of manually installing every service into Ubuntu.

Future shape:

```text
Ubuntu / WSL2
└── Docker
    ├── PostgreSQL
    ├── Redis
    ├── n8n
    ├── OpenGSC
    ├── DispatchSEO
    └── Postiz
```

## Verified prerequisites on the pilot

- Ubuntu 24.04 LTS
- WSL VERSION 2
- systemd = running
- WSL memory ceiling = 20 GB
- processors = 12
- swap = 8 GB
- RTX 3070 visible inside WSL

## Selected installation method

Install Docker Engine from Docker's **official apt repository**. Do not use Docker Desktop or an unreviewed convenience script.

Official reference:

- https://docs.docker.com/engine/install/ubuntu/

## Step 1 — Check for pre-existing/conflicting packages

```bash
docker --version
```

Then:

```bash
dpkg -l | grep -E 'docker|containerd|runc'
```

If Docker is absent and no conflicting packages are listed, continue. If packages are present, record the output before removing anything.

## Step 2 — Install repository prerequisites

```bash
sudo apt update
sudo apt install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

## Step 3 — Add Docker's official apt repository

```bash
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF
```

Then:

```bash
sudo apt update
```

Continue only if apt reads the Docker repository without GPG/Release errors.

## Step 4 — Install Docker Engine and Compose plugin

```bash
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## Step 5 — Verify the service and binaries

```bash
systemctl is-active docker
docker --version
docker compose version
sudo docker run hello-world
```

Expected service state:

```text
active
```

The `hello-world` container should print Docker's success message.

## Step 6 — Allow the managed Linux user to run Docker without sudo

```bash
sudo usermod -aG docker $USER
```

Refresh the session:

```bash
exit
```

Then from PowerShell:

```powershell
wsl -d Ubuntu-24.04
```

Verify:

```bash
docker run hello-world
```

> Membership in the `docker` group effectively grants high-level control of the machine. Only the managed operator account should receive it.

## Step 7 — Verify Compose v2

```bash
docker compose version
```

Use the modern `docker compose` subcommand, not the legacy `docker-compose` binary.

## Completion gate

P1-WSL-10 is complete only when:

- Docker Engine is installed.
- `systemctl is-active docker` returns `active`.
- `docker --version` works.
- `docker compose version` works.
- `hello-world` succeeds.
- Non-sudo Docker works after session refresh.

Record every failure and fix in `AGENT.md` and, when reusable, under `growth-os/troubleshooting/`.
