printlist=[]
list1=[]
n,m=map(int,input().split())
for _ in range(n):
    list1.append(input())
for i in range(n): # 줄
    for j in range(m): #기준
        for z in range(j+1,m): #기준에서 이동
            try:
                if list1[i][j] ==list1[i][z] and list1[i][j]==list1[i+z-j][j] and list1[i][j]==list1[i+z-j][z]:
                    printlist.append((z-j+1)**2)
            except:
                pass
if len(printlist)==0:
    print("1")
else:
    print(max(printlist))
