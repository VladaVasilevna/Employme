import pytest

from src.vacancy import Vacancy


def test_vacancy_initialization():
    vacancy = Vacancy("Python Developer", "https://example.com/vacancy1", 100000, "Разработка приложений на Python.")

    assert vacancy.title == "Python Developer"
    assert vacancy.url == "https://example.com/vacancy1"
    assert vacancy.salary == 100000
    assert vacancy.description == "Разработка приложений на Python."


def test_invalid_salary():
    with pytest.raises(ValueError):
        Vacancy("Invalid Salary", "https://example.com/vacancy2", -50000)
