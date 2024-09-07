from PyQt6.QtCore import QAbstractListModel, Qt, QModelIndex


class TasksModel(QAbstractListModel):
    def __init__(self, tasks=None):
        super().__init__()
        self.tasks = tasks or []

    def rowCount(self, parent=QModelIndex()):
        return len(self.tasks)

    def data(self, index, role):
        if not index.isValid():
            return None
        if role == Qt.ItemDataRole.UserRole:
            return self.tasks[index.row()]
        return None

    def setData(self, index, value, role):
        if not index.isValid():
            return False
        if role == Qt.ItemDataRole.UserRole:
            self.tasks[index.row()] = value
        self.dataChanged.emit(index, index, [role])
        print(f"Data changed at row {index.row()}")
        return True

    def flags(self, index):
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsUserCheckable

    def addTask(self, task):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.tasks.append(task)
        self.endInsertRows()
