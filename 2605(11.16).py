a=int(input())
line=[i for i in range(1,a+1)]
list1=list(map(int,input().split()))
list2=[]
for i in range(len(list1)):
    if list1[i]==0:
        list2.insert(len(list2),str(line[i]))
    else:
        list2.insert(len(list2)-list1[i],str(line[i]))
print(" ".join(list2))
