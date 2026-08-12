from utils import helpers


def main():
    while True:
        try:
            select_number = helpers.check_input_value(input(helpers.INFO_MESSAGE))

            match select_number:
                case 1:
                    print("1번 기능 실행")
                case 2:
                    print("2번 기능 실행")
                case 3:
                    print("3번 기능 실행")
                case 4:
                    print("4번 기능 실행")
                case 5:
                    return  # 프로그램 종료
        except ValueError as e:
            print(e)
            continue


if __name__ == "__main__":
    main()
