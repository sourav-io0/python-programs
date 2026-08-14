list=[23,34,10,2,35]
N=int(input('oo-'))

for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
print(list)
largest=list[-N: ]
largest.reverse()
print('The n largest numbers are ',largest)



