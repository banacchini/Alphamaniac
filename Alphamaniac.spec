# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('data/animals.json', 'data'),
        ('data/cities.json', 'data'),
        ('data/countries.json', 'data'),
        ('data/highscores.json', 'data'),
        ('data/occupations.json', 'data'),
        ('data/sports.json', 'data'),
        ('resources/icons/alphamaniacIcon.png', 'resources/icons'),
        ('gui/menu/menuDialog.ui', 'gui/menu'),
        ('gui/highscores/highscoresDialog.ui', 'gui/highscores'),
        ('gui/highscores/srHighscores.ui', 'gui/highscores'),
        ('gui/highscores/taHighscores.ui', 'gui/highscores'),
        ('gui/singleRound/singleRoundDialog.ui', 'gui/singleRound'),
        ('gui/singleRound/singleRoundResult.ui', 'gui/singleRound'),
        ('gui/timeAttack/timeRoundDialog.ui', 'gui/timeAttack'),
        ('gui/timeAttack/timeRoundResult.ui', 'gui/timeAttack')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Alphamaniac',
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
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Alphamaniac',
)
