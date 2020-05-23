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
