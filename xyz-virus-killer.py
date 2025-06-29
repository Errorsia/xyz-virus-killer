import os
import tkinter as tk

"""
Update Log:
Using loops instead of repetition code
Added path detection function

更新日志:
使用循环代替重复的代码
增加了路径检测功能
"""


def Kill_Viruses():  # Virus killer main module
    Clean()
    # var.set("Killing Processes")
    # print(var.get())
    t.insert("end", "Killing Processes:\n")
    for processes in ["Rundll32.exe", "AvastSvc.exe", "wscript.exe", "Autolt3.exe", "cmd.exe"]:
        # If you want to add other viruses. Add it in here.
        return_Taskkill_Processes(processes)
    t.insert("end", "\n")
    var.set("FINSIH")
    rename_Files()


def return_Taskkill_Processes(process_Name):
    return_taskkill = os.system("TASKKILL -F -IM " + process_Name + " -T")
    if return_taskkill == 1:
        t.insert("end", "Success to kill virus\n")
        return True
    elif return_taskkill == 128:
        t.insert("end", "Error: Virus process not Found\n")
        return False
    else:
        t.insert("end", "Error: Please tell developers!!\n")
        return False


def rename_Files():
    t.insert("end", "Renaming Files:\n")
    for dir_name in ["E", "F", "G"]:
        # If you want to add other dirs. Add it in here.
        return_Ren_Files(dir_name)
    t.insert("end", "\n")
    var.set("FINSIH")


def return_Ren_Files(dir_name):
    if os.path.exists(f"{dir_name}:\\"):
        result = os.system(f"ren {dir_name}:\\*.lnk *.vir")
        t.insert("end", f"Success to rename virus files in {dir_name}-disk\n")
    else:
        t.insert("end", f"{dir_name}-disk not found\n")


def Fix_What_Viruses_Make():
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
    var.set("FINSIH")


def Auto_Kill():
    Kill_Viruses()
    Fix_What_Viruses_Make()


def Clean_Button():
    var.set("VIRUS KILLER")
    t.delete("1.0", tk.END)


def Clean():
    t.delete("1.0", tk.END)


# Main Window

window = tk.Tk()
window.title("VIRUS KILLER")
window.geometry("1366x720")

var = tk.StringVar()

lable1 = tk.Label(window, textvariable=var, bg="cyan", width=45, font=("Arial", 40), height=2)
lable1.pack()

buttom1 = tk.Button(window, text="Kill Viruses", font=30, width=40, height=2, command=Kill_Viruses)
buttom1.pack()

buttom2 = tk.Button(window, text="Fix What Viruses Make", font=30, width=40, height=2, command=Fix_What_Viruses_Make)
buttom2.pack()

buttom3 = tk.Button(window, text="Auto Kill(Do #1 And #2)", font=30, width=40, height=2, command=Auto_Kill)
buttom3.pack()

buttom4 = tk.Button(window, text="Clean Screen", font=30, width=40, height=2, command=Clean_Button)
buttom4.pack()

# buttom5 = tk.Button(window, text = "©", width = 1, height= 1, command= Clean_Button)
# buttom5.pack()

lable2 = tk.Label(window, width=10, font=20, height=2)
lable2.pack()

# text = "If you want to clean screen, press the Clean Screen buttom",
lable3 = tk.Label(window, text="Output:", width=10, font=20, height=1)
lable3.pack()

t = tk.Text(window, height=25)
t.pack()

var.set("VIRUS KILLER")

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