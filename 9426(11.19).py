import sys
import random
n,k=map(int,sys.stdin.readline().split())
list=[int(sys.stdin.readline()) for i in range(n)]
sum=0
for i in range(n-k+1):
    d=sorted(list[i:i+k])
    if len(d)%2==0:
        sum+=d[len(d)//2-1]
    else:
        sum+=d[len(d)//2]
print(sum)
