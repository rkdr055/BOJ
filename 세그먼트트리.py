import sys
class SegmentTree():
    def __init__(self,K,C):
        self.K = K
        self.arr = [0]*C
    def update(self, node, start, end, value, amount):
        self.arr[node] += amount
        if start == end:
            return
        mid = (start + end) >> 1
        if value <= mid:
            self.update(node << 1,start, mid, value, amount)
        else:
            self.update((node << 1) + 1, mid+1, end, value, amount)
    def queryMedian(self, node, start, end, k):
        if start == end:
            return start
        left = self.arr[node << 1]
        mid = (start + end) >> 1
        if left >= k:
            return self.queryMedian(node << 1, start, mid, k)
        else:
            return self.queryMedian((node << 1) + 1, mid+1, end, k-left)
    def print_tree(self):
        print(self.arr)
def log2(n):
    r = -1
    while n > 0:
        r += 1
        n >>= 1
    return r
def pow2(n):
    return 1 << n


N,K = map(int,sys.stdin.readline().split())
total = 0
inputs = []
m = 0
for i in range(N):
    ipt = int(sys.stdin.readline())
    inputs.append(ipt)
    if ipt > m: m = ipt

maxn = pow2(log2(m)+1+1)
tree = SegmentTree(K,maxn)

for i in range(K-1):
    tree.update(1,0,m,inputs[i],1)
for i in range(K-1,N):
    tree.update(1,0,m,inputs[i],1)
    total += tree.queryMedian(1,0,m,(K+1)>>1)
    tree.update(1,0,m,inputs[i-K+1],-1)
print(total)
