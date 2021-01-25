
class Bag:

    maxW = 0
    nItems = 0
    cache = []

    def getSize(self):
        return self.nItems

    def setSize(self, nItems):
        self.nItems = nItems

    def getMaxW(self):
        return self.maxW

    def setMaxW(self, maxW):
        self.maxW = maxW

    def addItem(self, index, value, weight):
        item = (index, value, weight)
        self.cache.append(item)

    def getItem(self, index):
        return self.cache[index]

    def getItems(self):
        return self.cache