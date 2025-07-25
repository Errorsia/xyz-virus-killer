# -*- coding: utf-8 -*-
# Author: Ariskanyaa <Ariskanyaa@outlook.com>
# Author: Errorsia <Errorsia@outlook.com>
# License: GPL v3

# Version 3.0.0

"""
Main module for xyzvk

Copyright ©  2024 Errorsia.All Rights Reserved
"""

import logging
import os
import time
import tkinter as tk
from tkinter import messagebox

# Private Libraries
import xyz_virus_killer_gui as gui_module
import xyz_virus_killer_logic as logic_module

# import win11toast

"""
THE PROGRAMME ONLY RUNS ON WINDOWS(NT) !
I don't think someone will run an EXE programme on Linux(except wine), MacOS etc.

Update Log:
Rebuild all files

更新日志:
重构所有文件


Author's message:
    Why the codes is more and more complex, while the lines are fewer and fewer?
    There is no bugs at present!
    But programme is still TESTING!
"""


class ErrorsiaVirusKillerApp:
    def __init__(self):

        self.build_Log = None

        self.debug_frame_disable = True

        # Get the value of the environment variable %appdata%
        self.appdata = os.getenv("APPDATA")
        # appdata = os.path.expandvars("%APPDATA%")
        self.file_directory = self.appdata + '/Arthur/VirusKiller'

        # Whether show Easter Egg
        # Current condition: On (If Easter_Egg < 0, it's Off)
        self.Easter_Egg = 0

        self.logic = logic_module.ErrorsiaVirusKillerLogic(gui=None)

        self.logic.initialization()

        self.logger = logging.getLogger(__name__)
        self.handler = logging.FileHandler(f'{self.file_directory}/Log/Log_{time.time():.7f}.avk')

        self.formatter = logging.Formatter(
            '%(asctime)s - %(pathname)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')

        self.log = {
            'logging': logging,
            'logger': self.logger,
            'handler': self.handler
        }

        self.logic.set_log(self.log)

        self.logger.info('Successfully initialized logic module')

        self.handle_log_config()
        self.initialization_logger()

        self.logic.easy_clean_log()

        self.root = tk.Tk()
        self.var = tk.StringVar()

        gui = gui_module.ErrorsiaVirusKillerGUI(self.root, self.var, self.logger, self.logic)
        gui.initialization_root()
        gui.set_icon()
        gui.setup_ui()
        self.logger.info('Successfully initialized gui module')

        self.logic.gui = gui
        self.logger.info('Successfully loaded logic module')

        self.root.mainloop()

    def initialization_logger(self):
        print(self.build_Log)
        if self.build_Log:
            self.handler.setLevel(logging.DEBUG)
            self.logger.setLevel(level=logging.DEBUG)
        else:
            self.handler.setLevel(100)
            self.logger.setLevel(100)

        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    def handle_log_config(self):
        ask_enable_log = self.logic.read_log_config()
        match ask_enable_log:
            case 1:
                self.build_Log = True
            case 0:
                self.build_Log = False
            case -1:
                self.build_Log = tk.messagebox.askokcancel(
                    title="Save log or not",
                    message="Do you want to save log?\n你想要保存日志吗?"
                )
        self.logic.write_log_config(self.build_Log)


if __name__ == '__main__':
    ErrorsiaVirusKillerApp()
