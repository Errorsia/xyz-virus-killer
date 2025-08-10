# XYZ Virus Killer

![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![License](https://img.shields.io/badge/license-GPLv3-green)
![Stars](https://img.shields.io/github/stars/Errorsia/xyz-virus-killer?style=social)
![Last Update](https://img.shields.io/github/last-commit/Errorsia/xyz-virus-killer)

---

## 项目简介

`XYZ Virus Killer` 是一个使用 `Python` 编写的病毒清除工具, 支持定向杀毒、文件修复, 并提供简洁的图形界面。

## 功能特色

- **杀死病毒**：自动终止运行中的病毒进程, 内置支持杀死高达5种病毒。
- **修复文件**：恢复被病毒破坏的文件, 保护用户数据。
- **界面友好**：基于 `Tkinter` 构建, 操作简单直观。
- **隐藏彩蛋**：内置趣味元素, 提升使用体验。

### 操作说明

- `Kill Virus`：终止指定病毒进程
- `Fix What Viruses Make`：修复病毒造成的文件损坏
- `Auto Kill`：自动执行杀毒与修复操作

## 安装依赖

本项目基于 `Python 3.x` 运行, GUI仅使用标准库, 逻辑模块需额外安装第三方库 `pywin32` 。

请安装 `pywin32` 库：

```bash
pip install pywin32
```

如有需要, 请安装 `Tkinter` 库：
> 注意：`Tkinter` 通常随 Python 安装包一同提供, 若缺失可通过系统包管理器安装。

```bash
pip install tkinter
```

## 可选组件：ttkbootstrap

本项目支持使用 [`ttkbootstrap`](https://github.com/israel-dryer/ttkbootstrap) 来美化界面, 但该库为**可选依赖**, 非必须。

如果你希望使用增强版界面 (如 `xyz_virus_killer_main_ttkbootstrap.py` 和 `xyz_virus_killer_gui_ttkbootstrap.py`) , 请安装：

```bash
pip install ttkbootstrap
```

未安装该库时, 增强界面模块将无法运行, 但主程序仍可正常使用。

## 代码结构

```
xyz-virus-killer/
├── xyz_virus_killer_main.py              # 主程序入口
├── xyz_virus_killer_main_ttkbootstrap.py # 使用 ttkbootstrap 的主程序
├── xyz_virus_killer_gui.py               # GUI 控制模块
├── xyz_virus_killer_gui_ttkbootstrap.py  # 使用 ttkbootstrap 的 GUI 模块
├── xyz_virus_killer_logic.py             # 核心逻辑模块
├── xyz_virus_killer_config.py            # 配置管理模块
├── icon.py                               # 图标资源
├── README.md                             # 项目说明文档
│── LICENSE                               # GPLv3 开源协议
```

## 更新日志

详情请见: [CHANGELOG](./CHANGELOG.md)

## 贡献

欢迎提供建议或改进代码!
欢迎提交 Issue 或 Pull Request 来改进本项目。
如有建议或问题, 请联系作者或在 GitHub 上留言。

Copyright (C) 2025 Errorsia & Ariskanyaa
