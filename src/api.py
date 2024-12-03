import requests
from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HHAPI(AbstractAPI):
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {
            'User-Agent': 'Employme'
        }

    def get_vacancies(self, keyword):
        params = {'text': keyword, 'page': 0, 'per_page': 100}
        vacancies = []

        while True:
            response = requests.get(self.url, headers=self.headers, params=params)
            if response.status_code != 200:
                print(f"Ошибка: {response.status_code}")
                break

            data = response.json()
            items = data.get('items', [])
            if not items:
                break

            vacancies.extend(items)
            params['page'] += 1

        return vacancies
