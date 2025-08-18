<p align="center">
  <img src="https://github.com/user-attachments/assets/fc2e7ff3-25ab-4574-94b5-a5bb0ffd994e" width="210"/>
  <img src="https://github.com/user-attachments/assets/80479fda-fe42-438d-bec4-6e064e21cb65" width="210"/>
  <img src="https://github.com/user-attachments/assets/be0dbf87-7f35-48dd-9f1b-5656a1cc2610" width="210"/>
  <img src="https://github.com/user-attachments/assets/866f85d6-cd30-4283-9f58-f34aee315ede" width="210"/>
</p>

# 🛡️ SOAR Home Lab

A home lab integrating Wazuh, Shuffle, TheHive, and Cortex to demonstrate Security Orchestration, Automation, and Response (SOAR) workflows.

## 📌 Overview

This project showcases a hands-on SOAR implementation designed for incident response and security automation. The lab integrates multiple open-source security tools to simulate real-world detection, triage, and response processes.

By building and documenting this lab, I aim to demonstrate skills in:

- Threat detection with Wazuh (SIEM).
- Case management & investigations with TheHive.
- Automated playbooks with Shuffle (SOAR).
- Threat intelligence enrichment with Cortex analyzers.
- Containerized deployment using Docker.

## ⚙️ Tools & Components

- Wazuh (SIEM + Agents)
- Shuffle (Security Automation)
- TheHive (Incident Response Platform)
- Cortex (Threat Intelligence Enrichment)
- Docker (Containerized Environments)

## 🏗️ Architecture

flowchart LR
  A[Endpoints / Agents] --> B[Wazuh Manager]
  B --> C[Wazuh Indexer]
  B --> D[Wazuh Dashboard]
  B --> E[Shuffle SOAR]
  E --> F[TheHive Case Management]
  F --> G[Cortex Threat Intel]

## 🔧 Prerequisites

- Ubuntu/Debian-based VMs
- Docker Engine installed on your WSL or Linux host
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
