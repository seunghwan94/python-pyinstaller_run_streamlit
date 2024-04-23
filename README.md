## 설치

아래 명령어를 사용하여 필요한 패키지를 설치합니다:

```pip install streamlit pyinstaller```


## 실행

hooks 파일에 있는 라이브러리를 run.py에 넣기

```pyinstaller --onefile --additional-hooks-dir=./hooks run.py --clean```


## 추가 설정

run.spac 파일이 생성 됬을텐데 밑에 있는 코드로 수정

```python
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import copy_metadata

datas = [("lib/Lib/site-packages/streamlit/runtime", "./streamlit/runtime")]
datas += collect_data_files("streamlit")
datas += copy_metadata("streamlit")


block_cipher = None


a = Analysis(
    ["run.py"],
    pathex=["."],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=['./hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz[...]
```

수정 후 진행

```pyinstaller run.spec --clean```

## 라이브러리 추가 할 경우
### ./hooks/hook-streamlit.py 에 코드 추가할 것
```
# hiddenimports = collect_submodules('selenium')
# hiddenimports += collect_submodules('oauth2client')
# hiddenimports += collect_submodules('gspread')
# hiddenimports += collect_submodules('openai')
```