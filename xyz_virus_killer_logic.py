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
