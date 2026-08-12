INFO_MESSAGE = """
1. 도서 등록
2. 전체 도서 조회
3. 도서 검색
4. 대여/반납 처리
5. 종료
"""
_INPUT_ERROR_MESSAGE = "1 ~ 5까지의 메뉴를 선택해 주세요."


def check_input_value(value: str) -> int:
    if value.isdigit():
        select_number = int(value)

        if select_number in range(1, 6):
            return select_number
        else:
            raise ValueError(_INPUT_ERROR_MESSAGE)
    else:
        raise ValueError(_INPUT_ERROR_MESSAGE)
