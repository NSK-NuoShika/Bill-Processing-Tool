from typing import Iterator
from model.bill_model import BillRecord, BillList
from src.dao.excelsheet_dao import ExcelSheetReadDao, ExcelSheetAppendDao, ExcelSheetCreateDao


class ExcelSheetReadService:

    def __init__(self,
                 excel_file: str,
                 sheet_index: int,
                 start_now_index: int,
                 ty_val: list[str],
                 col_index: tuple[int, ...]) -> None:

        self._excelsheet_read_dao = ExcelSheetReadDao(excel_file, sheet_index, start_now_index, col_index)

        self._ty_val = ty_val
        self._col_index = col_index


    def load(self, n: int) -> Iterator[BillList]:
        while True:
            try:
                bills = BillList()
                for _ in range(n):
                    row_lst = next(self._excelsheet_read_dao)

                    time = row_lst[self._col_index[0]]
                    party = row_lst[self._col_index[1]]
                    product = row_lst[self._col_index[2]]

                    if row_lst[self._col_index[3]] == self._ty_val[0]:
                        ty = -1
                    elif row_lst[self._col_index[3]] == self._ty_val[1]:
                        ty = 0
                    else:
                        ty = 1

                    value = float(row_lst[self._col_index[4]])    #type: ignore

                    bills.add(BillRecord(time, party, product, ty, value))    # type: ignore

                yield bills

            except StopIteration:

                if len(bills) > 0:
                    yield bills
                break

        self._excelsheet_read_dao.close()



class ExcelSheetWriteService:
    pass



class ExcelSheetCreateService(ExcelSheetWriteService):

    def __init__(self,
                 sheet_file: str,
                 new_name: str,
                 index: int | None = None) -> None:

        self._excelsheet_create_dao = ExcelSheetCreateDao(excel_file = sheet_file, new_name = new_name, index = index)


    def append(self, data: BillList) -> None:
        for br in data:
            time = br.time
            party = br.party
            product = br.product

            if br.ty == -1:
                ty = 'outcome'
            elif br.ty == 0:
                ty = 'neutral'
            else:
                ty = 'income'

            cate = br.category

            self._excelsheet_create_dao.append([time, party, product, ty, cate])


    def save(self):
        self._excelsheet_create_dao.save()
        self._excelsheet_create_dao.close()



class ExcelSheetAppendService(ExcelSheetWriteService):

    def __init__(self,
                 excel_file: str,
                 index: int) -> None:

        self._excelsheet_append_dao = ExcelSheetAppendDao(excel_file, index)


    def append(self, data: BillList) -> None:
        for br in data:
            time = br.time
            party = br.party
            product = br.product

            if br.ty == -1:
                ty = 'outcome'
            elif br.ty == 0:
                ty = 'neutral'
            else:
                ty = 'income'

            cate = br.category

            self._excelsheet_append_dao.append([time, party, product, ty, cate])


    def save(self):
        self._excelsheet_append_dao.save()
        self._excelsheet_append_dao.close()
