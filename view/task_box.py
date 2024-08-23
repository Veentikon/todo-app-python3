from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class _Task(QtWidgets.QWidget):
    pass

class TaskBox(QtWidgets.QWidget):
    """
    Custom Qt Widget to show a power bar and dial.
    Demonstrating compound and custom-drawn widget.
    """

    def __init__(self, steps=5, *args, **kwargs):
        super(TaskBox, self).__init__(*args, **kwargs)

        layout = QtWidgets.QHBoxLayout()
        self._bar = _Task()
        layout.addWidget(self._bar)

        self._taskText = QtWidgets.QLabel("something wong")
        self._checkBox = QtWidgets.QCheckBox()
        layout.addWidget(self._taskText)
        layout.addWidget(self._checkBox)

        self.setLayout(layout)
