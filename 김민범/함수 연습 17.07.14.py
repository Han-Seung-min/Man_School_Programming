# 함수
def sum(a, b) :
    return a + b

# 기본형태 - 입출력값 존재
a = 3
b = 4
c = sum(a, b)
print(c)

print("*" * 30)

d = 3
f = 4
c = sum(d, f)

print(c)

print("*" * 30)

# 출력값만 존재
def say() :
    return "Hi"

print(say())

print("*" * 30)

# 결과값이 없는 함수
def sum2(a,b) : 
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

a = 3
b = 4
print(sum2(a, b))

print("*" * 30)

# 입출력값 둘다 없는 함수
def say() :
    print("Hi")

print(say())

print("*" * 30)

# 입력값 몇 개가 될지 모를 때
def sum_many(*args) :
    sum = 0
    for i in args :
        sum = sum + i
    return sum

result = sum_many(1,2,3)
print(result)

result = sum_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def sum_mul(choice, *args) :
    if choice == "sum" :
        result =0
        for i in args :
            result = result + i
    elif choice == "mul" :
        result = 1
        for i in args :
            result = result * i
    return result

result = sum_mul('sum', 1,2,3,4,5)
print(result)

result = sum_mul('mul', 1,2,3,4,5)
print(result)

# 함수의 결과값은 하나- 튜플값으로 하나가 됨
def sum_and_mul(a,b) :
    return a+b, a*b

print(sum_and_mul(3,4))

# 하나의 튜플값을 2개의 값으로 받고 싶다면
sum3, mul = sum_and_mul(3,4)
print(sum3, mul)

# return을 2번이상 넣었을 때
def sum_and_mul2(a,b) :
    return a+b
    return a*b

print(sum_and_mul2)

print('*' * 30)

# 특별한 상황이 도면 함수를 빠져나가고 싶을 때
def say_nick(nick) :
    if nick == "바보" :
        return
    print("나의 별명은 %s 입니다." % nick)

say_nick("야호")
say_nick("바보")

print('*' * 30)

# 입력 인수에 초깃값 미리 설정하기
def say_myself(name, old, man=True) :
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살 입니다." % old)
    if man :
        print("남자입니다.")
    else :
        print("여자입니다.")

say_myself("박", 20)
say_myself("박", 20, True)
say_myself("김", 20, False)

# 함수 입력 인수에 초깃값을 설정할 때 주의사항
"""
초깃값 설정할하고자 하는 입력 변수들은 항상 뒤쪽에 위치
"""

print("*" * 30)

# 함수 안에서 선언된 변수의 효력 범위
"""
함수에서 사용한 변수는 그 함수 안에서만 효력발생
"""
# 함수 안에서 함수 밖의 변수 변경하는 방법
"""
변수 동일시
"""
a = 1

def vartest(a) :
    a = a + 1
    return a

a = vartest(a)
print(a)

"""
global 명령어 이용

vartest2 함수 안의 global a라는 문장은 함수 안에서 함수 밖의 a 변수를 직접 사용하겠다는 뜻
프로그래밍 할 때 비추천방법 - 함수는 독립적 존재가 가장 좋으므로
"""

a = 1

def vartest2() :
    global a
    a = a + 1

vartest2()
print(a)
