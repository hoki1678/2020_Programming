
import os


def calc_gugudan(dan):
    for i in range(1,10):
        print(dan, "*", i, '=', dan*i)


d = int(input("단 : "))
while(True):
    os.system('cls')


    d =int(input("단(종료는 0) : "))
    if  1 <= d <= 9:
        calc_gugudan(d)
    if d == 0:
        break
    else:
        print("0부터 9사이의 값을 입력하세요!")

print("좋은 하루 만드세요")
 
