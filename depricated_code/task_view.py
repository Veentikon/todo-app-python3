# from PyQt6 import QtCore, QtGui, QtWidgets
# from PyQt6.QtCore import Qt

# from PyQt6.QtWidgets import QApplication


# class _Task(QtWidgets.QWidget):
#     pass

# class TaskBox(QtWidgets.QWidget):
#     """
#     Custom Qt Widget to show a power bar and dial.
#     Demonstrating compound and custom-drawn widget.
#     """

#     # id is used by view to retreive information stored in the model
#     def __init__(self, task_id, steps=5, *args, **kwargs):
#         self._task_id = task_id
#         super(TaskBox, self).__init__(*args, **kwargs)

#         layout = QtWidgets.QHBoxLayout()
#         self._bar = _Task()
#         layout.addWidget(self._bar)

#         # self._taskText = QtWidgets.QLabel("something wong")
#         self._checkBox = QtWidgets.QCheckBox()
#         layout.addWidget(self._taskText)
#         layout.addWidget(self._checkBox)

#         self.setLayout(layout)
    
#     def _set_task_title(self, taskTitle):
#         self._taskText.setText(taskTitle)

#     def _set_complete(self):
#         # the idea is to cross out the text in the task so that it is marked complete while still being visible
#         pass
    
#     def _delete_task(self):
#         # signal to the model that a task must be deleted when a checkbox/button is pressed
#         pass


# is there a need for a function to change the title of a task?
# this view is updated whenever a model changes, a task is either added or removed
# therefore the title is set when the task is created and is never changed
# unless we add a fancy way of crossing a task out instead of checkbox where a task
# is still visible but is crossed out

# should it have associated id tied to it by which a specific view object can refer to its
# corresponding model?

# currently tasks are stored in a list and are identified by their ids
#   What happens when a task is deleted? is the list reshuffled? in that case the
# tasks need to be reassigned ids? can I solve this with a list or is it better to use a dictionary?

# need a mechanism of assigning ids to tasks upon creation
# will later modify model to use SQLite or JSON instead of a dictionary, which make it possible to have
# persistent memory

# # Code for testing purposes
# app = QtWidgets.QApplication([])
# taskView = TaskBox("Some task")
# taskView.show()
# app.exec()
