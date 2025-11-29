# Baby-Ansible-Homelab
Mini network automation tool for my Cisco homelab (inventory + tasks + Python runner).
# Homelab NetAuto (Baby Ansible)

This project is a small "baby Ansible" style tool for my Cisco homelab.

The idea:

- My network devices ( Cisco 2960-X and 2960 switches).
- I want to describe what to do in simple YAML files (inventory + tasks).
- A Python script will read those files and later connect over SSH to push configs.

## Project layout (planned)

- `inventory.yaml`  
  Will store a list of my lab switches (name, IP, device_type, username, password).

- `tasks/`  
  Folder that will store YAML files for different labs.  
  Ex: `trunk_lab.yaml` to create VLANs 10/20/30 and configure trunk ports.

- `scripts/`  
  Folder that will store Python scripts that read the inventory + tasks and send commands.  
  Ex: `run_trunk_lab.py` to apply the trunk lab config to all switches.

## Status

As right now this project is at the starting point:

- Repo created
- Basic README describing the goal and layout
- Next steps:
  - Add `inventory.yaml` with my lab switches
  - Add `tasks/trunk_lab.yaml` with VLAN/trunk commands
  - Add a Python runner script that at first only prints the commands (dry run)
