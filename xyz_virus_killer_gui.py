# -*- coding: utf-8 -*-
# Author: Ariskanyaa <Ariskanyaa@outlook.com>
# Author: Errorsia <Errorsia@outlook.com>
# License: GPL v3

"""
GUI module for xyzvk
"""

import base64
import os
import tempfile
import tkinter as tk
from tkinter import ttk

import icon
# Private Libraries
import xyz_virus_killer_config as config


class ErrorsiaVirusKillerGUI:
    def __init__(self, root, var, logger, logic):
        self.root = root
        self.var = var
        self.logger = logger
        self.logic = logic
        self.label1 = None
        self.debug_frame = self.debug_combobox1 = self.output_text = None

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

        button_frame = tk.Frame(self.root, bg='palegreen')

        button1 = tk.Button(button_frame, text="Kill Viruses", font=30, width=40, height=2,
                            command=self.logic.kill_viruses)
        button1.grid(row=0, column=0, padx=10, pady=20)

        button2 = tk.Button(button_frame, text="Repair Infected Files", font=30, width=40, height=2,
                            command=self.logic.repair_infected_files)
        button2.grid(row=0, column=1, padx=10, pady=20)

        button3 = tk.Button(button_frame, text="Auto Kill(Do #1 And #2)", font=30, width=40, height=2,
                            command=self.logic.auto_kill)
        button3.grid(row=1, column=0, padx=10, pady=20)

        button4 = tk.Button(button_frame, text="Clean Screen", font=30, width=40, height=2,
                            command=self.logic.clean_button)
        button4.grid(row=1, column=1, padx=10, pady=20)

        button5 = tk.Button(button_frame, text="Debugger", font=30, width=40, height=2,
                            command=self.logic.debugger_button)
        button5.grid(row=2, column=0, padx=10, pady=20)

        button_frame.grid(row=2, column=0, rowspan=4, columnspan=2)

        self.debug_frame = tk.Frame(self.root, bg='red')

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
        self.debug_combobox1.current(0)

        # Bind events to combobox
        self.debug_combobox1.bind("<<ComboboxSelected>>", self.debug_combobox_on_select)

        debug_frame_sub1.pack(pady=10)

        self.var.set(config.FULL_VERSION)

    # Get the value of the combobox automatically and set the level of the logger & handler
    # noinspection PyUnusedLocal
    def debug_combobox_on_select(self, event):
        selected_value = self.debug_combobox1.get()
        self.logic.set_log_level(selected_value)
