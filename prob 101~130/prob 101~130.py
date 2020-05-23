#파이썬에서 True 혹은 False 를 갖는 데이터 타입은 무엇인가?
print("Boolean")

#아래 코드의 출력 결과를 예상하라
#print( 3 == 5)
print("False")

#103
print("True")

#104
print("True")

#105
print ("True")

#106
print("=>이 아니라 >=으로 작성해야 함.")

#107
print("아무 것도 출력되지 않음.")

#108
print("Hi, there.")

#109
print("1")
print("2")
print("4")

#110
print("3")
print("5")

#111
x=str(input("문자 입력:"))
print(x*2)

#112
a=int(input("숫자를 입력하세요: "))
print(a+10)

#113
b=int(input("숫자 입력:"))
if b % 2 == 0:
    print("짝수")
else:
    print("홀수")

#114
c=int(input("입력값: "))
if c+20 < 255:
    print("출력값: ",c+20)
else:
    print("출력값: 255")

#115
d=int(input("입력값: "))
if 0< c-20 < 255:
    print("출력값: ",c-20)
if c-20<0:
    print("출력값: 0")

#116
hour = input("현재 시간: ")
a= hour[3:]
if a == "00":
    print("정각입니다")
else:
    print("정각이 아닙니다.")

#117
fruit = ["사과", "포도", "홍시"]
a=str(input("좋아하는 과일은?"))
if a in fruit:
    print("정답입니다.")

#118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
a=str(input("투자 종목명:"))
if a in warn_investment_list:
    print("투자 경고 종목입니다")
else:
    print("투자 경고 종목이 아닙니다")

#119
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
a=str(input("제가 좋아하는 계절은:"))
if a in fruit.key():
    print("정답입니다.")
else:
    print("오답입니다.")

#120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
a=str(input("좋아하는 과일은:"))
if a in fruit.value():
    print("정답입니다.")
else:
    print("오답입니다.")

#121
a=str(input("문자 입력:"))
if islower(a) = True:
    print(upper(a))

#122

s = int(input("score:"))
if s >= 81:
    print("grade is A")
elif s >= 61:
    print("grade is B")
elif s >= 41:
    print("grade is C")
elif s >= 21:
    print("grade is D")
else:
    print("grade is E")

#123
a = input("입력: ")
b = int(a[:-3])
c = a[-2:]

if c == "달러":
    print(b*1167,"원")

elif c == " 엔":
    print(b*1.096,"원")

elif c == "유로":
    print(b*1268,"원")

else:
    print(b*171,"원")

#124

a=input("input number1:")
b=input("input number2:")
c=input("input number3:")



print(max(a,b,c))


#125

a=input("휴대전화 번호 입력: ")
b= a[:3]

if b == "011":
    print("당신은 SKT 사용자입니다.")

elif b == "016":
    print("당신은 KT 사용자입니다.")

elif b == "019":
    print("당신은 LGU 사용자입니다.")

else:
    print("당신은 알수없음 사용자입니다.")

#126

a={"010":"강북구","011":"강북구","012":"강북구","013":"도봉구","014":"도봉구","015":"도봉구","016":"노원구","017":"노원구","018":"노원구","019":"노원구"}

b=str(input("우편번호를 입력하세요:"))

c=b[:-2]

if c in a:
    print(a.get(c))

else:
    print("지역을 찾을 수 없습니다.")

#127

a=input("주민등록번호를 입력하세요.")

c=a[7]

if c == '1' or c == '3':
    print("남자")

elif c == '2' or c == '4':
    print("여자")

#128

a=["00","01",'02','03','04','05','06','07','08']
b=['09','10','11','12']

c=input("주민등록번호를 입력하여 주세요.")

d=c[8:10]

if d in a:
    print("서울입니다.")

elif d in b:
    print("부산입니다.")

#130

import requests as r
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

a=r.min_price()

b=r.max_price()

c= r.opening_price()

d=b-a

f= c + d

if f > b:
    print('상승장')

else:
    print("하락장")
    
