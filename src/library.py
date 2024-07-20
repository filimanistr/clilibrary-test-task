import json
from dataclasses import asdict, astuple

from config import Book, SearchFields, AddFields, \
                   UNKNOWN_BOOK_ID


class Library:
    """
    Отвечает за работу с книгами: создание, удаление, обновление, поиск
    он же сохраняет их в файл, хотя мб разделить на другой клас
    """
    name: str = "библиотека of moscow"
    books: dict[int, Book] = dict()
    count: int = 0

    def __init__(self):
        """
        Open data from file to self.books var
        """
        with open("data.txt", "r") as input:
            for line in input:
                book = json.loads(line)
                self.books[book["id"]] = Book(**book)
                self.count = book["id"]

    def _update_books(self):
        """
        Rewrite file completely, add all self.books to it
        """
        with open('data.txt', 'w') as f:
            for book in self.books.values():
                f.write(json.dumps(asdict(book)))
                f.write("\n")

    def _add_book(self, book: Book):
        """
        Add new line to the file (book)
        """
        with open('data.txt', 'a') as f:
            f.write(json.dumps(asdict(book)))
            f.write("\n")

    def add_book(self, fields: AddFields) -> Book:
        """
        Add book to the library
        """
        self.count += 1
        book = Book(id=self.count, **asdict(fields), status="в наличии")
        self.books[self.count] = book
        self._add_book(book)
        return book

    def search_for_book(self, fields: SearchFields) -> list[Book]:
        """
        Search in library for the book
        """
        filtered_books = []
        for book in self.books.values():
            if fields.title and fields.title.lower() not in book.title.lower():
                continue
            if fields.author and fields.author.lower() not in book.author.lower():
                continue
            if fields.year and fields.year != book.year:
                continue
            filtered_books.append(book)
        return filtered_books

    def remove_book(self, id: int) -> Book:
        """
        Remove book from the library
        """
        book = self.books.get(id)
        if book is None:
            raise Exception(UNKNOWN_BOOK_ID)

        del self.books[id]
        self._update_books()
        return book

    def update_book_status(self, id: int, status: str) -> Book:
        """
        Update book status in library
        """
        book = self.books.get(id)
        if book is None:
            raise Exception(UNKNOWN_BOOK_ID)

        book.status = status
        self._update_books()
        return book
