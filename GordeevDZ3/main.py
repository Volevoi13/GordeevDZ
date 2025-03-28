from PyQt5 import QtWidgets
from file import Ui_MainWindow
import sys

class my_win(QtWidgets.QMainWindow):
    def __init__(self):
        super(my_win, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn.clicked.connect(self.btnClicked)

    def btnClicked(self):
        try:
            rost = float(self.ui.le2.text())
            ves = float(self.ui.le1.text())

            if 0 < rost < 250 and 0 < ves < 350:
                imt = ves / ((rost / 100) ** 2)
                self.ui.lbl3.setText(str(imt))
            else:
                self.ui.lbl3.setText('ошибка')
        except ValueError:
            self.ui.lbl3.setText('?')


app = QtWidgets.QApplication([])  # Создание приложения
window = my_win()
window.show()  # Показ окна

sys.exit(app.exec())

