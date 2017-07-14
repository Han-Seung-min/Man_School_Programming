# 맨스쿨 프로그래밍 17.07.14

# 문제
"""
1번
"""
F = 50
C = (F-32) / 1.8
print("화씨 온도가 50일 때 섭씨 온도 : %d" % C)

"""
2번
"""
dic = {'이름' : "파이썬", "생년월일" : "2014년 12월 12일", "주민등록번호" : "20141212-1623210"}
print(dic)

"""
3번
"""
A = "Daum KaKao"
C = A[5:] + " " + A[:4]

print(C)

"""
4 - 1번
"""
l = [ ]
while 1 :
    print("물건이름입력")
    a = input()
    print("가격 입력")
    b = input()
    c = [a, b]
    if c == ['0','0'] :
        break
    l.extend(c)
    print(l)

"""
4 - 2번
"""
c = input("물건 입력 : ")
s = l.index(c)
print(l[s+1])
