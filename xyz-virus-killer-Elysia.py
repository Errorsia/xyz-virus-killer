import os
import time
import tkinter as tk
from os import mkdir
from tkinter import messagebox
import ttkbootstrap as ttkbs
from ttkbootstrap.constants import *

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

Author's message:
    The program is TESTING!
"""

'''
What is Class:
上帝每次都做抓老鼠的工作很累，所以上帝创造了一个全新类型的动物---猫，
上帝每次都丢东西很烦，所以上帝创造了一个全新类型的动物---狗，
女娲每次都捏人很累，所以女娲创造了能够自动生育的人---男人和女人，

上帝抓老鼠------函数模数
上帝定义了猫类-----内嵌抓老鼠的行为-----类模式------猫抓老鼠很简单。

走路-------函数模式
汽车-------类模式------走路变简单。

计算---函数

计算器-----类------计算变得简单


函数-----一种动作。

类-------解决问题的一类器物。
'''
Version = "VIRUS KILLER V1.6"

# Build log
# Condition: Messagebox return
build_Log = None

current_Log = None

appdata = os.path.expandvars("%APPDATA%")
file_directory = appdata + '/VIRUS_KILLER'

# Show Easter Egg
# Current condition: On (If Easter_Egg < 0, it's Off)
Easter_Egg = 0






def generate():

    global build_Log, file_directory

    check_working_path(file_directory)

    log(file_directory)



def check_working_path(_file_directory):

    dir_list = ['', '/Config', '/Log']
    for dir_tmp in dir_list:
        dir_tmp = _file_directory + dir_tmp
        if not os.path.exists(dir_tmp):
            mkdir(dir_tmp)


def log(_file_directory):
    global build_Log
    build_Log = log_configuration(build_Log, _file_directory)
    if build_Log:
        create_log()


def log_configuration(_build_log, _file_directory):
    # Config Module: Read & Check Config


    config_path = f'{_file_directory}/Config/VIRUS_KILLER_CONFIGURATION.Elysia'
    log_get_message = True
    log_config = None


    # Try to read config
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="UTF-8") as file:
            read_config = file.read()

        log_enable = read_config[0]
        if log_enable == "1":
            log_get_message = False
            _build_log = True
            log_config = 1

        elif log_enable == "0":
            log_get_message = False
            _build_log = False
            log_config = 0



    if log_get_message:
        _build_log = tk.messagebox.askokcancel(
            title="Save log or not",
            message="Do you want to save log?\n你想要保存日志吗?"
        )
        if _build_log:
            log_config = 1
        else:
            log_config = 0

    os.system(f"attrib -r -h {config_path}")
    with open(f"{config_path}", "w", encoding="UTF-8") as file:
        file.write(f"{log_config}")
    os.system(f"attrib +r +h {config_path}")

    return _build_log



def kill_viruses():
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


def repair_infected_files():
    # Virus File Repair Module: Show hidden files

    t.insert("end", "Showing Hidden Files:\n")
    write_Log("\nShowing Hidden Files:")

    for dir_tmp in ["E", "F", "G"]:
        # If you want to add other viruses. Add it in here.

        if os.path.exists(f"{dir_tmp}:\\"):
            os.system(f"ATTRIB -S -H {dir_tmp}:\\*.* /d /l")
            t.insert('end', f"Success to show hidden files in {dir_tmp}-disk\n")
            write_Log(f"Success to show hidden files in {dir_tmp}-disk")
        else:
            t.insert('end', f"{dir_tmp}-disk not found\n")
            write_Log(f"{dir_tmp}-disk not found")

    t.insert("end", "\n")
    var.set("FINISH")
    write_Log("Fix Virus Files Finished")


def Auto_Kill():
    # Call two functions

    kill_viruses()
    repair_infected_files()


def clean_Button():
    # Clean Screen Module: Clean Screen & Output

    global Easter_Egg

    var.set("VIRUS KILLER")
    t.delete("1.0", tk.END)

    # Easter_Egg module
    if Easter_Egg < 0:
        pass
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

    pass


def create_log():
    # Log Module: Create a log

    global build_Log, current_Log, Version, file_directory

    if build_Log:
        current_time_stamp = "%.7f" % time.time()
        current_Log = f"log{current_time_stamp}"
        current_time = time.asctime()

        with open(f"{file_directory}/Log/{current_Log}.log.avk", "x", encoding="UTF-8") as file:
            file.write(f"{Version}\n")
            file.write(f"{current_Log}:\n")
            file.write(f"Current Work Path: {os.getcwd()}\n\n")
            file.write(f"{current_time}  Successfully run the program\n")
            file.write(f"Your operating system is: {os.name}\n\n\n")
            file.write("Operation Log:\n")

        # Create a bat to clean Logs
        if not os.path.exists(f"{file_directory}/Log/Clean_Log.bat"):
            with open(f"{file_directory}/Log/Clean_Log.bat", "w", encoding="UTF-8") as file:
                file.write(f"del /f /q *.avk ")


def write_Log(content):
    # Log Module: Write OperationLog

    global build_Log, current_Log

    current_time = time.asctime()

    module = None
    level = None

    if build_Log:
        with open(f"{file_directory}/Log/{current_Log}.log.avk", "a", encoding="UTF-8") as file:
            file.write(f'{current_time}  {level}  [{module}]  {content}\n')


"""
def correct_log_config():
    # Haven't used

    global appdata
    content = None

    os.system(f"attrib -h {file_directory}/Config/VIRUS_KILLER_CONFIGURATION.Elysia")

    with open(f"{file_directory}/Config/VIRUS_KILLER_CONFIGURATION.Elysia", "r", encoding="UTF-8") as file1:
        content = file.read()



    with open(f"{file_directory}/Config/VIRUS_KILLER_CONFIGURATION.Elysia", "r", encoding="UTF-8") as file2:


    os.system(f"attrib +h {file_directory}/Config/VIRUS_KILLER_CONFIGURATION.Elysia")
"""
# Haven't Used



# Main Window (GUI)

window = ttkbs.Window()
window.title(Version)
window.geometry("1360x720")
window.minsize(1360, 720)
window.maxsize(1920, 1080)
window.iconbitmap("icon.ico")

var = tk.StringVar()

label1 = tk.Label(window, textvariable=var, bg="cyan", width=45, font=("Arial", 40), height=2)
label1.grid(row=0, column=0, columnspan=12)

label2 = tk.Label(window, width=10, font=20, height=2)
label2.grid(row=1, column=0, columnspan=12)


frame_button1 = tk.Frame(window, height=3, width=100)
button1 = ttkbs.Button(frame_button1, text="Kill Viruses", width=40, bootstyle=SUCCESS, command=kill_viruses)
button1.pack(side=LEFT, padx=10, pady=5)

button2 = ttkbs.Button(frame_button1, text="Fix What Viruses Make", width=40, bootstyle=SUCCESS, command=repair_infected_files)
button2.pack(side=LEFT, padx=10, pady=5)

frame_button1.grid(row=4, column=0, columnspan=6)


frame_button2 = tk.Frame(window, height=3, width=100)

button3 = ttkbs.Button(frame_button2, text="Auto Kill(Do #1 And #2)", width=40, bootstyle=SUCCESS, command=Auto_Kill)
button3.pack(side=LEFT, padx=10, pady=5)

button4 = ttkbs.Button(frame_button2, text="Clean Screen", width=40, bootstyle=SUCCESS, command=clean_Button)
button4.pack(side=LEFT, padx=10, pady=5)

frame_button2.grid(row=5, column=0, columnspan=6)

# button5 = tk.Button(window, text = "©", width = 1, height= 1, command= clean_Button)
# button5.pack()


# text = "If you want to clean screen, press the Clean Screen button",
label3 = tk.Label(window, text="Output:", width=10, font=20, height=1)
label3.grid(row=2, column=6, columnspan=6)


t = tk.Text(window, height=30)
output_Text = tk.Text(window, height=30)
output_Text.grid(row=3, column=6, columnspan=6, rowspan=10)
output_Text.configure(state='disabled')

var.set("VIRUS KILLER")

generate()

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