import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import (
    QApplication,
    QFormLayout,
    QMainWindow,
    QMessageBox,
    QWidget,
    QLabel,
)
from pytube import YouTube
from pathlib import Path

from ui_components.QButton import QButton
from ui_components.QTextField import QInputField


class ErrorBox(QMessageBox):
    def __init__(self, errorInfo="Erro", errorTitle="Erro"):
        super().__init__()
        msg = QMessageBox()
        msg.setText(errorInfo)
        msg.setWindowTitle(errorTitle)
        msg.exec_()


class SuccessBox(QMessageBox):
    def __init__(self, successInfo="Sucesso", successTitle="Sucesso"):
        super().__init__()
        msg = QMessageBox()
        msg.setText(successInfo)
        msg.setWindowTitle(successTitle)
        msg.exec_()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yube")

        self.layout = QFormLayout()

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
        self.layout.setContentsMargins(50, 30, 30, 50)

        self.render_ui_components()
        self.show()

    def render_ui_components(self):
        label = QLabel("<h1>Yube!</h1>")

        self.linkInput = QInputField(self)
        self.pasteButton = QButton("Colar")
        self.downloadButton = QButton("Download")
        self.downloadButton.clicked.connect(self.handle_download_video)
        self.pasteButton.clicked.connect(self.get_text_from_clipboard)
        self.layout.addRow(label)
        self.layout.addRow(self.linkInput)
        self.layout.addRow(self.pasteButton)
        self.layout.addRow(self.downloadButton)

    def change_file_extension(self, title):
        try:
            p = Path(title + ".mp4")
            p.rename(p.with_suffix(".mp3"))
        except Exception as e:
            print(e)
            ErrorBox(errorInfo="Error na Transformação, baixado como video")
        finally:
            SuccessBox(successInfo="Download concluído")

    def handle_download_video(self):
        try:
            yt = YouTube(self.linkInput.text())
            yt.streams.get_audio_only().download()

        except:
            ErrorBox(errorInfo="Erro no download")
            return

        self.change_file_extension(yt.title)

    def get_text_from_clipboard(
        self,
    ):
        try:
            paste = QGuiApplication.clipboard().text()
        except:
            ErrorBox(errorInfo="Erro ao acessar o Clipboard")
            return
        self.set_pasted_on_line_input(paste)

    def set_pasted_on_line_input(self, pasted):
        self.linkInput.setText(pasted)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
