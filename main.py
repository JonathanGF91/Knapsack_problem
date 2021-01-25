from FileReader import FileReader
from Bag import Bag

if __name__ == '__main__':

    file = FileReader("input-files\data_4")
    mochila = file.getBag()
    for i in range (mochila.getSize()):
        print(mochila.getItem(i))
