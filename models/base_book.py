class BaseBook:
    def __init__(self, title: str, author: str, isbn: int):
        self.__title = title
        self.__author = author
        self.__isbn = isbn

    def __str__(self):
        return f"도서명: {self.__title}, 저자: {self.__author}, ISBN: {self.__isbn}"

    def __eq__(self, other):
        if other == None:
            return False

        return self.__isbn == other.get_ibsn()

    def get_ibsn(self):
        return self.__isbn

    def get_title(self) -> str:
        return self.__title

    def get_author(self) -> str:
        return self.__author
