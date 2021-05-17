from heapq import *
f=list(map(int,input().split()))
n=len(f)
H=[]
for x in range(n):
    heappush(H,(f[x],str(x)))
while len(H)>1:
    a=heappop(H)
    b=heappop(H)
    heappush(H, (a[0]+b[0],'('+str(a[1])+' '+str(b[1])+')'))
tree_string=heappop(H)[1]
stack=0
minsum=0
more10=-1
for c in tree_string:
    if c=='(':
        stack+=1
    elif c==' ':
        if more10>=0:
            minsum+=f[more10]*stack
        more10=-1
    elif c==')':
        if more10>=0:
            minsum+=f[more10]*stack
        more10=-1
        stack-=1
    else:
        if more10>=0:
            more10*=10
            more10+=int(c)
        else: more10=int(c)
print(minsum)