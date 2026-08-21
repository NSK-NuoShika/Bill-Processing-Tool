import tkinter as tk
from tkinter import filedialog, messagebox
from typing import TYPE_CHECKING
from pathlib import Path
from controller.bill_controller import BillController
from model.excelsheet_model import ExcelSheetReadModel, ExcelSheetCreateModel
from src.model.config_model import Config
from controller.config_controller import ConfigController
from util.refresh import refresh

if TYPE_CHECKING:
    from src.ui.mainwindow import MainWindow


class HomePage(tk.Frame):
    def __init__(self, parent, controller: MainWindow) -> None:
        super().__init__(parent)
        self._controller = controller

        self._build_ui()


    def _build_ui(self) -> None:
        self._build_label()
        self._build_config()
        self._build_bill()


    def _build_label(self) -> None:
        tk.Button(self, text = '主页', font = ('宋体', 12), padx = 10, command = lambda: self._controller.show('home')).place(relx = 0.3, rely = 0.02, anchor ='n')
        tk.Button(self, text = '关于', font = ('宋体', 12), padx = 10, command = lambda: self._controller.show('about')).place(relx = 0.6, rely = 0.02, anchor ='n')


    def _build_config(self) -> None:
        config = self._load_config()

        self.url = tk.StringVar(value = config.llmconfig.url)
        self.key = tk.StringVar(value = config.llmconfig.key)
        self.model = tk.StringVar(value = config.llmconfig.model)
        self.user_prompt = config.promptconfig.user_prompt
        self.category = tk.StringVar(value = ','.join(config.billconfig.category) if config.billconfig.category is not None else '')


        self.config_lf = tk.LabelFrame(master = self, text = '配置', font = ('宋体', 11, 'bold'))
        self.config_lf.place(relx=0.5, rely=0.07, anchor='n', relwidth=0.9, relheight=0.30)

        self.url_lb = tk.Label(master=self.config_lf, text='Base_Url')
        self.url_lb.place(relx = 0.05, rely = 0.03, anchor = 'nw', relwidth = 0.1)

        self.url_et = tk.Entry(master=self.config_lf, textvariable = self.url)
        self.url_et.place(relx = 0.2, rely = 0.03, anchor = 'nw', relwidth = 0.7)

        self.key_lb = tk.Label(master=self.config_lf, text='Key')
        self.key_lb.place(relx=0.05, rely=0.18, anchor='nw', relwidth=0.1)

        self.key_et = tk.Entry(master=self.config_lf, textvariable = self.key)
        self.key_et.place(relx = 0.2, rely=0.18, anchor='nw', relwidth=0.7)

        self.model_lb = tk.Label(master=self.config_lf, text='Model')
        self.model_lb.place(relx = 0.05, rely = 0.33, anchor = 'nw', relwidth = 0.1)

        self.model_et = tk.Entry(master=self.config_lf, textvariable = self.model)
        self.model_et.place(relx = 0.2, rely = 0.33, anchor = 'nw', relwidth = 0.3)

        self.category_lb = tk.Label(master=self.config_lf, text='种类')
        self.category_lb.place(relx = 0.05, rely = 0.48, anchor = 'nw', relwidth = 0.1)

        self.category_et = tk.Entry(master=self.config_lf, textvariable = self.category)
        self.category_et.place(relx = 0.2, rely = 0.48, anchor = 'nw', relwidth = 0.7)

        self.prompt_lb = tk.Label(master = self.config_lf, text = '提示词')
        self.prompt_lb.place(relx = 0.05, rely = 0.63, anchor = 'nw', relwidth = 0.1)

        self.prompt_tx = tk.Text(master = self.config_lf)
        self.prompt_tx.place(relx = 0.2, rely = 0.63, anchor = 'nw', relwidth = 0.7, relheight = 0.32)
        self.prompt_tx.insert('1.0', self.user_prompt if self.user_prompt is not None else '')

        tk.Button(master = self, text = '提交配置', command = self._save_config).place(relx = 0.95, rely = 0.38, anchor = 'ne')


    def _build_bill(self):
        self.path1 = tk.StringVar()
        self.row_index1 = tk.IntVar()
        self.time_index1 = tk.IntVar()
        self.party_index1 = tk.IntVar()
        self.product_index1 = tk.IntVar()
        self.type_index1 = tk.IntVar()
        self.value_index1 = tk.IntVar()
        self.income1 = tk.StringVar()
        self.neutral1 = tk.StringVar()
        self.outcome1 = tk.StringVar()

        self.path2 = tk.StringVar()
        self.row_index2 = tk.IntVar()
        self.time_index2 = tk.IntVar()
        self.party_index2 = tk.IntVar()
        self.product_index2 = tk.IntVar()
        self.type_index2 = tk.IntVar()
        self.value_index2 = tk.IntVar()
        self.income2 = tk.StringVar()
        self.neutral2 = tk.StringVar()
        self.outcome2 = tk.StringVar()

        self.tar_path = tk.StringVar()

        self.bill_lfr = tk.LabelFrame(self, text = '账单文件', font = ('宋体', 11, 'bold'))
        self.bill_lfr.place(relx=0.5, rely=0.42, anchor='n', relwidth=0.9, relheight=0.48)

        self.bill1_lfr = tk.LabelFrame(self.bill_lfr, text = '账单 1', font = ('宋体', 10, 'bold'))
        self.bill1_lfr.place(relx=0.5, rely=0.02, anchor='n', relwidth=0.9, relheight=0.45)

        self.file_lb1 = tk.Label(self.bill1_lfr, text='路径')
        self.file_lb1.place(relx=0.02, rely=0.03, anchor='nw', relwidth=0.1)

        self.file_et1 = tk.Entry(self.bill1_lfr, textvariable = self.path1)
        self.file_et1.place(relx=0.13, rely=0.03, anchor='nw', relwidth=0.65)

        self.file_bt1 = tk.Button(master = self.bill1_lfr, text ='选择文件', font = ('宋体', 9), command = lambda: self._choose_file(self.path1))
        self.file_bt1.place(relx=0.8, rely=0.03, anchor='nw', relwidth=0.15)

        self.row_index_lb1 = tk.Label(master = self.bill1_lfr, text ='首行索引')
        self.row_index_lb1.place(relx = 0.02, rely = 0.3)

        self.row_index_et1 = tk.Entry(self.bill1_lfr, textvariable = self.row_index1)
        self.row_index_et1.place(relx = 0.15, rely = 0.3, relwidth = 0.15)

        self.time_index_lb1 = tk.Label(master = self.bill1_lfr, text ='时间列索引')
        self.time_index_lb1.place(relx = 0.32, rely = 0.3)

        self.time_index_et1 = tk.Entry(self.bill1_lfr, textvariable = self.time_index1)
        self.time_index_et1.place(relx = 0.475, rely = 0.3, relwidth = 0.15)

        self.party_index_lb1 = tk.Label(master=self.bill1_lfr, text='交易方索引')
        self.party_index_lb1.place(relx=0.65, rely=0.3)

        self.party_index_et1 = tk.Entry(self.bill1_lfr, textvariable = self.party_index1)
        self.party_index_et1.place(relx=0.80, rely=0.3, relwidth=0.15)

        self.product_index_lb1 = tk.Label(master=self.bill1_lfr, text='商品索引')
        self.product_index_lb1.place(relx=0.02, rely=0.55)

        self.product_index_et1 = tk.Entry(self.bill1_lfr,textvariable = self.product_index1)
        self.product_index_et1.place(relx=0.15, rely=0.55, relwidth=0.15)

        self.type_index_lb1 = tk.Label(master=self.bill1_lfr, text='收支索引')
        self.type_index_lb1.place(relx=0.32, rely=0.55)

        self.type_index_et1 = tk.Entry(self.bill1_lfr, textvariable = self.type_index1)
        self.type_index_et1.place(relx=0.475, rely=0.55, relwidth=0.15)

        self.value_index_lb1 = tk.Label(master=self.bill1_lfr, text='金额索引')
        self.value_index_lb1.place(relx=0.65, rely=0.55)

        self.value_index_et1 = tk.Entry(self.bill1_lfr, textvariable = self.value_index1)
        self.value_index_et1.place(relx=0.80, rely=0.55, relwidth=0.15)

        self.income_lb1 = tk.Label(master=self.bill1_lfr, text='收入示例')
        self.income_lb1.place(relx=0.02, rely=0.8)

        self.income_et1 = tk.Entry(self.bill1_lfr, textvariable = self.income1)
        self.income_et1.place(relx=0.15, rely=0.8, relwidth=0.15)

        self.neutral_lb1 = tk.Label(master=self.bill1_lfr, text='中性示例')
        self.neutral_lb1.place(relx=0.32, rely=0.8)

        self.neutral_et1 = tk.Entry(self.bill1_lfr, textvariable = self.neutral1)
        self.neutral_et1.place(relx=0.475, rely=0.8, relwidth=0.15)

        self.outcome_lb1 = tk.Label(master=self.bill1_lfr, text='支出示例')
        self.outcome_lb1.place(relx=0.65, rely=0.8)

        self.outcome_et1 = tk.Entry(self.bill1_lfr, textvariable = self.outcome1)
        self.outcome_et1.place(relx=0.80, rely=0.8, relwidth=0.15)

        self.bill2_lfr = tk.LabelFrame(self.bill_lfr, text='账单 2', font=('宋体', 10, 'bold'))
        self.bill2_lfr.place(relx=0.5, rely=0.5, anchor='n', relwidth=0.9, relheight=0.45)

        self.file_lb2 = tk.Label(self.bill2_lfr, text='路径')
        self.file_lb2.place(relx=0.02, rely=0.03, anchor='nw', relwidth=0.1)

        self.file_et2 = tk.Entry(self.bill2_lfr, textvariable=self.path2)
        self.file_et2.place(relx=0.13, rely=0.03, anchor='nw', relwidth=0.65)

        self.file_bt2 = tk.Button(master=self.bill2_lfr, text='选择文件', font=('宋体', 9), command=lambda: self._choose_file(self.path2))
        self.file_bt2.place(relx=0.8, rely=0.03, anchor='nw', relwidth=0.15)

        self.row_index_lb2 = tk.Label(master=self.bill2_lfr, text='首行索引')
        self.row_index_lb2.place(relx=0.02, rely=0.3)

        self.row_index_et2 = tk.Entry(self.bill2_lfr, textvariable=self.row_index2)
        self.row_index_et2.place(relx=0.15, rely=0.3, relwidth=0.15)

        self.time_index_lb2 = tk.Label(master=self.bill2_lfr, text='时间列索引')
        self.time_index_lb2.place(relx=0.32, rely=0.3)

        self.time_index_et2 = tk.Entry(self.bill2_lfr, textvariable=self.time_index2)
        self.time_index_et2.place(relx=0.475, rely=0.3, relwidth=0.15)

        self.party_index_lb2 = tk.Label(master=self.bill2_lfr, text='交易方索引')
        self.party_index_lb2.place(relx=0.65, rely=0.3)

        self.party_index_et2 = tk.Entry(self.bill2_lfr, textvariable=self.party_index2)
        self.party_index_et2.place(relx=0.80, rely=0.3, relwidth=0.15)

        self.product_index_lb2 = tk.Label(master=self.bill2_lfr, text='商品索引')
        self.product_index_lb2.place(relx=0.02, rely=0.55)

        self.product_index_et2 = tk.Entry(self.bill2_lfr, textvariable=self.product_index2)
        self.product_index_et2.place(relx=0.15, rely=0.55, relwidth=0.15)

        self.type_index_lb2 = tk.Label(master=self.bill2_lfr, text='收支索引')
        self.type_index_lb2.place(relx=0.32, rely=0.55)

        self.type_index_et2 = tk.Entry(self.bill2_lfr, textvariable=self.type_index2)
        self.type_index_et2.place(relx=0.475, rely=0.55, relwidth=0.15)

        self.value_index_lb2 = tk.Label(master=self.bill2_lfr, text='金额索引')
        self.value_index_lb2.place(relx=0.65, rely=0.55)

        self.value_index_et2 = tk.Entry(self.bill2_lfr, textvariable=self.value_index2)
        self.value_index_et2.place(relx=0.80, rely=0.55, relwidth=0.15)

        self.income_lb2 = tk.Label(master=self.bill2_lfr, text='收入示例')
        self.income_lb2.place(relx=0.02, rely=0.8)

        self.income_et2 = tk.Entry(self.bill2_lfr, textvariable=self.income2)
        self.income_et2.place(relx=0.15, rely=0.8, relwidth=0.15)

        self.neutral_lb2 = tk.Label(master=self.bill2_lfr, text='中性示例')
        self.neutral_lb2.place(relx=0.32, rely=0.8)

        self.neutral_et2 = tk.Entry(self.bill2_lfr, textvariable=self.neutral2)
        self.neutral_et2.place(relx=0.475, rely=0.8, relwidth=0.15)

        self.outcome_lb2 = tk.Label(master=self.bill2_lfr, text='支出示例')
        self.outcome_lb2.place(relx=0.65, rely=0.8)

        self.outcome_et2 = tk.Entry(self.bill2_lfr, textvariable=self.outcome2)
        self.outcome_et2.place(relx=0.80, rely=0.8, relwidth=0.15)

        self.tar_path_lb = tk.Label(master = self, text = '输出路径')
        self.tar_path_lb.place(relx=0.05, rely=0.92, anchor = 'nw')

        self.tar_path_et = tk.Entry(self, textvariable=self.tar_path)
        self.tar_path_et.place(relx=0.15, rely=0.92, relwidth=0.5)

        self.tar_path_bt = tk.Button(master=self, text='选择文件', font=('宋体', 9), command=lambda: self._choose_dir(self.tar_path))
        self.tar_path_bt.place(relx=0.67, rely=0.92, anchor='nw', relwidth=0.15)

        self.bill_bt = tk.Button(self, text = '开始分类', command = self._start_classify)
        self.bill_bt.place(relx = 0.95, rely = 0.92, anchor = 'ne')


    def _load_config(self) -> Config:
        config = ConfigController().load()
        return config


    def _save_config(self) -> None:
        config = Config()

        config.llmconfig.url = self.url.get() if self.url.get() != '' else None
        config.llmconfig.key = self.key.get() if self.key.get() != '' else None
        config.llmconfig.model = self.model.get() if self.model.get() != '' else None
        config.billconfig.category = [x.strip()
                                      for x in self.category.get().split(',')] if self.category.get() != '' else None
        config.promptconfig.user_prompt = self.prompt_tx.get('1.0', tk.END) if self.prompt_tx.get('1.0', tk.END) not in ('', '\n') else None

        ConfigController().save(config)


    def _choose_file(self, path: tk.StringVar) -> None:
        path.set(filedialog.askopenfilename())


    def _choose_dir(self, path: tk.StringVar) -> None:
        path.set(filedialog.askdirectory())


    def _start_classify(self) -> None:

        from time import time
        tar_path = str(Path(self.tar_path.get()) / f'bill_{int(time()*1000)}.xlsx')

        ty1 = [self.outcome1.get(), self.neutral1.get(), self.income1.get()]
        ty2 = [self.outcome2.get(), self.neutral2.get(), self.income2.get()]

        excel1 = ExcelSheetReadModel(self.path1.get(),0, self.row_index1.get(), ty1, (self.time_index1.get(), self.party_index1.get(), self.product_index1.get(), self.type_index1.get(), self.value_index1.get()))
        excel2 = ExcelSheetReadModel(self.path2.get(),0, self.row_index2.get(), ty2, (self.time_index2.get(), self.party_index2.get(), self.product_index2.get(), self.type_index2.get(), self.value_index2.get()))
        tar_excel_c = ExcelSheetCreateModel(tar_path, '总账单')
        tar_excel_r = ExcelSheetReadModel(tar_path, 0, 0, ['outcome', 'neutral', 'income'], (0, 1, 2, 3, 4))

        BillController().merge([excel1, excel2], tar_excel_c)
        BillController().classify('llmclassifier', tar_excel_r, tar_path)

        refresh(tar_path)

        messagebox.showinfo('提示', '分类成功')
