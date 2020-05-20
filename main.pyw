import sys
from PyQt5.QtWidgets import QApplication

from Model.LandmarkRecognitionModel import LandmarkRecognitionModel
from Controller.LandmarkRecognitionController import LandmarkRecognitionController


def main():
    app = QApplication(sys.argv)

    # создаём модель
    model = LandmarkRecognitionModel()

    # создаём контроллер и передаём ему ссылку на модель
    controller = LandmarkRecognitionController(model)

    app.exec()


if __name__ == '__main__':
    sys.exit(main())
