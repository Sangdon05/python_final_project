from models.base_book import BaseBook


class GeneralBook(BaseBook):
    def __init__(self, title: str, author: str, isbn: int, pages: int):
        super().__init__(title, author, isbn)
        self.pages = pages

    def __str__(self):
        return f"{super().__str__()}, 총 페이지: {self.pages}"


class EBook(BaseBook):
    def __init__(self, title: str, author: str, isbn: int, letters: int):
        super().__init__(title, author, isbn)
        self.letters = letters

    def __str__(self):
        return f"{super().__str__()}, 총 글자수: {self.letters}"
