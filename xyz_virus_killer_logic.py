# -*- coding: utf-8 -*-
# Authors:
#   - Ariskanyaa <Ariskanyaa@outlook.com>
#   - Errorsia <Errorsia@outlook.com>
# License: GNU General Public License v3.0 or later (GPLv3+)
# See: https://www.gnu.org/licenses/gpl-3.0.html
# Copyright (C) 2024 Errorsia, Ariskanyaa
#
# This file is part of the xyzvk project and is distributed under
# the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.


"""
Logic module for xyzvk
"""

import os
import subprocess
import time
import tkinter as tk
from tkinter import messagebox

import win32api
import win32file

# Mudules
import xyzvk_config as config


class ErrorsiaVirusKillerLogic:
    def __init__(self, gui):
        self.gui = gui
        self.logging = self.logger = self.handler = None
        self._log_ready = False

        # Whether TSET ENVIRONMENT
        # test = True

        self.disable_debug_frame = True

        # Get the value of the environment variable %appdata%
        self.appdata = os.getenv("APPDATA")
        # appdata = os.path.expandvars("%APPDATA%")
        self.file_directory = self.appdata + '/Arthur/VirusKiller'

        # Whether show Easter Egg
        # Current condition: On (If Easter_Egg < 0, it's Off)
        self.Easter_Egg = 0

    def set_log(self, log):
        # self.logging = log['logging']
        # self.logger = log['logger']
        # self.handler = log['handler']
        # Safer
        self.logging = log.get('logging')
        self.logger = log.get('logger')
        self.handler = log.get('handler')
        self._log_ready = all([self.logger, self.handler])

    def initialization(self):
        self.check_operate_system()

        self.run_command('chcp 65001')

        self.check_path()

    # Check whether OS is Windows nt
    @staticmethod
    def check_operate_system():
        if os.name != 'nt':
            exit('UNSUPPORTED SYSTEMS')

    # Check the working directories
    def check_path(self):
        father_directory = self.appdata + '/Arthur'
        dir_list = ['', '/VirusKiller', '/VirusKiller/Config', '/VirusKiller/Log']

        for dir_tmp in dir_list:
            dir_tmp = father_directory + dir_tmp
            if not os.path.exists(dir_tmp):
                os.mkdir(dir_tmp)

    @staticmethod
    def run_command(command):
        return subprocess.call(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    @staticmethod
    def subprocess_run(command):
        return subprocess.run(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)

    # Config Module: Read & Check Config
    def read_log_config(self):
        config_path = f'{self.file_directory}/Config/VirusKiller_Configuration.Elysia'

        # Try to read config
        if not os.path.isfile(config_path):
            return -1

            # try:
            #     with open(config_path, "r", encoding="UTF-8") as file:
            #         read_config = file.read()
            # except PermissionError:
            #     return -1

        with open(config_path, "r", encoding="UTF-8") as file:
            read_config = file.read()

        enable_log = read_config[0]

        if enable_log == "1":
            return 1
            # log_get_message = False
            # _build_log = True
            # log_config = 1

        elif enable_log == "0":
            return 0
        else:
            return -1

    def write_log_config(self, build_log):
        log_cfg_content = 1 if build_log else 0
        config_path = f'{self.file_directory}/Config/VirusKiller_Configuration.Elysia'

        self.run_command(f"attrib -s -r -h {config_path}")
        with open(f"{config_path}", "w", encoding="UTF-8") as file:
            file.write(f"{log_cfg_content}")
        self.run_command(f"attrib +s +r +h {config_path}")

    def easy_clean_log(self):
        # Create a bat to clean all the Logs
        if not os.path.exists(f"{self.file_directory}/Log/Clean_Log.bat"):
            with open(f"{self.file_directory}/Log/Clean_Log.bat", "w", encoding="UTF-8") as file:
                file.write(f"del /f /q *.avk \ndel /f /q *.bat")

    # Check for updates
    def check_update(self):
        internal_version = int(config.INTERNAL_VERSION)
        online_update_version = -1
        local_update_version = int(self.local_update())

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

    def local_update(self):
        if os.path.exists(f'{self.file_directory}/Config/Local_Update.Elysia'):

            with open(f'{self.file_directory}/Config/Local_Update.Elysia', 'r') as local_update_config:
                local_version = local_update_config.read()

            if self.is_legal_version(local_version):

                if int(config.INTERNAL_VERSION) <= int(local_version):
                    return local_version

        self.build_local_update_config()
        return -1

    # Check whether local_version is legal
    @staticmethod
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

    def build_local_update_config(self):
        if os.path.exists(f'{self.file_directory}/Config/Local_Update.Elysia'):
            self.run_command(f'attrib -r -h {self.file_directory}/Config/Local_Update.Elysia')

        with open(f'{self.file_directory}/Config/Local_Update.Elysia', 'w', encoding="UTF-8") as local_version:
            local_version.write(config.INTERNAL_VERSION)

        self.run_command(f'attrib +r +h {self.file_directory}/Config/Local_Update.Elysia')

    # def get_removable_disks(self):
    #     drives, drives_type = self.get_drives_and_types()
    #     removable_disks = []
    #
    #     for cnt in range(len(drives)):
    #         if drives_type[cnt] == '可移动磁盘':
    #             removable_disks.append(drives[cnt].rstrip(':'))
    #
    #     return removable_disks
    #
    # @staticmethod
    # def get_drives_and_types():
    #
    #     # Execute the WMIC command to obtain disk information
    #     result = subprocess.run(
    #         'wmic logicaldisk get caption, description',
    #         capture_output=True,
    #         text=True,
    #         encoding='gbk',  # Chinese system uses GBK encoding
    #         shell=True
    #     )
    #
    #     drives = []
    #     drives_type = []
    #     # Parsing output results
    #     output = result.stdout.strip()
    #     for line in output.split('\n'):
    #         # Skip empty lines and header lines
    #         if not line.strip() or line.startswith('Caption'):
    #             continue
    #
    #         # Clean extra spaces and split columns
    #         parts = list(filter(None, line.split()))
    #         drives.append(parts[0])
    #         drives_type.append(parts[1])
    #
    #     return drives, drives_type

    @staticmethod
    def get_removable_drives():
        drives = []
        drive_bits = win32file.GetLogicalDrives()
        for i in range(26):
            if drive_bits & (1 << i):
                drive_letter = f"{chr(65 + i)}"
                drive_path = f"{chr(65 + i)}:\\"
                drive_type = win32file.GetDriveType(drive_path)
                # DRIVE_REMOVABLE = 2
                if drive_type == win32file.DRIVE_REMOVABLE:
                    drives.append(drive_letter)
        # print(drives)
        return drives

    # Virus killer main module
    def kill_viruses(self):
        # self.gui.button1.configure(state='disabled')
        # self.gui.button1.update()
        #
        # self.gui.var.set('Killing Virus Processes')
        # self.gui.label1.update()

        self.set_insert_simplified('\nKilling Processes:')

        # If you want to add more viruses' processes. Add them in here.
        virus_processes = ['Rundll32.exe', 'AvastSvc.exe', 'wscript.exe', 'Autolt3.exe']  # 'cmd.exe'

        for processes in virus_processes:
            self.taskkill_processes(processes)
        # wintoast('Antivirus completed')

        self.handle_virus_files()

        # self.gui.button1.configure(state='normal')

    # Virus killer module: Taskkill virus processes
    def taskkill_processes(self, process_name):
        module_name = 'taskkill_processes'
        result_taskkill = self.run_command(f"TASKKILL -F -IM {process_name} -T")

        if result_taskkill == 0:
            condition = 'success'
            output_content = f'The process has been terminated'
            self.logger.info(f'The process ({process_name}) has been terminated (Return code {result_taskkill})')

        elif result_taskkill == 128:
            condition = 'failed'
            output_content = f'The process not found'
            self.logger.warning(f'The process ({process_name}) not found (Return code {result_taskkill})')

        elif result_taskkill == 1:
            condition = 'failed'
            output_content = 'The process could not be terminated'
            self.logger.warning(f'The process ({process_name}) could not be terminated (Return code {result_taskkill})')

        else:
            condition = 'failed'
            output_content = 'Unknown Error: Please tell developers!!'
            self.logger.warning(f'Unknown Error (Return code {result_taskkill})')

        self.set_insert(module_name, condition, output_content)

    @staticmethod
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
    def handle_virus_files(self):
        module_name = 'handle_virus_files'
        condition_list = []
        log_content_list = []

        self.set_insert_simplified('\nRenaming Files:')

        # If you want to add more dirs. Add them in here.
        disks = self.get_removable_disks()

        if disks:
            for disk in disks:
                current_disk_name = self.get_volume_label(disk)

                if os.path.exists(f'{disk}:\\{current_disk_name}.lnk'):
                    os.remove(f'{disk}:\\{current_disk_name}.lnk')
                    condition_list.append('success')
                    log_content_list.append(f'Success to remove virus files in {disk}-disk')
                    self.logger.info(f'Success to rename virus files in {disk}-disk')
                else:
                    condition_list.append('failed')
                    log_content_list.append(f'Virus files not found')
                    self.logger.warning(f'Virus files not found')

        else:
            condition_list.append('failed')
            self.logger.warning(f'Removable disk not found')
            log_content_list.append(f'Removable disk not found')

        for cnt in range(0, len(log_content_list)):
            log_content = log_content_list[cnt]
            condition = condition_list[cnt]

            self.set_insert(module_name, condition, log_content)

    # Virus File Repair Module: Show hidden files
    def repair_infected_files(self):
        self.set_insert_simplified('\nShowing Hidden Files:')

        # If you want to add other dirs. Add it in here.
        disks = self.get_removable_disks()

        module_name = 'repair_infected_files'

        condition_list = []
        log_content_list = []

        if disks:
            for disk in disks:
                infected_folder_path = f'{disk}:\\ '
                result_repair_infected_folder = None

                if os.path.exists(infected_folder_path):
                    self.subprocess_run(['attrib', '-r', infected_folder_path, '/d', '/s'])
                    result_repair_infected_folder = self.subprocess_run(
                        ['attrib', '-s', '-h', '-r', infected_folder_path, '/d']).returncode

                    if result_repair_infected_folder == 0:
                        self.logger.info(
                            f'The attribute of the Infected folder in {disk}-disk has been changed (Return code {result_repair_infected_folder})')
                        condition_list.append('success')
                        log_content_list.append(f'The attribute of the Infected folder in {disk}-disk was changed')

                    else:
                        self.logger.warning(f'The attribute of the Infected folder cannot be changed')
                        condition_list.append('failed')
                        log_content_list.append(f'The attribute of the Infected folder cannot be changed')

                if os.path.exists(f'{disk}:\\ \\desktop.ini'):
                    result_change_attrib_of_virus_files = self.subprocess_run(
                        ['attrib', '-s', '-h', '-R', f'{disk}:\\ \\desktop.ini', "/d"])

                    if result_change_attrib_of_virus_files.returncode == 0:
                        self.logger.info(
                            f'The attribute of the virus file ({disk}:\\xa0\\desktop.ini) has been changed (Return {result_change_attrib_of_virus_files})')
                        condition_list.append('success')
                        log_content_list.append(f'The attribute of the virus file in {disk}-disk was changed')

                        os.remove(f'{disk}:\\ \\desktop.ini')
                        self.logger.info(f'Virus file ({disk}:\\xa0\\desktop.ini) has been removed')
                        condition_list.append('success')
                        log_content_list.append(f'Virus file in {disk}-disk was renamed')

                    else:
                        self.logger.warning(f'The attribute of the virus file cannot be changed')
                        condition_list.append('failed')
                        log_content_list.append(f'The attribute of the virus file cannot be changed')

                if result_repair_infected_folder == 0 and os.path.exists(infected_folder_path):
                    # os.rename(infected_folder_path, f'{disk}:\\Files Hidden by Viruses')
                    # os.rename(infected_folder_path, f'{disk}:\\被病毒隐藏的文件')

                    # self.logger.info(f'Infected folder in {disk}-disk has been renamed')
                    # condition_list.append('success')
                    # log_content_list.append(f'Infected folder in {disk}-disk was renamed')

                    try:
                        os.rename(infected_folder_path, f'{disk}:\\Files Hidden by Viruses')
                        # os.rename(infected_folder_path, f'{disk}:\\被病毒隐藏的文件')
                        self.logger.info(f'Infected folder in {disk}-disk has been renamed')
                        # print(f'Successfully renamed')
                    except PermissionError as error:
                        self.logger.error(f'Permission denied: {error}')
                        condition_list.append('failed')
                        log_content_list.append(f'Permission denied')
                        # print('Permission denied. Please run the script as an administrator.')
                    except FileNotFoundError:
                        self.logger.error(f'The directory does not exist')
                        condition_list.append('failed')
                        log_content_list.append(f'The directory does not exist')
                        # print(f'The directory does not exist.')
                    except Exception as error:
                        self.logger.error(f'An error occurred: {error}')
                        condition_list.append('failed')
                        log_content_list.append(f'An error occurred: {error}')
                        # print(f'An error occurred: {error}')

                else:
                    self.logger.warning(f'The directory does not exist')
                    condition_list.append('failed')
                    log_content_list.append(f'The directory does not exist')
                    # print(f'The directory does not exist.')

        else:
            self.logger.warning(f'Removable disk not found')
            condition_list.append('failed')
            log_content_list.append(f'Removable disk not found')

        for cnt in range(0, len(log_content_list)):
            log_content = log_content_list[cnt]
            condition = condition_list[cnt]

            output_content = log_content
            self.set_insert(module_name, condition, output_content)

        # wintoast('Repair Infected Files completed')

    # Call two functions
    def auto_kill(self):
        self.kill_viruses()
        self.repair_infected_files()

    # Clean Screen Module: Clean Screen & Output
    def clean_button(self):

        self.gui.var.set("Virus Killer")
        self.gui.output_text.configure(state='normal')
        self.gui.output_text.delete("1.0", tk.END)
        self.gui.output_text.configure(state='disabled')

        self.easter_egg()

    # Easter_Egg module
    def easter_egg(self):

        if self.Easter_Egg < 0:
            pass
        elif self.Easter_Egg < 4:
            self.Easter_Egg += 1
        else:
            self.gui.var.set("Copyright © 2024 - 2030 Arthur_xyz.All Rights Reserved")

            self.logger.debug('=' * 52)
            self.logger.debug('Copyright 2024 - 2030 Arthur_xyz.All Rights Reserved')
            self.logger.debug('The Easter Egg was discovered by you!')
            self.logger.debug('Developer:\tArthur_xyz')
            self.logger.debug('Email:\tArthur_xyz@outlook.com')
            self.logger.debug('=' * 52)

            self.Easter_Egg = 0

    def debugger_button(self):
        if self.disable_debug_frame:
            self.gui.debug_frame.grid(row=2, column=2, rowspan=10, columnspan=2)
            self.disable_debug_frame = False
        else:
            self.gui.debug_frame.grid_forget()
            self.disable_debug_frame = True

    # Get the value of the combobox automatically and set the level of the logger & handler
    # noinspection PyUnusedLocal
    def set_log_level(self, level):
        if level == 'Debug':
            self.handler.setLevel(self.logging.DEBUG)
            self.logger.setLevel(level=self.logging.DEBUG)
        elif level == 'Info':
            self.handler.setLevel(self.logging.INFO)
            self.logger.setLevel(level=self.logging.INFO)
        elif level == 'Warning':
            self.handler.setLevel(self.logging.WARNING)
            self.logger.setLevel(level=self.logging.WARNING)
        elif level == 'Error':
            self.handler.setLevel(self.logging.ERROR)
            self.logger.setLevel(level=self.logging.ERROR)
        elif level == 'Critical':
            self.handler.setLevel(self.logging.CRITICAL)
            self.logger.setLevel(level=self.logging.CRITICAL)
        elif level == 'Silent':
            self.handler.setLevel(100)
            self.logger.setLevel(100)

    def set_insert_simplified(self, content):
        minus_sign_quantity = '-' * 50
        output = f'{minus_sign_quantity}{content}\n\n'

        self.gui.output_text.configure(state='normal')
        self.gui.output_text.insert('end', output)
        self.gui.output_text.configure(state='disabled')

    def set_insert(self, module, condition, content):
        current_time = time.asctime()[-13:-5]

        module = module.upper()
        condition = condition.upper()

        output = f'{current_time} | [{module}]\t|\t{condition}\t|\t{content}\n'
        self.gui.output_text.configure(state='normal')
        self.gui.output_text.insert('end', output)
        self.gui.output_text.configure(state='disabled')

    def handle_close_event(self):
        self.logger.info('Application shutdown initiated by user')
        self.logger.info('Graceful termination completed')
        self.gui.root.destroy()
