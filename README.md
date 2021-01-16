# SteveSercerScripts
Automation scripts for MacOS Servers

## AutoBoot.py
This script will check if the list of programs in ```check_list.txt``` is running. Each time the script is called the ```AutoBoot.log``` file is 
updated with the go/no-go status of each program in the list. If a program is found to be stalled or unresponsive the script will attempt to reboot it.

The log file is cleared every 30 days (script is meant to be ran daily), and will only clear if the log reports no ```ERROR``` cases.

This tool is used to diagnose when/if certian programs are failing and find paterns of why they would fail.
