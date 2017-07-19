# Python Basic Training01

# 1번
a = int(input("숫자입력>"))
print(a)
print("%d" % (a ** 3))

# 2번 ???
a = int(input("숫자입력>"))
print("%d" % (a%3))


# 3번
a = int(input("a 입력"))
b = int(input("b 입력"))

print("%d" % (a//b))

# 4번
print("'작은 따옴표가 들어간 string'")

# 5번
print('"큰 따옴표가 들어간 string"')

# 6번
family_name = input("성 입력>")
first_name = input("이름 입력>")

full_name = family_name + first_name
print(full_name)

# 7번
tupleA = (1, 2)
tupleB = (3, 4)
tuple_sum = tupleA + tupleB
print(tuple_sum)


# 8번
a = int(input("a값 입력>"))

if a < 0 :
    a = a * -1
print(a)

# 9번
a = int(input("a값 입력>"))
b = int(input("b값 입력>"))

if a+b <= 999 :
    print(a+b)
else :
    print("999")

# 10번
a = int(input("a 입력>"))

if a % 2 :
    print("홀수")
else :
    print("짝수")

# 11번
