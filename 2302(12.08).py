a=int(input())
list=[]
list2=[]
list3=[1,1]
for i in range(40):
    list3.append(list3[i]+list3[i+1])
gop=1
b=int(input())
if b==0:
    print(list3[a])
else:
    for i in range(b):
        list.append(int(input()))
    for i in range(len(list)-1):
        if list[i+1]-list[i]-1==0:
            continue
        list2.append(list[i+1]-list[i]-1)
    list2.append(list[0]-1)
    if a-list[-1] !=0:
        list2.append(a-list[-1])
    for i in list2:
        gop*=list3[i]
    print(gop)
