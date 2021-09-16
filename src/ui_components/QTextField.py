from PyQt5.QtWidgets import QLineEdit


class QInputField(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(
            """
            QLineEdit {
                background-color: #fafafa;
                border: 1px solid #ccc;
                border-radius: 12px;
                padding: 12px 8px;
            }
        """
        )
