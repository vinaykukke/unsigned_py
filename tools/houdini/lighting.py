"""
Custom scripts to create basic lighting setup
"""
import hou
from PySide2 import QtUiTools, QtCore, QtWidgets   # type: ignore

class MyWidget(QtWidgets.QWidget):
    """
    q
    """
    def __init__(self):
        super(MyWidget,self).__init__()
        ui_file = "/Users/vinaykukke/Documents/Work/unsigned_py/tools/houdini/ui_asset.ui"
        self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget=self)
        self.setParent(hou.qt.mainWindow(), QtCore.Qt.Window) # type: ignore

def setup():
    """
    d
    """
    # Create an instance of the custom window
    win = MyWidget()
    win.show()
