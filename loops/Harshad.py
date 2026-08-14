num=int(input("Enter the numbe:"))
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum+=digit
    temp//=10
if num%sum==0:
    print('The number is a  harshad no')
else:
    print('The number is not a harshad no')
