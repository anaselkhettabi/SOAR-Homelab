# Wazuh Setup (SIEM)

**Note:** These instructions are based on Wazuh version 4.12.

## Prerequisites

- Docker and Docker Compose installed
- Docker host with at least 6GB RAM

## 1. Increase max_map_count

Wazuh indexer creates many memory-mapped areas. Increasing `max_map_count` lets the stack work properly and avoids errors due to memory limits.

```bash
sudo sysctl -w vm.max_map_count=262144
```

To make this change permanent, add the following line to `/etc/sysctl.conf`:

```bash
echo "vm.max_map_count=262144" | sudo tee -a /etc/sysctl.conf
```

**Reload sysctl to apply changes without rebooting:**

```bash
sudo sysctl -p
```

Verify the value:

```bash
sysctl vm.max_map_count
```

## 2. Clone the Wazuh Docker Repository

Wazuh provides two Docker deployment options:
- **Single-node:** Simple setup, suitable for labs and small environments.
- **Multi-node:** Scalable, for production or large environments.

For this lab, I use the single-node deployment for simplicity and easier resource management.

```bash
git clone https://github.com/wazuh/wazuh-docker.git -b v4.12.0
cd wazuh-docker
cd single-node
```

## 3. Configure Wazuh (Optional)

To customize your deployment, you can change the exposed ports or modify the default password by editing the `docker-compose.yml` file; for additional settings, refer to the comments inside the compose file.

## 4. Generate Self-Signed Certificates (Required)

Wazuh requires certificates to secure communication between cluster nodes. For most lab setups, you can generate self-signed certificates using the provided Docker image:

```bash
docker-compose -f generate-indexer-certs.yml run --rm generator
```

This command saves the certificates into the `config/wazuh_indexer_ssl_certs` directory. If your system uses a proxy, add the `HTTP_PROXY` environment variable to the `generate-indexer-certs.yml` file as shown in the Wazuh documentation.

If you have your own certificates, place them in the `config/wazuh_indexer_ssl_certs` directory as described in the official docs.

## 4. Start Wazuh Containers

```bash
docker-compose up -d
```

This will start the following nodes:

**Node descriptions:**
- `wazuh.manager`: Handles agent management, event analysis, and alerting.
- `wazuh.indexer`: Stores and indexes security data for fast searching and correlation.
- `wazuh.dashboard`: Provides a web interface to visualize alerts, data, and manage the stack.

## 5. Access Wazuh Dashboard

Open your browser and go to: `https://<docker-host-ip>` (replace `<docker-host-ip>` with your host's IP address).
Default credentials:
  - **Username:** admin
  - **Password:** SecretPassword (see the `docker-compose.yml` file)

## 6. Stopping Wazuh

To stop the containers:

```bash
docker-compose down
```

## Wazuh Architecture

![Wazuh Architecture](docs/images/wazuh_arch.png)

**Note:** In this lab, we use the single-node Docker deployment, so you'll have only one Wazuh manager node (not a cluster as shown in the architecture diagram).

---

For more details, see the [official Wazuh Docker documentation](https://documentation.wazuh.com/current/deployment-options/docker/index.html).