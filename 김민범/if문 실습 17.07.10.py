# if문
if 1 :
    print("참")
else :
    print("거짓")

# and, or, not
money = 2000
card = 1

print("=" * 30)
if money >= 3000 or card : 
    print("택시를 타고 가")
else :
    print("걸어가")

print("=" * 30)

math = 3
english = 4
science = 1

if math < 4 and science < 4 : 
    print("합격")
else :
    print("불합격")

print("=" * 30)

if not english >= 4 : 
    print("안전")
else :
    print("위험")
    
print("=" * 30)

# x int s, not in s
print(1 in [1,2,3])
print(1 not in [1,2,3])

print('a' in ('a', 'b', 'c'))
print('j' not in "python")
print('p' in "python")

pocket = ["paper", "cellphone", "money"]

if "money" in pocket :
    print("택시타고가")
else :
    print("걸어가")

print("=" * 30)

# pass
pocket = ["paper", "cellphone", "money"]

if "money" in pocket :
    pass
else :
    print("카드꺼내")

print("=" * 30)

# 다양한 조건 판단 elif
pocket = ["paper", "handphone"]
card = 1

if "money" in pocket :
    print("택시타고가")
else :
    if card :
        print("택시타고가")
    else :
        print("걸어가")

print("=" * 30)

if "money" in pocket :
    print("택시타고가")
elif card :
    print("택시타고가")
else :
    print("걸어가")
