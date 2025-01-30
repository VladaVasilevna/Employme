def format_salary(salary: dict) -> str:
    """Форматирует строку зарплаты в зависимости от значений from и to."""
    salary_from = salary.get('from')
    salary_to = salary.get('to')
    currency = salary.get('currency', '')

    if salary_from is None and salary_to is None:
        return "Зарплата не указана"
    elif salary_from is not None and salary_to is None:
        return f"Зарплата от {salary_from} {currency}"
    elif salary_from is None and salary_to is not None:
        return f"Зарплата до {salary_to} {currency}"
    elif salary_from == salary_to:
        return f"Зарплата {salary_from} {currency}"
    else:
        return f"Зарплата от {salary_from} до {salary_to} {currency}"
