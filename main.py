import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTextEdit, QFileDialog, \
    QButtonGroup, QRadioButton
from transcribe import Whisper


class UrlDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.url_label = QLabel("Enter URL:")
        self.url_input = QLineEdit()

        # Radio buttons for selecting the model
        self.model_group = QButtonGroup()
        self.tiny_button = QRadioButton("Tiny")
        self.base_button = QRadioButton("Base")
        self.small_button = QRadioButton("Small")
        self.medium_button = QRadioButton("Medium")
        self.large_button = QRadioButton("Large")
        self.model_group.addButton(self.tiny_button)
        self.model_group.addButton(self.base_button)
        self.model_group.addButton(self.small_button)
        self.model_group.addButton(self.medium_button)
        self.model_group.addButton(self.large_button)
        self.model_group.setExclusive(True)
        self.tiny_button.setChecked(True)

        self.load_button = QPushButton("Load")
        self.load_button.clicked.connect(self.load_url)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_text)

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.tiny_button)
        layout.addWidget(self.base_button)
        layout.addWidget(self.small_button)
        layout.addWidget(self.medium_button)
        layout.addWidget(self.large_button)
        layout.addWidget(self.load_button)
        layout.addWidget(self.text_area)
        layout.addWidget(self.save_button)

        self.setLayout(layout)
        self.setWindowTitle("Youtube Transcriber")
        self.show()

    def load_url(self):
        if os.path.isfile('audio.mp3'):
            os.remove('audio.mp3')
        selected_model = self.model_group.checkedButton().text()
        url = self.url_input.text()
        w = Whisper(selected_model.lower())
        if url.endswith('.mp3'):
            w.download_mp3(url)
            self.text_area.setText(w.transcribe())
        else:
            w.download_video(url)
            self.text_area.setText(w.transcribe())

    def save_text(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Text", "",
                                                   "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'w') as f:
                f.write(self.text_area.toPlainText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = UrlDisplay()
    sys.exit(app.exec_())

