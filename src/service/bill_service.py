from classifier.classifier import Classifier
from service.classify_service import ClassifyService
from src.service.excelsheet_service import ExcelSheetCreateService, ExcelSheetReadService
from src.model.excelsheet_model import ExcelSheetReadModel, ExcelSheetCreateModel


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


    def classify(self,
                 from_excel: ExcelSheetReadModel,
                 to_excel_path: str,
                 category: list[str],
                 classifier: Classifier) -> None:

        excel_read = ExcelSheetReadService(from_excel)
        excel_write = {x:ExcelSheetCreateService(ExcelSheetCreateModel(to_excel_path, x)) for x in category}
        cls_service = ClassifyService(classifier)

        it = excel_read.load(30)

        while True:
            try:
                bl = next(it)
            except StopIteration:
                break

            res = cls_service.run(bl)

            for i in res:
                excel_write[i.category].append(i)

        for i in excel_write.values():
            i.save()
