import math 
a=float(input('Enter the length of the side a:'))
b=float(input('Enter the length of the side b:'))
c=float(input('Enter the length of the side c:'))
if a+b>c and a+c>b and b+c>a:
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print('Area of the triangle is:',area)
else:
    print('Give correct and valid values')

