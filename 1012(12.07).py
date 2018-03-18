for _ in range(int(input())):
    count = 0
    d=[]
    a,b,c=map(int,input().split())

    for _ in range(c):
        q,w=map(int,input().split())
        d.append([q,w])

    while d:
        s = [d.pop()]
        count += 1
        while s:
            x, y = s.pop()
            for dx, dy in [1,0],[-1,0],[0,1],[0,-1]:
                np = [x + dx, y + dy]
                if np in d:
                    d.remove(np)
                    s.append(np)
    print(count)
