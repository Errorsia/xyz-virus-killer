# XYZ Virus Killer

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-GPLv3-green)
![Stars](https://img.shields.io/github/stars/Errorsia/xyz-virus-killer?style=social)
<!-- [Dependencies](https://img.shields.io/librariesio/github/Errorsia/xyz-virus-killer) -->
![Last Update](https://img.shields.io/github/last-commit/Errorsia/xyz-virus-killer)

---

## 项目简介

`XYZ Virus Killer` 是一个基于 `Python` 的简单病毒定向清除软件。用户可以通过此程序杀死病毒程序, 处理病毒文件和修复被感染的文件。

## 功能特色

- **杀死病毒**：自动杀死运行的病毒, 内置支持杀死高达5种病毒。
- **修复被感染的文件**：修复被感染的文件, 保护使用者的数据不被破坏。
- **界面友好**：基于 `Tkinter` 创建图形界面，简单直观。
- **Easter Egg**：内置隐藏彩蛋，增加趣味性。

## 使用方法

1. **运行程序**：确保 Python 环境已安装，运行 `xyz-virus-killer.py`。
2. **点击 `Kill Virus (杀死病毒)`按钮**：
   - 如果有指定的病毒正在运行, 则杀死指定的病毒。
3. **点击 `Fix What Viruses Make (修复被感染的文件)`按钮**：
   - 可修复指定病毒带来的破坏。
4. **点击 `Auto Kill (自动运行)` 按钮**：
   - 将自动运行杀死病毒和修复被感染的文件功能。

## 安装依赖

本项目基于 `Python 3.x` 运行，GUI仅使用标准库，逻辑模块需额外安装第三方库 `pywin32` 。

如有需要，请安装 `pywin32` 库：

```bash
pip install pywin32
```

如有需要，请安装 `Tkinter` 库：

```bash
pip install tkinter
```

## 代码结构

```
xyz-virus-killer/
│── xyz_virus_killer_main.py                   # 主程序文件
│── xyz_virus_killer_gui.py                    # GUI模块文件
│── xyz_virus_killer_logic.py                  # Logic模块文件
```

## 贡献

欢迎提供建议或改进代码！如有问题，请联系作者。

Copyright (C) 2025 Errorsia & Ariskanyaa
