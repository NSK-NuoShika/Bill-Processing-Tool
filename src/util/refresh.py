import ctypes
import sys
from pathlib import Path

def refresh(path: str):
    if sys.platform == "win32":
        path = Path(path)
        shell32 = ctypes.windll.shell32
        shell32.SHChangeNotify(0x1000, 0x1005, ctypes.c_wchar_p(str(path.parent)), None)
