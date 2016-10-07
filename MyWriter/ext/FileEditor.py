
import sys
from PyQt4 import QtGui,QtCore
from PyQt4 import Qt
from PyQt4.QtGui import QTextEdit
class FileEditor(QTextEdit):
    def __init__( self, parent=None ):
            super(FileEditor, self).__init__(parent)
            self.setAcceptDrops(True)

    def dragEnterEvent( self, event ):
        data = event.mimeData()
        urls = data.urls()
        if ( urls and urls[0].scheme() == 'file' ):
            event.acceptProposedAction()

    def dragMoveEvent( self, event ):
        data = event.mimeData()
        urls = data.urls()
        if ( urls and urls[0].scheme() == 'file' ):
            event.acceptProposedAction()

    def dropEvent( self, event ):
        data = event.mimeData()
        urls = data.urls()
        if ( urls and urls[0].scheme() == 'file' ):
            # for some reason, this doubles up the intro slash
            filepath = str(urls[0].path())[1:]
            self.setText(filepath)
def main():
    app = QtGui.QApplication(sys.argv)

    main = FileEditor()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
