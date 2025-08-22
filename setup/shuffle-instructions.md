# Shuffle Setup (SOAR)

## Prerequisites

- Docker and Docker Compose installed
- Linux host (recommended)
- Minimum hardware for testing: 2 vCPU, 2GB RAM, >20GB disk
- Recommended for production: 2 vCPU, 8GB RAM, >100GB SSD

Note: Shuffle works fine on a single server for testing and small labs. For production, two or more servers are recommended to avoid congestion and improve stability. Opensearch is RAM heavy and benefits from more resources.

## 1. Prepare System

- Make sure Docker is installed and running.
- Disable swap (recommended for Opensearch):
	```bash
	sudo swapoff -a
	```
- Increase max_map_count for Opensearch:
	```bash
	sudo sysctl -w vm.max_map_count=262144
	```

## 2. Download and Set Up Shuffle

```bash
git clone https://github.com/Shuffle/Shuffle.git
cd Shuffle
mkdir shuffle-database
sudo chown -R 1000:1000 shuffle-database
```

## 3. Start Shuffle with Docker Compose

```bash
docker-compose up -d
```

## 4. Access Shuffle Web UI

After installation, open your browser and go to:
- `http://<docker-host-ip>:3001` (replace `<docker-host-ip>` with your host's IP address)
- Or use HTTPS: `https://<docker-host-ip>:3443`

## 5. Default Credentials

Set up your admin account (choose your own username and password; Shuffle does not have a default).
Sign in with the same credentials you just created.

Go to `/apps` in the Shuffle UI to check for available apps. If none appear, you may need to configure proxies.

For more configuration tips and troubleshooting, see the [Shuffle configuration docs](https://shuffler.io/docs/configuration).

## Shuffle Architecture

![Shuffle Architecture](docs/images/shuffle_arch.png)

The Shuffle architecture includes several main components:
- **Frontend:** Web interface for users to create, manage, and monitor workflows.
- **Backend:** Handles API requests, workflow execution, and system logic.
- **Orborus:** Manages workflow scheduling and execution across distributed environments.
- **Opensearch:** Database for storing workflow data, logs, and search operations.
- **Workers:** Execute workflows and tasks, allowing Shuffle to scale and distribute processing.

---

For more details, see the [Shuffle documentation](https://shuffler.io/docs/getting_started).