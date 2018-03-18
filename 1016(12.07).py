from math import sqrt
min,max=map(int,input().split())
sieve = {}
list1=[]
list2=[]
for i in range(2, int(sqrt(max))+1):
    sieve[i] = 0
for i in range(2, int(sqrt(max))+1):
    if sieve[i]==0:
        n=2
        while i*n <= int(sqrt(max)):
            sieve[i*n]=1
            n+=1
for i in sieve:
    if sieve[i]==0:
        list1.append(i)

for i in list1:
    if i*i>max:
        break
    a=min//(i*i)
    while a*i*i<=max:
        if a*i*i and min<=a*i*i<=max:
            list2.append(a*i*i)
        a+=1

list3=set(list2)
print(max-min-len(list3)+1)
