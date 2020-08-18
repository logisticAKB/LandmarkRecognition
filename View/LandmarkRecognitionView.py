import os
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QPoint

from Utility.LandmarkRecognitionObserver import LandmarkRecognitionObserver
from Utility.LandmarkRecognitionMeta import LandmarkRecognitionMeta
from View.MainWindow import Ui_MainWindow


class Thread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, mController):
        QThread.__init__(self)
        self.mController = mController

    def run(self):
        self.mController.predictLandmark()
        self.signal.emit('predictionCompleted')


class LandmarkRecognitionView(QtWidgets.QMainWindow, LandmarkRecognitionObserver, metaclass=LandmarkRecognitionMeta):
    """
    Класс отвечающий за визуальное представление LandmarkRecognitionModel.
    """
    def __init__(self, inController, inModel, parent=None):
        """
        Конструктор принимает ссылки на модель и контроллер.
        """
        super(QtWidgets.QMainWindow, self).__init__(parent)
        self.mController = inController
        self.mModel = inModel

        # подключаем визуальное представление
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # создаем поток для обработки изображения
        self.thread = Thread(self.mController)

        # регистрируем представление в качестве наблюдателя
        self.mModel.addObserver(self)

        # связываем события нажания кнопок
        self.ui.openImage.clicked.connect(self.showFileDialog)
        self.ui.findLabel.clicked.connect(self.predictButtonClicked)

        # и сигнал окончания обработки изображения
        self.thread.signal.connect(self.predictFinished)

    def modelIsChanged(self):
        """
        Метод вызывается при изменении модели.
        Запрашивает и отображает значение метки.
        """
        prediction = self.mController.getPrediction()
        predictionStatus = self.mController.getPredictionStatus()

        if predictionStatus == self.mModel.NOT_PREDICTED:
            text = ''
        elif predictionStatus == self.mModel.PREDICTED_NOT_LANDMARK:
            text = f'<html><head/><body><p>' \
                   f'<span style=" font-family:\'Museo Sans Cyrl\',\'Arial\',\'sans-serif\'; ' \
                   f'font-size:10pt;">Looks like image doesn\'t contain any landmarks</span></p></body></html>'
        else:
            text = f'<html><head/><body><p>' \
                   f'<span style=" font-family:\'Museo Sans Cyrl\',\'Arial\',\'sans-serif\'; font-size:10pt;">This is </span>' \
                   f'<a href="https://www.google.com/search?q={prediction}">' \
                   f'<span style=" font-family:\'Museo Sans Cyrl\',\'Arial\',\'sans-serif\'; font-size:10pt; ' \
                   f'text-decoration: underline; color:#0000ff;">{prediction}</span></a></p></body></html>'

        self.ui.answer.setText(text)

    def showFileDialog(self):
        curDir = os.path.abspath(os.getcwd())
        imagePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open image', curDir, 'Images (*.jpg)')

        if imagePath != '':
            self.showImage(imagePath)

            self.mController.setImagePath(imagePath)
            self.ui.findLabel.setEnabled(True)

    def showImage(self, imagePath):
        w = self.ui.image.frameGeometry().width()
        h = self.ui.image.frameGeometry().height()

        pixmap = QPixmap(imagePath)
        pixmap = pixmap.scaled(min(w, pixmap.width()), min(h, pixmap.height()), Qt.KeepAspectRatio)

        if self.thread.isRunning():
            new_pixmap = QPixmap(pixmap.size())
            new_pixmap.fill(Qt.transparent)
            painter = QPainter(new_pixmap)
            painter.setOpacity(0.4)
            painter.drawPixmap(QPoint(), pixmap)
            painter.end()

            self.ui.image.setPixmap(new_pixmap)
        else:
            self.ui.image.setPixmap(pixmap)

    def predictButtonClicked(self):
        self.ui.openImage.setEnabled(False)
        self.ui.findLabel.setEnabled(False)

        self.ui.spinner.start()
        self.thread.start()
        self.showImage(self.mController.getImagePath())

    def predictFinished(self):
        self.ui.spinner.stop()
        self.showImage(self.mController.getImagePath())
        self.ui.openImage.setEnabled(True)

    def resizeEvent(self, *args, **kwargs):
        imagePath = self.mController.getImagePath()
        if imagePath != '':
            self.showImage(imagePath)
        pass
