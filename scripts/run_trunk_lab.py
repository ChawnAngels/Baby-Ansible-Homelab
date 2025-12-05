# scripts/run_trunk_lab.py
# Baby Ansible – trunk lab runner for my Cisco homelab.
#
# I wrote this script to practice network automation without actually
# touching the real switches yet. Right now it:
#   - locates the repo root based on this file's location
#   - loads inventory.yaml (my lab switches and their IPs)
#   - loads tasks/trunk_lab.yaml (the commands I want to push)
#   - prints what it would send to each device (dry run only)
#
# Later I want to replace the print step with real SSH connections (Netmiko),
# so this file is basically my "brain" for planning changes.

import yaml
from pathlib import Path

# Figure out project root based on THIS file, not on where I run Python from.
# __file__            -> scripts\run_trunk_lab.py
# .parent             -> scripts\
# .parent.parent      -> repo root (Baby-Ansible-Homelab\)
BASE_DIR = Path(__file__).resolve().parent.parent

INVENTORY_FILE = BASE_DIR / "inventory.yaml"
TASKS_FILE = BASE_DIR / "tasks" / "trunk_lab.yaml"

# 1. Load inventory (devices) from YAML file
with INVENTORY_FILE.open() as f:
    inventory = yaml.safe_load(f)

# 2. Load trunk lab tasks from YAML file
with TASKS_FILE.open() as f:
    trunk_lab = yaml.safe_load(f)

# 3. Pull out the parts I care about from the YAML data
hosts = inventory["switches"]["hosts"]
defaults = inventory.get("defaults", {})
tasks = trunk_lab["tasks"]



def print_plan_for_task(task):
    """
    For a single task from trunk_lab.yaml, show which device I'm targeting
    and which commands I plan to send. This is my "dry run" view before
    I automate the real SSH part.
    """
    target_host_name = task["hosts"]  # e.g. 'core_2960x' or 'access_2960'
    host_info = hosts.get(target_host_name)

    # If I mess up a host name in the tasks file, I want to see it clearly.
    if host_info is None:
        print(f"\n[!] Task '{task['name']}' targets '{target_host_name}', "
              f"but that host is not in inventory.yaml")
        return

    device_ip = host_info["host"]
    platform = host_info.get("platform", "unknown")
    username = defaults.get("username", "unknown")

    print("\n========================================")
    print(f"Task      : {task['name']}")
    print(f"Target    : {target_host_name} ({device_ip})")
    print(f"Platform  : {platform}")
    print(f"Username  : {username}")
    print("Planned commands:")
    for cmd in task["commands"]:
        print(f"  {cmd}")
    print("========================================")


if __name__ == "__main__":
    print("=== DRY RUN: trunk_lab ===")
    print("(No SSH connections are made here. I'm only printing the plan.)")

    for task in tasks:
        print_plan_for_task(task)
