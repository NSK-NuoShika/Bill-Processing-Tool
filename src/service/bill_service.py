from src.dao.excel_merge_dao import ExcelMergeDao
from src.model.bill_model import BillList
from src.classifier.classifier import Classifier
from src.service.classify_service import ClassifyService
from src.service.excelsheet_service import ExcelSheetCreateService, ExcelSheetReadService
from src.model.excelsheet_model import ExcelSheetReadModel, ExcelSheetCreateModel
import uuid
import os

class BillService:

    def merge(self,
              from_excel: list[ExcelSheetReadModel],
              to_excel: ExcelSheetCreateModel):

        excel_write = ExcelSheetCreateService(to_excel)

        for e in from_excel:
            excel_read = ExcelSheetReadService(e)
            it = excel_read.load(1000)

            while True:
                try:
                    excel_write.append(next(it))
                except StopIteration:
                    break

        excel_write.save()


    def classify(self,
                 from_excel: ExcelSheetReadModel,
                 to_excel_path: str,
                 category: list[str],
                 classifier: Classifier) -> None:

        excel_read = ExcelSheetReadService(from_excel)
        tmp_to_excel = dict()

        for cate in category:
            u = uuid.uuid4()
            tmp_to_excel[cate] = (ExcelSheetCreateService(ExcelSheetCreateModel(f'{u}.xlsx', cate)),
                                  f'{u}.xlsx')


        cls_service = ClassifyService(classifier)

        it = excel_read.load(30)

        while True:
            try:
                bl = next(it)
            except StopIteration:
                break

            res = cls_service.run(bl)

            for i in res:
                t = BillList()
                t.add(i)
                tmp_to_excel[i.category][0].append(t)

        excel_merge_dao = ExcelMergeDao(to_excel_path)
        for k, v  in tmp_to_excel.items():
            v[0].save()
            excel_merge_dao.merge(v[1])
            os.remove(v[1])

        excel_merge_dao.save()
