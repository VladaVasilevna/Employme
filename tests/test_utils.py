import pytest

from src.utils import format_salary


@pytest.mark.parametrize(
    "salary_input, expected_output",
    [
        ({"from": None, "to": None}, "Зарплата не указана"),
        ({"from": 100000, "to": None}, "Зарплата от 100000 "),
        ({"from": None, "to": 150000}, "Зарплата до 150000 "),
        ({"from": 100000, "to": 100000}, "Зарплата 100000 "),
        ({"from": 80000, "to": 120000}, "Зарплата от 80000 до 120000 "),
    ],
)
def test_format_salary(salary_input, expected_output):
    assert format_salary(salary_input) == expected_output
