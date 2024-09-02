from model.tasks_model import TasksModel
# from view.tasks_view import TaskView
# from controller.task_delegate import TaskDelegate
from PyQt6.QtWidgets import QApplication
from view.main_window import MainWindow

import sys

def main():
    app = QApplication(sys.argv)

    model = TasksModel()
    view = MainWindow(model)
    # listViewDelegate = TaskDelegate() # has been initialized during main window creation

    view.show()
    
    # Exit program upon press on 'x' button
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


