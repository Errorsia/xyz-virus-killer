# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['D:\\Programming\\Python\\PythonProjects\\pythonProject-xyz\\test\\xyzvk\\xk1.6.5\\xyzvk_v1.6.5_(Elysium).py'],
    pathex=[],
    binaries=[],
    datas=[('resources','resources')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='xyzvk_v1.6.5_(Elysium)',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['D:\\Programming\\Python\\PythonProjects\\pythonProject-xyz\\test\\xyzvk\\xk1.6.5\\icon.ico'],
)
