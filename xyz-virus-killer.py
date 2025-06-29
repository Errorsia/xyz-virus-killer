import os
import tkinter as tk
import time

"""
Update Log:
Add the Log System

更新日志:
增添了日志系统
"""

version = "VIRUS KILLER V1.2"
build_log = True
current_log = None


def Kill_Viruses():  # Virus killer main module

    clean_Output()
    t.insert("end", "Killing Processes:\n")
    log("Killing Processes:")

    for processes in ["Rundll32.exe", "AvastSvc.exe", "wscript.exe", "Autolt3.exe", "cmd.exe"]:
        # If you want to add other viruses. Add it in here.
        return_Taskkill_Processes(processes)

    t.insert("end", "\n")
    var.set("FINISH")
    log("Killing Processes Finished\n")
    rename_Files()


def return_Taskkill_Processes(process_Name):
    return_taskkill = os.system("TASKKILL -F -IM " + process_Name + " -T")
    if return_taskkill == 1:
        t.insert("end", "Success to kill virus\n")
        log("Success to kill virus")
        return True
    elif return_taskkill == 128:
        t.insert("end", "Error: Virus process not Found\n")
        log(f"Error: Virus process ({process_Name}) not Found")
        return False
    else:
        t.insert("end", "Error: Please tell developers!!\n")
        log(f"Unknown Error: Please tell developers!!")
        return False


def rename_Files():
    # Virus killer module: Rename the Virus Files

    t.insert("end", "Renaming Files:\n")
    log("Renaming Files:")

    for dir_name in ["E", "F", "G"]:
        # If you want to add other dirs. Add it in here.
        return_Ren_Files(dir_name)

    t.insert("end", "\n")
    var.set("FINISH")
    log("Renaming Files Finished")


def return_Ren_Files(dir_name):
    if os.path.exists(f"{dir_name}:\\"):
        result = os.system(f"ren {dir_name}:\\*.lnk *.vir")
        t.insert("end", f"Success to rename virus files in {dir_name}-disk\n")
        log(f"Success to rename virus files in {dir_name}-disk")
    else:
        t.insert("end", f"{dir_name}-disk not found\n")
        log(f"Error: {dir_name}-disk not found  Please check and restart the program")


def fix_What_Viruses_Make():
    t.insert("end", "Showing Hidden Files:\n")

    for dir_tmp in ["E", "F", "G"]:
        # If you want to add other viruses. Add it in here.
        if os.path.exists(f"{dir_tmp}:\\"):
            os.system(f"ATTRIB -S -H {dir_tmp}:\\*.* /d /l")
            t.insert("end", f"Success to show hidden files in {dir_tmp}-disk\n")
        else:
            t.insert("end", f"{dir_tmp}-disk not found\n")

    t.insert("end", "\n")
    # More ATTRIB commands here
    var.set("FINISH")


def Auto_Kill():
    Kill_Viruses()
    fix_What_Viruses_Make()


def clean_Button():
    var.set("VIRUS KILLER")
    t.delete("1.0", tk.END)


def clean_Output():
    t.delete("1.0", tk.END)


def create_Log():
    # Log System: Create a log
    global build_log, current_log, version

    if build_log:
        current_time_stamp = time.time()
        current_log = f"log{current_time_stamp}"
        current_time = time.asctime()

        with open(f"./log{current_time_stamp}.arthur", "x", encoding="utf-8") as file:
            file.write(f"{version}\n")
            file.write(f"{current_log}:\n\n")
            file.write(f"{current_time}  Successfully run the program\n")
            file.write(f"Your operating system is: {os.name}\n\n\n")
            file.write("Operationlog:\n")


def log(log):
    # Log System: Write OperationLog

    global build_log, current_log
    if build_log:
        with open(f"./{current_log}.arthur", "a", encoding="utf-8") as file:
            file.write(f"{log}\n")


# Main Window

window = tk.Tk()
window.title("VIRUS KILLER Copyright © 2030")
window.geometry("1366x720")

var = tk.StringVar()

lable1 = tk.Label(window, textvariable=var, bg="cyan", width=45, font=("Arial", 40), height=2)
lable1.pack()

buttom1 = tk.Button(window, text="Kill Viruses", font=30, width=40, height=2, command=Kill_Viruses)
buttom1.pack()

buttom2 = tk.Button(window, text="Fix What Viruses Make", font=30, width=40, height=2, command=fix_What_Viruses_Make)
buttom2.pack()

buttom3 = tk.Button(window, text="Auto Kill(Do #1 And #2)", font=30, width=40, height=2, command=Auto_Kill)
buttom3.pack()

buttom4 = tk.Button(window, text="Clean Screen", font=30, width=40, height=2, command=clean_Button)
buttom4.pack()

# buttom5 = tk.Button(window, text = "©", width = 1, height= 1, command= clean_Button)
# buttom5.pack()

lable2 = tk.Label(window, width=10, font=20, height=2)
lable2.pack()

# text = "If you want to clean screen, press the Clean Screen buttom",
lable3 = tk.Label(window, text="Output:", width=10, font=20, height=1)
lable3.pack()

t = tk.Text(window, height=25)
t.pack()

var.set("VIRUS KILLER")

create_Log()

window.mainloop()

"""
Copyright © 2030
© 2024-2030 Arthur_xyz版权所有

如果您意外获取了源码，请联系 Arthur_xyz (Arthur_xyz@outlook.com)
If you accidentally obtain the source code, please contact Arthur_xyz (Arthur_xyz@outlook.com)

如果你想创建依赖于(xyz病毒杀手)的项目,
请联系Arthur_xyz (Arthur_xyz@outlook.com)
If you want to create your own project depend on this (xyz virus killer),
please contact Arthur_xyz (Arthur_xyz@outlook.com)
"""