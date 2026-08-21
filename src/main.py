import sys

from pathlib import Path
sys.path.append(str(Path(__file__).parents[1].resolve()))

from src.ui.mainwindow import MainWindow

if __name__ == "__main__":
    MainWindow().run()
