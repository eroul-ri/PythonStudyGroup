class CustomError(Exception):
    def __str__(self):
        return '커스텀 에러 발생 : 사용할 수 없습니다.'







# 커스텀 에러
class IdLengthError(Exception):
    pass