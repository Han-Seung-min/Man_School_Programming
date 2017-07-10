# while문
treeHit = 0

while treeHit < 10 :
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    
    if treeHit == 10 :
        print("나무 넘어갑니다.")

print("=" * 30)

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number : """

number = 0

while number != 4 :
    print(prompt)
    number = int(input())

print("=" * 30)

# while문 강제로 빠져나가기
coffee = 10
money = 300

while money :
    print("돈 받았으니 커피 준다")
    coffee -= 1
    print("남은 커피 양 %d개" % coffee)

    if not coffee :
        print("커피 다 떨어졌다 판매중지")
        break

print("=" * 30)

# break문 이용해 자판기 작동 과정 만들기
coffee = 5

while True :
    money = int(input("돈 넣어 : "))
    if money == 300 :
        print("커피준다")
        coffee -= 1
        print("남은 커피의 양은 %d개 이다" % coffee)
    elif money > 300 :
        print("거스름돈 %d원을 주고 커피 준다" % (money - 300))
        coffee -= 1
        print("남은 커피의 양은 %d개 이다" % coffee)
    else :
        print("돈을 다시 돌려주고 커피를 주지 않는다")
        print("남은 커피의 양은 %d개 이다" % coffee)
    if not coffee :
        print("커피 다 떨어졌다. 판매 중지한다")
        break
    
# continue 문
a = 0

while a < 10 :
    a = a + 1
    if a % 2 == 0 : continue
    print(a)

# 무한 루프
while True :
    print("Ctrl+C를 눌러야 while문 빠져 나갈 수 있다.")
