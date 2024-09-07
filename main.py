# from PyQt6.QtWidgets import QApplication
# import sys

# from view.main_window import MainWindow
# from controller.task_delegate import TaskDelegate
# from model.tasks_model import TasksModel


# def main():
#     app = QApplication(sys.argv)

#     # Initialize model view and delegate
#     model = TasksModel()
#     view = MainWindow()
#     delegate = TaskDelegate()

#     # Connect model view and delegate
#     view.setModel(model)
#     view.setItemDelegate(delegate)

#     # Show the interface
#     view.show()
    
#     # Exit program upon press on 'x' button
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()



from PyQt6.QtWidgets import QApplication
import sys

from view.main_window import MainWindow
from controller.task_delegate import TaskDelegate
from model.tasks_model import TasksModel


def main():
    app = QApplication(sys.argv)

    # Initialize model, view, and delegate
    model = TasksModel()
    view = MainWindow()
    delegate = TaskDelegate()

    # Connect model, view, and delegate
    view.setModel(model)
    view.setItemDelegate(delegate)

    # Show the interface
    view.show()
    
    # Exit program upon press on 'x' button
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
