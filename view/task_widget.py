from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QCheckBox

class TaskWidget(QWidget):
    def __init__(self, task, completed, parent=None):
        super().__init__(parent)
        self.layout = QHBoxLayout(self)
        self.label = QLabel(task)
        self.checkbox = QCheckBox()
        self.checkbox.setChecked(completed)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.checkbox)
        self.setLayout(self.layout)
