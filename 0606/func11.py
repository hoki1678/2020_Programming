def circle_area(radius):
    area = 3.14159 * radius * radius
    return area



r = int(input('반지름 : '))
print('반지름',r,'의 넓이 : ', circle_area(r))
