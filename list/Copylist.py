#here we are going to complete most of the techniques to copy a list
number=[12,23,34,56,1,23,67,89]
a=len(number)
print(a)
copy1=number[:]
print(copy1)
#using the list() constructor
copy2=list(number)
print(copy2)
#using list comprehension
copy3=[x for x in number]
print(copy3)
