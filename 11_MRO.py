class SimpleList:
    def __init__(self, items):
        self.items = list(items)

    def add(self, item):
        self.items.append(item)

    def __getitem__(self, index):
        return self.items[index]
    
    def sort(self):
        self.items.sort()

    def __len__(self):
        return len(self.items)
    
    def __repr__(self):
        return f"{type(self).__name__}({self.items!r})"


class SortedList(SimpleList):
    def __init__(self, items):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()


class IntList(SimpleList):
    def __init__(self, items = ()):
        for x in items: self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only supports integer values.')
        
    def add(self, item):
        self._validate(item)
        super().add(item)


class SortedIntList(IntList, SortedList):
    pass


def main():
    try:
        sil = SortedIntList([42, 23, 3])
        sil.add(-1234)
        print(sil)
    except BaseException as e:
        print(type(e), e)

    try:
        sil2 = SortedIntList([3, 2, '1'])
    except BaseException as e:
        print(type(e), e)

    try:
        sil = SortedIntList([42, 23, 3])
        sil.add('Something new')
    except BaseException as e:
        print(type(e), e)


if __name__ == '__main__' :
    main()