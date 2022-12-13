from tkinter import *
from PIL import ImageTk, Image
import subprocess, os, pathlib

# We calling opened applicatiosn
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
root = Tk()
root.geometry("950x500")

# Images directive
logo_file_name = "logo-title.png"
current_dir = pathlib.Path(__file__).parent.resolve() # current directory
# Complete logo path
img_path = current_dir.joinpath("assets\\" + logo_file_name) # join with your image's file name
# Complete arrows path
arrow_down_file_name = "arrow-down.png"
arrow_up_file_name = "arrow-up.png"
arrow_down_path = current_dir.joinpath("assets\\" + arrow_down_file_name) # join with your image's file name
arrow_up_path = current_dir.joinpath("assets\\" + arrow_up_file_name) # join with your image's file name

arrow_down = ImageTk.PhotoImage(master = root, data = arrow_down_path)
arrow_up = ImageTk.PhotoImage(master = root, data = arrow_up_path)


# Start 
root.title("STOP PROCASTINATION")

# Logo
imgLogo = ImageTk.PhotoImage(Image.open(img_path))
 
# Creating a Label Widget
myLabel1 = Label(root, image=imgLogo, bd=25)
myLabel2 = Label(root, text="The program that will help you stop procrastinating")
myLabel3 = Label(root, text="Select the application you want to don't use:")

# Apps menu
combo = StringVar(root)
combo.set("Which app that make you procastinating?") # Default value
dropDown = OptionMenu(root, combo, *apps)



# Time
timeInput = Entry()

# Submit button

submit = Button(root, text="Submit", bg="#00a6fb", justify=CENTER, width=30, height=2)

# Showing it onto the screen
myLabel1.pack()
myLabel2.pack()
myLabel3.pack()
dropDown.pack()
timeInput.pack()
submit.pack()

# Kepps windows opend until user close it
root.mainloop()