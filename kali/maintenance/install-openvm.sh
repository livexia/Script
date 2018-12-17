#/bin/sh
sudo apt update && apt -y full-upgrade

# Reboot now in case you have updated to a new kernel. Once rebooted:
sudo apt -y --reinstall install open-vm-tools-desktop fuse
