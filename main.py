from src.api import HHAPI
from src.vacancy import Vacancy
from src.storage import JSONStorage
from src.user_interface import user_interface


def main():
    api = HHAPI()
    storage = JSONStorage()

    user_interface(api, storage)


if __name__ == "__main__":
    main()
