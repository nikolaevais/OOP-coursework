
class Vacancy:
    "класс для работы с данными вакансий"
    def __init__(self, name, url, salary_from, city, employment):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.city = city
        self.employment_name = employment

    def __repr__(self):
        return (f'Название вакансии: {self.name};  Ссылка: {self.url};  Зарплата от: {self.salary_from};  Город: {self.city};   Тип занятости: {self.employment_name}')

    @staticmethod
    def validate_salary(salary):
        if salary:
            salary_from = salary.get('from')
            if salary_from:
                return salary_from
        return 0

    @staticmethod
    def validate_city(area):
        if area:
            city = area.get('name')
            if city:
                return city
        return "Город не указан"


    @staticmethod
    def validate_employment(employment):
        if employment:
            employment_name = employment.get('name')
            if employment_name:
                return employment_name
        return "не указан"

