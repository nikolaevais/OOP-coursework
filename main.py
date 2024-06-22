from src.api_hh import HHApi
from src.vacancy import Vacancy
from src.utils import answer_user
from src.fileworker import JSONWorker

import sys



search_query = input("Введите название вакансии для поиска на сайте hh.ru: ")
hh_vac = HHApi()
vacancy = Vacancy.create_vacancies(hh_vac.get_vacancy(search_query))
JSONSave = JSONWorker('vacancies.json').write_file(vacancy)
list_vacancy = JSONWorker('vacancies.json').read_file('vacancies.json')

user_answer_2 = None

while user_answer_2 != "1":
    print("""Для уточнения Вашего запроса выберите следующее действие:
            1 - ввести название города
            2 - ввести минимальную зарплату
            3 - ввести тип занятости
            4 - вывести топ вакансий с максимальной зарплатой
            5 - вывести все вакансии""")
    user_answer = input()
    user_inter = answer_user(user_answer, list_vacancy, search_query)
    user_answer_2 = input("Нажмите 1 для того чтобы выйти из программы или 2 для того чтобы вернуться в предыдущее меню: ")