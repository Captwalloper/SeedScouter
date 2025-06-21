import sys, os, psutil
from time import sleep
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QTextEdit

from app.assets import Icon
from app.keybind.keybind import ScouterBinds, Keybind as KB

binds = ScouterBinds(
    restartHD2="f8",
)

def restart_HD2():
    hd2_process = None
    for proc in psutil.process_iter():
        if proc.name() == 'helldivers2.exe':
            hd2_process = proc
    if (hd2_process != None):
        hd2_process.kill()
        sleep(2)
    os.system('start steam://rungameid/553850')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SeedScouter")

        control_layout = QHBoxLayout()
        self.restartButton = QPushButton("(Re)Start")
        control_layout.addWidget(self.restartButton)
        self.restartButton.clicked.connect(restart_HD2)

        # log_layout = QVBoxLayout()
        # self.log = QTextEdit()
        # self.log.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        # self.log.setReadOnly(True)
        # log_layout.addWidget(self.log)

        outer_layout = QVBoxLayout()
        outer_layout.addLayout(control_layout)
        # outer_layout.addLayout(log_layout)
        window = QWidget()
        window.setLayout(outer_layout)
        self.setCentralWidget(window)
    
app = QApplication(sys.argv)
app.setWindowIcon(QIcon(Icon.blitz))
window = MainWindow()
window.show()

KB.SetupKeybinds([
    KB(binds.restartHD2, restart_HD2),
])

app.exec()