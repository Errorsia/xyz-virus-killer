# XYZ Virus Killer

![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![License](https://img.shields.io/badge/license-GPLv3-green)
![Stars](https://img.shields.io/github/stars/Errorsia/xyz-virus-killer?style=social)
![Last Update](https://img.shields.io/github/last-commit/Errorsia/xyz-virus-killer)

---

## Project Overview

`XYZ Virus Killer` is a virus removal tool written in `Python`, featuring targeted virus termination, file recovery, and a clean graphical interface.

## Key Features

- **Kill Viruses**: Automatically terminates running virus processes. Supports up to 5 built-in virus types.
- **Repair Files**: Restores files damaged by viruses to protect user data.
- **User-Friendly Interface**: Built with `Tkinter`, offering simple and intuitive operation.
- **Hidden Easter Eggs**: Includes fun elements to enhance the user experience.

### Usage Instructions

- `Kill Virus`: Terminates specified virus processes  
- `Fix What Viruses Make`: Repairs files damaged by viruses  
- `Auto Kill`: Automatically performs virus removal and file recovery  

## Installation

This project runs on `Python 3.x`. The GUI uses only standard libraries, while the logic module requires the third-party library `pywin32`.

Install the required `pywin32` library:

```bash
pip install pywin32
```

If needed, install the Tkinter module:
> Note: Tkinter is usually included with standard Python distributions. If missing, it can be installed via your system's package manager.

```bash
pip install tkinter
```

## Optional Component: ttkbootstrap

This project supports enhanced UI styling via [`ttkbootstrap`](https://github.com/israel-dryer/ttkbootstrap), which is an optional dependency.

To use the enhanced interface (e.g., xyz_virus_killer_main_ttkbootstrap.py and xyz_virus_killer_gui_ttkbootstrap.py), install:

```bash
pip install ttkbootstrap
```

Without this library, the enhanced interface modules will not run, but the main program remains fully functional.

## Project Structure

```
xyz-virus-killer/
├── xyz_virus_killer_main.py              # Main program entry
├── xyz_virus_killer_main_ttkbootstrap.py # Main program with ttkbootstrap
├── xyz_virus_killer_gui.py               # GUI controller module
├── xyz_virus_killer_gui_ttkbootstrap.py  # GUI module with ttkbootstrap
├── xyz_virus_killer_logic.py             # Core logic module
├── xyz_virus_killer_config.py            # Configuration management
├── icon.py                               # Icon resources
├── README.md                             # Project documentation
│── LICENSE                               # GPLv3 license
```

## Changelog

For details, see: [CHANGELOG](./CHANGELOG.md)

## Contributing

Suggestions and improvements are welcome! 
Feel free to submit an Issue or Pull Request to help improve the project. 
For feedback or questions, contact the author or leave a comment on GitHub.

Copyright (C) 2025 Errorsia & Ariskanyaa
