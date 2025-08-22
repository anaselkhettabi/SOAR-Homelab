# TheHive & Cortex Setup (Case Management & Threat Intelligence)

This setup runs both TheHive and Cortex together using Docker. For this lab, I used the testing environment profile since it was running on a single server and intended for testing purposes.

## Prerequisites

- Docker Engine v23.0.15 or later
- Docker Compose Plugin v2.20.2 or later
- jq installed
- User with sudo permissions

## Hardware Requirements

- Minimum: 4 vCPUs, 16GB RAM, 100GB storage
- Recommended for intensive use: 8 vCPUs, 32GB RAM, 150GB storage

## 1. Clone the StrangeBee Docker Repository

```bash
git clone https://github.com/StrangeBeeCorp/docker.git
cd docker
```

## 2. Initialize the Environment

Run the initialization script to set up secrets, certificates, and environment files:

```bash
bash ./scripts/init.sh
```

## 3. Start TheHive & Cortex Stack

```bash
docker compose up -d
```

## 4. Access TheHive Web UI


- Testing profile: `https://<docker-host-ip>/thehive`
- Production profile: `https://<docker-host-ip>/`

Default login credentials:
	- **Username:** admin@thehive.local
	- **Password:** secret

## TheHive & Cortex Architecture

![TheHive & Cortex Architecture](docs/images/hive_cortex_arch.png)

**Note:** This diagram shows the general integration between TheHive and Cortex. The actual deployment may differ in newer versions; refer to official documentation for up-to-date architecture.

A standalone server setup for TheHive Docker deployment includes:
- **Cassandra:** Stores case and alert data for TheHive.
- **Elasticsearch:** Indexes and searches data for fast retrieval and analysis.
- **File storage (local filesystem or MinIO):** Stores attachments and files related to cases.
- **TheHive:** Main application for case management and incident response.
- **Optional NGINX:** Manages HTTPS communications and reverse proxying.

For detailed installation instructions, refer to the official step-by-step guide.

---

For more details, see the [official deployment guide](https://docs.strangebee.com/thehive/installation/docker/).