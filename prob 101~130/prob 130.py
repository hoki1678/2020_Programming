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
