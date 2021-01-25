
class Bag:

    maxW = 0
    nItems = 0
    cache = []

    def getSize(self):
        return self.nItems

    def setSize(self, nItems):
        self.nItems = int(nItems)

    def getMaxW(self):
        return self.maxW

    def setMaxW(self, maxW):
        self.maxW = int(maxW)

    def addItem(self, index, value, weight):
        item = (index, int(value), int(weight))
        self.cache.append(item)

    def getItem(self, index):
        return self.cache[index]