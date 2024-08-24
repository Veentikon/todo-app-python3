from PyQt6.QtWidgets import QApplication, QListView
from ..model.tasks_model import TasksModel, Task


def add_task():
    new_task = Task("New Task", "New Description")
    model.addTask(new_task)


app = QApplication([])

view = QListView()
model = TasksModel([Task("Task 1", "Description 1"), Task("Task 2", "Description 2")])
view.setModel(model)
view.show()

app.exec()