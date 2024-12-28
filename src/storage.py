import json
from abc import ABC, abstractmethod
from src.vacancy import Vacancy

class AbstractStorage(ABC):
    @abstractmethod
    def save(self, vacancies):
        pass

    @abstractmethod
    def load(self):
        pass

class JSONStorage(AbstractStorage):
    def __init__(self, filename='vacancies.json'):
        self.filename = filename

    def save(self, vacancies):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([v.__dict__ for v in vacancies], f, ensure_ascii=False)

    def load(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return [Vacancy(**data) for data in json.load(f)]
        except FileNotFoundError:
            return []
