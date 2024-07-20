from library import Library
from config import SearchFields, AddFields, UpdateFields, UNKNOWN_BOOK_ID

from colors import green, red, yellow


class Librarian:
    """
    Отвечает за общение с пользователем
    Получает от него на вход команды

    Библиотекарь заведует библиотеками
    """
    library = Library()

    def list(self):
        print(green("Список доступных книг: "))
        for book in self.library.books.values():
            print(book)
        print()

    def add(self) -> None:
        title = input("Укажите название книги: ").strip()
        author = input("Укажите автора книги: ").strip()
        year = input("Укажите год книги: ").strip()

        try:
            fields = AddFields(title=title, author=author, year=year)
            self.library.add_book(fields)
            print(green(f"Книга {fields.title} добавленна в библиотеку\n"))
        except Exception as e:
            print(red(str(e)), "\n")

    def update(self) -> None:
        bookid = input("Введите id книги, статус которой надо обновить: ").strip()
        status = input("Новый статус для книги (в наличии/выдана): ").strip()

        try:
            fields = UpdateFields(id=bookid, status=status)
            book = self.library.update_book_status(int(fields.id), fields.status)
            print(green(f"Для книиги {book.title} был обновлен статус\n"))
        except Exception as e:
            print(red(str(e)), "\n")

    def search(self):
        print(yellow("Оставьте поля пустыми по которым не будет идти фильтрация"))
        title = input("Введите название книги: ").strip()
        author = input("Введите автора книги: ").strip()
        year = input("Введите год издания книги: ").strip()

        print(green("Найденные книги: "))
        fields = SearchFields(title=title, author=author, year=year)
        for book in self.library.search_for_book(fields):
            print(book)
        print()

    def remove(self) -> None:
        id = input("Введите id книги которую бы вы хотели удалить: ").strip()
        if not id.isdigit():
            print(red(UNKNOWN_BOOK_ID), "\n")
            return

        try:
            book = self.library.remove_book(int(id))
            print(green(f"Книга {book.title} была удалена из библиоткеи\n"))
        except Exception as e:
            print(red(str(e)), "\n")
