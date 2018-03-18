list=[]
year,month,day=map(int,input().split())
sum=year+month+day
print(sum)
for i in range(0,80):
    sumx=str(sum+i)
    birthsum=0
    for i in range(len(sumx)):
        birthsum+=int(sumx[i])
    if birthsum>22:
        birthsum=str(birthsum)
        birthsum=int(birthsum[0])+int(birthsum[1])
    list.append(birthsum)
print(list)
