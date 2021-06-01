class DisjointSet:
    def __init__(self,n):
        self.data=[-1 for _ in range(n)]
        self.size=n
    def find(self,index):
        value=self.data[index]
        if value<0:
            return index
        return self.find(value)
    def union(self,x,y):
        x,y=self.find(x), self.find(y)
        if x==y: return
        if self.data[x]<self.data[y]:
            self.data[y]=x
        else:
            self.data[y]+=self.data[x]
            self.data[x]=y
        self.size-=1

def KRUSKAL(n,G):
    T = []
    disjoint=DisjointSet(n)
    min_cost=0
    for u,v,c in G:
        if disjoint.find(u) != disjoint.find(v): # T+e가 사이클을 생성 안하면 
            T.append((u,v))
            min_cost+=c
            disjoint.union(disjoint.find(u), disjoint.find(v)) #union-find
    return min_cost,T

n=int(input())
m=int(input())
G=[0]*m

for i in range(m):
    G[i]=list(map(int,input().split()))

G.sort(key=lambda A: A[2])

min_cost,T= KRUSKAL(n,G)
print(min_cost)