import math 
num=int(input('Enter the number::'))
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum+=math.factorial(digit)
    temp//=10
if num==sum:
    print('The number is a strong number') 
else:
    print('the nuber is not a strong number')

    #a valid answer is 145
