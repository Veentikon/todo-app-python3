from PyQt6.QtCore import QAbstractListModel, Qt, QModelIndex


class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description


class TasksModel(QAbstractListModel):
    def __init__(self, tasks=None):
        super().__init__()
        self.tasks = tasks or []

    def rowCount(self, parent=QModelIndex()):
        return len(self.tasks)

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.tasks[index.row()]['task']
        elif role == Qt.ItemDataRole.CheckStateRole:
            return self.tasks[index.row()]['completed']

    def addTask(self, task):

        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.tasks.append({'task': task, 'completed': False})

        print("after: ", self.tasks)

        self.endInsertRows()


