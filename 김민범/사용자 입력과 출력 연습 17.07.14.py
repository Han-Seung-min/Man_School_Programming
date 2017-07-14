# 사용자 입력과 출력
"""
input은 입력되는 모든 것을 문자열로 취급
"""
print('*' * 30)

a = input()
print(a)

print('*' * 30)

# 프롬프트를 띄어서 사용자 입력 받기
number = input("숫자를 입력하세요 : ")
print(number)

print('*' * 30)

# print 자세히 알기
"""
큰 따옴표(")로 둘러싸인 문자열은 + 연산과 동일
"""
print("life " "is " "too short")
print("life " + "is " + "too short")

"""
문자열 띄어쓰기는 콤마로 한다
"""
print("life", "is", "too short")

"""
한 줄에 결과값 출력하기
"""
for i in range(10) :
    print(i, end=' ')
