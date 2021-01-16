# Imports
import subprocess
import os
import logging
import psutil
from datetime import datetime, timedelta
from time import sleep

# Check if single process is running
def check_running(process_name):
    for process in psutil.process_iter():
        try:
            if process_name.lower() in process.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            return False

# Create log file
LOG_FORMAT = "%(levelname)s %(asctime)s: %(message)s"
logging.basicConfig(filename = "AutoBoot.log", level = logging.DEBUG, format = LOG_FORMAT)
logger = logging.getLogger()

# Clear log file if no ERRORS and log file is over 30 days old
with open('AutoBoot.log') as input_log:
    check_date = input_log.readline().split()
    past = datetime.strptime(check_date[1], '%Y-%m-%d')
    present = datetime.today()
    check_log = input_log.read()
    if (present-past).days > 30 and not 'ERROR' in check_log:
        open('AutoBoot.log', 'w').close()
    else:
        pass

logger.debug("Running AutoBoot") # write to debug so script starting date can be established
# List of Programs that need to be checked
with open('check_list.txt') as input_txt:
    check_list = input_txt.read().splitlines()

# Check if Programs in list are running
for process in check_list:
    if check_running(process):
        # print running
        logger.info("Process: " + process + " Status: RUNNING")
    else:
        # print not running
        logger.warning("Process: " + process + " Status: STOPPED")
        # Attempt process restart
        os.system("""osascript -e 'tell app """+ process +""" to open'""")
        sleep(1) # Wait for process to boot
        if check_running(process):  # Check if running
            logger.info("Process: " + process + " Status: FIXED")
        else:                       # If not throw ERROR
            logger.error("Process: " + process + " Status: BROKEN")




