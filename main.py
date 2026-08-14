from database.book_database import BookDatabase
from models.specialized_books import EBook, GeneralBook
from services.book_service import BookService
from utils.helpers import *

database = BookDatabase()
service = BookService(database)


def main():
    while True:
        try:
            select_number = input_number_range(input(SERVICE_INFO_MESSAGE), range(1, 6))

            match select_number:
                case 1:
                    input_book_info()
                case 2:
                    for book in service.all_books():
                        print(book)
                case 3:
                    book = input_search_isbn()
                    if book:
                        print(book)
                case 4:
                    rent_checkout_menu()
                case 5:
                    return  # 프로그램 종료
        except ValueError as e:
            print(e)
            continue


def rent_checkout_menu():
    while True:
        try:
            sub_menu = input_number_range(
                input(RENT_CHECKOUT_INFO_MESSAGE), range(1, 4)
            )
        except ValueError as e:
            print(e)
            continue

        match sub_menu:
            case 1:
                book = input_checkout_book()
                if book:
                    print("도서 반납이 완료되었습니다.")
                break
            case 2:
                book = input_rent_book()
                if book:
                    print("도서 대여가 완료되었습니다.")
                break
            case 3:
                break


def input_rent_book():
    while True:
        try:
            isbn = int(input("대여할 도서의 ISBN을 입력해 주세요: "))

            return service.rent_book(isbn)
        except ValueError as e:
            print(e)
            break


def input_checkout_book():
    while True:
        try:
            isbn = int(input("반납할 도서의 ISBN을 입력해 주세요: "))

            return service.checkout_book(isbn)
        except ValueError as e:
            print(e)
            break


def input_search_isbn():
    # 제목, 저자, ISBN을 통한 검색 확장 필요
    while True:
        try:
            isbn = int(input("ISBN을 입력해 주세요: "))

            return service.search_book(isbn)
        except ValueError as e:
            print(e)
            break


def input_book_info():
    while True:
        try:
            book_type = input_number_range(input(ADD_BOOK_INFO_MESSAGE), range(1, 4))

            match book_type:
                case 1:
                    book_info = input_general_book()
                    service.add_book(GeneralBook(**book_info))
                    break
                case 2:
                    book_info = input_ebook()
                    service.add_book(EBook(**book_info))
                    break
                case 3:
                    break
        except ValueError as e:
            print(e)
            continue


def input_general_book():
    book_info = {}
    steps = iter(
        [input_book_name, input_book_author, input_book_isbn, input_book_pages]
    )
    input = next(steps)
    while True:
        if not input(book_info):
            continue

        try:
            input = next(steps)
        except StopIteration:
            break

    return book_info


def input_ebook():
    book_info = {}
    steps = iter(
        [input_book_name, input_book_author, input_book_isbn, input_book_letters]
    )
    input = next(steps)
    while True:
        if not input(book_info):
            continue

        try:
            input = next(steps)
        except StopIteration:
            break

    return book_info


def input_book_name(book_info) -> bool:
    title = input("도서명을 입력해 주세요: ")

    if not title:
        return False

    book_info["title"] = title
    return True


def input_book_author(book_info) -> bool:
    author = input("저자명을 입력해 주세요: ")

    if not author:
        return False

    book_info["author"] = author
    return True


def input_book_isbn(book_info) -> bool:
    isbn = input("ISBN 번호를 입력해 주세요: ")

    if not isbn.isdigit() or not isbn:
        return False

    book_info["isbn"] = int(isbn)
    return True


def input_book_letters(book_info) -> bool:
    letters = input("총 글자수를 입력해 주세요: ")

    if not letters.isdigit() or not letters:
        return False

    book_info["letters"] = int(letters)
    return True


def input_book_pages(book_info) -> bool:
    total_pages = input("총 페이지수를 입력해 주세요: ")

    if not total_pages.isdigit() or not total_pages:
        return False

    book_info["pages"] = int(total_pages)
    return True


if __name__ == "__main__":
    main()
