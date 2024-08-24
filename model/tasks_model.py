# from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QAbstractListModel, Qt, QModelIndex


class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description


class TasksModel(QAbstractListModel):

    def __init__(self, tasks=None):
        super().__init__()
        self.tasks = tasks or []

    #TODO
    # implement the following three functions
    """Returns the number of rows under the given parent. 
    When the parent is valid it means that rowCount is returning the number of children of 
    parent."""
    def rowCount(self, parent=QModelIndex()):
        return len(self.tasks)
    
    """Returns the data stored under the given role for the item referred to by the index.
    const QModelIndex &index, int role = Qt::DisplayRole"""
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < len(self.tasks)):
            return None
        task = self.tasks[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:
            return task.title
        return None

    def addTask(self, task):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.tasks.append(task)
        self.endInsertRows()

    def headerData():
        pass


