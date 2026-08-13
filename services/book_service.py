from database.book_database import BookDatabase


# 도서 대여 반납 시스템
class BookService:
    def __init__(self, database: BookDatabase):
        self.__database = database

    # 도서 대여
    def rent_book(self):
        pass

    # 도서 반납
    def checkout_book(self):
        pass

    # 도서 등록
    def add_book(self):
        pass

    # 도서 검색
    def search_book(self):
        pass

    # 전체 도서 조히
    def all_books(self):
        pass
