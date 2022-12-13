
""" To close programs """
import subprocess
import os, time
""" To open programs """


""" subprocess.Popen("valorant.exe") """
time.sleep(t)
os.system("taskkill /f /im VALORANT-Win64-Shipping.exe")
""" os.system("run mspaint.exe") """


########################################

import subprocess
cmd = 'powershell "gps | where {$_.MainWindowTitle } | select ProcessName'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

apps = []

for line in proc.stdout:
    if line.rstrip():
        # only print lines that are not empty
        # decode() is necessary to get rid of the binary string (b')
        # rstrip() to remove `\r\n`
        app = line.decode().rstrip()
        apps.append(app)

print(apps)

######################################