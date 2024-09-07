from PyQt6.QtWidgets import QStyledItemDelegate
from view.task_widget import TaskWidget
from PyQt6.QtCore import Qt


class TaskDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        task_data = index.data(Qt.ItemDataRole.UserRole)
        editor = TaskWidget(task_data['task'], task_data['completed'], parent)
        print("Editor created")
        return editor

    def setEditorData(self, editor, index):
        task_data = index.data(Qt.ItemDataRole.UserRole)
        editor.label.setText(task_data['task'])
        editor.checkbox.setChecked(task_data['completed'])
        print("Editor data set")

    def setModelData(self, editor, model, index):
        task_data = {
            'task': editor.label.text(),
            'completed': editor.checkbox.isChecked()
        }
        model.setData(index, task_data, Qt.ItemDataRole.UserRole)
        print("Model data set")

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
