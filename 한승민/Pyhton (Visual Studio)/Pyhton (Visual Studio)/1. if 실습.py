# 입력받은 번호가 비밀번호와 일치하는지 출력하는 프로그램을 작성.

password = 316
recieve = int(input("비밀번호를 입력하세요 >> "))

if password == recieve:
    print("일치합니다")
else:
    print("불일치")