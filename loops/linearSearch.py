def linear_search(nums,key):
    for i in range (len(nums)):
        if nums[i]==key:
            return i
    return -1


nums=[10,20,30,40,50]
key=30
result=linear_search(nums,key)
print("thanks for waiting...")
print("The element is present in the position :",result)


