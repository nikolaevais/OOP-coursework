
def answer_user(user_answer, list_vacancy, search_query):
    "Функция для взаимодействия с пользователем"
    if user_answer == "1":
        city = input("Введите названия города для поиска вакансий ")
        for vac in list_vacancy:
            if city.casefold() == vac.city.casefold():
                print(vac)

    if user_answer == "2":
        salary_range = int(input(f"Введите минимальную зарплату для вакансии {search_query}: "))
        for vac in list_vacancy:
            if salary_range <= vac.salary_from:
                print(vac)

    if user_answer == "3":
        employment = input("Выберите тип занятости:\n"
                           "1 - полная занятость\n"
                           "2 - частичная занятость\n"
                           "3 - стажировка\n"
                           "4 - проектная работа\n"
                           "5 - волонтерство\n")
        for vac in list_vacancy:
            if employment == "1":
                if "Полная занятость" == vac.employment_name:
                    print(vac)
            elif employment == "2":
                if "Частичная занятость" == vac.employment_name:
                    print(vac)
            elif employment == "3":
                if "Стажировка" == vac.employment_name:
                    print(vac)
            elif employment == "4":
                if "Проектная работа" == vac.employment_name:
                    print(vac)
            elif employment == "5":
                if "Волонтерство" == vac.employment_name:
                    print(vac)
            else:
                print("Введена не верная цифра")
                break

    if user_answer == "4":
        user_answer_3 = int(input("Введите количество вакансий для вывода в топ: "))
        sort_vacancy = sorted(list_vacancy, reverse=True)
        sort_vacancies = sort_vacancy[:user_answer_3]
        print(*sort_vacancies, sep='\n')

    if user_answer == "5":
        for vac in list_vacancy:
            print(vac)
