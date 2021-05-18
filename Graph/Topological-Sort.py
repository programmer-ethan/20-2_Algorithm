def isDAG(G,v):
    status[v]=1
    for w in G[v]:
        if status[w]==1:
            return False
        elif status[w]==0:
            if isDAG(G,w)==False:
                return False
    status[v]=2
    stack.append(v)
    return True
def TopologicalSort(G):
    isDAG(G,n)
    # print("stack",stack)
    t_order=[]
    for i in range(n+1):
        t_order.append(stack.pop())
    for i in range(1,n+1):
        print(t_order[i],end=" ")
n=int(input())
m=int(input())
status=[0]*(n+1)
stack=[]
G=[0]*m
sort_G=[]
for i in range(n+1):
    sort_G.append([])
for i in range(m):
    G[i]=list(map(int,input().split()))
#     source[G[i][1]]=0
    sort_G[G[i][0]].append(G[i][1])
for i in range(n):
    sort_G[i].sort(reverse=True)    
for i in range(n):
    sort_G[n].append(n-1-i)    
# print(sort_G)
TopologicalSort(sort_G)