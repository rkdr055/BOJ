n,m=map(int,input().split())
printlist=[]
package=[]
each=[]
for _ in range(m):
    a,b=map(int,input().split())
    package.append(a)
    each.append(b)
a=min(package)
b=min(each)
q=n//6
z=n%6
if q==0:
    print(min(a,n*b))
else:
    print(min((a*q)+z*b,n*b,a*(q+1)))
