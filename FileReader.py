from Bag import Bag

class FileReader:
    fileName = ""
    path = ""
    mochila = Bag()

    def __init__(self, route):
        try:
            file = open(route, "r")
            self.getData(file)
        except IOError:
            print("File not accessible or file not found")
        finally:
            file.close()

    def getData(self, file):
        flag = True
        i = 0
        for line in file:
            x = line.split()
            if flag:
                self.mochila.setSize(x[0])    #number of items
                self.mochila.setMaxW(x[1])    #maximun bag size
                flag = False
            else:
                self.mochila.addItem(i, x[0], x[1])  #(index, item value, item weight)
            i += 1

    def getBag(self):
        return self.mochila