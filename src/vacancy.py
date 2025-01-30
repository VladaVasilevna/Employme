class Vacancy:
    __slots__ = ["title", "url", "salary", "description"]

    def __init__(self, title, url, salary=None, description=""):
        self.title = title
        self.url = url
        self.salary = self.__validate_salary(salary)
        self.description = description

    @staticmethod
    def __validate_salary(salary):
        """Валидирует значение зарплаты."""
        if salary is None:
            return 0  # Если зарплата не указана, присваиваем 0
        elif isinstance(salary, (int, float)) and salary >= 0:
            return salary
        else:
            raise ValueError("Зарплата должна быть положительным числом или None.")

    def to_dict(self):
        """Возвращает атрибуты объекта в виде словаря."""
        return {"title": self.title, "url": self.url, "salary": self.salary, "description": self.description}

    def __repr__(self):
        """Строковое представление объекта вакансии."""
        salary_display = "Зарплата не указана" if self.salary == 0 else self.salary
        return (
            f"Vacancy(title={self.title}, url={self.url}, " f"salary={salary_display}, description={self.description})"
        )
