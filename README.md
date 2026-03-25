<p align="center">
  <img src="docs/images/wazuh_logo.png" width="185"/>
  <img src="docs/images/shuffle_logo.png" width="210"/>
  <img src="docs/images/thehive_logo.png" width="210"/>
  <img src="docs/images/cortex_logo.png" width="210"/>
</p>

# SOAR Homelab

## Overview
This project demonstrates a **Security Orchestration, Automation, and Response (SOAR)** pipeline using open-source tools. It simulates how security teams **detect, investigate, and respond to threats** in a real-world environment.

## Technologies

- **Wazuh** — SIEM and threat detection  
- **Shuffle** — Security automation (SOAR)  
- **TheHive** — Case management  
- **Cortex** — Threat intelligence enrichment  

All components are deployed using **Docker**.

---

## Workflow

1. **Wazuh** detects suspicious activity  
2. Alerts are sent to **Shuffle**  
3. **Shuffle** automates:
   - Case creation in **TheHive**  
   - Data enrichment via **Cortex**  
4. Full flow: **Detection → Investigation → Response**

---

## Key Features

- End-to-end SOAR pipeline  
- Automated alert triage and case management  
- Threat intelligence enrichment  
- Modular Docker-based setup  

---

## Setup

See [`setup/`](setup/) for installation steps.

---

## Project Structure

- `docs/` — Architecture and screenshots  
- `configs/` — Configuration files  
- `scripts/` — Automation scripts  
- `setup/` — Deployment guide  
