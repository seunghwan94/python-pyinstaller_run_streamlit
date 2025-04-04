# -*- mode: python ; coding: utf-8 -*-



block_cipher = None

import os
import streamlit
from PyInstaller.utils.hooks import collect_data_files, copy_metadata, collect_submodules


###############################################
# 상수 변수 선언
exe_name    = 'AutoKeyword'          # 최종 생성될 실행 파일 이름
icon_path   = 'config/AP.ico'        # 아이콘 파일 경로
st_filename = 'app.py'               # st.py 파일 이름
console     =  True                  # 콘솔창 표시

# 포함 할 폴더들 (예: config, utils 등)
include_dirs = ['config']   


# streamlit 서브모듈 (라이브러리 추가 시 사용)
additional_libs = ['pandas']
###############################################







# streamlit 패키지 경로 및 static 폴더 경로
streamlit_path = os.path.dirname(streamlit.__file__)
static_path  = os.path.join(streamlit_path, "static")

# datas 설정: streamlit의 static 폴더, 기타 데이터 파일, 메타데이터 포함
datas = [
    (static_path, os.path.join("streamlit", "static")),  # streamlit/static 디렉터리 포함
]
datas += collect_data_files('streamlit')
datas += copy_metadata('streamlit')




datas.append((st_filename, '.'))
# 리스트에 있는 폴더들을 반복문으로 추가
for folder in include_dirs:
    datas.append((folder, folder))

# 리스트에 있는 라이브러리리 반복문으로 추가
hiddenimports = collect_submodules('streamlit')
for lib in additional_libs:
    try:
        hiddenimports += collect_submodules(lib)
        print(f"'{lib}' 의 서브모듈이 hiddenimports에 추가되었습니다.")
    except Exception as e:
        print(f"'{lib}' 의 서브모듈 수집 실패: {e}")




a = Analysis(
    ["run.py"],
    pathex=["."],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
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
    a.datas,
    [],
    name=exe_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=console,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_path  # 아이콘 지정
)

app = BUNDLE(
    exe,
    name=exe_name,
    icon=icon_path,  # 아이콘 지정
    onefile=True
)
