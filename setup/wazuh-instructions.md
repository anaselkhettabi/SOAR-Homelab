For this lab, I used the docker version of wazuh to simplfy the deployment and management of the application.

## Docker installation
1. Increase max_map_count on your Docker host: sysctl -w vm.max_map_count=262144
2. Update the vm.max_map_count setting in /etc/sysctl.conf to set this value permanently. To verify after rebooting, run “sysctl vm.max_map_count”.