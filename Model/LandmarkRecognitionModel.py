import tensorflow as tf

# Раскомментировать для видеокарт серии RTX
# physical_devices = tf.config.experimental.list_physical_devices('GPU')
# tf.config.experimental.set_memory_growth(physical_devices[0], True)

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, decode_predictions, preprocess_input
from tensorflow.keras.applications.inception_v3 import InceptionV3, decode_predictions, preprocess_input


class LandmarkRecognitionModel:
    """
    Класс LandmarkRecognitionModel представляет собой реализацию модели данных.
    В модели хранятся классификатор не метки/метки, классификатор метки,
    путь к изображению и предсказание классификатора.

    Модель предоставляет интерфейс, через который можно работать
    с хранимыми значениями.

    Модель содержит методы регистрации, удаления и оповещения
    наблюдателей.
    """

    NOT_PREDICTED = 0
    PREDICTED_LANDMARK = 1
    PREDICTED_NOT_LANDMARK = 2

    def __init__(self):
        self._mPredictionStatus = self.NOT_PREDICTED
        self._mLandmarkNonLandmarkClassifier = load_model('./NN/models/landmark_non_landmark_model.h5')
        self._mLandmarkClassifier = load_model('./NN/models/landmark_classification_model.h5')
        self._mImagePath = ''
        self._mPrediction = None

        self._mObservers = []

    @property
    def predictionStatus(self):
        return self._mPredictionStatus

    @property
    def imagePath(self):
        return self._mImagePath

    @property
    def prediction(self):
        return self._mPrediction

    @imagePath.setter
    def imagePath(self, value):
        self._mImagePath = value

        self._mPredictionStatus = self.NOT_PREDICTED
        self._mPrediction = None

        self.notifyObservers()

    def predict(self):
        for i in range(1000000): print("kek")

    def addObserver(self, inObserver):
        self._mObservers.append(inObserver)

    def removeObserver(self, inObserver):
        self._mObservers.remove(inObserver)

    def notifyObservers(self):
        for x in self._mObservers:
            x.modelIsChanged()
