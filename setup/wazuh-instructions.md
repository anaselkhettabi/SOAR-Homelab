# Wazuh Setup (SIEM)

## Prerequisites

- Docker and Docker Compose installed
- Linux host with at least 4GB RAM

## 1. Increase max_map_count

```bash
sudo sysctl -w vm.max_map_count=262144
```

To make this change permanent, add the following line to `/etc/sysctl.conf`:

```bash
echo "vm.max_map_count=262144" | sudo tee -a /etc/sysctl.conf
```

Verify after reboot:

```bash
sysctl vm.max_map_count
```

## 2. Clone the Wazuh Docker Repository

```bash
git clone https://github.com/wazuh/wazuh-docker.git
cd wazuh-docker
```

## 3. Configure Wazuh (Optional)

Edit the `docker-compose.yml` file or configuration files if you want to customize settings.

## 4. Start Wazuh Containers

```bash
docker-compose up -d
```

This will start Wazuh, Elasticsearch, and Kibana containers.

## 5. Access Wazuh Dashboard

- Open your browser and go to: [https://localhost:5601](https://localhost:5601)
- Default credentials:
  - **Username:** admin
  - **Password:** admin

## 6. Stopping Wazuh

To stop the containers:

```bash
docker-compose down
```

---

For more details, see the [official Wazuh Docker documentation](https://documentation.wazuh.com/current/deployment/docker/).