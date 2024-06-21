class BaseApi(ABC):
    "абстрактный класс для подключения API"
    @abstractmethod
    def get_vacancy(self, keyword):
        pass