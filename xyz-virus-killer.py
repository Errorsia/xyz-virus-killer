import os
import tkinter as tk
import time

"""
Update Log:
Add the Log Module
Add an Easter Egg

更新日志:
增添了日志模块
增添了一个彩蛋

Introduction:
This project mainly depend on 5 main modules:
    Kill Virus, Rename Virus Files, Repair Files, Log and the GUI (window).
    The note of each function is below its name.
"""

Version = "VIRUS KILLER V1.3"

# Build log
# Current condition: On
build_Log = True

current_Log = None

# Show Easter Egg
# Current condition: On (If Easter_Egg < 0, it's Off)
Easter_Egg = 0


def Kill_Viruses():
    # Virus killer main module

    # clean_Output()
    t.insert("end", "Killing Processes:\n")
    write_Log("\nKilling Processes:")

    for processes in ["Rundll32.exe", "AvastSvc.exe", "wscript.exe", "Autolt3.exe", "cmd.exe"]:
        # If you want to add other viruses' processes. Add it in here.
        taskkill_Processes(processes)

    t.insert("end", "\n")
    var.set("FINISH")
    write_Log("Killing Processes Finished\n")
    rename_Virus_Files()


def taskkill_Processes(process_Name):
    # Virus killer module: Taskkill virus processes

    return_taskkill = os.system(f"TASKKILL -F -IM {process_Name} -T")
    if return_taskkill == 1:
        t.insert("end", "Success to kill virus \n")
        write_Log(f"Success to kill virus: {process_Name}")
        return True
    elif return_taskkill == 128:
        t.insert("end", "Error: Virus process not Found\n")
        write_Log(f"Error: Virus process ({process_Name}) not Found")
        return False
    else:
        t.insert("end", "Error: Please tell developers!!\n")
        write_Log(f"Unknown Error: Please tell developers!!")
        return False


def rename_Virus_Files():
    # Virus Files Rename Module: Select disks

    t.insert("end", "Renaming Files:\n")
    write_Log("Renaming Files:")

    for disk_name in ["E", "F", "G"]:
        # If you want to add other dirs. Add it in here.
        rename_Files(disk_name)

    t.insert("end", "\n")
    var.set("FINISH")
    write_Log("Renaming Files Finished")


def rename_Files(dir_name):
    # Virus Files Rename Module: Rename the Virus Files

    if os.path.exists(f"{dir_name}:\\"):
        result = os.system(f"ren {dir_name}:\\*.lnk *.vir")
        t.insert("end", f"Success to rename virus files in {dir_name}-disk\n")
        write_Log(f"Success to rename virus files in {dir_name}-disk")
    else:
        t.insert("end", f"{dir_name}-disk not found\n")
        write_Log(f"Error: {dir_name}-disk not found  Please check and restart the program")


def fix_What_Viruses_Make():
    # Virus File Repair Module: Show hidden files

    t.insert("end", "Showing Hidden Files:\n")
    write_Log("\nShowing Hidden Files:")

    for dir_tmp in ["E", "F", "G"]:
        # If you want to add other viruses. Add it in here.

        if os.path.exists(f"{dir_tmp}:\\"):
            os.system(f"ATTRIB -S -H {dir_tmp}:\\*.* /d /l")
            t.insert("end", f"Success to show hidden files in {dir_tmp}-disk\n")
            write_Log(f"Success to show hidden files in {dir_tmp}-disk")
        else:
            t.insert("end", f"{dir_tmp}-disk not found\n")
            write_Log(f"{dir_tmp}-disk not found")

    t.insert("end", "\n")
    var.set("FINISH")
    write_Log("Fix Virus Files Finished")


def Auto_Kill():
    Kill_Viruses()
    fix_What_Viruses_Make()


def clean_Button():
    global Easter_Egg

    var.set("VIRUS KILLER")
    t.delete("1.0", tk.END)

    # Easter_Egg module
    if Easter_Egg < 0:
        None
    elif Easter_Egg < 4:
        Easter_Egg += 1
    else:
        var.set("Copyright © 2024 - 2030 Arthur_xyz.All Rights Reserved")
        write_Log("\n\nCopyright © 2024 - 2030 Arthur_xyz.All Rights Reserved")
        write_Log("The Easter Egg was discovered by you!\n被你发现啦!")
        write_Log("Developer: Arthur_xyz\nEmail: Arthur_xyz@outlook.com\n\n")
        Easter_Egg = 0


def clean_Output():
    # t.delete("1.0", tk.END)
    None


def create_Log():
    # Log Module: Create a log
    global build_Log, current_Log, Version

    if build_Log:
        current_time_stamp = time.time()
        current_Log = f"log{current_time_stamp}"
        current_time = time.asctime()

        with open(f"./log{current_time_stamp}.log.arthur", "x", encoding="utf-8") as file:
            file.write(f"{Version}\n")
            file.write(f"{current_Log}:\n")
            file.write(f"Current Work Path: {os.getcwd()}\n\n")
            file.write(f"{current_time}  Successfully run the program\n")
            file.write(f"Your operating system is: {os.name}\n\n\n")
            file.write("Operation Log:\n")

        # Create a bat to clean Logs
        # Current condition: Off
        if False:
            with open(f"./Clean_Log.bat", "w", encoding="utf-8") as file:
                file.write(f"del /f /q *.arthur ")


def write_Log(log):
    # Log Module: Write OperationLog

    global build_Log, current_Log
    if build_Log:
        with open(f"./{current_Log}.log.arthur", "a", encoding="utf-8") as file:
            file.write(f"{log}\n")


# Main Window (GUI)

window = tk.Tk()
window.title(Version)
window.geometry("1366x720")

var = tk.StringVar()

lable1 = tk.Label(window, textvariable=var, bg="cyan", width=45, font=("Arial", 40), height=2)
lable1.pack()

button1 = tk.Button(window, text="Kill Viruses", font=30, width=40, height=2, command=Kill_Viruses)
button1.pack()

button2 = tk.Button(window, text="Fix What Viruses Make", font=30, width=40, height=2, command=fix_What_Viruses_Make)
button2.pack()

button3 = tk.Button(window, text="Auto Kill(Do #1 And #2)", font=30, width=40, height=2, command=Auto_Kill)
button3.pack()

button4 = tk.Button(window, text="Clean Screen", font=30, width=40, height=2, command=clean_Button)
button4.pack()

# button5 = tk.Button(window, text = "©", width = 1, height= 1, command= clean_Button)
# button5.pack()

lable2 = tk.Label(window, width=10, font=20, height=2)
lable2.pack()

# text = "If you want to clean screen, press the Clean Screen button",
lable3 = tk.Label(window, text="Output:", width=10, font=20, height=1)
lable3.pack()

t = tk.Text(window, height=25)
t.pack()

var.set("VIRUS KILLER")

create_Log()

window.mainloop()

"""
Copyright © 2030
Copyright © 2024 - 2030 Arthur_xyz.All Rights Reserved
© 2024 - 2030 Arthur_xyz版权所有

如果您意外获取了源码，请联系 Arthur_xyz (Arthur_xyz@outlook.com)
If you accidentally obtain the source code, please contact Arthur_xyz (Arthur_xyz@outlook.com)

如果你想创建依赖于(xyz病毒杀手)的项目,
请联系Arthur_xyz (Arthur_xyz@outlook.com)
If you want to create your own project depend on this (xyz virus killer),
please contact Arthur_xyz (Arthur_xyz@outlook.com)
"""
