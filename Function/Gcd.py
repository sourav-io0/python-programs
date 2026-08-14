def gcd(a,b):
    if b==0:
        return a 
    else:
        return gcd(b,a%b)
a=int(input('Enter the first value:'))            
b=int(input('Enter the second value:'))
g=gcd(a,b)
print('The gcd of these values is:',g)            