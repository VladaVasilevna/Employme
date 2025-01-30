from unittest.mock import patch

from src.api import HeadHunterAPI


def test_connect_success():
    api = HeadHunterAPI()

    with patch("src.api.requests.get") as mock_get:
        mock_get.return_value.status_code = 200

        assert api.connect() is True


def test_get_vacancies_success(mock_api_response):
    api = HeadHunterAPI()

    with patch("src.api.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_api_response

        vacancies = api.get_vacancies("Python Developer")
        assert len(vacancies) == 2


def test_get_vacancies_failure():
    api = HeadHunterAPI()

    with patch("src.api.requests.get") as mock_get:
        mock_get.return_value.status_code = 404

        vacancies = api.get_vacancies("Python Developer")
        assert vacancies == []
