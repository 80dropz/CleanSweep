import subprocess
import os
filesfound = []


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



def systemscandef(directory):
    global sizeremoved
    for entry in os.scandir(directory):
        print(entry)
        if entry.is_file():
            if os.path not in filesfound:
                filesfound.append(os.path.basename(entry))
            else:
                size += get_directory_size(entry)
                os.remove(entry)
        elif entry.is_dir():
            systemscandef(os.path.join(directory, entry))
    print("Done!")


if __name__ == "__main__":
    systemscandef(r"D:\code-shi\socket-rat")