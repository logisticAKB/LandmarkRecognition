from View.LandmarkRecognitionView import LandmarkRecognitionView


class LandmarkRecognitionController:
    """
    Класс LandmarkRecognitionController представляет реализацию контроллера.
    Согласовывает работу представления с моделью.
    """

    def __init__(self, inModel):
        """
        Конструктор принимает ссылку на модель.
        Конструктор создаёт и отображает представление.
        """
        self.mModel = inModel
        self.mView = LandmarkRecognitionView(self, self.mModel)

        self.mView.show()

    def setImagePath(self, path):
        self.mModel.imagePath = path

    def getImagePath(self):
        return self.mModel.imagePath

    def getPrediction(self):
        return self.mModel.prediction

    def getPredictionStatus(self):
        return self.mModel.predictionStatus

    def predictLandmark(self):
        self.mModel.predict()
