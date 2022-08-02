# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('logo/logo2.jpeg', 'logo'),('users/fdd.json', 'users'),('data/word.json', 'data'), ('ui/login.ui', 'ui'), ('ui/menu.ui', 'ui'), ('ui/game.ui', 'ui'), ('ui/about.ui', 'ui'), ('logo/logo.qrc', 'logo')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='FlashCards',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='fenyx.icns',
)
app = BUNDLE(
    exe,
    name='FlashCards.app',
    icon='fenyx.icns',
    bundle_identifier=None,
)
