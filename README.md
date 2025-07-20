<p align="center">
  <img src="https://github.com/user-attachments/assets/fc2e7ff3-25ab-4574-94b5-a5bb0ffd994e" width="240"/>
  <img src="https://github.com/user-attachments/assets/80479fda-fe42-438d-bec4-6e064e21cb65" width="240"/>
  <img src="https://github.com/user-attachments/assets/be0dbf87-7f35-48dd-9f1b-5656a1cc2610" width="240"/>
  <img src="https://github.com/user-attachments/assets/866f85d6-cd30-4283-9f58-f34aee315ede" width="240"/>
</p>

# SOAR Home Lab (Wazuh + Shuffle + TheHive + Cortex)

This project showcases a basic Security Orchestration, Automation, and Response (SOAR) setup using open-source tools: Wazuh (SIEM), Shuffle (Automation), TheHive (Ticketing), and Cortex (Enrichment). The lab simulates real-world alerting, ticket creation, and automated enrichment workflows.

## 🧰 Stack

- Wazuh (SIEM + Agent)
- Shuffle (SOAR)
- TheHive (Alert Management)
- Cortex (Threat Intelligence Enrichment)

## 🔧 Prerequisites

- Ubuntu/Debian-based VMs or Docker containers
- Basic networking setup (e.g., `/etc/hosts` configuration)
- Admin access to modify service files (Wazuh `ossec.conf`)
- Internet access for enrichment API lookups

## 🚀 What This Lab Does

- Wazuh detects suspicious activity (scheduled task creation)
- Alert sent to Shuffle via webhook
- Shuffle automates:
  - Alert creation in TheHive
  - Enriches with observables (e.g., IP, file hashes via Wazuh logs)
- Cortex enriches observables (future step or optional)

## 📁 Folder Overview

- `docs/`: Architecture summary and screenshots
- `configs/`: Sample config files for Wazuh, Shuffle, and TheHive
- `scripts/`: Windows and validation scripts used in the lab
- `setup/`: Setup instructions and connection steps

## 🏁 Flag Script

To verify completion:
```bash
cd ~/Desktop
./flag1.sh
