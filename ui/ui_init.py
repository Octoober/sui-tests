from PyQt6.QtWidgets import (QApplication,
                             QWidget,
                             QMainWindow,
                             QPushButton,
                             QVBoxLayout,
                             QHeaderView,
                             QTableWidget, QTableWidgetItem)
from PyQt6.QtCore import QSize

from helpers import get_wallets


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Wallets")

        wallets = get_wallets()

        table = QTableWidget()
        table.setRowCount(len(wallets))
        table.setColumnCount(2)

        table.setHorizontalHeaderLabels(['Account', 'Recovery phrase'])
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode(1))

        for row, wallet in enumerate(wallets):
            for column, item in enumerate(wallet.values()):
                table.setItem(row, column, QTableWidgetItem(item))

        v_box = QVBoxLayout()
        v_box.addWidget(table)

        self.setLayout(v_box)


def init():
    app = QApplication([])
    window = MainWindow()
    window.showMaximized()
    window.setMinimumSize(QSize(768, 550))
    window.show()

    app.exec()
