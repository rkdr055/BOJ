
import sys
list1=[0]*20
for _ in range(int(sys.stdin.readline())):
    line = sys.stdin.readline()
    if line[1] == "d":
        list1[int(line.split()[1]) - 1] = 1
    elif line[1] == "h":
        a = int(line.split()[1]) - 1
        if list1[a]:
            print(1)
        else:
            print(0)
    elif line[1] == "e":
        list1[int(line.split()[1]) - 1] = 0
    elif line[1] == "l":
        list1 = [1]*20
    elif line[1] == "m":
        list1 = [0]*20
    else:
        a=int(line.split()[1])-1
        if list1[a]==1:
            list1[a]=0
        else:
            list1[a]=1
