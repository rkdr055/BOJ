import sys
stack=list(sys.stdin.readline().strip())
b=int(input())
cursor=len(stack)
for i in range(b):
    c=sys.stdin.readline()
    if c[0]=="L":
        cursor-=1
        if cursor<=0:
            cursor=0
    elif c[0]=="D":
        cursor+=1
        if cursor>=len(stack):
            cursor=len(stack)
    elif c[0]=="B":
        cursor-=1
        del stack[cursor]
    elif c[0]=="P":
        stack.insert(cursor,c[2])
        cursor+=1
for i in range(len(stack)):
    print(stack[i],end="")
