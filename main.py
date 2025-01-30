from src.api import HeadHunterAPI
from src.user_interface import user_interaction

if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    user_interaction(hh_api)
