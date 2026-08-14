#Write a program to find out the reverse of a  number
num=int(input('Enter the number::'))
temp=num
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp//=10
print(rev)    
