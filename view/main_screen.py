from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QTabBar
from PyQt6.QtCore import QSize, Qt

import sys


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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # When you subclass a Qt class you must always call the super __init__ function to allow Qt to set up the object.
        self.setMinimumSize(QSize(400, 300)) # setMaximumSize(), setFixedSize() work on any widget
        self.setWindowTitle("todo-app-vee")

        # self.button = QPushButton("my todo")
        # self.button.released.connect(self.the_button_clicked)
        # self.setCentralWidget(self.button)

        layout = QtWidgets.QVBoxLayout()
        listView = QtWidgets.QListView()
    
    def the_button_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()