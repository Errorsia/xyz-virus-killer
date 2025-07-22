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