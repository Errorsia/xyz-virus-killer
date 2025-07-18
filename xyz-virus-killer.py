"""
@author Arthur_xyz <Arthur_xyz@outlook.com>
"""

import base64
import os
import logging
import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import tempfile
# import win11toast

# Private Libraries
import icon

"""
THE PROGRAMME ONLY RUNS ON WINDOWS(NT) !
I don't think someone will run an EXE programme on Linux(except wine) and MacOS etc.

Update Log:
Rebuild repair_infected_files module
Change the name of rename_virus_files to handle_virus_files
Added logging to handle_virus_files
Added a module to obtain the drive letters
Added a module to obtain the drive letter of removable disks
Added a module to obtain the volume label of disks
Optimize the logic of judging whether a string can be formatted into an integer

更新日志:
重构了修复被感染的文件(repair_infected_files)模块
将rename_virus_files的名字改为handle_virus_files
在处理病毒文件(handle_virus_files)中加入了日志记录
新增获取磁盘盘符模块
新增获取可移动磁盘盘符模块
新增获取磁盘名称模块
优化判断字符串是否可以格式化成整型的逻辑


Author's message:
    Why the codes is more and more complex, while the lines are fewer and fewer?
    There is no bugs at present!
    But programme is still TESTING!
"""

'''
File name: xyzvk_v2.0.1.py
Copyright: Copyright ©  2024 - 2070 Arthur_xyz.All Rights Reserved
Description: XYZ Virus Killer XYZ virus killer program (Code: Pardofelis)
Modified by: xyz
Modified on: February 07, 2025
Modified content: Addition and refactoring

文件名：xyzvk_v2.0.1.py
版权：Copyright © 2024 - 2070 Arthur_xyz.All Rights Reserved
描述：XYZ Virus Killer XYZ病毒杀手程序 (代号: Pardofelis)
修改人：xyz
修改时间：2024-02-07
修改内容：新增和重构
'''

'''
Copyright © 2024
Copyright © 2024 - 2070 Arthur_xyz.All Rights Reserved
© 2024 - 2070 Arthur_xyz版权所有

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
# general = {
#     'Name': 'Virus Killer',
#     'version': '2.0.0',
#     # 'Full_version' : f'{name} V{version}',
# }
programme_name = 'Virus Killer'
version = '2.0.1'
Full_version = f'{programme_name} V{version}'
Internal_version = '%03d%03d%03d' % (2, 0, 1)
code_name = 'Pardofelis'
nickname = 'Ego'

# Whether TSET ENVIRONMENT
# test = True

# Build log(Messagebox return)
# log_dictionary = {'build_Log': None}
build_Log = None

debug_frame_disable = True

# Get the value of the environment variable %appdata%
appdata = os.getenv("APPDATA")
# appdata = os.path.expandvars("%APPDATA%")
file_directory = appdata + '/Arthur/VirusKiller'

# Whether show Easter Egg
# Current condition: On (If Easter_Egg < 0, it's Off)
Easter_Egg = 0


def start():
    check_operate_system()

    run_command('chcp 65001')

    check_path()

    log()

    update()


# Check whether OS is Windows nt
def check_operate_system():
    if os.name != 'nt':
        exit('UNSUPPORTED SYSTEMS')


# Check the working directories
def check_path():
    father_directory = appdata + '/Arthur'
    dir_list = ['', '/VirusKiller', '/VirusKiller/Config', '/VirusKiller/Log']

    for dir_tmp in dir_list:
        dir_tmp = father_directory + dir_tmp
        if not os.path.exists(dir_tmp):
            os.mkdir(dir_tmp)


def run_command(command):
    return subprocess.call(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def subprocess_run(command):
    return subprocess.run(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def log():
    global build_Log

    build_Log = log_configuration()

    easy_clean_log()


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


def easy_clean_log():
    # Create a bat to clean all the Logs
    if not os.path.exists(f"{file_directory}/Log/Clean_Log.bat"):
        with open(f"{file_directory}/Log/Clean_Log.bat", "w", encoding="UTF-8") as file:
            file.write(f"del /f /q *.avk \ndel /f /q *.bat")



# Check for updates
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
            'Do you want to download the new version?\n\n'
            'You can also ask Arthur_xyz<Arthur_xyz@outlook.com> for the update.\n\n'
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


# Check whether local_version is legal
def is_legal_version(local_version):
    local_version = str(local_version)
    digit_is_int = 0

    if len(local_version) != 9:
        return False

    for tmp_local_version in local_version:
        for tmp_num in range(10):
            if tmp_local_version == str(tmp_num):
                digit_is_int += 1
                break

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


def get_drives_and_types():

    # Execute the WMIC command to obtain disk information
    result = subprocess.run(
        'wmic logicaldisk get caption, description',
        capture_output=True,
        text=True,
        encoding='gbk',  # Chinese system uses GBK encoding
        shell=True
    )

    drives = []
    drives_type = []
    # Parsing output results
    output = result.stdout.strip()
    for line in output.split('\n'):
        # Skip empty lines and header lines
        if not line.strip() or line.startswith('Caption'):
            continue

        # Clean extra spaces and split columns
        parts = list(filter(None, line.split()))
        drives.append(parts[0])
        drives_type.append(parts[1])

    return drives, drives_type

def get_removable_disks():
    drives, drives_type = get_drives_and_types()
    removable_disks = []

    for cnt in range(len(drives)):
        if drives_type[cnt] == '可移动磁盘':
            removable_disks.append(drives[cnt].rstrip(':'))

    return removable_disks


# Virus killer main module
def kill_viruses():

    set_insert_simplified('\nKilling Processes:')

    # If you want to add more viruses' processes. Add them in here.
    virus_processes = ['Rundll32.exe', 'AvastSvc.exe', 'wscript.exe', 'Autolt3.exe']  # 'cmd.exe'

    for processes in virus_processes:
        taskkill_processes(processes)

    var.set("FINISH")

    # wintoast('Antivirus completed')

    handle_virus_files()


# Virus killer module: Taskkill virus processes
def taskkill_processes(process_name):
    module_name = 'taskkill_processes'
    result_taskkill = run_command(f"TASKKILL -F -IM {process_name} -T")

    if result_taskkill == 0:
        condition = 'success'
        output_content = f'The process has been terminated'
        logger.info(f'The process ({process_name}) has been terminated (Return code {result_taskkill})')

    elif result_taskkill == 128:
        condition = 'failed'
        output_content = f'The process not found'
        logger.warning(f'The process ({process_name}) not found (Return code {result_taskkill})')

    elif result_taskkill == 1:
        condition = 'failed'
        output_content = 'The process could not be terminated'
        logger.warning(f'The process ({process_name}) could not be terminated (Return code {result_taskkill})')

    else:
        condition = 'failed'
        output_content = 'Unknown Error: Please tell developers!!'
        logger.warning(f'Unknown Error (Return code {result_taskkill})')

    set_insert(module_name, condition, output_content)


def get_volume_label(disk_letter):
    # Make sure the disk letter format is correct
    disk_letter = disk_letter.upper().rstrip(':') + ':'

    # Execute the WMIC command to obtain disk information
    result = subprocess.run(
        'wmic logicaldisk get name,volumename',
        capture_output=True,
        text=True,
        encoding='gbk',  # Chinese system uses GBK encoding
        shell=True
    )

    # Parsing output results
    output = result.stdout.strip()
    for line in output.split('\n'):
        # Skip empty lines and header lines
        if not line.strip() or line.startswith('Name'):
            continue

        # Clean extra spaces and split columns
        parts = list(filter(None, line.split()))
        if len(parts) >= 2:
            disk_name = parts[0]
            disk_label = ' '.join(parts[1:])
            if disk_name == disk_letter:
                return disk_label

    return None  # No corresponding drive letter found


# Virus Files Rename Module: Rename the Virus Files
def handle_virus_files():
    module_name = 'handle_virus_files'
    condition_list = []
    log_content_list = []

    set_insert_simplified('\nRenaming Files:')

    # If you want to add more dirs. Add them in here.
    disks = get_removable_disks()

    if disks:
        for disk in disks:
            current_disk_name =get_volume_label(disk)

            if os.path.exists(f'{disk}:\\{current_disk_name}.lnk'):
                os.remove(f'{disk}:\\{current_disk_name}.lnk')
                condition_list.append('success')
                log_content_list.append(f'Success to remove virus files in {disk}-disk')
                logger.info(f'Success to rename virus files in {disk}-disk')
            else:
                condition_list.append('failed')
                log_content_list.append(f'Virus files not found')
                logger.warning(f'Virus files not found')

    else:
        condition_list.append('failed')
        logger.warning(f'Removable disk not found')
        log_content_list.append(f'Removable disk not found')

    for cnt in range(0, len(log_content_list)):
        log_content = log_content_list[cnt]
        condition = condition_list[cnt]

        set_insert(module_name, condition, log_content)

    var.set("FINISH")


# Virus File Repair Module: Show hidden files
def repair_infected_files():
    set_insert_simplified('\nShowing Hidden Files:')

    # If you want to add other dirs. Add it in here.
    disks = get_removable_disks()

    module_name = 'repair_infected_files'

    condition_list = []
    log_content_list = []

    if disks:
        for disk in disks:
            infected_folder_path = f'{disk}:\\ '
            result_repair_infected_folder = None

            if os.path.exists(infected_folder_path):
                subprocess_run(['attrib', '-r', infected_folder_path, '/d', '/s'])
                result_repair_infected_folder = subprocess_run(['attrib', '-s', '-h', '-r', infected_folder_path, '/d']).returncode

                if result_repair_infected_folder == 0:
                    logger.info(f'The attribute of the Infected folder in {disk}-disk has been changed (Return code {result_repair_infected_folder})')
                    condition_list.append('success')
                    log_content_list.append(f'The attribute of the Infected folder in {disk}-disk was changed')

                else:
                    logger.warning(f'The attribute of the Infected folder cannot be changed')
                    condition_list.append('failed')
                    log_content_list.append(f'The attribute of the Infected folder cannot be changed')

            if os.path.exists(f'{disk}:\\ \\desktop.ini'):
                result_change_attrib_of_virus_files = subprocess_run(['attrib', '-s', '-h', '-R', f'{disk}:\\ \\desktop.ini', "/d"])

                if result_change_attrib_of_virus_files.returncode == 0:
                    logger.info(f'The attribute of the virus file ({disk}:\\xa0\\desktop.ini) has been changed (Return {result_change_attrib_of_virus_files})')
                    condition_list.append('success')
                    log_content_list.append(f'The attribute of the virus file in {disk}-disk was changed')

                    os.remove(f'{disk}:\\ \\desktop.ini')
                    logger.info(f'Virus file ({disk}:\\xa0\\desktop.ini) has been removed')
                    condition_list.append('success')
                    log_content_list.append(f'Virus file in {disk}-disk was renamed')

                else:
                    logger.warning(f'The attribute of the virus file cannot be changed')
                    condition_list.append('failed')
                    log_content_list.append(f'The attribute of the virus file cannot be changed')

            if result_repair_infected_folder == 0 and os.path.exists(infected_folder_path):
                # os.rename(infected_folder_path, f'{disk}:\\Files Hidden by Viruses')
                # os.rename(infected_folder_path, f'{disk}:\\被病毒隐藏的文件')

                # logger.info(f'Infected folder in {disk}-disk has been renamed')
                # condition_list.append('success')
                # log_content_list.append(f'Infected folder in {disk}-disk was renamed')

                try:
                    os.rename(infected_folder_path, f'{disk}:\\Files Hidden by Viruses')
                    # os.rename(infected_folder_path, f'{disk}:\\被病毒隐藏的文件')
                    logger.info(f'Infected folder in {disk}-disk has been renamed')
                    # print(f'Successfully renamed')
                except PermissionError as error:
                    logger.error(f'Permission denied: {error}')
                    condition_list.append('failed')
                    log_content_list.append(f'Permission denied')
                    # print('Permission denied. Please run the script as an administrator.')
                except FileNotFoundError:
                    logger.error(f'The directory does not exist')
                    condition_list.append('failed')
                    log_content_list.append(f'The directory does not exist')
                    # print(f'The directory does not exist.')
                except Exception as error:
                    logger.error(f'An error occurred: {error}')
                    condition_list.append('failed')
                    log_content_list.append(f'An error occurred: {error}')
                    # print(f'An error occurred: {error}')

            else:
                logger.warning(f'The directory does not exist')
                condition_list.append('failed')
                log_content_list.append(f'The directory does not exist')
                # print(f'The directory does not exist.')

    else:
        logger.warning(f'Removable disk not found')
        condition_list.append('failed')
        log_content_list.append(f'Removable disk not found')

    for cnt in range(0, len(log_content_list)):
        log_content = log_content_list[cnt]
        condition = condition_list[cnt]

        output_content = log_content
        set_insert(module_name, condition, output_content)

    # wintoast('Repair Infected Files completed')

    var.set("FINISH")


# Call two functions
def auto_kill():
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


# Easter_Egg module
def easter_egg():
    global Easter_Egg

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
        handler.setLevel(100)
        logger.setLevel(100)
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


# Set logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler(f'{file_directory}/Log/Log_{time.time():.7f}.avk')
if build_Log:
    handler.setLevel(logging.DEBUG)
    logger.setLevel(level=logging.DEBUG)
else:
    handler.setLevel(100)
    logger.setLevel(100)
formatter = logging.Formatter('%(asctime)s - %(pathname)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


# Main Window (GUI)
window = tk.Tk()
window.title(Full_version)
window.geometry("1360x720")
window.minsize(1360, 720)
window.maxsize(3840, 2160)

# Set icon
with tempfile.NamedTemporaryFile(suffix='.ico', delete=False) as tmp:
    tmp.write(base64.b64decode(icon.img))
window.iconbitmap(tmp.name)
os.unlink(tmp.name)


var = tk.StringVar()


label1 = tk.Label(window, textvariable=var, bg="lightcyan", width=44, font=("Arial", 40), height=2)
label1.grid(row=0, column=0, columnspan=4)

label2 = tk.Label(window, width=10, font=20, height=2)
label2.grid(row=1, column=0, columnspan=4)


button_frame = tk.Frame(window)

button1 = tk.Button(button_frame, text="Kill Viruses", font=30, width=40, height=2, command=kill_viruses)
button1.grid(row=0, column=0, padx=10, pady=20)

button2 = tk.Button(button_frame, text="Repair Infected Files", font=30, width=40, height=2,
                    command=repair_infected_files)
button2.grid(row=0, column=1, padx=10, pady=20)

button3 = tk.Button(button_frame, text="Auto Kill(Do #1 And #2)", font=30, width=40, height=2, command=auto_kill)
button3.grid(row=1, column=0, padx=10, pady=20)

button4 = tk.Button(button_frame, text="Clean Screen", font=30, width=40, height=2, command=clean_button)
button4.grid(row=1, column=1, padx=10, pady=20)

button5 = tk.Button(button_frame, text="Debugger", font=30, width=40, height=2, command=debugger_button)
button5.grid(row=2, column=0, padx=10, pady=20)

button_frame.grid(row=2, column=0, rowspan=4, columnspan=2)


debug_frame = tk.Frame(window)

debug_label1 = tk.Label(debug_frame, text="Debugger Output:", width=17, font=('TkDefaultFont', 20), height=1)
debug_label1.pack()

output_text = tk.Text(debug_frame, height=30)
output_text.pack()
output_text.configure(state='disabled')

debug_frame_sub1 = tk.Frame(debug_frame)

debug_label2 = tk.Label(debug_frame_sub1, text="Select log output level: ", width=25, font=20, height=1)
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