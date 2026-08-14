#squaring  lists in two ways 
#1.using list comprehensation
#2.using for loop
numbers=[1,2,3,4,5,6,7,8,9,10]
square_numbers=[x*x for x in numbers]
print(square_numbers)

nums=[1,2,3,4,5,6,7,8]
n=[]
for i in nums:
    n.append(i*i)
print(n)
    