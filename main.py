import os
import customtkinter
import subprocess
from datetime import datetime
logfilecreate = open("log.txt", "w")
log = open("log.txt", "a")
time = datetime.now()
def cleaning():
    log.write(f"\n cleaning button pressed at {time}")
    try:
        os.system(f'python cleaner.py')
    except FileNotFoundError:
        log.write(f"\n File not found (this is possibly due to not download zipfile from github) {time}")

def optimization():
    log.write(f"\n Optimization button pressed at {time}")
    print("Opitimizer")
    try:
        os.system(f'python optimize.py')
    except FileNotFoundError:
        log.write(f"\n File not found (this is possibly due to not download zipfile from github) {time}")

main = customtkinter.CTk()
main.title("Windows Cleaner / Optimizer")
main.geometry("300x150")
log.write(f"\n Main Gui started at {time}")

header = customtkinter.CTkLabel(main, text="Windows Cleaner / Optimizer", font=("Roboto", 20))
header.place(relx=.5, rely=.05, anchor="center")
subheader = customtkinter.CTkLabel(main, text="By: @80dropz", font=("Roboto", 10))
subheader.place(relx=.5, rely=.25, anchor="center")


optimizerbtn = customtkinter.CTkButton(main, text="Optimization", command=optimization, fg_color="Green", width=75, height=50)
optimizerbtn.place(relx=.25, rely=.6, anchor="center")
cleaningbtn = customtkinter.CTkButton(main, text="COMING SOON", command=cleaning, fg_color="Red", width=75, height=50)
cleaningbtn.place(relx=.75, rely=.6, anchor="center")



main.mainloop()