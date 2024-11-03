import customtkinter
import subprocess
import os
import time
from os import listdir
import tkinter
from datetime import datetime
from elevate import elevate
try:
    elevate()
except:
    print("Some features may be dissabled due to not running in administartor mode \n Some features may be dissabled due to not running in administartor mode \nSome features may be dissabled due to not running in administartor mode \nSome features may be dissabled due to not running in administartor mode \n")

#grabs the 4 letter handle of the user running the script
whoami = subprocess.run(["whoami"], capture_output=True, text=True, check=True)
username = whoami.stdout.strip()
user = username[-5:]

#starts the log appending on this script
log = open("log.txt", "a")
time = datetime.now()

filepathh = os.path.abspath("main.py")
filepath = filepathh[:-7]
batch = f"{filepath}batch-scripts"
#counts the number of optimizations made
optimzations = 0


#just deletes temp folder and clears the recyling bin
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



#should clear the cache of most common apps installed in computers
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
        #creates the variables for all the checkboxes in the function so when running will check for them and run the correct command
        powercfgvar = tkinter.IntVar(value=0)
        ramvar = tkinter.IntVar(value=0)
        drivervar = tkinter.IntVar(value=0)
        corruptedvar = tkinter.IntVar(value=0)
        
        #just creates the buttons, text, and placement of the buttons
        powercfg = customtkinter.CTkCheckBox(main, text="Preformance Mode", onvalue=1, offvalue=0, variable=powercfgvar, width=30, height=15)
        powercfg.place(relx=.125, rely=.35)
        ram = customtkinter.CTkCheckBox(main, text="ram Optimization", onvalue=1, offvalue=0, variable=ramvar, width=30, height=15, command=lambda: print("ram is clicked"))
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

#should run the corrupted file remover from batch scripts
def corruptedoptimization():
    global optimzations
    try:
        corrupted_optimizer = os.path.join("batch-scripts", "sfc-scan.bat")
        subprocess.run([corrupted_optimizer], shell=True)
        optimzations = optimzations + 1
    except:
        log.write(f"Unkown error has accoured please report to 80dropz on twitter")

#should optimize your drivers i can check this
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




#runs the ram optimization script off the optimized folder
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



#runs the higher performance script from batch scripts folder
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




#checks if for every optimization to see if it has been checked or not
def start():
    try:
        if cache.get():
            log.write(f"cache ran noramlly at {time}")
            clearcache()
            print("Cleared Cache")
            pass
        if basic.get():
            log.write(f"basic configuration ran noramlly at {time}")
            print("basic error")
            basiccleanup()
            print("basic cleanup")
            pass
        if ram.get():
            log.write(f"ram ran noramlly at {time}")
            print("ram optimization")
            ramoptimization()
            pass
        if powercfg.get():
            log.write(f"powercfg ran noramlly at {time}")
            high_performance()
            print("powercfg")
            pass
        if driver.get():
            log.write(f"driver ran noramlly at {time}")
            driveroptimization()
            print("Driver Optimized")
        if corrupted.get():
            log.write(f"Corrupted ran noramlly at {time}")
            corruptedoptimization()
            print("Corrupted Optimized")
            pass
        else:
            print("none selected")
            pass
        log.write(f"\n finished optimization at {time} optimized {optimzations} things")
        finished()
    except:
        log.write(f"no optimizations were found {time}")
        print("none selected")
        pass



def finished():
    print("\n \n \n \n \n \n \n \n YOUR PC HAS BEEN OPTIMIZED")






        
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

#creats the basic cleanup (overall optimzations)
basicvar = tkinter.IntVar(value=0)
basic = customtkinter.CTkCheckBox(main, text="basic Cleanup", onvalue=1, offvalue=0, variable=basicvar)
basic.place(relx=.5, rely=.3, anchor="center")

main.mainloop()
