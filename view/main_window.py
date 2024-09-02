from PyQt6.QtWidgets import QMainWindow, QPushButton, QListView, QVBoxLayout
from PyQt6.QtCore import QSize, Qt

# from controller.task_delegate import TaskDelegate
# import sys


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         # When you subclass a Qt class you must always call the super __init__ function to allow Qt to set up the object.

#         self.setWindowTitle("todo-app-vee")
#         self.button_is_checked = True

#         button = QPushButton("my todo")
#         button.setCheckable(True) # button can be made toggable, has checked attribute
#         # when an event is sent to the handler, handler can receive checked property
        
#         # tabBar = QTabBar()

#         # button.pressed.connect(self.update_title) # when a button is pressed action happens
#         # another way to do this is to use released handler, to have action happening when button is released
#         button.released.connect(self.update_title)
        
#         button.clicked.connect(self.the_button_was_toggled)

#         self.setMinimumSize(QSize(400, 300)) # setMaximumSize(), setFixedSize() work on any widget

#         self.setCentralWidget(button)
    
#     def update_title(self):
#         self.setWindowTitle("someting wong")

#     def the_button_was_toggled(self, checked):
#         self.button_is_checked = checked # store the property of the button into a variable


# class MainWindow(QMainWindow):
#     def __init__(self, model):
#         super().__init__()
#         self.model = model
#         # When you subclass a Qt class you must always call the super __init__ function to allow Qt to set up the object.
#         self.setMinimumSize(QSize(400, 300)) # setMaximumSize(), setFixedSize() work on any widget
#         self.setWindowTitle("todo-app-vee")

#         layout = QVBoxLayout()

#         listView = QListView()
#         listView.setItemDelegate(TaskDelegate())

#         button = QPushButton("new Task")
#         button.clicked.connect(self.the_button_clicked)

#         # Assemble the general layout
#         layout.

#         self.setCentralWidget(layout)

#     def the_button_clicked(self):
#         self.model.addTask("This is new task")


from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QListView, QPushButton, QLineEdit
from PyQt6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
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

        # Initialize delegate for listView
        # self.listView.setItemDelegate(TaskDelegate())
        self.listView.setModel(self.model)

        outer_layout.addWidget(self.listView)

        # Create and add the QPushButton to the second_layout
        new_task_button = QPushButton("New Task")
        self.task_input = QLineEdit()

        # Set up connection for the button
        new_task_button.clicked.connect(self.the_button_clicked)

        # Add task_input and button to the second layout
        input_button_container = QWidget()

        second_layout.addWidget(new_task_button)
        second_layout.addWidget(self.task_input)
        
        input_button_container.setLayout(second_layout)
        outer_layout.addWidget(input_button_container)

        # Set the layout on the container widget
        container.setLayout(outer_layout)

        # Set the container widget as the central widget of the main window
        self.setCentralWidget(container)

    def the_button_clicked(self):
        # Take user input and clear the input field
        self.model.addTask(self.task_input.text())
        self.task_input.clear()
