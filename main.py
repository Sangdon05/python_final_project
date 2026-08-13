from database.book_database import BookDatabase
from services.book_service import BookService
from utils import helpers

database = BookDatabase()
service = BookService(database)


def main():
    while True:
        try:
            select_number = helpers.input_number_range(
                input(helpers.SERVICE_INFO_MESSAGE), range(1, 6)
            )

            match select_number:
                case 1:
                    service.add_book()
                case 2:
                    service.all_books()
                case 3:
                    service.search_book()
                case 4:
                    while True:
                        sub_menu = helpers.input_number_range(
                            input(helpers.RENT_CHECKOUT_INFO_MESSAGE), range(1, 3)
                        )

                        match sub_menu:
                            case 1:
                                service.rent_book()
                            case 2:
                                service.checkout_book()
                            case 3:
                                break
                case 5:
                    return  # 프로그램 종료
        except ValueError as e:
            print(e)
            continue


if __name__ == "__main__":
    main()
