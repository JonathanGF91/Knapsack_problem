from FileReader import FileReader
from Bag import Bag
from Tabulation import Tabulation

if __name__ == '__main__':

    file = FileReader("input-files\data_4")
    mochila = file.getBag()
    #print(type(mochila.getItems()[0][2]))
    Tabulation(mochila.getSize(), mochila.getMaxW(), mochila.getItems())
