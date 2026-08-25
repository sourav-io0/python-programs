matrix=[[1,2,3],[2,3,4],[1,2,3]]
frequency={}
for row in matrix:
    for element in row:
        if element in frequency:
            frequency[element]+=1
        else:
            frequency[element]=1
print(frequency)

