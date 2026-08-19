class ExcelSheetReadModel:
    def __init__(self,
                 excel_file: str,
                 sheet_index: int,
                 start_now_index: int,
                 ty_val: list[str],
                 col_index: tuple[int, ...]
                 ):

        self.excel_file = excel_file
        self.sheet_index = sheet_index
        self.start_now_index = start_now_index
        self.ty_val = ty_val
        self.col_index = col_index



class ExcelSheetWriteModel:
    pass



class ExcelSheetCreateModel(ExcelSheetWriteModel):
    def __init__(self,
                 sheet_file: str,
                 new_name: str,
                 index: int | None = None):

        self.sheet_file = sheet_file
        self.new_name = new_name
        self.index = index



class ExcelSheetAppendModel(ExcelSheetWriteModel):
    def __init__(self,
                 excel_file: str,
                 index: int) -> None:


        self.excel_file = excel_file
        self.index = index
