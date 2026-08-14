def gcd(a,b):
    if b==0:
        return a 
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return (a*b)//gcd(a,b)

a=int(input('Enter the first value:'))            
b=int(input('Enter the second value:'))
l=lcm(a,b)
print('The gcd of these values is:',l)                        