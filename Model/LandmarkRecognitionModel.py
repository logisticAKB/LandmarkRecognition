import numpy as np
import pandas as pd
import tensorflow as tf

# Для видеокарт серии RTX
physical_devices = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input as preprocess_input_vgg16
from tensorflow.keras.applications.inception_v3 import decode_predictions as decode_predictions_inception_v3, \
    preprocess_input as preprocess_input_inception_v3


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

        self._mLandmarkWhiteList = set()
        with open('./NN/meta/white_list.txt', 'r') as white_list:
            for line in white_list.readlines():
                self._mLandmarkWhiteList.add(line.strip())

        self._mIdLabelDf = pd.read_csv('./NN/meta/id_to_label.csv')

        self._mImagePath = ''
        self._mPrediction = ''

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
        self._mPrediction = ''

        self.notifyObservers()

    def predict(self):
        img = image.load_img(self._mImagePath, target_size=(299, 299))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input_inception_v3(x)

        preds = self._mLandmarkNonLandmarkClassifier.predict(x)
        decoded_preds = decode_predictions_inception_v3(preds)[0]
        preds_set = set(pred[1] for pred in decoded_preds)

        if len(self._mLandmarkWhiteList.intersection(preds_set)):
            img = image.load_img(self._mImagePath, target_size=(224, 224))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input_vgg16(x)

            preds = self._mLandmarkClassifier.predict(x)

            self._mPrediction = self._mIdLabelDf[self._mIdLabelDf.id == np.argmax(preds[0])].label.values[0]
            self._mPredictionStatus = self.PREDICTED_LANDMARK
        else:
            self._mPredictionStatus = self.PREDICTED_NOT_LANDMARK

        self.notifyObservers()

    def addObserver(self, inObserver):
        self._mObservers.append(inObserver)

    def removeObserver(self, inObserver):
        self._mObservers.remove(inObserver)

    def notifyObservers(self):
        for x in self._mObservers:
            x.modelIsChanged()
