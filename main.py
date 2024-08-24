from model.tasks_model import TasksModel, Task
from view.tasks_view import TaskView
from controller.tasks_controller import TasksController

def main():
    app = QApplication([])
    model = TasksModel([Task("Task 1", "Description 1"), Task("Task 2", "Description 2")])
    view = TaskView(model)
    controller = TaskController(model, view)
    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


