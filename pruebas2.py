from tkinter import *
import subprocess

# We calling opened applicatiosn
cmd = 'powershell "gps | where {$_.MainWindowTitle } | select ProcessName,Path'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
apps = []
for line in proc.stdout:
    if line.rstrip():
        # only print lines that are not empty
        # decode() is necessary to get rid of the binary string (b')
        # rstrip() to remove `\r\n`
        app = line.decode().rstrip()
        apps.append(app)

root = Tk()

root.title("STOP PROCASTINATION")


# Creating a Label Widget
myLabel1 = Label(root, text="STOP PROCASTINATION")
myLabel2 = Label(root, text="The program that will help you stop procrastinating")

combo = StringVar(root)
combo.set("Select the app that make you procastinating") # Default value

w = OptionMenu(root, combo, *apps)

# Showing it onto the screen
myLabel1.pack()
myLabel2.pack()
w.pack()


root.mainloop()