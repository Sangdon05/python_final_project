SERVICE_INFO_MESSAGE = """
1. 도서 등록
2. 전체 도서 조회
3. 도서 검색
4. 대여/반납 처리
5. 종료
"""
RENT_CHECKOUT_INFO_MESSAGE = """
1. 반납
2. 대여
3. 취소
"""
__INPUT_ERROR_MESSAGE = "메뉴를 선택해 주세요."


def input_number_range(value: str, menu_range: range) -> int:
    if value.isdigit():
        select_number = int(value)

        if select_number in menu_range:
            return select_number
        else:
            raise ValueError(__INPUT_ERROR_MESSAGE)
    else:
        raise ValueError(__INPUT_ERROR_MESSAGE)
