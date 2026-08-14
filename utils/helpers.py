from utils.messages import build_menu_message

SELECT_MENU_RETRY_MESSAGE = "메뉴 범위가 아닙니다. 다시 선택해 주세요."
SELECT_MENU_MESSAGE = "메뉴를 선택하세요: "
SERVICE_INFO_MESSAGE = build_menu_message(
    "도서 관리 시스템",
    """1. 도서 등록
2. 전체 도서 조회
3. 도서 검색
4. 대여/반납 처리
5. 종료\
    """,
    SELECT_MENU_MESSAGE,
)

RENT_CHECKOUT_INFO_MESSAGE = build_menu_message(
    "대여/반납",
    """1. 반납
2. 대여
3. 취소\
    """,
    SELECT_MENU_MESSAGE,
)

ADD_BOOK_INFO_MESSAGE = build_menu_message(
    "도서 등록",
    """1. 일반 단행본
2. 전자 도서
3. 취소\
    """,
    SELECT_MENU_MESSAGE,
)

def input_number_range(value: str, menu_range: range) -> int:
    if value.isdigit():
        select_number = int(value)

        if select_number in menu_range:
            return select_number
        else:
            raise ValueError(SELECT_MENU_RETRY_MESSAGE)
    else:
        raise ValueError(SELECT_MENU_RETRY_MESSAGE)
