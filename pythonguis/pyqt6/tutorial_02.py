import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checkled = True

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(400,300))

        button = QPushButton("Press Me")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self, checked):
        print(self.button_is_checkled)
        self.button_is_checkled = checked
        print("Checked?", checked)
        print(self.button_is_checkled)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
