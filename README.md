<p align="center">
  <img src="https://github.com/user-attachments/assets/fc2e7ff3-25ab-4574-94b5-a5bb0ffd994e" width="210"/>
  <img src="https://github.com/user-attachments/assets/80479fda-fe42-438d-bec4-6e064e21cb65" width="210"/>
  <img src="https://github.com/user-attachments/assets/be0dbf87-7f35-48dd-9f1b-5656a1cc2610" width="210"/>
  <img src="https://github.com/user-attachments/assets/866f85d6-cd30-4283-9f58-f34aee315ede" width="210"/>
</p>

# SOAR Homelab

A simple homelab for learning Security Orchestration, Automation, and Response (SOAR) using open-source tools.

## What is This Lab?

This project helps you explore how security teams detect, investigate, and respond to threats using:

- **Wazuh** for threat detection (SIEM)
- **Shuffle** for automating security workflows (SOAR)
- **TheHive** for case management
- **Cortex** for threat intelligence enrichment

All components run in Docker containers for easy setup.

## How Does It Work?

1. **Wazuh** detects suspicious activity on endpoints.
2. **Shuffle** receives alerts and automates responses:
    - Creates cases in **TheHive**
    - Enriches data with **Cortex** (optional)
3. You can follow the flow from detection to investigation and response.

## Quick Start

- **Requirements:** Docker, Linux, admin access, internet connection.
- **Setup:** See [`setup/`](setup/) for installation and connection steps.

## Project Structure

- `docs/` — Architecture and screenshots
- `configs/` — Example config files
- `scripts/` — Helper and validation scripts
- `setup/` — Step-by-step setup instructions

## Lab Hardware

Main SOC server: Old laptop
- CPU: 12 x Intel Core i7-8750H @ 2.20GHz
- RAM: 12GB DDR4
- Storage: 1TB HDD
- Hypervisor: Proxmox
- VM: Ubuntu 22.04.5 (runs Wazuh and Shuffle containers)

Windows desktop:
- VMware Workstation 17 Pro
- VMs: TheHive/Cortex, Linux agent, Windows agent

## Learn More

For detailed guides and walkthroughs, check the files in the `setup/` and `docs/` folders.

---

*This README gives a high-level overview. For step-by-step instructions, see the other markdown files in this repo.*