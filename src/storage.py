import csv
import json
import os
from abc import ABC, abstractmethod


class AbstractStorage(ABC):
    @abstractmethod
    def add_item(self, item):
        """Добавляет элемент в хранилище."""
        pass

    @abstractmethod
    def get_items(self, **criteria):
        """Получает элементы по указанным критериям."""
        pass

    @abstractmethod
    def delete_item(self, item_id):
        """Удаляет элемент из хранилища по ID."""
        pass


class JSONStorage(AbstractStorage):
    def __init__(self, filename="vacancies.json"):
        self.__filename = filename
        self.items = self.load_items()

    def load_items(self):
        """Загружает элементы из JSON-файла."""
        if os.path.exists(self.__filename):
            with open(self.__filename, "r", encoding="utf-8") as file:
                return json.load(file)
        return []

    def save_items(self):
        """Сохраняет элементы в JSON-файл без дубликатов."""
        unique_items = {item["url"]: item for item in self.items}
        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump(list(unique_items.values()), file, ensure_ascii=False, indent=4)

    def add_item(self, item):
        """Добавляет элемент в хранилище."""
        # Проверка на дубликаты перед добавлением
        existing_urls = {existing_item["url"] for existing_item in self.items}
        if item.url not in existing_urls:
            self.items.append(item.to_dict())  # Используем to_dict()
            self.save_items()
        else:
            print(f"Вакансия с URL {item.url} уже существует. Не добавляем дубликат.")

    def get_items(self, **criteria):
        """Получает элементы по указанным критериям."""
        result = self.items
        for key, value in criteria.items():
            result = [item for item in result if item.get(key) == value]
        return result

    def delete_item(self, url):
        """Удаляет элемент из хранилища по URL."""
        self.items = [item for item in self.items if item["url"] != url]
        self.save_items()


class CSVStorage(AbstractStorage):
    def __init__(self, filename="vacancies.csv"):
        self.__filename = filename
        self.items = self.load_items()

    def load_items(self):
        """Загружает элементы из CSV-файла."""
        items = []
        if os.path.exists(self.__filename):
            with open(self.__filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                items = list(reader)
        return items

    def save_items(self):
        """Сохраняет элементы в CSV-файл без дубликатов."""
        unique_items = {item["url"]: item for item in self.items}
        with open(self.__filename, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=unique_items[next(iter(unique_items))].keys())
            writer.writeheader()
            writer.writerows(unique_items.values())

    def add_item(self, item):
        """Добавляет элемент в хранилище."""
        existing_urls = {existing_item["url"] for existing_item in self.items}
        if item.url not in existing_urls:
            self.items.append(item.to_dict())
            self.save_items()
        else:
            print(f"Вакансия с URL {item.url} уже существует. Не добавляем дубликат.")

    def get_items(self, **criteria):
        """Получает элементы по указанным критериям."""
        result = self.items
        for key, value in criteria.items():
            result = [item for item in result if item.get(key) == value]
        return result

    def delete_item(self, url):
        """Удаляет элемент из хранилища по URL."""
        self.items = [item for item in self.items if item["url"] != url]
        self.save_items()


# Пример использования класса JSONStorage
if __name__ == "__main__":
    from vacancy import Vacancy

    storage = JSONStorage()

    # Создаем несколько вакансий
    vacancy1 = Vacancy("Python Developer", "https://example.com/vacancy1", 100000, "Разработка приложений на Python.")
    vacancy2 = Vacancy("Java Developer", "https://example.com/vacancy2", None, "Разработка приложений на Java.")

    # Добавляем вакансии в хранилище
    storage.add_item(vacancy1)
    storage.add_item(vacancy2)

    # Получаем все вакансии
    all_vacancies = storage.get_items()
    print("Все вакансии:", all_vacancies)
