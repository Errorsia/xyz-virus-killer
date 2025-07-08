import os
import time
import tkinter as tk
from os import mkdir
from tkinter import messagebox
import sys


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
Version = "VIRUS KILLER V1.6.5 (Elysium)"

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


    log(file_directory)

    os.system('chcp 65001')


def check_working_path(_file_directory):

    dir_list = ['', '/Config', '/Log', '/Resource']
    for dir_tmp in dir_list:
        dir_tmp = _file_directory + dir_tmp
        if not os.path.exists(dir_tmp):
            mkdir(dir_tmp)


def get_resource_path(relative_path):
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


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

    t.insert("end", "Killing Processes:\n")

    # If you want to add other viruses' processes. Add it in here.
    virus_processes = ["Rundll32.exe", "AvastSvc.exe", "wscript.exe", "Autolt3.exe", "cmd.exe"]

    for processes in virus_processes:
        taskkill_processes(processes)

    t.insert("end", "\n")
    var.set("FINISH")

    rename_virus_files()


def taskkill_processes(process_name):
    # Virus killer module: Taskkill virus processes

    module_name = 'taskkill_processes'


    result_taskkill = os.system(f"TASKKILL -F -IM {process_name} -T")

    if result_taskkill == 0:
        t.insert("end", "SUCCESS: The process has been terminated\n")
        condition = 'success'
        log_content = f'The process  ({process_name}) has been terminated'

    elif result_taskkill == 128:
        t.insert("end", "ERROR: The process not found\n")
        condition = 'failed'
        log_content = f'The process ({process_name}) not found'

    elif result_taskkill == 1:
        t.insert("end", "ERROR: The process could not be terminated\n")
        condition = 'failed'
        log_content = f'The process ({process_name}) could not be terminated'

    else:
        t.insert("end", "Error: Please tell developers!!\n")
        condition = 'failed'
        log_content = 'Unknown Error: Please tell developers!!'

    write_log(module_name, 'info', condition, result_taskkill, log_content)


def rename_virus_files():
    # Virus Files Rename Module: Select disks
    # Virus Files Rename Module: Rename the Virus Files

    t.insert("end", "Renaming Files:\n")

    module_name = 'rename_virus_files'
    result_rename_files = 'none'
    condition = None
    log_content = None

    # If you want to add other dirs. Add it in here.
    disks = ['E', 'F', 'G']

    for disk_name in disks:

        if os.path.exists(f"{disk_name}:\\"):
            result_rename_files = os.system(f"ren {disk_name}:\\*.lnk *.vir")
            t.insert("end", f"Success to rename virus files in {disk_name}-disk\n")
            condition = 'success'
            log_content = f'Success to rename virus files in {disk_name}-disk'
        else:
            t.insert("end", f"{disk_name}-disk not found\n")
            condition = 'failed'
            log_content = f'{disk_name}-disk not found'

    t.insert("end", "\n")
    write_log(module_name, 'info', condition, result_rename_files, log_content)

    var.set("FINISH")



def repair_infected_files():
    # Virus File Repair Module: Show hidden files

    t.insert("end", "Showing Hidden Files:\n")

    # If you want to add other dirs. Add it in here.
    disks = ['E', 'F', 'G', 'H']

    module_name = 'repair_infected_files'
    result_repair_infected_files = 'none'
    condition = None
    log_content = []

    for dir_tmp in disks:

        if os.path.exists(f"{dir_tmp}:\\"):
            result_repair_infected_files = os.system(f"ATTRIB -S -H {dir_tmp}:\\*.* /d /l")
            t.insert("end", f"Success to show hidden files in {dir_tmp}-disk\n")
            condition = 'success'
            log_content.append(f'Success to rename virus files in {dir_tmp}-disk')

        else:
            t.insert("end", f"{dir_tmp}-disk not found\n")
            condition = 'failed'
            log_content.append(f'{dir_tmp}-disk not found')

    t.insert("end", "\n")
    var.set("FINISH")

    for _log_content in log_content:
        write_log(module_name, 'info', condition, result_repair_infected_files, _log_content)


def auto_kill():
    # Call two functions

    kill_viruses()
    repair_infected_files()


def clean_button():
    # Clean Screen Module: Clean Screen & Output

    global Easter_Egg, file_directory, current_Log

    var.set("VIRUS KILLER")
    t.delete("1.0", tk.END)

    text1 = 'Copyright © 2024 - 2030 Arthur_xyz.All Rights Reserved'
    text2 = 'The Easter Egg was discovered by you!\n被你发现啦!'
    text3 = 'Developer:\tArthur_xyz\nEmail:\tArthur_xyz@outlook.com'

    # Easter_Egg module
    if Easter_Egg < 0:
        pass
    elif Easter_Egg < 4:
        Easter_Egg += 1
    else:
        var.set("Copyright © 2024 - 2030 Arthur_xyz.All Rights Reserved")




        if build_Log:
            with open(f"{file_directory}/Log/{current_Log}.log.avk", "a", encoding="UTF-8") as file:
                file.write(f'\n\n{text1}\n{text2}\n{text3}\n\n')
        Easter_Egg = 0

    set_insert('clean_screen', 'none', 'hi')


def clean_output():
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
                file.write(f"del /f /q *.avk \ndel /f /q *.bat")


def write_log(module, level, condition, value, content):
    # Log Module: Write OperationLog

    global build_Log, current_Log

    current_time = time.asctime()

    module = module.upper()
    level = level.upper()
    condition = condition.upper()
    value = str(value).upper()

    if build_Log:
        with open(f"{file_directory}/Log/{current_Log}.log.avk", "a", encoding="UTF-8") as file:
            file.write(f'{current_time}\t|\t[{module}]\t|\t{level}\t|\t{condition}\t|\t{value}\t|\t{content}\n')




def set_insert_simplified(content):

    output = content
    output_text.configure(state='normal')
    output_text.insert('end', output)
    output_text.configure(state='disabled')


def set_insert(module, condition, content):


    current_time = time.asctime()[-13:-5]

    module = module.upper()
    condition = condition.upper()

    output = f'{current_time}\t|\t[{module}]\t|\t{condition}\t|\t{content}\n'
    output_text.configure(state='normal')
    output_text.insert('end', output)
    output_text.configure(state='disabled')






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
"""  # Haven't Used




# __Main__

check_working_path(file_directory)

# Main Window (GUI)

window = tk.Tk()
window.title(Version)
window.geometry("1360x720")
window.minsize(1360, 720)
window.maxsize(3840, 2160)
# window.iconbitmap("icon.ico")
LOGO_PATH = get_resource_path(os.path.join("resources","icon.ico"))
window.iconbitmap(LOGO_PATH)




var = tk.StringVar()

label1 = tk.Label(window, textvariable=var, bg="cyan", width=45, font=("Arial", 40), height=2)
label1.grid(row=0, column=0, columnspan=4)

label2 = tk.Label(window, width=10, font=20, height=2)
label2.grid(row=1, column=0, columnspan=4)


button_frame1 = tk.Frame(window, height=3)
button1 = tk.Button(button_frame1, text="Kill Viruses", font=30, width=40, height=2, command=kill_viruses)
button1.pack(side='left', padx=10, pady=5)

button2 = tk.Button(button_frame1, text="Fix What Viruses Make", font=30, width=40, height=2, command=repair_infected_files)
button2.pack(side='left', padx=10, pady=5)

# button_frame1.configure(background="red")
button_frame1.grid(row=3, column=0, columnspan=2)


button_frame2 = tk.Frame(window, height=3)
button3 = tk.Button(button_frame2, text="Auto Kill(Do #1 And #2)", font=30, width=40, height=2, command=auto_kill)
button3.pack(side='left', padx=10, pady=5)

button4 = tk.Button(button_frame2, text="Clean Screen", font=30, width=40, height=2, command=clean_button)
button4.pack(side='left', padx=10, pady=5)

# button_frame2.configure(background="green")
button_frame2.grid(row=4, column=0, columnspan=2)


# button5 = tk.Button(window, text = "©", width = 1, height= 1, command= clean_button)
# button5.pack()


# text = "If you want to clean screen, press the Clean Screen button",
label3 = tk.Label(window, text="Output:", width=10, font=('TkDefaultFont',20), height=1)
label3.grid(row=2, column=2, columnspan=2)

t = tk.Text(window, height=30)
t.grid(row=3, column=2, rowspan=10, columnspan=2)
output_text = tk.Text(window, height=10)
# output_text.grid(row=5, column=0, columnspan=2)
# output_text.configure(state='disabled')

var.set("VIRUS KILLER")


generate()

window.mainloop()

'''
class MainWindow:
    def __init__(self, version):
        self.window = tk.Tk()
        self.window.title(Version)
        self.window.geometry("1366x720")

        self.var = tk.StringVar()

        label1 = tk.Label(self.window, textvariable=self.var, bg="cyan", width=45, font=("Arial", 40), height=2)
        label1.grid(row=0, column=0, columnspan=2)

        button1 = tk.Button(self.window, text="Kill Viruses", font=30, width=40, height=2, command=kill_viruses)
        button1.grid(row=1, column=0)

        button2 = tk.Button(self.window, text="Fix What Viruses Make", font=30, width=40, height=2,
                            command=repair_infected_files)
        button2.grid(row=2, column=0)

        button3 = tk.Button(self.window, text="Auto Kill(Do #1 And #2)", font=30, width=40, height=2, command=auto_kill)
        button3.grid(row=1, column=1)

        button4 = tk.Button(self.window, text="Clean Screen", font=30, width=40, height=2, command=clean_button)
        button4.grid(row=2, column=1)

        # button5 = tk.Button(window, text = "©", width = 1, height= 1, command= clean_button)
        # button5.pack()

        label2 = tk.Label(self.window, width=10, font=20, height=2)
        label2.grid(row=3, column=0, columnspan=2)

        # text = "If you want to clean screen, press the Clean Screen button",
        label3 = tk.Label(self.window, text="Output:", width=10, font=20, height=1)
        label3.grid(row=4, column=0, columnspan=2)

        self.t = tk.Text(self.window, height=30)
        self.t.grid(row=5, column=0, columnspan=2)

        self.var.set("VIRUS KILLER")

        log_configuration()

        self.window.mainloop()




if __name__ == '__main__':
    MainWindow(version=Version)
'''

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