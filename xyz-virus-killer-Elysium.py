"""
@author Arthur_xyz <Arthur_xyz@outlook.com>
"""

import os
import time
import tkinter as tk
from os import mkdir
from tkinter import messagebox
import base64
from icon import img


"""
Update Log:
NONE

更新日志:
无 纯粹是喜欢'7'用来占位


Introduction:
This project mainly consists of  6 main modules:
    Kill Virus, Rename Virus Files, Repair Files, Write Log, Create & Read & Check config and the GUI (window).

And it also contains some other modules:
    Easter Egg.

The note of each function is below its name.

Author's message:
    There is no bugs at present!
    The programme is TESTING!
"""

'''
File name: xyzvk_v2.0.0.py
Copyright: Copyright ©  2024 - 2030 Arthur_xyz. All Rights Reserved
Description: XYZ VIRUS KILLER (Elysium) XYZ virus killer program (code: Elysia)
Modified by: xyz
Modified on: December 5, 2024
Modified content: Addition and refactoring

文件名：xyzvk_v2.0.0.py
版权：Copyright © 2024 - 2030 Arthur_xyz.All Rights Reserved
描述：XYZ VIRUS KILLER (Elysium) XYZ病毒杀手程序 (分支号: Elysia)
修改人：xyz
修改时间：2024-12-5
修改内容：新增和重构
'''

'''
Copyright © 2030
Copyright © 2024 - 2030 Arthur_xyz.All Rights Reserved
© 2024 - 2030 Arthur_xyz版权所有

如果您意外获取了源码，请联系 Arthur_xyz (Arthur_xyz@outlook.com)
If you accidentally obtain the source code, please contact Arthur_xyz (Arthur_xyz@outlook.com)

如果你想创建依赖于(xyz病毒杀手)的项目,
请联系Arthur_xyz (Arthur_xyz@outlook.com)
If you want to create your own project depend on this (xyz virus killer),
please contact Arthur_xyz (Arthur_xyz@outlook.com)
'''


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

'''
Code Name List:
Artemis, Aphrodite, Apollo, Ares, Athena, Poseidon, Hestia, Hephaestus, Zeus, Demeter, Hermes, and Hera
'''
# Full_version
name = 'VIRUS KILLER'
version = '1.7.7'
code_name = 'Artemis'
nickname = 'Elysia'
Full_version = f'{name} V{version}'
# Full_version = "VIRUS KILLER V1.7.7 (Elysium)"

Internal_version = '%03d%03d%03d' %(1,7,7)


# Whether or not TSET ENVIRONMENT
test = True


# Build log
# Condition: Messagebox return
build_Log = None

current_Log = None

appdata = os.path.expandvars("%APPDATA%")
file_directory = appdata + '/Arthur/VirusKiller'

# Show Easter Egg
# Current condition: On (If Easter_Egg < 0, it's Off)
Easter_Egg = 0


def start():

    check_path()

    update()





def check_path():

    father_directory = appdata + '/Arthur'

    dir_list = ['', '/VirusKiller', '/VirusKiller/Config', '/VirusKiller/Log']
    for dir_tmp in dir_list:
        dir_tmp = father_directory + dir_tmp
        if not os.path.exists(dir_tmp):
            mkdir(dir_tmp)


def update():

    internal_version = int(Internal_version)
    online_update_version = -1
    local_update_version = int(local_update())
    # print(local_update_version)

    if internal_version >= online_update_version and internal_version >= local_update_version:
        return


    if online_update_version >=local_update_version:

        execute_update = tk.messagebox.askokcancel(
            'Update Available',
            'A new version is available.\n'
            f'Do you want to download {online_update_version}'
            'Please ask Arthur_xyz<Arthur_xyz@outlook.com> for the update.\n\n'
            )

        if execute_update:
            print('⚠☣Downloading☣⚠')


            return


        else:
            tk.messagebox.showwarning('Update Available',
                                'A new version is available.\n'
                                'Please ask Arthur_xyz<Arthur_xyz@outlook.com> for the update.\n\n'
                                )

    else:
        tk.messagebox.showwarning('Update Available',
                                'A new version is available.\n'
                                'Please ask Arthur_xyz<Arthur_xyz@outlook.com> for the update.\n\n'
                                )

    exit('UPDATE AVAILABLE')




def local_update():

    if os.path.exists(f'{file_directory}/Config/local_update.Elysia'):

        with open(f'{file_directory}/Config/local_update.Elysia', 'r') as local_update_config:
            local_version = local_update_config.read()

        if is_legal_version(local_version):

            if int(Internal_version) <= int(local_version):
                return local_version

    build_local_update_config()
    return -1



def is_legal_version(local_version):
    # Check whether local_version is legal

    local_version = str(local_version)
    digit_is_int = 0

    if len(local_version) != 9:
        return False

    for tmp_local_version in local_version:

        for tmp_num in range(10):

            if tmp_local_version == str(tmp_num):
                digit_is_int += 1


    if digit_is_int == 9:
        return True
    else:
        return False



def build_local_update_config():

    if os.path.exists(f'{file_directory}/Config/local_update.Elysia'):
        os.system(f'attrib -r -h {file_directory}/Config/local_update.Elysia')
        # os.remove(f'{file_directory}/Config/local_update.Elysia')

    with open(f'{file_directory}/Config/local_update.Elysia', 'w', encoding="UTF-8") as local_version:
        local_version.write(Internal_version)

    os.system(f'attrib +r +h {file_directory}/Config/local_update.Elysia')




def generate():

    global build_Log, test

    log()

    if test:
        os.system('chcp 65001')


def log():
    global build_Log
    build_Log = log_configuration(build_Log)
    if build_Log:
        create_log()


def log_configuration(_build_log):
    # Config Module: Read & Check Config

    config_path = f'{file_directory}/Config/VIRUS_KILLER_CONFIGURATION.Elysia'
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

    os.system(f"attrib -s -r -h {config_path}")
    with open(f"{config_path}", "w", encoding="UTF-8") as file:
        file.write(f"{log_config}")
    os.system(f"attrib +s +r +h {config_path}")

    return _build_log



def kill_viruses():
    # Virus killer main module

    set_insert_simplified('\nKilling Processes:')

    # If you want to add more viruses' processes. Add them in here.
    virus_processes = ['Rundll32.exe', 'AvastSvc.exe', 'wscript.exe', 'Autolt3.exe', 'cmd.exe']

    for processes in virus_processes:
        taskkill_processes(processes)


    var.set("FINISH")

    rename_virus_files()


def taskkill_processes(process_name):
    # Virus killer module: Taskkill virus processes

    module_name = 'taskkill_processes'


    result_taskkill = os.system(f"TASKKILL -F -IM {process_name} -T")

    if result_taskkill == 0:
        condition = 'success'
        output_content = f'The process has been terminated'
        log_content = f'The process ({process_name}) has been terminated'

    elif result_taskkill == 128:
        condition = 'failed'
        output_content = f'The process not found'
        log_content = f'The process ({process_name}) not found'

    elif result_taskkill == 1:
        condition = 'failed'
        output_content = 'The process could not be terminated'
        log_content = f'The process ({process_name}) could not be terminated'

    else:
        condition = 'failed'
        output_content = 'Unknown Error: Please tell developers!!'
        log_content = 'Unknown Error: Please tell developers!!'


    set_insert(module_name, condition, output_content)
    write_log(module_name, 'info', condition, result_taskkill, log_content)



def rename_virus_files():
    # Virus Files Rename Module: Select disks
    # Virus Files Rename Module: Rename the Virus Files

    set_insert_simplified('\nRenaming Files:')

    module_name = 'rename_virus_files'
    result_rename_files = 'none'
    condition_list = []
    log_content_list = []

    # If you want to add more dirs. Add them in here.
    disks = ['E', 'F', 'G']

    for disk_name in disks:

        if os.path.exists(f"{disk_name}:\\"):
            result_rename_files = os.system(f"ren {disk_name}:\\*.lnk *.vir")
            condition_list.append('success')
            log_content_list.append(f'Success to rename virus files in {disk_name}-disk')

        else:
            condition_list.append('failed')
            log_content_list.append(f'{disk_name}-disk not found')



    for cnt in range(0, len(log_content_list)):

        log_content = log_content_list[cnt]
        condition = condition_list[cnt]

        output_content = log_content
        set_insert(module_name, condition, output_content)
        write_log(module_name, 'info', condition, result_rename_files, log_content)

    var.set("FINISH")



def repair_infected_files():
    # Virus File Repair Module: Show hidden files

    set_insert_simplified('\nShowing Hidden Files:')

    # If you want to add other dirs. Add it in here.
    disks = ['E', 'F', 'G', 'H']

    module_name = 'repair_infected_files'
    result_repair_infected_files = 'none'
    condition_list = []
    log_content_list = []


    for dir_tmp in disks:

        if os.path.exists(f"{dir_tmp}:\\"):
            result_repair_infected_files = os.system(f"ATTRIB -S -H {dir_tmp}:\\*.* /d /l")
            condition_list.append('success')
            log_content_list.append(f'Virus files in {dir_tmp}-disk was renamed')

        else:
            condition_list.append('failed')
            log_content_list.append(f'{dir_tmp}-disk not found')



    for cnt in range(0, len(log_content_list)):

        log_content = log_content_list[cnt]
        condition = condition_list[cnt]

        output_content = log_content
        set_insert(module_name, condition, output_content)
        write_log(module_name, 'info', condition, result_repair_infected_files, log_content)



    var.set("FINISH")


def auto_kill():
    # Call two functions

    kill_viruses()
    repair_infected_files()


def clean_button():
    # Clean Screen Module: Clean Screen & Output

    global Easter_Egg, file_directory, current_Log

    var.set("VIRUS KILLER")
    output_text.configure(state='normal')
    output_text.delete("1.0", tk.END)
    output_text.configure(state='disabled')

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

    # set_insert('clean_screen', 'none', 'hi')


def clean_output():
    # Nothing will call this function
    # t.delete("1.0", tk.END)

    pass


def create_log():
    # Log Module: Create a log

    global build_Log, current_Log, Full_version, file_directory

    if build_Log:
        current_time_stamp = "%.7f" % time.time()
        current_Log = f"log{current_time_stamp}"
        current_time = time.asctime()

        with open(f"{file_directory}/Log/{current_Log}.log.avk", "x", encoding="UTF-8") as file:
            file.write(f"{Full_version}\n")
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


    minus_sign_quantity = '-' * 50
    output = f'{minus_sign_quantity}{content}\n\n'
    output_text.configure(state='normal')
    output_text.insert('end', output)
    output_text.configure(state='disabled')




def set_insert(module, condition, content):


    current_time = time.asctime()[-13:-5]

    module = module.upper()
    condition = condition.upper()

    output = f'{current_time} | [{module}]\t|\t{condition}\t|\t{content}\n'
    output_text.configure(state='normal')
    output_text.insert('end', output)
    output_text.configure(state='disabled')



# Haven't Used
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


start()


# Main Window (GUI)

window = tk.Tk()
window.title(Full_version)
window.geometry("1360x720")
window.minsize(1360, 720)
window.maxsize(3840, 2160)

# Set icon
# https://www.cnblogs.com/duanminkid/p/14208356.html
with open("tmp.ico","wb+") as tmp:
    tmp.write(base64.b64decode(img))
window.iconbitmap("tmp.ico")
os.remove("tmp.ico")




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


label3 = tk.Label(window, text="Output:", width=10, font=('TkDefaultFont',20), height=1)
label3.grid(row=2, column=2, columnspan=2)


output_text = tk.Text(window, height=30)
output_text.grid(row=3, column=2, rowspan=10, columnspan=2)
output_text.configure(state='disabled')

var.set("VIRUS KILLER")




generate()

window.mainloop()