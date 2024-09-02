from PyQt6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem, QCheckBox
from PyQt6.QtCore import Qt, QRect

class TaskDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        task = index.data()
        rect = option.rect

        # Draw the text
        painter.drawText(rect, Qt.AlignmentFlag.AlignLeft, task)

        # Draw the checkbox
        checkbox_rect = QRect(rect.right() - 20, rect.top(), 20, rect.height())
        checkbox = QCheckBox()
        checkbox.setChecked(False)
        checkbox.setGeometry(checkbox_rect)
        checkbox.render(painter)

