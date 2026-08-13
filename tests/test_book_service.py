from models.specialized_books import EBook, GeneralBook
from services.book_service import BookDatabase, BookService


def test_add_book():
    database = BookDatabase()
    service = BookService(database)

    service.add_book(GeneralBook("123", "aaaa", 120, 100))
    service.add_book(EBook("789", "aaaa", 123, 15000))

    result = service.all_books()
    assert len(result) == 2


def test_search_book():
    database = BookDatabase()
    service = BookService(database)

    service.add_book(GeneralBook("123", "aaaa", 120, 100))
    service.add_book(EBook("789", "aaaa", 123, 15000))

    assert service.search_book(120) != None

    try:
        assert service.search_book(0000) == None
    except ValueError:
        assert True


def test_rent_book():
    database = BookDatabase()
    service = BookService(database)

    service.add_book(GeneralBook("123", "aaaa", 120, 100))
    service.add_book(EBook("789", "aaaa", 123, 15000))

    try:
        assert service.rent_book(120) != None
    except ValueError:
        assert False

    try:
        assert service.rent_book(120) != None
    except ValueError:
        assert True

    assert service.search_book(120).is_rent == True

    try:
        assert service.rent_book(999) != None
    except ValueError:
        assert True


def test_checkout_book():
    database = BookDatabase()
    service = BookService(database)

    service.add_book(GeneralBook("123", "aaaa", 120, 100))
    service.add_book(EBook("789", "aaaa", 123, 15000))

    try:
        assert service.checkout_book(120) == None
    except ValueError:
        assert True

    try:
        assert service.rent_book(120) != None
    except ValueError:
        assert False

    try:
        assert service.checkout_book(120) != None
    except ValueError:
        assert False

    assert service.search_book(120).is_rent == False
