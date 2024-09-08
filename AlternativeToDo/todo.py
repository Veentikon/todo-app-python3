import sys
import json
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt


qt_ui_file = "todo_design2.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_ui_file)
tick = QtGui.QImage("tick.png")


class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, *args, todos=None, **kwargs): # where todos is a list of tuples [(bool, text),]
        super(TodoModel, self).__init__(*args, **kwargs)
        self.todos = todos or []
        
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            _, text = self.todos[index.row()]
            return text
        
        if role == Qt.ItemDataRole.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return tick

    def rowCount(self, index):
        return len(self.todos)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.model = TodoModel()
        self.load()
        self.listView.setModel(self.model)
        self.addTask.pressed.connect(self.add)
        self.removeTask.pressed.connect(self.remove)
        self.completeTask.pressed.connect(self.complete)

    def add(self):
        text = self.lineEdit.text()
        if text:
            self.model.todos.append((False, text))
            # Trigger refresh
            self.model.layoutChanged.emit()
            # Empty input
            self.lineEdit.clear()
            self.save()

    def remove(self):
        indexes = self.listView.selectedIndexes()
        if indexes:
            # Indexes is a list of a single item in single-select mode.
            index = indexes[0]
            # Remove the item and refresh.
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            # Clear the selection
            self.listView.clearSelection()
            self.save()

    def complete(self):
        indexes = self.listView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = [True, text]
            # .dataChanged takes top-left and bottom right, which are equal 
            # for a single selection.
            self.model.dataChanged.emit(index, index)
            # clear selection.
            self.listView.clearSelection()
            self.save()

    def load(self):
        try:
            with open('data.db', 'r') as f:
                self.model.todos = json.load(f)
        except Exception:
            pass

    def save(self):
        with open('data.db', 'w') as f:
            data = json.dump(self.model.todos, f)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()