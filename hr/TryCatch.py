# 예외처리
from hr.CustomError import IdLengthError, CustomError

a = 0
result = False
try:
    a = int("1-")
    result = True
except ValueError as e:  # Exception이 발생하면 블럭안의 코드를 수행
    a = -1
finally:  # Exception이 발생과 관계 없이 항상 마지막에 수행
    if result:
        print('익셉션이 발생하지 않았습니다.', a)
    else:
        print('익셉션이 발생 하였습니다.', a)
    a = 1

try:
    4 / 0
except Exception as e:
    print('에러발생!')

# 다중 Exception 처리
# Exception이 발생하면 아래는 더이상 수행하지 않음.
num = 0
try:
    num = int("1-")
    num = 4 / 0  # zeroDivisionError.....
except ZeroDivisionError as e:
    print('zeroDivisionError 발생!')
except ValueError as e:
    print('valueError 발생!')

try:
    num = int("1-")
    num = 4 / 0  # zeroDivisionError.....
except (ZeroDivisionError, ValueError) as e:
    print('Error 발생!', e)

# 다음 작업을 위해서 주석처리.
# try:
#     4 / 0
# finally:
#     print('finally를 가장 먼저 수행한 다음에 에러를 출력!')

print('-' * 30)

# 강제로 exception 호출
# raise : 강제로 Exception 발생 시킬때 사용함.
id = "hr0001"
try:
    if len(id) >= 3:
        print('valueError2')
        # 사실은 에러가 아니지만 커스텀한 에러를 만들어서 발생 시켰음.
        raise IdLengthError
    print('valueError 1')
    # 강제로 에러를 발생 시킴.
    raise ZeroDivisionError
except IdLengthError as e:
    print('내가 만든 custom Error:: 아이디 길이 에러!')
except ValueError as e:
    print('raise ValueError!::입력값이 유효하지 않습니다.')
except ZeroDivisionError as e:
    print('raise ZeroDivisionError!')

print('-' * 30)


# customException을 호출해주는 함수
def isCustomError(nickname):
    findIndex = nickname.find('바보')
    if findIndex >= 0:
        print(findIndex + 1,  '번째 자리에 포함할 수 없는 단어를 가지고 있습니다.')
        raise CustomError
    else:
        print(nickname, '은(는) 사용 가능한 닉네임 입니다.')


nickname = '김경진바보'
try:
    isCustomError(nickname)
except CustomError as e:
    pass  # 회피 더이상 수행할 코드가 없다는 의미
    # print(e)
    # print(nickname, '은(는) 사용할 수 없는 닉네임 입니다.')
