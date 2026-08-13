from models.base_book import BaseBook


class BookData:
    def __init__(self, book: BaseBook, is_rent: bool = False):
        self.__book = book
        self.is_rent = is_rent

    def __eq__(self, other: BaseBook):
        return self.__book == other

    def __str__(self):
        return f"{'[대여중]' if self.is_rent else '[대여 가능]'} {self.__book}"

    def get_book(self):
        return self.__book

    def get_ibsn(self):
        return self.__book.get_ibsn()
