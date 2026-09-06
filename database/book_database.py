import copy

from models.book_data import BookData
from utils.errors import DuplicatedISBN


# 도서 목록 관리 데이터 베이스
class BookDatabase:
    def __init__(self):
        self.__books: list[BookData] = []

    def create(self, book_data: BookData):
        if self.search_isbn(book_data.get_ibsn()):
            raise DuplicatedISBN()

        self.__books.append(book_data)

    def all(self):
        return self.__books.copy()

    def search(self, keyword: str) -> list[BookData]:
        isbn = None
        if keyword.isnumeric():
            isbn = int(keyword)

        result: list[BookData] = [
            x
            for x in self.__books
            if keyword in x.get_title()
            or keyword in x.get_author()
            or x.get_ibsn() == isbn
        ]

        return result

    def search_isbn(self, isbn: int) -> BookData | None:
        result = [x for x in self.__books if x.get_ibsn() == isbn]

        # TODO: create 시 예외 처리는 하겠지만 혹시 동일한 isbn이 여러게일떄 예외처리 필요
        if len(result) == 0:
            return None
        else:
            # update 전까지 dict에 반영되지 않기때문에 참조가 아닌 복사로 전달
            return copy.copy(result[0])

    def update(self, book_data: BookData):
        index = self.__books.index(book_data)
        self.__books[index] = book_data
