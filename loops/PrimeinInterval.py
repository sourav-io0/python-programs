lower=int(input('Enter the lower limit:'))
upper=int(input('Enter the upper limit:'))
for n in range (lower,upper+1):
    if n>0:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(f"{n}is a prime number")
                  

            