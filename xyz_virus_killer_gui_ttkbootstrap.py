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
GUI module for xyzvk
"""

import base64
import os
import tempfile
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttkbs
from ttkbootstrap.constants import *

# Private Libraries
import icon
import xyz_virus_killer_config as config


class ErrorsiaVirusKillerGUI:
    def __init__(self, root, var, logger, build_log, logic):
        self.root = root
        self.var = var
        self.logger = logger
        self.build_log = build_log
        self.logic = logic
        # Define widgets
        self.label1 = None
        self.debug_frame = self.debug_combobox1 = self.output_text = None
        self.button1 = self.button2 = self.button3 = self.button4 = self.button5 = None
        self.widgets = None

    def initialization_root(self):
        self.root.title(config.FULL_VERSION)
        self.root.geometry("1360x720")
        self.root.minsize(1360, 720)
        self.root.maxsize(3840, 2160)
        self.root.protocol("WM_DELETE_WINDOW", self.logic.handle_close_event)
        self.logger.info('Successfully initialized root window')

    # Set icon
    def set_icon(self):
        with tempfile.NamedTemporaryFile(suffix='.ico', delete=False) as tmp:
            tmp.write(base64.b64decode(icon.img))
        self.root.iconbitmap(tmp.name)
        os.unlink(tmp.name)
        self.logger.info('Successfully set the icon')

    def setup_ui(self):
        self.label1 = tk.Label(self.root, textvariable=self.var, bg="lightcyan", width=44, font=("Arial", 40), height=2)
        self.label1.grid(row=0, column=0, columnspan=4)

        # self.label2 = tk.Label(self.root, width=10, font=20, height=2)
        # self.label2.grid(row=1, column=0, columnspan=4)

        tk.Label(self.root, width=10, font=20, height=2).grid(row=1, column=0, columnspan=4)

        button_frame = tk.Frame(self.root)

        self.button1 = ttkbs.Button(button_frame, text="Kill Viruses",  width=40, bootstyle=SUCCESS,
                                 command=self.kill_virus_main)
        self.button1.grid(row=0, column=0, padx=10, pady=20)

        self.button2 = ttkbs.Button(button_frame, text="Repair Infected Files",  width=40, bootstyle=SUCCESS,
                                 command=self.logic.repair_infected_files)
        self.button2.grid(row=0, column=1, padx=10, pady=20)

        self.button3 = ttkbs.Button(button_frame, text="Auto Kill(Do #1 And #2)",  width=40, bootstyle=SUCCESS,
                                 command=self.auto_kill_main)
        self.button3.grid(row=1, column=0, padx=10, pady=20)

        self.button4 = ttkbs.Button(button_frame, text="Clean Screen",  width=40, bootstyle=SUCCESS,
                                 command=self.logic.clean_button)
        self.button4.grid(row=1, column=1, padx=10, pady=20)

        self.button5 = ttkbs.Button(button_frame, text="Debugger",  width=40, bootstyle=SUCCESS,
                                 command=self.logic.debugger_button)
        self.button5.grid(row=2, column=0, padx=10, pady=20)

        button_frame.grid(row=2, column=0, rowspan=4, columnspan=2)

        self.debug_frame = tk.Frame(self.root)

        debug_label1 = tk.Label(self.debug_frame, text="Debugger Output:", width=17, font=('TkDefaultFont', 20),
                                height=1)
        debug_label1.pack()

        self.output_text = tk.Text(self.debug_frame, height=30)
        self.output_text.pack()
        self.output_text.configure(state='disabled')

        debug_frame_sub1 = tk.Frame(self.debug_frame)

        debug_label2 = tk.Label(debug_frame_sub1, text="Select log output level: ", width=25, font=20, height=1)
        debug_label2.pack(side='left', padx=10)

        log_options = ['Debug', 'Info', 'Warning', 'Error', 'Critical', 'Silent']
        self.debug_combobox1 = ttk.Combobox(debug_frame_sub1, values=log_options)
        self.debug_combobox1.pack(side='left', padx=10)

        # Set default values
        self.debug_combobox1.current(0 if self.build_log else 5)

        # Bind events to combobox
        self.debug_combobox1.bind("<<ComboboxSelected>>", self.debug_combobox_on_select)

        debug_frame_sub1.pack(pady=10)

        self.widgets = [
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.debug_combobox1
        ]

        self.var.set(config.FULL_VERSION)

    def disable_widgets(self):
        for widget in self.widgets:
            widget.configure(state='disabled')
            widget.update()

    def enable_widgets(self):
        for widget in self.widgets:
            widget.configure(state='normal')
            widget.update()

    def kill_virus_main(self):
        self.disable_widgets()

        self.var.set('Killing Virus Processes')
        self.label1.update()

        self.logic.kill_viruses()

        self.enable_widgets()

        self.var.set("FINISH")

    def auto_kill_main(self):
        self.disable_widgets()

        self.var.set('Auto Kill')
        self.label1.update()

        self.logic.auto_kill()

        self.enable_widgets()

        self.var.set("FINISH")

    # Get the value of the combobox automatically and set the level of the logger & handler
    # noinspection PyUnusedLocal
    def debug_combobox_on_select(self, event):
        selected_value = self.debug_combobox1.get()
        self.logic.set_log_level(selected_value)
