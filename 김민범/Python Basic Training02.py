# Python Basic Training02

# 1번
a = [1, 2, 3, 4, 5]
sum1 = 0

for i in a :
    sum1 = sum1 + i
print(sum1)

# 2번
a = 16
b = 77
a,b = b,a
print(a)
print(b)

# 3번
menupan = {"짬뽕" : 5000, "짜장면" : 4000, "탕수육" : 12000}

menu = input("메뉴를 입력하세요>>")

print(menupan[menu])
