# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from View.waitingspinnerwidget import QtWaitingSpinner


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 715)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setTextFormat(QtCore.Qt.MarkdownText)
        self.image.setScaledContents(False)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setWordWrap(False)
        self.image.setObjectName("image")
        self.image.setMinimumSize(1, 1)
        self.verticalLayout.addWidget(self.image)
        self.answer = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer.sizePolicy().hasHeightForWidth())
        self.answer.setSizePolicy(sizePolicy)
        self.answer.setMinimumSize(QtCore.QSize(0, 25))
        self.answer.setTextFormat(QtCore.Qt.MarkdownText)
        self.answer.setScaledContents(False)
        self.answer.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.answer.setOpenExternalLinks(True)
        self.answer.setObjectName("answer")
        self.verticalLayout.addWidget(self.answer)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openImage = QtWidgets.QPushButton(self.centralwidget)
        self.openImage.setEnabled(True)
        self.openImage.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.openImage.setObjectName("openImage")
        self.horizontalLayout.addWidget(self.openImage)
        self.findLabel = QtWidgets.QPushButton(self.centralwidget)
        self.findLabel.setEnabled(False)
        self.findLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.findLabel.setObjectName("findLabel")
        self.horizontalLayout.addWidget(self.findLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.about = QtWidgets.QAction(MainWindow)
        self.about.setObjectName("about")
        self.open = QtWidgets.QAction(MainWindow)
        self.open.setObjectName("open")
        self.exit = QtWidgets.QAction(MainWindow)
        self.exit.setObjectName("exit")
        self.recognize = QtWidgets.QAction(MainWindow)
        self.recognize.setObjectName("recognize")
        self.exportToJson = QtWidgets.QAction(MainWindow)
        self.exportToJson.setObjectName("exportToJson")

        self.spinner = QtWaitingSpinner(self.image)
        self.spinner.setNumberOfLines(30)
        self.spinner.setInnerRadius(15)
        self.spinner.setLineLength(15)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Landmark Recognition"))
        self.image.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Museo Sans Cyrl\',\'Arial\',\'sans-serif\'; font-size:15pt; color:#b0b0b0;\">In order to start open image</span></p><p><br/></p></body></html>"))
        self.answer.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Museo Sans Cyrl\',\'Arial\',\'sans-serif\'; font-size:10pt;\"></span><a href=\"http://stackoverflow.com/\"><span style=\" font-family:\'Museo Sans Cyrl\',\'Arial\',\'sans-serif\'; font-size:10pt; text-decoration: underline; color:#0000ff;\"></span></a></p></body></html>"))
        self.openImage.setText(_translate("MainWindow", "Open image"))
        self.findLabel.setText(_translate("MainWindow", "Recognize"))
        self.about.setText(_translate("MainWindow", "О программе"))
        self.open.setText(_translate("MainWindow", "Открыть изображение"))
        self.exit.setText(_translate("MainWindow", "Выход"))
        self.recognize.setText(_translate("MainWindow", "Найти метки"))
        self.exportToJson.setText(_translate("MainWindow", "Экспорт в JSON"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
