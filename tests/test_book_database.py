from database.book_database import BookData, BookDatabase
from models.specialized_books import EBook, GeneralBook


# database create 검증
def test_create():
    database = BookDatabase()

    books = [
        BookData(GeneralBook("123", "aaaa", 120, 100)),
        BookData(GeneralBook("546", "aaaa", 122, 120)),
        BookData(EBook("789", "aaaa", 123, 15000)),
    ]

    for book in books:
        database.create(book)

    assert len(database.all()) == len(books)


# ISBN 중복 추가 오류 검증
def test_create_duplicate():
    database = BookDatabase()

    books = [
        BookData(GeneralBook("123", "aaaa", 120, 100)),
        BookData(GeneralBook("546", "aaaa", 122, 120)),
        BookData(EBook("789", "aaaa", 123, 15000)),
    ]

    for book in books:
        database.create(book)

    try:
        database.create(
            BookData(GeneralBook("546", "ccc", 122, 120)),
        )
    except ValueError:
        assert True

    assert len(database.all()) == len(books)


# 검색 결과 검증
def test_search():
    database = BookDatabase()

    books = [
        BookData(GeneralBook("123", "aaaa", 120, 100)),
        BookData(GeneralBook("546", "aaaa", 122, 120)),
        BookData(EBook("789", "aaaa", 123, 15000)),
    ]

    for book in books:
        database.create(book)

    assert database.search_isbn(120).get_ibsn() == 120
    assert database.search_isbn(999) == None


# 자료 수정 후 업데이트 검증
def test_update():
    database = BookDatabase()

    books = [
        BookData(GeneralBook("123", "aaaa", 120, 100)),
        BookData(GeneralBook("546", "aaaa", 122, 120)),
        BookData(EBook("789", "aaaa", 123, 15000)),
    ]

    for book in books:
        database.create(book)

    result = database.search_isbn(120)
    result.is_rent = True

    # database update 전까지는 적용되지 않아야 한다.
    assert database.search_isbn(120).is_rent == False

    database.update(result)

    assert database.search_isbn(120).is_rent == True

    try:
        database.update(BookData(EBook("789", "aaaa", 333, 15000)))
    except ValueError:
        # ISBN이 존재하지 않을 경우 예외처리할수있는가?
        assert True
