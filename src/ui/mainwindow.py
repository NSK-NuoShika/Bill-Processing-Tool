import tkinter as tk
from src.ui.pages.about import About
from src.ui.pages.home_page import HomePage


class MainWindow(tk.Tk):

    def __init__(self) -> None:
        super().__init__()

        self.title('Bill-Processing-Tool')
        self.geometry('750x900+300+50')

        fr = tk.Frame(self)
        fr.pack(fill = 'both', expand = True)
        fr.rowconfigure(0, weight = 1)
        fr.columnconfigure(0, weight = 1)

        class_pages = {'home': HomePage,
                       'about': About}

        self.pages = dict()
        for n, p in class_pages.items():
            self.pages[n] = p(fr, self)
            self.pages[n].grid(row = 0, column = 0, sticky = 'nsew')

        self.show('home')


    def show(self, page: str) -> None:
        self.pages[page].tkraise()


    def run(self):
        self.mainloop()
