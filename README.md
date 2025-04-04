## 설치

아래 명령어를 사용하여 필요한 패키지를 설치합니다:

```pip install -r requirements.txt```



## 추가 설정

run.spac 파일 이부분만 수정

```
###############################################
# 상수 변수 선언
exe_name    = 'AutoKeyword'          # 최종 생성될 실행 파일 이름
icon_path   = 'config/AP.ico'        # 아이콘 파일 경로
st_filename = 'app.py'               # st.py 파일 이름
console     =  True                  # 콘솔창 표시

# 포함 할 폴더들 (예: config, utils 등)
include_dirs = ['config']   


# streamlit 서브모듈 (라이브러리 추가 시 사용)
hiddenimports = collect_submodules('streamlit')
# hiddenimports += collect_submodules('oauth2client')
###############################################
```

수정 후 진행

```pyinstaller --clean --noconfirm run.spec ```