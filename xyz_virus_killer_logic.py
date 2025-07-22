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