import customtkinter
import subprocess
import os
import time
from os import listdir
import tkinter
from datetime import datetime
from elevate import elevate


elevate()
whoami = subprocess.run(["whoami"], capture_output=True, text=True, check=True)
username = whoami.stdout.strip()
user = username[-5:]
log = open("log.txt", "a")
time = datetime.now()
filepathh = os.path.abspath("main.py")
filepath = filepathh[:-7]
batch = f"{filepath}batch-scripts"
optimzations = 0



def basiccoffon():
    if basic.get():
        print("true")
    else:
        print("False")
    
def basiccleanup():
    global optimzations
    print("openeing tempfiles :()")
    try:
        for tempfile in listdir("C:\\Users\\acole\\AppData\\Local\\Temp"):
            os.remove(tempfile)
            optimzations = optimzations + 1
        for tempfile2  in listdir("C:\\Windows\\Temp"):
            os.remove(tempfile2)
            optimzations = optimzations + 1
    except FileNotFoundError:
        print("temps have already been deleted")
        pass
    subprocess.run("rd /s %systemdrive%\$Recycle.bin", shell=True)
    optimzations = optimzations + 1

def clearcache():
    global optimzations
    if os.path.exists("C:\\ProgramData\\LGHUB"):
        os.system(f"RMDIR /S /Q C:\\ProgramData\\LGHUB\\Cache")
        optimzations = optimzations + 1
        pass
    if os.path.exists(f"C:\\Users\\{user}\\AppData\\Roaming\\discord"):
        os.system(f"RMDIR /S /Q C:\\Users\\{user}\\AppData\\Roaming\\discord\\Cache")
        optimzations = optimzations + 1
        pass
    if os.path.exists(f"C:\\Users\\{user}\\AppData\\Roaming\\battle.net"):
        os.system(f"RMDIR /S /Q C:\\Users\\{user}\\AppData\\Roaming\\battle.net\\Cache")
        optimzations = optimzations + 1
        pass
    if os.path.exists(f"C:\\Users\\{user}\\AppData\\Roaming\\NVIDIA"):
        os.system(f"RMDIR /S /Q C:\\Users\\{user}\\AppData\\Roaming\\NVIDIA\\Cache")
        optimzations = optimzations + 1
        pass

    else:
        print("none can be found to be cleared")
        pass

def debloatlistcmd():
    global cachevar
    global cache
    if debloatlist.get():
        cachevar = tkinter.IntVar(value=0)
        cache = customtkinter.CTkCheckBox(main, text="Clear Cache", onvalue=1, offvalue=0, variable=cachevar, width=30, height=15)
        cache.place(relx=.73, rely=.35)
    else:
        cache.destroy()


def speedlist():
    global powercfg
    global powercfgvar
    global corruptedvar
    global drivervar
    global ramvar
    global ram
    global driver
    global corrupted

    if speedlists.get():
        powercfgvar = tkinter.IntVar(value=0)
        ramvar = tkinter.IntVar(value=0)
        drivervar = tkinter.IntVar(value=0)
        corruptedvar = tkinter.IntVar(value=0)
        powercfg = customtkinter.CTkCheckBox(main, text="Preformance Mode", onvalue=1, offvalue=0, variable=powercfgvar, width=30, height=15)
        powercfg.place(relx=.125, rely=.35)
        ram = customtkinter.CTkCheckBox(main, text="ram Optimization", onvalue=1, offvalue=0, variable=ramvar, width=30, height=15)
        ram.place(relx=.125, rely=.45)
        driver = customtkinter.CTkCheckBox(main, text="Driver Optimization", onvalue=1, offvalue=0, variable=drivervar, width=30, height=15)
        driver.place(relx=.125, rely=.55)
        corrupted = customtkinter.CTkCheckBox(main, text="Fix Corrupted Files", onvalue=1, offvalue=0, variable=corruptedvar, width=30, height=15)
        corrupted.place(relx=.125, rely=.65)
    else:
        powercfg.destroy()
        ram.destroy()
        driver.destroy()
        corrupted.destroy()
def corruptedoptimization():
    global optimzations
    try:
        corrupted_optimizer = os.path.join("batch-scripts", "sfc-scan.bat")
        subprocess.run([corrupted_optimizer], shell=True)
        optimzations = optimzations + 1
    except:
        log.write(f"Unkown error has accoured please report to 80dropz on twitter")
def driveroptimization():
    global optimzations
    try:
        driver_optimizer = os.path.join("batch-scripts", "Driver-Optimizor.bat")
        subprocess.run([driver_optimizer], shell=True)
        optimzations = optimzations + 1
    except FileNotFoundError:
        log.write(f"\n File not found (this is possibly due to not download zipfile from github) {time}")
    except:
        log.write(f"Unkown error has accoured please report to 80dropz on twitter")
def ramoptimization():
    global optimzations
    try:
        ram_optimizer = os.path.join("batch-scripts", "Ram-Optimizor.bat")
        subprocess.run([ram_optimizer], shell=True)
        optimzations = optimzations + 1
    except FileNotFoundError:
        log.write(f"\n File not found (this is possibly due to not download zipfile from github) {time}")
    except:
        log.write(f"Unkown error has accoured please report to 80dropz on twitter")
def high_performance():
    global optimzations
    try:
        # Run the powercfg command and capture the output
        result = subprocess.run(["powercfg", "-list"], capture_output=True, text=True, check=True)
        

        power_plans = result.stdout.splitlines()
        

        for line in power_plans:
            if "(High performance)" in line:
                parts = line.split()
                code = parts[3]
                time.sleep(1)
                os.system(f"powercfg -setactive {code}")
                print(f"set power config to high performance at {time}")
                log.write(f"\n set power config to high performance at {time}")
                optimzations = optimzations + 1

    except subprocess.CalledProcessError as e:
        log.write(f"An error occurred while running powercfg: {e}")
    except Exception as e:
        log.write(f"An unexpected error occurred: {e}")
    except:
        log.write(f"An unexpected error occurred")





def start():
    try:
        if cache.get():
            clearcache()
            print("Cleared Cache")
            pass
        if basic.get():
            print("basic error")
            basiccleanup()
            print("basic cleanup")
            pass
        if ram.get():
            print("ram optimization")
            ramoptimization()
            pass
        if powercfg.get():
            high_performance()
            print("powercfg")
            pass
        if driver.get():
            driveroptimization()
            print("Driver Optimized")
        if corrupted.get():
            corruptedoptimization()
            print("Corrupted Optimized")
            pass
        else:
            print("none selected")
            pass
    except:
        print("none selected")
        pass







        
main = customtkinter.CTk()
main.title("Windows Optimizer")
main.geometry("600x400")


header= customtkinter.CTkLabel(main, text="Windows Optimizer", font=("Roboto", 24))
header.place(relx=.5, rely=.05, anchor="center")
subheader= customtkinter.CTkLabel(main, text="By: @80dropz", font=("Roboto", 12))
subheader.place(relx=.5, rely=.12, anchor="center")

startbutton = customtkinter.CTkButton(main, text="Start", command=start, fg_color="Green", width=50, height=25)
startbutton.place(relx=.5, rely=.8, anchor="center")

speedlistsvar = tkinter.IntVar(value=0)
speedlists = customtkinter.CTkCheckBox(main, text="Boost Performance", onvalue=1, offvalue=0, command=speedlist, variable=speedlistsvar)
speedlists.place(relx=.2, rely=.3, anchor="center")

debloatlistvar = tkinter.IntVar(value=0)
debloatlist = customtkinter.CTkCheckBox(main, text="Debloat Windows", onvalue=1, offvalue=0, command=debloatlistcmd, variable=debloatlistvar)
debloatlist.place(relx=.8, rely=.3, anchor="center")

basicvar = tkinter.IntVar(value=0)
basic = customtkinter.CTkCheckBox(main, text="basic Cleanup", onvalue=1, offvalue=0, variable=basicvar, command=basiccoffon)
basic.place(relx=.5, rely=.3, anchor="center")

main.mainloop()