from model.bill_model import BillList
import copy
from src.classifier.classifier import Classifier


class ClassifyService:
    def __init__(self,
                 classifier: Classifier) -> None:

        self.classifier = classifier


    def run(self, data: BillList) -> BillList:
        res = self.classifier.classify([str(x) for x in data])

        bl = copy.deepcopy(data)
        for i in range(len(res)):
            bl[i].category = res[i]

        return bl
