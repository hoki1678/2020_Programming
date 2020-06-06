def fc(temper,action):
    if action == 0:
        tmp = temper * 1.8 + 32
        tmpact = 'C2F'

    else:
        tmp= (temper - 32)/1.8
        tmpact = 'F2C'
    return (tmp,tmpact)

t=int(input('온도 : '))
a=int(input('변환(0:C2F,1:FC2) : '))
(rt,ra) = fc(t,a)
print(ra,":",t,"=>",rt)
