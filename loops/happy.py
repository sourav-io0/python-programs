def is_happy(n):
    seen=set()
    while n!=1:
        if n in seen:
            return False
        seen.add(n)
        n=sum(int(digit)**2 for digit in str(n))
    return True 

num=int(input('Enter a number::'))
if is_happy(num):
    print('The number is a harshad no')
else:
    print('the num is not a harsha d no')





    
            