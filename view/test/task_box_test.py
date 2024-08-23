from PyQt6 import QtCore, QtGui, QtWidgets
from view.task_box import TaskBox

# this code is for testing purposes
app = QtWidgets.QApplication([])
volume = TaskBox()
volume.show()
app.exec()