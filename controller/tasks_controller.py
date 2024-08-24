import sys
import os

# # Add the model and view directories to sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'view')))

from model.task_model import TasksModel, Task
from view.task_view import TaskView

class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self, title, description):
        new_task = Task(title, description)
        self.model.addTask(new_task)

def main():
    app = QApplication([])
    model = TasksModel([Task("Task 1", "Description 1"), Task("Task 2", "Description 2")])
    view = TaskView(model)
    controller = TaskController(model, view)
    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
