from models.base_book import BaseBook


class BookData:
    def __init__(self, book: BaseBook, is_rent: bool = False):
        self.__book = book
        self.is_rent = is_rent

    def __eq__(self, other):
        if isinstance(other, BookData):
            return self.__book == other.get_book()

        return False

    def __str__(self):
        return f"{'[대여중]' if self.is_rent else '[대여 가능]'} {self.__book}"

    def get_book(self) -> BaseBook:
        return self.__book

    def get_ibsn(self) -> int:
        return self.__book.get_ibsn()

    def get_title(self) -> str:
        return self.__book.get_title()

    def get_author(self) -> str:
        return self.__book.get_author()
