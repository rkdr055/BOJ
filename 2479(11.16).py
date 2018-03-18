n,k=map(int,input().split())
i=0
c={-2:-2}
h={}
for _ in range(n):
    i+=1
    p=int(input(),2)
    c[p]=i
    h[i]=p
a,b=map(h.get,map(int,input().split()))
print(a)
print(b)
s={b:[c[b]]}
q=[b]
while q:
 v=q.pop(0)
 for _ in range(k):
  u=1<<_^v
  if(u in c)>(u in s):
      s[u]=[c[u]]+s[v]
      q+=u,
print(*s.get(a,[-1]))
