class DuplicatedISBN(Exception):
    def __str__(self):
        return "중복 ISBN이 있습니다."
