from src.vacancy import Vacancy


def format_salary(salary):
    if salary is None or (isinstance(salary, int) and salary == 0):
        return "Уровень дохода не указан"
    elif isinstance(salary, dict):
        salary_from = salary.get('from')
        salary_to = salary.get('to')
        currency = salary.get('currency', 'руб.')
        if salary_from and salary_to:
            return f"от {salary_from:,} до {salary_to:,} {currency} на руки"
        elif salary_from:
            return f"от {salary_from:,} {currency} на руки"
        elif salary_to:
            return f"до {salary_to:,} {currency} на руки"
    return "Уровень дохода не указан"


def user_interface(api, storage):
    while True:
        print("1. Получить вакансии по запросу")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Получить вакансии с ключевым словом в описании")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            keyword = input("Введите поисковый запрос: ").strip()
            vacancies_data = api.get_vacancies(keyword)
            if vacancies_data:
                vacancies = [
                    Vacancy(v['name'], v['alternate_url'], v.get('salary'), v.get('snippet', {}).get('requirement', ''))
                    for v in vacancies_data]
                storage.save(vacancies)
                print(f"Получено {len(vacancies)} вакансий.")

        elif choice == '2':
            n = int(input("Введите количество вакансий для отображения: "))
            vacancies = storage.load()
            top_vacancies = sorted(vacancies, reverse=True)[:n]
            for vacancy in top_vacancies:
                print(vacancy.title)
                print(f"Зарплата: {vacancy.formatted_max_salary()}")
                print(f"Ссылка: {vacancy.url}\n")

        elif choice == '3':
            keyword = input("Введите ключевое слово: ")
            vacancies = storage.load()
            filtered_vacancies = [
                v for v in vacancies
                if v.description and keyword.lower() in v.description.lower()
            ]
            for vacancy in filtered_vacancies:
                print(vacancy.title)
                print(f"Зарплата: {vacancy.salary()}")
                print(f"Ссылка: {vacancy.url}\n")

        elif choice == '4':
            break

        else:
            print("Неверный выбор. Попробуйте снова.")
