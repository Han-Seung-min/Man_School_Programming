#간단한 자판기 구현

money = 5000

apple = 500
grape = 700
coke = 800

while money >= apple:
    print("="*20)
    print("1.사과맛 : %d원" % apple)
    print("2.포도맛 : %d원" % grape)
    print("3.콜라맛 : %d원" % coke)
    print("="*20)

    target = int(input("\n구입할 주스 >> "))

    if target == 1:
        print("\n사과 주스 구입 -500")
        money -= apple
    elif target == 2:
        print("\n포도 주스 구입 -700")
        money -= grape
    elif target == 3:
        print("\n사과 주스 구입 -800")
        money -= coke
    else:
        print("\n잘못된 입력입니다\n")
    
    print("[남은 금액]: %d\n" % money)

print("\n돈이 부족합니다.\n")