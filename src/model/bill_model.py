import datetime

class BillRecord:
    def __init__(self,
                 time: datetime.datetime,
                 party: str,
                 product: str,
                 ty: int,
                 value: float,
                 category: None | str = None):
        self.time = time
        self.party = party
        self.product = product
        self.ty = ty
        self.value = value
        self.category = category


    def __str__(self):
        string: str = ''
        string += 'time: ' + self.time.isoformat() + ', '
        string += 'party: ' + self.party + ', '
        string += 'product: ' + self.product + ', '

        string += 'ty: '

        if self.ty == -1:
             string += 'expense'
        elif self.ty == 1:
            string += 'income'
        elif self.ty == 0:
            string += 'neutral'

        string += ', '

        string += 'value: ' + f'{self.value:.2f}'

        if self.category is not None:
            string += ', ' + 'category: '  + self.category

        return string



class BillList:
    def __init__(self, bills: list[BillRecord] | None = None):
        self._bills: list[BillRecord] = []

        if bills is not None:
            self._bills = bills
            self.len = len(bills)


    def add(self, record: BillRecord):
        self._bills.append(record)


    def delete(self, index: int | None = None):
        if index is not None:
            self._bills.pop(index)
        else:
            self._bills.pop()


    def __getitem__(self, index: int) -> BillRecord:
        return self._bills[index]

    def __setitem__(self, index: int, value: BillRecord) -> None:
        self._bills[index] = value


    def __len__(self) -> int:
        return len(self._bills)


    def __iter__(self):
        return BillListIterator(self._bills)



class BillListIterator:
    def __init__(self, bills: list[BillRecord]):
        self._bills: list[BillRecord] = bills
        self.current: int = -1


    def __iter__(self):
        return self


    def __next__(self):
        self.current += 1

        if self.current < len(self._bills):
            return self._bills[self.current]
        else:
            raise StopIteration
