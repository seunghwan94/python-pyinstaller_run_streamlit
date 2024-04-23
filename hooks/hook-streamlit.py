from PyInstaller.utils.hooks import copy_metadata, collect_submodules
datas = copy_metadata('streamlit')
# hiddenimports = collect_submodules('selenium')
# hiddenimports += collect_submodules('oauth2client')
# hiddenimports += collect_submodules('gspread')
# hiddenimports += collect_submodules('openai')