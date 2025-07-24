# -*- coding: utf-8 -*-
# Author: Ariskanyaa <Ariskanyaa@outlook.com>
# Author: Errorsia <Errorsia@outlook.com>
# License: GPL v3

"""
Logic module for xyzvk
"""

import os
import time
import tkinter as tk
from tkinter import messagebox
import subprocess
import xyzvk_v3_0_0_config as config


class ErrorsiaVirusKillerLogic:
    def __init__(self, gui):
        self.gui = gui
        self.logging = self.logger = self.handler = None

        # Whether TSET ENVIRONMENT
        # test = True

        # Build log(Messagebox return)
        # log_dictionary = {'build_Log': None}a
        self.build_Log = None

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
        # Saftier
        self.logging = log.get('logging')
        self.logger = log.get('logger')
        self.handler = log.get('handler')

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
        # print(self.build_Log)
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
        # print(self.build_Log)

    # Check for updates
    def update(self):
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
        return -11

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

    def get_removable_disks(self):
        drives, drives_type = self.get_drives_and_types()
        removable_disks = []

        for cnt in range(len(drives)):
            if drives_type[cnt] == '可移动磁盘':
                removable_disks.append(drives[cnt].rstrip(':'))

        return removable_disks