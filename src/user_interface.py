from api import HeadHunterAPI
from utils import format_salary


def user_interaction(api):
    """Функция для взаимодействия с пользователем."""
    while True:
        # Шаг 1: Ввод запроса для поиска вакансий
        query = input("Введите запрос для поиска вакансий из hh.ru: ").strip()

        # Получаем вакансии из API
        vacancies = api.get_vacancies(query)
        print(f"Найдено {len(vacancies)} вакансий.")

        if not vacancies:
            print("\nПо вашему запросу ничего не найдено. Попробуйте еще раз.")
            continue

        # Шаг 2: Ввод числа N для вывода топ N вакансий по зарплате
        while True:
            n_input = input("\nВывести топ N вакансий по зарплате: ").strip()
            if n_input.isdigit():
                n = int(n_input)
                break
            else:
                print("\nНекорректный запрос. Повторите попытку.")

        # Шаг 3: Отфильтровать по валюте
        unique_currencies = {vac['salary']['currency'] for vac in vacancies if
                             isinstance(vac.get('salary'), dict) and 'currency' in vac['salary']}

        if not unique_currencies:
            print("\nПо вашему запросу ничего не найдено. Попробуйте еще раз.")
            continue

        currency_list = list(unique_currencies)

        while True:
            print("\nОтфильтровать по валюте? Если нет, нажмите Enter, если да, выберите валюту:")
            for idx, currency in enumerate(currency_list, start=1):
                print(f"{idx}. {currency}")

            currency_input = input().strip()
            if not currency_input:
                filtered_by_currency = vacancies
                print(f"Найдено {len(filtered_by_currency)} вакансий.")
                break

            if currency_input.isdigit() and 1 <= int(currency_input) <= len(currency_list):
                selected_currency = currency_list[int(currency_input) - 1]
                filtered_by_currency = [vac for vac in vacancies if
                                        isinstance(vac.get('salary'), dict) and vac['salary'][
                                            'currency'] == selected_currency]
                print(f"Найдено {len(filtered_by_currency)} вакансий.")
                break
            else:
                print("\nНекорректный запрос. Повторите попытку.")

        # Шаг 4: Фильтрация по ключевому слову в описании
        while True:
            filter_keyword = input(
                "\nОтфильтровать полученные вакансии по ключевому слову в описании? y/n: ").strip().lower()
            if filter_keyword in ['y', 'да', 'yes']:
                keyword = input("\nВведите ключевое слово для поиска в описании: ").strip()
                filtered_final = [vac for vac in filtered_by_currency if
                                  keyword.lower() in vac.get('description', '').lower()]

                print(f"Найдено {len(filtered_final)} вакансий.")

                if not filtered_final:
                    print("\nПо вашему запросу ничего не найдено. Попробуйте еще раз.")
                    continue
                break
            elif filter_keyword in ['n', 'нет', 'no', '']:
                filtered_final = filtered_by_currency
                print(f"Найдено {len(filtered_final)} вакансий.")
                break

        # Шаг 5: Вывод вакансий с учетом условий сравнения зарплаты
        top_vacancies = sorted(
            filtered_final,
            key=lambda x: (
                (x['salary'].get('to') if x.get('salary') and x['salary'].get('to') is not None else (
                            x['salary'].get('from') or 0))
            ),
            reverse=True
        )[:n]

        if len(top_vacancies) < n:
            print("\nК сожалению, были найдены только эти вакансии по вашему запросу:")

        for i, vacancy in enumerate(top_vacancies, start=1):
            salary_display = format_salary(vacancy.get('salary', {}))  # Обработка случая, если salary отсутствует
            print(
                f"{i}. {vacancy.get('name', 'Без названия')}\n{salary_display}\n{vacancy.get('alternate_url', 'Нет ссылки')}\n")


# Пример использования функции
if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    user_interaction(hh_api)
