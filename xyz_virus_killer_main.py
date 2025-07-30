# -*- coding: utf-8 -*-
# Project Name: xyzvk
# Version: 3.1.0
# Authors:
#   - Ariskanyaa <Ariskanyaa@outlook.com>
#   - Errorsia <Errorsia@outlook.com>
# License: GNU General Public License v3.0 or later (GPLv3+)
# See: https://www.gnu.org/licenses/gpl-3.0.html

# Project Name: xyzvk
# Copyright (C) 2024 Errorsia, Ariskanyaa
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# THE PROGRAMME ONLY RUNS ON WINDOWS(NT) !
# I don't think someone will run an EXE programme on Linux(except wine), MacOS etc.


"""
Main module for xyzvk
"""

# Update Log:
# The copyright information has been modified to comply with the open source license
#
# 更新日志:
# 修改了版权信息, 以符合开源协议

# Author's message:
#     Why the codes is more and more complex, while the lines are fewer and fewer?
#     There is no bugs at present!
#     But programme is still TESTING!

import logging
import time
import tkinter as tk
from tkinter import messagebox

# Private Libraries
import xyz_virus_killer_gui as gui_module
import xyz_virus_killer_logic as logic_module


# import win11toast


class ErrorsiaVirusKillerApp:
    def __init__(self):

        self.build_Log = None

        self.debug_frame_disable = True

        self.logic = logic_module.ErrorsiaVirusKillerLogic(gui=None)

        self.logic.initialization()

        # Get the value of the environment variable %appdata%
        self.appdata = self.logic.appdata
        # Get config and log directory
        self.file_directory = self.logic.file_directory

        self.logger = logging.getLogger(__name__)
        self.handler = logging.FileHandler(f'{self.file_directory}/Log/Log_{time.time():.7f}.avk')

        self.formatter = logging.Formatter(
            '%(asctime)s - %(pathname)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')

        self.log = {
            'logging': logging,
            'logger': self.logger,
            'handler': self.handler
        }

        self.handle_log_config()
        self.initialization_logger_level()

        self.logic.set_log(self.log)
        self.logger.info('Successfully initialized logic module')

        self.logic.easy_clean_log()

        self.logic.check_update()

        self.root = tk.Tk()
        self.var = tk.StringVar()

        gui = gui_module.ErrorsiaVirusKillerGUI(self.root, self.var, self.logger, self.build_Log, self.logic)
        gui.initialization_root()
        gui.set_icon()
        gui.setup_ui()
        self.logger.info('Successfully initialized gui module')

        self.logic.gui = gui
        self.logger.info('Successfully loaded logic module')

        self.root.mainloop()

    def initialization_logger_level(self):
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
            case -2:
                self.build_Log = False
                # tk.messagebox.showerror("PermissionError")
        self.logic.write_log_config(self.build_Log)


if __name__ == '__main__':
    ErrorsiaVirusKillerApp()

# Project Name: [你的项目名称]
# Author: [你的名字或组织名] <[你的电子邮件或网站]>
# Copyright (C) [年份] [你的名字或组织名]
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
