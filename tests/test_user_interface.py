from unittest.mock import patch

import pytest

from src.user_interface import user_interaction


@pytest.mark.parametrize(
    "inputs, expected_calls",
    [
        (
            ["Developer", "3", "", "n", "n"],  # Ввод пользователя
            [
                "Найдено 3 вакансий.",  # Ожидаемый вывод количества вакансий
                "1. Python Developer\nЗарплата от 10000 USD\nhttp://example.com/python\n",  # Ожидаемый вывод первой вакансии
                "2. Java Developer\nЗарплата от 1200 до 55000 USD\nhttp://example.com/java\n",  # Ожидаемый вывод второй вакансии
                "3. C++ Developer\nЗарплата до 12500 EUR\nНет ссылки\n",  # Ожидаемый вывод третьей вакансии
            ],
        ),
        (
            ["Java", "2", "2", "y", "разработка", "n"],  # Другой набор входных данных
            [
                "Найдено 1 вакансий.",  # Ожидаемый вывод количества вакансий после фильтрации по ключевому слову
                "1. Java Developer\nЗарплата от 1200 до 55000 USD\nhttp://example.com/java\n",  # Ожидаемый вывод первой вакансии
            ],
        ),
    ],
)
@patch("builtins.print")
@patch("builtins.input")
def test_user_interaction(mock_input, mock_print, api_mock, inputs, expected_calls):
    """
    Тестирование функции user_interaction с различными входными данными.
    """
    # Подмена ввода пользователя
    mock_input.side_effect = inputs

    # Вызов тестируемой функции
    user_interaction(api_mock)

    # Проверка вызовов print с ожидаемыми значениями
    for expected_call in expected_calls:
        mock_print.assert_any_call(expected_call)
