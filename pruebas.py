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
apps = apps[2:]
print(apps)


def onactivate(evt):
    menu = optmenu['menu']
    menu.delete(0, tkinter.END)
    menu.add_command(label='new choice 1')
    menu.add_command(label='new choice 2')
    menu.add_separator()
    menu.add_command(label='new choice 3')
    optvar.set('new choice 1')