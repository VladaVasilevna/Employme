from functools import total_ordering

@total_ordering
class Vacancy:
    def __init__(self, title, url, salary=None, description=''):
        self.title = title
        self.url = url
        self.salary = self._process_salary(salary)  # Обработка зарплаты
        self.description = description

    @staticmethod
    def _process_salary(salary):
        if isinstance(salary, dict):
            return salary  # Возвращаем словарь без изменений
        elif isinstance(salary, int) and salary > 0:
            return {'from': salary, 'to': salary, 'currency': 'руб.'}  # Превращаем в словарь
        else:
            return None  # Уровень дохода не указан

    def max_salary(self):
        """Метод для получения максимальной зарплаты с учетом форматирования"""
        if self.salary and isinstance(self.salary, dict):
            return self.salary.get('to', 0) or 0  # Если 'to' не указано, возвращаем 0
        return 0  # Если зарплата не указана

    def formatted_max_salary(self):
        """Метод для получения отформатированной максимальной зарплаты"""
        max_salary_value = self.max_salary()
        currency = self.salary.get('currency', 'руб.') if self.salary else 'руб.'
        return f"{max_salary_value:,.0f} {currency}".replace(',', ' ')  # Форматируем с пробелами

    def __lt__(self, other):
        """Сравнение по максимальной зарплате"""
        return self.max_salary() < other.max_salary()

    def __eq__(self, other):
        """Сравнение по максимальной зарплате"""
        return self.max_salary() == other.max_salary()

    def __repr__(self):
        return f"Vacancy(title={self.title}, salary={self.salary}, url={self.url})"
