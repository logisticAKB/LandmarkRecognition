import sys
from PyQt5 import QtWidgets
from View.MainWindow import Ui_MainWindow


class App(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def resizeEvent(self, event):
        print("hi")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
