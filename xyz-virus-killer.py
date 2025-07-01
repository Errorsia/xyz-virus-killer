import os
import time
import tkinter as tk
from tkinter import messagebox

# from tkinter import columnspan

"""
Update Log:
Add Create & Read & Check config module.
Change name of some variables.

更新日志:
添加创建,读取和校验配置模块.
更改某些变量的名称.

Introduction:
This project mainly consists of  6 main modules:
    Kill Virus, Rename Virus Files, Repair Files, Write Log, Create & Read & Check config and the GUI (window).

And it also contains some other modules:
    Easter Egg.

The note of each function is below its name.
"""

Version = "VIRUS KILLER V1.4"

# Build log
# Condition: Messagebox return
build_Log = None

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
        tk.messagebox.showerror(title="error", message="Unknown Error: Please tell developers!!")
        write_Log("Unknown Error: Please tell developers!!")
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
    # Call two functions

    Kill_Viruses()
    fix_What_Viruses_Make()


def clean_Button():
    # Clean Screen Module: Clean Screen & Output

    global Easter_Egg

    var.set("VIRUS KILLER")
    t.delete("1.0", tk.END)

    # Easter_Egg module
    if Easter_Egg < 0:
        nothing = None
    elif Easter_Egg < 4:
        Easter_Egg += 1
    else:
        var.set("Copyright © 2024 - 2030 Arthur_xyz.All Rights Reserved")
        write_Log("\n\nCopyright © 2024 - 2030 Arthur_xyz.All Rights Reserved")
        write_Log("The Easter Egg was discovered by you!\n被你发现啦!")
        write_Log("Developer: Arthur_xyz\nEmail: Arthur_xyz@outlook.com\n\n")
        Easter_Egg = 0


def clean_Output():
    # Nothing will call this function
    # t.delete("1.0", tk.END)

    nothing = None


def create_Log():
    # Log Module: Create a log

    global build_Log, current_Log, Version

    if build_Log:
        current_time_stamp = "%.7f" % time.time()
        current_Log = f"log{current_time_stamp}"
        current_time = time.asctime()

        with open(f"./log{current_time_stamp}.log.arthur", "x", encoding="UTF-8") as file:
            file.write(f"{Version}\n")
            file.write(f"{current_Log}:\n")
            file.write(f"Current Work Path: {os.getcwd()}\n\n")
            file.write(f"{current_time}  Successfully run the program\n")
            file.write(f"Your operating system is: {os.name}\n\n\n")
            file.write("Operation Log:\n")

        # Create a bat to clean Logs
        if not os.path.exists("./Clean_Log.bat"):
            with open(f"./Clean_Log.bat", "w", encoding="UTF-8") as file:
                file.write(f"del /f /q *.arthur ")


def write_Log(log):
    # Log Module: Write OperationLog

    global build_Log, current_Log
    if build_Log:
        with open(f"./{current_Log}.log.arthur", "a", encoding="UTF-8") as file:
            file.write(f"{log}\n")


def log_configuration():
    # Config Module: Read & Check Config

    global build_Log

    if os.path.exists("./VIRUS_KILLER_CONFIGURATION.arthur_config"):
        with open(f"./VIRUS_KILLER_CONFIGURATION.arthur_config", "r", encoding="UTF-8") as file:
            log_config_read = file.read()
            log_enable = log_config_read[:1]

            if log_enable == "1":
                build_Log = True
                create_Log()
            elif log_enable == "0":
                build_Log = False
            else:
                # os.remove("./VIRUS_KILLER_CONFIGURATION.arthur_config")
                # os.system(f"del /f /q {os.getcwd()}\\VIRUS_KILLER_CONFIGURATION.arthur_config")
                log_get_message()

    else:
        log_get_message()


def log_get_message():
    # Config Module: If used for the first time, ask users

    global build_Log

    log_enable_bool = tk.messagebox.askokcancel(title="Save log or not",
                                                message="Do you want to save log?\n你想要保存日志吗?")
    if log_enable_bool:
        build_Log = True
        log_config(1)
        create_Log()
    else:
        build_Log = False
        log_config(0)


def log_config(log_config_value):
    # Config Module: Create Config

    os.system(f"attrib -h {os.getcwd()}\\VIRUS_KILLER_CONFIGURATION.arthur_config")
    with open("./VIRUS_KILLER_CONFIGURATION.arthur_config", "w", encoding="UTF-8") as file:
        file.write(f"{log_config_value};")
    os.system(f"attrib +h {os.getcwd()}\\VIRUS_KILLER_CONFIGURATION.arthur_config")


# Main Window (GUI)

window = tk.Tk()
window.title(Version)
window.geometry("1366x720")

var = tk.StringVar()

label1 = tk.Label(window, textvariable=var, bg="cyan", width=45, font=("Arial", 40), height=2)
label1.grid(row=0, column=0, columnspan=2)

button1 = tk.Button(window, text="Kill Viruses", font=30, width=40, height=2, command=Kill_Viruses)
button1.grid(row=1, column=0)

button2 = tk.Button(window, text="Fix What Viruses Make", font=30, width=40, height=2, command=fix_What_Viruses_Make)
button2.grid(row=2, column=0)

button3 = tk.Button(window, text="Auto Kill(Do #1 And #2)", font=30, width=40, height=2, command=Auto_Kill)
button3.grid(row=1, column=1)

button4 = tk.Button(window, text="Clean Screen", font=30, width=40, height=2, command=clean_Button)
button4.grid(row=2, column=1)

# button5 = tk.Button(window, text = "©", width = 1, height= 1, command= clean_Button)
# button5.pack()

label2 = tk.Label(window, width=10, font=20, height=2)
label2.grid(row=3, column=0, columnspan=2)

# text = "If you want to clean screen, press the Clean Screen button",
label3 = tk.Label(window, text="Output:", width=10, font=20, height=1)
label3.grid(row=4, column=0, columnspan=2)

t = tk.Text(window, height=30)
t.grid(row=5, column=0, columnspan=2)

var.set("VIRUS KILLER")

log_configuration()

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