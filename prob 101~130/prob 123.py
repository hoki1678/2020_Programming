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

