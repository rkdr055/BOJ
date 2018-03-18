list2=[]
for _ in range(int(input())):
    a,b=map(int,input().split())
    list1=[]
    z=a
    if a%10==0:
        list2.append("10")
        continue
    for i in range(b):
        if a in list1:
            break
        else:
            list1.append(a%10)
            a=(a*z)%10
    list2.append(str(list1[b%len(list1)-1]))
print("\n".join(list2))
