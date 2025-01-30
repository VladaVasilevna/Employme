from abc import ABC, abstractmethod

import requests


class AbstractAPI(ABC):
    @abstractmethod
    def connect(self):
        """Метод для подключения к API."""
        pass

    @abstractmethod
    def get_vacancies(self, query):
        """Метод для получения вакансий по запросу."""
        pass


class HeadHunterAPI(AbstractAPI):
    __BASE_URL = "https://api.hh.ru/vacancies"

    def connect(self):
        """Подключение к API hh.ru (проверка доступности)."""
        try:
            response = requests.get(self.__BASE_URL)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Ошибка подключения: {e}")
            return False

    def get_vacancies(self, query):
        """Получение вакансий по запросу."""
        if not self.connect():
            return []

        params = {"text": query}
        response = requests.get(self.__BASE_URL, params=params)

        if response.status_code == 200:
            return response.json().get("items", [])
        else:
            print(f"Ошибка получения вакансий: {response.status_code}")
            return []


if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    vacancies = hh_api.get_vacancies("Python Developer")

    for vacancy in vacancies:
        print(f"Название: {vacancy['name']}, Ссылка: {vacancy['alternate_url']}")
