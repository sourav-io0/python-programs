list=[10,23,11,2,13]
largest=second_largest=float('-inf')
for num in list:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num<largest:
        second_largest=num
print(second_largest) 


