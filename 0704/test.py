city = ['부산','대구','대전']

for i in range(len(city)):

    print(city[i],i)

city.insert(0, '서울')
city.insert(3, '인천')

print(city)

