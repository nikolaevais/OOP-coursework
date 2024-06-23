from abc import ABC, abstractmethod
from src.vacancy import Vacancy
import os
import json
from config import ROOT_DIR

FILE_PATH = os.path.join(ROOT_DIR, 'data', 'operations.json')

class SaveFile(ABC):
    """абстрактный класс для работы с файлами"""
    @abstractmethod
    def write_file(self):
        pass

    @abstractmethod
    def read_file(self):
        pass


class JSONWorker(SaveFile):
    """
    класс для работы с json файлами
    """
    def __init__(self, file_name: str):
        self.path = os.path.join(ROOT_DIR, 'data', file_name)

    def read_file(self, file):
        "функция для открытия файла"
        with open(self.path, encoding="UTF-8") as file:
            data = json.load(file)
        vacancies = []
        for vacanci in data:
            vacancies.append(Vacancy(**vacanci))
        return vacancies



    def write_file(self, data):
        "функция для сохранения файла"
        with open(self.path, 'w', encoding="UTF-8") as file:
            return json.dump(data, file, indent=4, ensure_ascii=False)
