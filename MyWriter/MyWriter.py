import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

from ext.mainTextEditor import MainTextEditor

class Main():
    def __init__(self):
        text = MainTextEditor()
        text.show()




def main():
    app = QtGui.QApplication(sys.argv)
    main= Main()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
