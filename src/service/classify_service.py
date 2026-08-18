from model.bill_model import BillList
import copy
from src.classifier.classifier import Classifier

class ClassifyService:
    def __init__(self,
                 classifier: Classifier) -> None:
        self.classifier = classifier


    def run(self, data: BillList, category: list[str]) -> BillList:
        res = self.classifier.classify([str(i) for i in data], category)

        bl = copy.deepcopy(data)

        for i in range(len(data)):
            bl[i].category = res[i]

        return bl
