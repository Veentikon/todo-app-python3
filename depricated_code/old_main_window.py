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