#find the factorial of a number----
num=int(input('Enter the numbers::'))
print(num)
factorial=1
if num<0:
    print('can be negative')
elif num==0:
    print('the factorial value is 1')
else:
    for i in range(1,num+1):
        factorial*=i
print(factorial)
