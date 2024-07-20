from dataclasses import dataclass

# Общая информация для всего проекта
# Типы данные + валидация


HELP_MESSAGE = """Электронная библиотека, комманды:
    add         Добавитть книгу в библиотеку
    list        Отобразить список всех книг в библиотеке
    search      Найти книгу в библиотеке
    update      Обновить статус книги
    remove      Удалить книгу из библиотеки
    help        Отобразить более подробную информацию
"""

SEARCH_OPTIONS = "Укажите поля по которым будует производиться поиск"

UNKNOWN_COMMAND = "Неизвестная комманда"
UNKNOWN_BOOK_ID = "Книги с таким id не существует"

TITLE_IS_MISSING = "Название книги не было указано"
AUTHOR_IS_MISSING = "Автор книги не был указан"
YEAR_IS_MISSING = "Год не был указан"
STATUS_IS_MISSING = "Статус не был указан"

UNDEFINED_YEAR = "Год должен быть записан цифрами"

ALLOWED_COMMANDS = ["add", "list", "update", "remove", "search"]


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: str
    status: str


@dataclass
class SearchFields:
    title: str | None = None
    author: str | None = None
    year: str | None = None


@dataclass
class AddFields:
    title: str
    author: str
    year: str

    def __post_init__(self):
        """Validation"""
        if not self.title:
            raise Exception(TITLE_IS_MISSING)
        if not self.author:
            raise Exception(AUTHOR_IS_MISSING)
        if not self.year:
            raise Exception(YEAR_IS_MISSING)
        if not self.year.isdigit():
            raise Exception(UNDEFINED_YEAR)


@dataclass
class UpdateFields:
    id: str
    status: str

    def __post_init__(self):
        """Validation"""
        if not self.id:
            raise Exception(UNKNOWN_BOOK_ID)
        if not self.status:
            raise Exception(STATUS_IS_MISSING)
        if not self.id.isdigit():
            raise Exception(UNKNOWN_BOOK_ID)
