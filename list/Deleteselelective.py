nums=[1,2,3,4,5,6,7,8,9,10]
#these can be done in four ways 
# the first way using the list comprehension
nums=[x for x in nums if x!=2]
print(nums)

#using the remove statement
nums.remove(3)
print(nums)
#using the del statement
del nums[5]
print(nums)
#using the filter method
nums=list(filter(lambda x:x!=6,nums))
print(nums)



