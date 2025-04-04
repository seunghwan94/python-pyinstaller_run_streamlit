import os
import sys
import threading
import webbrowser
import streamlit.web.cli as stcli
import pystray
from PIL import Image

def resolve_path(filename):
    """PyInstaller 빌드 유무에 따라 파일 경로를 올바르게 찾는 함수"""
    if getattr(sys, 'frozen', False):  # PyInstaller로 빌드된 경우
        base_path = sys._MEIPASS
    else:
        base_path = os.getcwd()
    return os.path.join(base_path, filename)

def run_streamlit():
    """메인 스레드에서 Streamlit 앱 실행"""
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("app.py"),  # st.py를 exe 내부에 포함했다면 여기서 resolve_path 사용
        "--global.developmentMode=false",  # 이 옵션 때문에 signal 등록 로직이 실행됨
    ]
    stcli.main()

def open_browser():
    """브라우저를 열어 Streamlit 앱 페이지로 이동"""
    webbrowser.open("http://localhost:8501")

def on_exit(icon, item):
    """트레이 아이콘 종료 + 전체 프로그램 종료"""
    icon.stop()
    sys.exit(0)

def run_tray_icon():
    """백그라운드 스레드에서 트레이 아이콘 실행"""
    # AP.ico 아이콘 파일 경로
    icon_path = resolve_path("config/AP.ico")

    # 아이콘 이미지 로드
    image = Image.open(icon_path)

    # 트레이 아이콘 메뉴 구성
    menu = pystray.Menu(
        pystray.MenuItem("Open Browser", lambda icon, item: open_browser()),
        pystray.MenuItem("Exit", on_exit),
    )

    # 아이콘 생성 및 실행 (이 메서드는 blocking)
    tray_icon = pystray.Icon("StreamlitApp", image, "My Streamlit App", menu)
    tray_icon.run()

if __name__ == "__main__":
    # 1) 트레이 아이콘을 백그라운드 스레드에서 실행
    tray_thread = threading.Thread(target=run_tray_icon, daemon=True)
    tray_thread.start()

    # 2) 메인 스레드에서 Streamlit 실행
    run_streamlit()
