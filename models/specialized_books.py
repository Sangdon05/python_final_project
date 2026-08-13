from models.base_book import BaseBook


class GeneralBook(BaseBook):
    def __init__(self, title: str, author: str, isbn: int, pages: int):
        super().__init__(title, author, isbn)
        self.pages = pages


class EBook(BaseBook):
    def __init__(self, title: str, author: str, isbn: int, words: int):
        super().__init__(title, author, isbn)
