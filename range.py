"""
range遍历解析
"""
class RangeInterator:
    def __init__(self, data):
        self.number = -1
        self.data = data


    def __next__(self):
        if self.number == self.data -1:
            raise StopIteration()
        self.number += 1
        return self.number




class MyRange:
    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        return RangeInterator(self.stop)


controller = MyRange(10)
interator = controller.__iter__()
while True:
    try:
        item = interator.__next__()
        print(item)
    except StopIteration:
        break

