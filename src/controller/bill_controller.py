from classifier.llmclassifier import LLMClassifier
from service.bill_service import BillService
from service.config_service import ConfigService
from model.excelsheet_model import ExcelSheetReadModel, ExcelSheetCreateModel


class BillController:

    def merge(self,
              from_excel: list[ExcelSheetReadModel],
              to_excel: ExcelSheetCreateModel) -> None:

        BillService().merge(from_excel, to_excel)


    def classify(self,
                 classifier: str,
                 from_excel: ExcelSheetReadModel,
                 to_excel_file: str):

        config = ConfigService().load()

        if classifier == "llmclassifier":
            bill_service = BillService()
            bill_service.classify(from_excel,
                                  to_excel_file,
                                  config.billconfig.category,    # type: ignore
                                  LLMClassifier(config.llmconfig.url,    # type: ignore
                                                config.llmconfig.key,    # type: ignore
                                                config.llmconfig.model,    # type: ignore
                                                config.promptconfig.sys_prompt,    # type: ignore
                                                config.promptconfig.user_prompt,    # type: ignore
                                                config.billconfig.category))    # type: ignore
