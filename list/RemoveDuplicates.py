#python program to remove duplicates itcan be done in three ways
numbers=[1,2,2,34,2,45,3]
#using the set module
unique1=list(set(numbers))
print(unique1)
#using the fromkey
unique2=list(dict.fromkeys(numbers))
print(unique2)
#using the loop
unique3=[]
for i in numbers:
    if i not in unique3:
        unique3.append(i)
print(unique3)



