# Python Basic Training01

# 1번
a = int(input("숫자입력>"))
print(a)
print("%d" % (a ** 3))

print("-" * 30)

# 2번
a = int(input("숫자입력>"))
print("%d" % (a%3))

print("-" * 30)

# 3번
a = int(input("a 입력"))
b = int(input("b 입력"))

print("%d" % (a//b))

print("-" * 30)

# 4번
print("'작은 따옴표가 들어간 string'")

print("-" * 30)

# 5번
print('"큰 따옴표가 들어간 string"')

print("-" * 30)

# 6번
family_name = input("성 입력>")
first_name = input("이름 입력>")

full_name = family_name + first_name
print(full_name)

print("-" * 30)

# 7번
tupleA = (1, 2)
tupleB = (3, 4)
tuple_sum = tupleA + tupleB
print(tuple_sum)

print("-" * 30)

# 8번
a = int(input("a값 입력>"))

if a < 0 :
    a = a * -1
print(a)

print("-" * 30)

# 9번
a = int(input("a값 입력>"))
b = int(input("b값 입력>"))

if a+b <= 999 :
    print(a+b)
else :
    print("999")

print("-" * 30)

# 10번
a = int(input("a 입력>"))

if a % 2 :
    print("홀수")
else :
    print("짝수")

print("-" * 30)

# 11번
x1 = int(input("x1 입력>"))
y1 = int(input("y1 입력>"))
A = (x1, y1)

x2 = int(input("x2 입력>"))
y2 = int(input("y2 입력>"))
B = (x2, y2)

print(A)
print(B)

a = (x2 - x1) ** 2
b = (y2 - y1) ** 2
c = a + b

print("A(x1, y1)와 B(x2, y2)의 거리 : %f" % (c ** (1/2)) )

print("-" * 30)

# 12번
for i in [2, 4, 6, 8] :
    for j in range(1,i) :
        j += 1
        print("%d * %d = %.2d" % (i, j, (i * j)), end = "  ")
    print(" ")

print("-" * 30)

# 13번
sample = []

while i != " " :
    for i in [input("sample 입력(space 입력시 중단)")] :
        if i == " ": continue
        else :
            list(i)
            sample.append(i)

print(sample)

print("-" * 30)

# 14번

for x in range(0,10) :
    for y in range(0,10) :
        if ((x*10) + y) + ((y*10) + x) == 99 :
            print("x의 값 : %d" % x)
            print("y의 값 : %d" % y)
            print("%d + %d = %d" % (((x*10) + y), ((y*10) + x), ((x*10) + y) + ((y*10) + x)))
            print("=" * 20)
    
print("-" * 30)
