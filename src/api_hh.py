class BaseApi(ABC):
    "абстрактный класс для подключения API"
    @abstractmethod
    def get_vacancy(self, keyword):
        pass


class HHApi(BaseApi):
    "класс для подключения к API HH.ru"
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}


    def get_vacancy(self, keyword):
        "поиск вакансий на сайте HH.ru по ключевому слову"
        self.params.update({'text': keyword})
        response = requests.get(self.url,params=self.params)
        return response.json()['items']