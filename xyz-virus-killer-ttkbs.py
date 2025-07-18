"""
@author Arthur_xyz <Arthur_xyz@outlook.com>
"""

import base64
import os
from os import mkdir
import logging
import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
# from win11toast import notify
import ttkbootstrap as ttkbs
from ttkbootstrap.constants import *

# Private Libraries
from icon import img

"""
Update Log:
Change the code names
Add the debug frame & debugger button 
Fixed the problem of black frame popping up during runtime
# Use dictionaries to replace some variables (It seems unnecessary)
Rebuild log module

更新日志:
更改了代号
新增调试框架和调试按钮
修复运行时有黑框弹出的问题
# 使用字典代替了部分变量 (似乎没有必要)
重构了日志模块


Author's message:
    Why the codes is more and more complex, while the lines are fewer and fewer?
    There is no bugs at present!
    The programme is TESTING!
"""

'''
File name: xyzvk_v2.0.0.py
Copyright: Copyright ©  2024 - 2030 Arthur_xyz. All Rights Reserved
Description: XYZ Virus Killer XYZ virus killer program (code: Pardofelis)
Modified by: xyz
Modified on: January 29, 2025
Modified content: Addition and refactoring

文件名：xyzvk_v2.0.0.py
版权：Copyright © 2024 - 2030 Arthur_xyz.All Rights Reserved
描述：XYZ Virus Killer XYZ病毒杀手程序 (代号: Pardofelis)
修改人：xyz
修改时间：2024-01-29
修改内容：新增和重构
'''

'''
Copyright © 2024
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

计算---函数
计算器-----类------计算变得简单

函数-----一种动作。
类-------解决问题的一类器物。
'''

'''
Code Name List:
Kevin, Elysia, Aponia, Eden, Vill-V, Kalpas, Su, Sakura, Kosma, Mobius, Griseo, Hua, Pardofelis
'''

# General Information
general = {
    'Name': 'Virus Killer',
    'version': '2.0.0',
    # 'Full_version' : f'{name} V{version}',
}
name = 'Virus Killer'
version = '2.0.0'
# Full_version = "Virus Killer V1.7.7 (Elysium)"
Full_version = f'{name} V{version}'
Internal_version = '%03d%03d%03d' % (2, 0, 0)
code_name = 'Pardofelis'
nickname = 'Ego'

# Whether TSET ENVIRONMENT
# test = True


# Build log
# Condition: Messagebox return
# log_dictionary = {'build_Log': None}
build_Log = None

debug_frame_disable = True

appdata = os.path.expandvars("%APPDATA%")
file_directory = appdata + '/Arthur/VirusKiller'

# Show Easter Egg
# Current condition: On (If Easter_Egg < 0, it's Off)
Easter_Egg = 0


def start():
    run_command('chcp 65001')

    check_path()

    log()

    update()


def check_path():
    father_directory = appdata + '/Arthur'
    dir_list = ['', '/VirusKiller', '/VirusKiller/Config', '/VirusKiller/Log']

    for dir_tmp in dir_list:
        dir_tmp = father_directory + dir_tmp
        if not os.path.exists(dir_tmp):
            mkdir(dir_tmp)


def run_command(command):
    return subprocess.call(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def update():
    internal_version = int(Internal_version)
    online_update_version = -1
    local_update_version = int(local_update())

    if internal_version >= online_update_version and internal_version >= local_update_version:
        return

    if online_update_version >= local_update_version:

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
            tk.messagebox.showwarning(
                'Update Available',
                'A new version is available.\n'
                'Please ask Arthur_xyz<Arthur_xyz@outlook.com> for the update.\n\n'
            )

    else:
        tk.messagebox.showwarning(
            'Update Available',
            'A new version is available.\n'
            'Please ask Arthur_xyz<Arthur_xyz@outlook.com> for the update.\n\n'
        )

    exit('UPDATE AVAILABLE')


def local_update():
    if os.path.exists(f'{file_directory}/Config/Local_Update.Elysia'):

        with open(f'{file_directory}/Config/Local_Update.Elysia', 'r') as local_update_config:
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
    if os.path.exists(f'{file_directory}/Config/Local_Update.Elysia'):
        run_command(f'attrib -r -h {file_directory}/Config/Local_Update.Elysia')

    with open(f'{file_directory}/Config/Local_Update.Elysia', 'w', encoding="UTF-8") as local_version:
        local_version.write(Internal_version)

    run_command(f'attrib +r +h {file_directory}/Config/Local_Update.Elysia')


def log():
    global build_Log

    build_Log = log_configuration()



# Config Module: Read & Check Config
def log_configuration():
    config_path = f'{file_directory}/Config/VirusKiller_Configuration.Elysia'
    log_get_message = True
    log_config = None
    _build_log = None

    # Try to read config
    if os.path.isfile(config_path):

        with open(config_path, "r", encoding="UTF-8") as file:
            read_config = file.read()

        enable_log = read_config[0]

        if enable_log == "1":
            log_get_message = False
            _build_log = True
            log_config = 1

        elif enable_log == "0":
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

    run_command(f"attrib -s -r -h {config_path}")
    with open(f"{config_path}", "w", encoding="UTF-8") as file:
        file.write(f"{log_config}")
    run_command(f"attrib +s +r +h {config_path}")

    return _build_log



# Virus killer main module
def kill_viruses():

    set_insert_simplified('\nKilling Processes:')

    # If you want to add more viruses' processes. Add them in here.
    virus_processes = ['Rundll32.exe', 'AvastSvc.exe', 'wscript.exe', 'Autolt3.exe']  # 'cmd.exe'

    for processes in virus_processes:
        taskkill_processes(processes)

    var.set("FINISH")

    # notify('Antivirus completed')

    rename_virus_files()


# Virus killer module: Taskkill virus processes
def taskkill_processes(process_name):
    module_name = 'taskkill_processes'
    result_taskkill = run_command(f"TASKKILL -F -IM {process_name} -T")

    if result_taskkill == 0:
        condition = 'success'
        output_content = f'The process has been terminated'
        logger.info(f'The process ({process_name}) has been terminated (With return value {result_taskkill})')

    elif result_taskkill == 128:
        condition = 'failed'
        output_content = f'The process not found'
        logger.warning(f'The process ({process_name}) not found (With return value {result_taskkill})')

    elif result_taskkill == 1:
        condition = 'failed'
        output_content = 'The process could not be terminated'
        logger.warning(f'The process ({process_name}) could not be terminated (With return value {result_taskkill})')

    else:
        condition = 'failed'
        output_content = 'Unknown Error: Please tell developers!!'
        logger.warning(f'Unknown Error (With return value {result_taskkill})')

    set_insert(module_name, condition, output_content)


# Virus Files Rename Module: Select disks
# Virus Files Rename Module: Rename the Virus Files
def rename_virus_files():
    module_name = 'rename_virus_files'
    condition_list = []
    log_content_list = []

    set_insert_simplified('\nRenaming Files:')

    # If you want to add more dirs. Add them in here.
    disks = ['E', 'F', 'G']

    for disk_name in disks:

        if os.path.exists(f"{disk_name}:\\"):
            result_rename_files = run_command(f"ren {disk_name}:\\*.lnk *.vir")
            condition_list.append('success')
            log_content_list.append(f'Success to rename virus files in {disk_name}-disk (With return value {result_rename_files})')

        else:
            condition_list.append('failed')
            log_content_list.append(f'{disk_name}-disk not found')

    for cnt in range(0, len(log_content_list)):
        log_content = log_content_list[cnt]
        condition = condition_list[cnt]

        output_content = log_content
        set_insert(module_name, condition, output_content)

    var.set("FINISH")


# Virus File Repair Module: Show hidden files
def repair_infected_files():
    set_insert_simplified('\nShowing Hidden Files:')

    # If you want to add other dirs. Add it in here.
    disks = ['E', 'F', 'G', 'H']

    module_name = 'repair_infected_files'

    condition_list = []
    log_content_list = []

    for dir_tmp in disks:

        if os.path.exists(f"{dir_tmp}:\\"):
            result_repair_infected_files = run_command(f"ATTRIB -S -H {dir_tmp}:\\*.* /d /l")
            condition_list.append('success')
            logger.info(f'Virus files in {dir_tmp}-disk was renamed')
            log_content_list.append(f'Virus files in {dir_tmp}-disk was renamed (With return value {result_repair_infected_files})')

        else:
            condition_list.append('failed')
            logger.warning(f'{dir_tmp}-disk not found')
            log_content_list.append(f'{dir_tmp}-disk not found')

    for cnt in range(0, len(log_content_list)):
        log_content = log_content_list[cnt]
        condition = condition_list[cnt]

        output_content = log_content
        set_insert(module_name, condition, output_content)

    # notify('Repair Infected Files completed')

    var.set("FINISH")


def auto_kill():
    # Call two functions

    kill_viruses()
    repair_infected_files()


# Clean Screen Module: Clean Screen & Output
def clean_button():
    global file_directory

    var.set("Virus Killer")
    output_text.configure(state='normal')
    output_text.delete("1.0", tk.END)
    output_text.configure(state='disabled')

    easter_egg()


def easter_egg():
    global Easter_Egg

    # Easter_Egg module
    if Easter_Egg < 0:
        pass
    elif Easter_Egg < 4:
        Easter_Egg += 1
    else:
        var.set("Copyright © 2024 - 2030 Arthur_xyz.All Rights Reserved")

        logger.debug('=' * 52)
        logger.debug('Copyright 2024 - 2030 Arthur_xyz.All Rights Reserved')
        logger.debug('The Easter Egg was discovered by you!')
        logger.debug('Developer:\tArthur_xyz')
        logger.debug('Email:\tArthur_xyz@outlook.com')
        logger.debug('=' * 52)

        Easter_Egg = 0


def debugger_button():
    global debug_frame_disable

    if debug_frame_disable:
        debug_frame.grid(row=2, column=2, rowspan=10, columnspan=2)
        debug_frame_disable = False
    else:
        debug_frame.grid_forget()
        debug_frame_disable = True


# Define a function to get the value of the combobox automatically
# noinspection PyUnusedLocal
def debug_combobox_on_select(event):
    selected_value = debug_combobox1.get()

    if selected_value == 'Debug':
        handler.setLevel(logging.DEBUG)
        logger.setLevel(level=logging.DEBUG)
    elif selected_value == 'Info':
        handler.setLevel(logging.INFO)
        logger.setLevel(level=logging.INFO)
    elif selected_value == 'Warning':
        handler.setLevel(logging.WARNING)
        logger.setLevel(level=logging.WARNING)
    elif selected_value == 'Error':
        handler.setLevel(logging.ERROR)
        logger.setLevel(level=logging.ERROR)
    elif selected_value == 'Critical':
        handler.setLevel(logging.CRITICAL)
        logger.setLevel(level=logging.CRITICAL)
    elif selected_value == 'Silent':
        handler.setLevel(logging.CRITICAL + 1)
        logger.setLevel(level=logging.CRITICAL + 1)
    # print("Current log level:", selected_value)
    # print(logger)


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



start()

# Main Window (GUI)
window = ttkbs.Window()
window.title(Full_version)
window.geometry("1360x720")
window.minsize(1360, 720)
window.maxsize(3840, 2160)


# Set icon
# https://www.cnblogs.com/duanminkid/p/14208356.html
with open("tmp.ico", "wb+") as tmp:
    tmp.write(base64.b64decode(img))
window.iconbitmap("tmp.ico")
os.remove("tmp.ico")


# Set logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler(f'{file_directory}/Log/Log{'%.7f' % time.time()}.avk')
if build_Log:
    handler.setLevel(logging.DEBUG)
    logger.setLevel(level=logging.DEBUG)
else:
    handler.setLevel(logging.CRITICAL + 1)
    logger.setLevel(level=logging.CRITICAL + 1)
formatter = logging.Formatter('%(asctime)s - %(pathname)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


var = tk.StringVar()


label1 = tk.Label(window, textvariable=var, bg="lightcyan", width=44, font=("Arial", 40), height=2)
label1.grid(row=0, column=0, columnspan=4)

label2 = tk.Label(window, width=10, font=20, height=2)
label2.grid(row=1, column=0, columnspan=4)


button_frame = tk.Frame(window)

# noinspection PyArgumentList
button1 = ttkbs.Button(button_frame, text="Kill Viruses", width=40, bootstyle=SUCCESS, command=kill_viruses)
button1.grid(row=0, column=0, padx=10, pady=20)

# noinspection PyArgumentList
button2 = ttkbs.Button(button_frame, text="Repair Infected Files", width=40, bootstyle=SUCCESS,
                    command=repair_infected_files)
button2.grid(row=0, column=1, padx=10, pady=20)

# noinspection PyArgumentList
button3 = ttkbs.Button(button_frame, text="Auto Kill(Do #1 And #2)", width=40, bootstyle=SUCCESS, command=auto_kill)
button3.grid(row=1, column=0, padx=10, pady=20)

# noinspection PyArgumentList
button4 = ttkbs.Button(button_frame, text="Clean Screen", width=40, bootstyle=SUCCESS, command=clean_button)
button4.grid(row=1, column=1, padx=10, pady=20)

# noinspection PyArgumentList
button5 = ttkbs.Button(button_frame, text="Debugger", width=40, bootstyle=SUCCESS, command=debugger_button)
button5.grid(row=2, column=0, padx=10, pady=20)

button_frame.grid(row=2, column=0, rowspan=4, columnspan=2)


debug_frame = tk.Frame(window)

debug_label1 = tk.Label(debug_frame, text="Debugger Output:", width=17, font=('TkDefaultFont', 20), height=1)
debug_label1.pack()

output_text = tk.Text(debug_frame, height=25)
output_text.pack()
output_text.configure(state='disabled')

debug_frame_sub1 = tk.Frame(debug_frame)

debug_label2 = tk.Label(debug_frame_sub1, text="Select log output level: ", width=25, font=30, height=1)
debug_label2.pack(side='left', padx=10)

log_options = ['Debug', 'Info', 'Warning', 'Error', 'Critical', 'Silent']
debug_combobox1 = ttk.Combobox(debug_frame_sub1, values=log_options)
debug_combobox1.pack(side='left', padx=10)

# Set default values
debug_combobox1.current(0)

# Bind events to combobox
debug_combobox1.bind("<<ComboboxSelected>>", debug_combobox_on_select)

debug_frame_sub1.pack(pady=10)


var.set("Virus Killer")

window.mainloop()