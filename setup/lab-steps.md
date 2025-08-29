# Lab Steps: SOAR Homelab Workflow

This guide walks you through the main steps to connect and integrate Wazuh, Shuffle, TheHive, and Cortex in your cybersecurity homelab. Follow these steps after completing the initial setup for each tool.

---

## 1. Connect Wazuh to Shuffle

- Configure Wazuh to forward alerts to Shuffle using a webhook integration.
- In Wazuh Manager, edit the configuration to add a webhook pointing to your Shuffle instance.
- Test the connection by generating a test alert in Wazuh and verifying it appears in Shuffle.

## 2. Create and Test a Shuffle Workflow

- In Shuffle, create a workflow that receives alerts from Wazuh.
- Add actions to the workflow, such as sending notifications, creating cases in TheHive, or enriching data with Cortex.
- Test the workflow by triggering an alert from Wazuh and confirming the workflow runs as expected.

## 3. Integrate Shuffle with TheHive and Cortex

- Configure Shuffle to connect to TheHive and Cortex using their API endpoints and credentials.
- In Shuffle, add steps to your workflow to create a case in TheHive and send observables to Cortex for enrichment.
- Verify integration by checking that cases and observables are created and enriched correctly.

## 4. Deploy and Test Agents

- Install Wazuh agents on endpoints (Linux, Windows, etc.) to send logs and events to your Wazuh Manager.
- Confirm that agent data is received and processed by Wazuh, and alerts are forwarded to Shuffle.

## 5. End-to-End Test

- Simulate a security event on an endpoint.
- Follow the flow: Wazuh detects the event → alert sent to Shuffle → workflow triggers case creation in TheHive and enrichment in Cortex.
- Check each tool’s dashboard to confirm the event is tracked and processed through the full workflow.

---

For detailed setup and configuration, refer to the individual setup guides for Wazuh, Shuffle, and TheHive/Cortex in this repository.
