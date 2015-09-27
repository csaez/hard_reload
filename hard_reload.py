#!/usr/bin/env python
import sys
from PySide import QtGui, QtCore


class HardReload(QtGui.QDialog):

    def __init__(self, parent=None):
        super(HardReload, self).__init__(parent)
        self.setWindowTitle("Hard Reload")

        self.ui_lineEdit = QtGui.QLineEdit(self)
        ui_completer = QtGui.QCompleter(
            [i.split(".")[0] for i in sys.modules.keys()], self)
        ui_completer.setCompletionMode(QtGui.QCompleter.InlineCompletion)
        ui_completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui_lineEdit.setCompleter(ui_completer)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.ui_lineEdit)
        self.setLayout(hbox)

        self.ui_lineEdit.returnPressed.connect(self.accept)

    def move_window(self, pos=None):
        pos = pos or QtGui.QCursor.pos()
        self.move(pos.x(), pos.y())

    def accept(self, *args, **kwds):
        module_name = str(self.ui_lineEdit.text())
        if len(module_name):
            hard_reload(module_name)
        super(HardReload, self).close(*args, **kwds)


def get_parent():
    parent = QtGui.QApplication.activeWindow()
    if parent:
        _ = parent.parent()
        while _:
            parent = _
            _ = parent.parent()
    return parent


def hard_reload(module_name):
    for k in sys.modules.keys():
        if k.startswith(module_name):
            del sys.modules[k]


def show():
    w = HardReload(get_parent())
    w.move_window()
    w.exec_()


def __main__():
    QtGui.QApplication(sys.argv)
    show()
    sys.exit()


if __name__ == "__main__":
    __main__()
