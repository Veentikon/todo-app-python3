from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QListView, QPushButton, QLineEdit
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QAbstractItemView
# from controller.task_delegate import TaskDelegate


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setMinimumSize(QSize(400, 300))
#         self.setWindowTitle("todo-app-vee")

#         # Create a QWidget to act as a container for the layout
#         container = QWidget()
        
#         # Create the QVBoxLayout for ListView and button/input field
#         outer_layout = QVBoxLayout()
#         # Create the QHBoxLayout for text input field and a button
#         second_layout = QHBoxLayout()
        
#         # Create and add the QListView to the layout
#         self.listView = QListView()

#         # Initialize delegate for listView
#         # self.listView.setItemDelegate(TaskDelegate())
#         # self.listView.setModel(self.model)

#         outer_layout.addWidget(self.listView)

#         # Create and add the QPushButton to the second_layout
#         new_task_button = QPushButton("New Task")
#         self.task_input = QLineEdit()

#         # Set up connection for the button
#         new_task_button.clicked.connect(self.the_button_clicked)

#         # Add task_input and button to the second layout
#         input_button_container = QWidget()

#         second_layout.addWidget(new_task_button)
#         second_layout.addWidget(self.task_input)
        
#         input_button_container.setLayout(second_layout)
#         outer_layout.addWidget(input_button_container)

#         # Set the layout on the container widget
#         container.setLayout(outer_layout)

#         # Set the container widget as the central widget of the main window
#         self.setCentralWidget(container)

#     def the_button_clicked(self):
#         # Take user input and clear the input field
#         self.model.addTask(self.task_input.text())
#         self.task_input.clear()

#     def setItemDelegate(self, delegate):
#         self.listView.setItemDelegate(delegate)

#     def setModel(self, model):
#         self.model = model
#         self.listView.setModel(model)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("todo-app-vee")

        # Create a QWidget to act as a container for the layout
        container = QWidget()
        
        # Create the QVBoxLayout for ListView and button/input field
        outer_layout = QVBoxLayout()
        # Create the QHBoxLayout for text input field and a button
        second_layout = QHBoxLayout()
        
        # Create and add the QListView to the layout
        self.listView = QListView()

        # Settings for ListView, make it editeble
        self.listView.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked | QAbstractItemView.EditTrigger.SelectedClicked)

        # Create and add the QPushButton to the second_layout
        new_task_button = QPushButton("New Task")
        self.task_input = QLineEdit()

        # Set up connection for the button
        new_task_button.clicked.connect(self.new_task_action)

        # Add task_input and button to the second layout
        second_layout.addWidget(self.task_input)
        second_layout.addWidget(new_task_button)
        outer_layout.addWidget(self.listView)
        outer_layout.addLayout(second_layout)

        # Set the layout on the container widget
        container.setLayout(outer_layout)

        # Set the container widget as the central widget of the main window
        self.setCentralWidget(container)

    def new_task_action(self):
        task_text = self.task_input.text()
        if task_text:  # Ensure the task is not empty
            new_task = {'task': task_text, 'completed': False}
            self.model.addTask(new_task)
            self.task_input.clear()
            self.listView.update()  # Force view update

    def setItemDelegate(self, delegate):
        self.listView.setItemDelegate(delegate)
        print("ListView delegate set")

    def setModel(self, model):
        self.model = model
        self.listView.setModel(model)
