from database.book_database import BookData, BookDatabase
from models.specialized_books import BaseBook
from utils.errors import DuplicatedISBN


# 도서 대여 반납 시스템
class BookService:
    def __init__(self, database: BookDatabase):
        self.__database = database

    # 도서 대여
    def rent_book(self, isbn: int) -> BookData:
        book = self.__database.search_isbn(isbn)

        if book:
            if book.is_rent:
                raise ValueError("이미 대여중인 도서입니다.")

            book.is_rent = True
            self.__database.update(book)

            return book
        else:
            raise ValueError("도서가 존재하지 않습니다.")

    # 도서 반납
    def checkout_book(self, isbn: int) -> BookData:
        book = self.__database.search_isbn(isbn)

        if book:
            if book.is_rent:
                book.is_rent = False
                self.__database.update(book)

                return book
            else:
                raise ValueError("대여중인 도서가 아닙니다.")
        else:
            raise ValueError("도서가 존재하지 않습니다.")

    # 도서 등록
    def add_book(self, book: BaseBook):
        try:
            self.__database.create(BookData(book))
        except DuplicatedISBN as e:
            raise ValueError(e)
        except TypeError:
            raise ValueError("도서 데이터로 입력해 주세요.")

    # 도서 검색
    def search_book(self, isbn: int) -> BookData:
        book = self.__database.search_isbn(isbn)

        if book:
            return book
        else:
            raise ValueError("도서가 존재하지 않습니다.")

    # 전체 도서 조히
    def all_books(self) -> [BookData]:
        return self.__database.all()
