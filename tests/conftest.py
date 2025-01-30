import os
from unittest.mock import MagicMock

import pytest

from src.storage import CSVStorage, JSONStorage
from src.vacancy import Vacancy


@pytest.fixture
def vacancy_data():
    return Vacancy("Python Developer", "https://example.com/vacancy1", 100000, "Разработка приложений на Python.")


@pytest.fixture
def mock_api_response():
    return {
        "items": [
            {
                "name": "Python Developer",
                "salary": {"from": 80000, "to": 120000, "currency": "RUB"},
                "alternate_url": "https://example.com/vacancy1",
            },
            {
                "name": "Java Developer",
                "salary": {"from": 90000, "to": 130000, "currency": "RUB"},
                "alternate_url": "https://example.com/vacancy2",
            },
        ]
    }


@pytest.fixture
def json_storage(tmp_path):
    """Фикстура для JSONStorage с использованием временной директории."""
    storage = JSONStorage(filename=tmp_path / "test_vacancies.json")
    return storage


@pytest.fixture(scope="module")
def csv_storage(tmp_path):
    storage = CSVStorage(filename=tmp_path / "test_vacancies.csv")
    yield storage
    os.remove(tmp_path / "test_vacancies.csv")


@pytest.fixture
def api_mock():
    """Фикстура для мока API."""
    mock = MagicMock()
    mock.get_vacancies.return_value = [
        {
            "name": "Python Developer",
            "alternate_url": "http://example.com/python",
            "salary": {"from": 10000, "to": None, "currency": "USD"},
            "description": "Разработка на Python",
        },
        {
            "name": "Java Developer",
            "alternate_url": "http://example.com/java",
            "salary": {"from": 1200, "to": 55000, "currency": "USD"},
            "description": "Разработка на Java",
        },
        {
            "name": "C++ Developer",
            "alternate_url": "",
            "salary": {"from": None, "to": 12500, "currency": "EUR"},
            "description": "Разработка на C++",
        },
    ]
    return mock
