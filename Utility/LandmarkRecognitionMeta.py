"""
Модуль реализации метакласса, необходимого для работы представления.

QObject - метакласс общий для оконных компонентов Qt.
ABCMeta - метакласс для реализации абстрактных суперклассов.

LandmarkRecognitionMeta - метакласс для представления.
"""

from PyQt5.QtCore import QObject
from abc import ABCMeta


class LandmarkRecognitionMeta(type(QObject), ABCMeta):
    pass
