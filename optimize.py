try:
    import customtkinter
    import subprocess
    import os
    import time
    from os import listdir
    import tkinter
    from datetime import datetime
    from elevate import elevate
except:
    subprocess.run("pip install customtkinter os tkinter datetime elevate", shell=True)
try:
    elevate()
except:
    print("Some features may be dissabled due to not running in administartor mode \n Some features may be dissabled due to not running in administartor mode \nSome features may be dissabled due to not running in administartor mode \nSome features may be dissabled due to not running in administartor mode \n")


print(r"           /$$$$$$  /$$       /$$$$$$$$  /$$$$$$  /$$   /$$  /$$$$$$  /$$      /$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$$ ")
print(r"          /$$__  $$| $$      | $$_____/ /$$__  $$| $$$ | $$ /$$__  $$| $$  /$ | $$| $$_____/| $$_____/| $$__  $$")
print(r"         | $$  \__/| $$      | $$      | $$  \ $$| $$$$| $$| $$  \__/| $$ /$$$| $$| $$      | $$      | $$  \ $$")
print(r"         | $$      | $$      | $$$$$   | $$$$$$$$| $$ $$ $$|  $$$$$$ | $$/$$ $$ $$| $$$$$   | $$$$$   | $$$$$$$/")
print(r"         | $$      | $$      | $$__/   | $$__  $$| $$  $$$$ \____  $$| $$$$_  $$$$| $$__/   | $$__/   | $$____/ ")
print(r"         | $$    $$| $$      | $$      | $$  | $$| $$\  $$$ /$$  \ $$| $$$/ \  $$$| $$      | $$      | $$      ")
print(r"         |  $$$$$$/| $$$$$$$$| $$$$$$$$| $$  | $$| $$ \  $$|  $$$$$$/| $$/   \  $$| $$$$$$$$| $$$$$$$$| $$      ")
print(r"          \______/ |________/|________/|__/  |__/|__/  \__/ \______/ |__/     \__/|________/|________/|__/      ")

#grabs the 4 letter handle of the user running the script
filesfound = []
commands = ["cache", "basic", "ram", "powercfg", "driver", "corrupted"]
whoami = subprocess.run(["whoami"], capture_output=True, text=True, check=True)
username = whoami.stdout.strip()
user = username[-5:]
cachelocation = [fr"C:\ProgramData\LGHUB\Cache",fr"C:\Users\{user}\AppData\Roaming\discord\Cache", fr"C:\Users\{user}\AppData\Roaming\battle.net\Cache", fr"C:\Users\{user}\AppData\Roaming\NVIDIA\Cache", fr"C:\Users\{user}\AppData\Roaming\G HUB\Cache", fr"C:\Users\{user}\AppData\Roaming\G HUB\Code Cache", fr"C:\Users\{user}\AppData\Roaming\G HUB\GPUCache",
                 fr"C:\Users\{user}\AppData\Roaming\NVIDIA\ComputeCache", fr"C:\Users\{user}\AppData\Roaming\.minecraft\webcache2\Code Cache", fr"C:\Users\{user}\AppData\Roaming\.minecraft\webcache2\Cache", fr"C:\Users\{user}\AppData\Local\VALORANT\Saved\Crashes"]

#starts the log appending on this script
log = open("log.txt", "a")
time = datetime.now()

filepathh = os.path.abspath("main.py")
filepath = filepathh[:-7]
batch = f"{filepath}batch-scripts"
#counts the number of optimizations made
optimzations = 0
sizeremoved = 0



#I skidded this from "https://thepythoncode.com/article/get-directory-size-in-bytes-using-python" goat article just cant be asked to type allat SHOUTOUT "Abdeladim Fadheli"
def get_directory_size(directory):

    total = 0
    try:
        # print("[+] Getting the size of", directory)
        for entry in os.scandir(directory):
            if entry.is_file():
                # if it's a file, use stat() function
                total += entry.stat().st_size
            elif entry.is_dir():
                # if it's a directory, recursively call this function
                try:
                    total += get_directory_size(entry.path)
                except FileNotFoundError:
                    pass
    except NotADirectoryError:
        # if `directory` isn't a directory, get the file size then
        return os.path.getsize(directory)
    except PermissionError:
        # if for whatever reason we can't open the folder, return 0
        return 0
    return total


#i also skidded this thank you sm "Abdeladim Fadheli" ---- "https://thepythoncode.com/article/get-directory-size-in-bytes-using-python"
def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"

def basiccleanup():
    global optimzations
    global sizeremoved
    print("openeing tempfiles :()")
    try:
        for tempfile in listdir("C:\\Users\\acole\\AppData\\Local\\Temp"):
            size = get_directory_size(tempfile)
            os.remove(tempfile)
            sizeremoved += size
            optimzations += 1
        for tempfile2  in listdir("C:\\Windows\\Temp"):
            size = get_directory_size(tempfile2)
            os.remove(tempfile2)
            sizeremoved += size
            optimzations += 1
    except FileNotFoundError:
        print("temps have already been deleted")
        pass
    subprocess.run("rd /s %systemdrive%\\$Recycle.bin", shell=True)
    optimzations += 1

def clearcache():
    global optimzations
    global sizeremoved
    for path in cachelocation:
        print(f"Checking: {path}")
        if os.path.exists(path):
            size = get_directory_size(path)
            try:
                # Enclose the path in double quotes to handle spaces
                subprocess.run(f'RMDIR /S /Q "{path}"', shell=True, check=True)
                print(f"Removed: {path}")
                sizeremoved += size
                optimzations += 1
            except subprocess.CalledProcessError as e:
                print(f"Failed to remove {path}. Error: {e}")
            except Exception as e:
                print(f"Unknown error while removing {path}. Error: {e}")
        else:
            print(f"Path not found: {path}")


def systemscandef(directory):
    global sizeremoved
    for file in os.listdir(directory):
        print(file)
        if file.is_file():
            if os.path not in filesfound:
                filesfound.append(os.path.basename(file))
            else:
                size += get_directory_size(file)
                os.remove(file)
        elif file.is_dir():
            systemscandef(os.path.join(directory, file))
    print("Done!")





def debloatlistcmd():
    global cachevar
    global systemscan
    global systemscanvar
    global cache
    if debloatlist.get():
        cachevar = tkinter.IntVar(value=0)
        systemscanvar = tkinter.IntVar(value=0)
        systemscan = customtkinter.CTkCheckBox(main, text="System Scan (Will take a while)", onvalue=1, offvalue=0, variable=cachevar, width=30, height=15)
        systemscan.place(relx=.73, rely=.45)
        cache = customtkinter.CTkCheckBox(main, text="Clear Cache", onvalue=1, offvalue=0, variable=systemscanvar, width=30, height=15)
        cache.place(relx=.73, rely=.35)
    else:
        systemscan.destroy()
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
        optimzations += 1
    except:
        log.write(f"Unkown error has accoured please report to 80dropz on twitter")

#should optimize your drivers i can check this
def driveroptimization():
    global optimzations
    try:
        driver_optimizer = os.path.join("batch-scripts", "Driver-Optimizor.bat")
        subprocess.run([driver_optimizer], shell=True)
        optimzations += 1
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
        optimzations += 1
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
                optimzations += 1
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
                clearcache()
                print("Cleared Cache")
                pass
        except:
            pass
        try:
            if systemscan.get():
                print("scanning system")
                systemscandef("C:\\")
                print("Scanned System")
                pass
        except:
            pass
        try:
            if basic.get():
                print("basic error")
                basiccleanup()
                print("basic cleanup")
                pass
        except:
            pass
        try:
            if ram.get():
                print("ram optimization")
                ramoptimization()
                pass
        except:
            pass
        try:
            if powercfg.get():
                high_performance()
                print("powercfg")
                pass
        except:
            pass
        try:
            if driver.get():
                driveroptimization()
                print("Driver Optimized")
        except:
            pass
        try:
            if corrupted.get():
                corruptedoptimization()
                print("Corrupted Optimized")
                pass
        except:
            pass
        print("\n \n \n \n \n \n \n \n YOUR PC HAS BEEN OPTIMIZED")
        print("Total Size Removed: ", get_size_format(sizeremoved))




        
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
