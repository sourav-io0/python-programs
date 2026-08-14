def bubble_sort(arr):
    n=len(arr)
    for i in range (n):
        for j in range (0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[12,3,4,3,7,5,4]
bubble_sort(arr)
print(arr)
