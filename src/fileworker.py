
class SaveFile(ABC):
    """абстрактный класс для работы с файлами"""
    @abstractmethod
    def write_file(self):
        pass

    @abstractmethod
    def read_file(self):
        pass

