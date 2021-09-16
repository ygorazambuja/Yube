from PyQt5.QtWidgets import QPushButton


class QButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setObjectName(text)
        self.setStyleSheet(
            """
            QPushButton {
                background-color: #f5f5f5;
                border: 1px solid #d5d5d5;
                border-radius: 12px;
                color: #333;
                font-size: 16px;
                padding: 12px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e6e6e6;
            }
            QPushButton:pressed {
                background-color: #d5d5d5;
            }
        """
        )
