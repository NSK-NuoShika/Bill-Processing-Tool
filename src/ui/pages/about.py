from __future__ import annotations

import tkinter as tk
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.ui.mainwindow import MainWindow

class About(tk.Frame):
    def __init__(self, parent, controller: MainWindow):
        super().__init__(parent)
        self._controller = controller

        self._build_ui()


    def _build_ui(self):
        self._build_label()
        self._build_content()


    def _build_label(self):
        tk.Button(self, text='主页', font=('宋体', 12), padx=10, command=lambda: self._controller.show('home')).place(
            relx=0.3, rely=0.02, anchor='n')
        tk.Button(self, text='关于', font=('宋体', 12), padx=10, command=lambda: self._controller.show('about')).place(
            relx=0.6, rely=0.02, anchor='n')


    def _build_content(self):
        lf_pg = tk.LabelFrame(master = self, text = '项目信息', font = ('宋体', 11, 'bold'))
        tk.Label(master = lf_pg, text = '作者: NSK（NuoShika）', font = ('宋体', 11), anchor = 'w').place(relx = 0.1, rely = 0.2)
        tk.Label(master = lf_pg, text = '邮箱: nsk_nuoshika@outlook.com', font = ('宋体', 11), anchor = 'w').place(relx = 0.1, rely = 0.55)
        lf_pg.place(relx = 0.5, rely = 0.2, anchor = 'n', relwidth = 0.8, relheight = 0.2)

        lf_rp = tk.LabelFrame(master = self, text = '仓库地址', font = ('宋体', 11, 'bold'))
        tk.Label(master = lf_rp, text = 'GitHub: https://github.com/NSK-NuoShika/Bill-Processing-Tool', font = ('宋体', 10), anchor = 'w').place(relx = 0.03, rely = 0.4)
        lf_rp.place(relx = 0.5, rely = 0.5, anchor = 'n', relwidth = 0.8, relheight = 0.15)
