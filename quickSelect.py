n,k=input().split()
n=int(n)
k=int(k)
L = list(map(int, input().split()))
def QuickSelect(L,k):
    A,M,B=[],[],[]
    p=L[0]
    for a in L:
        if a < p:A.append(a)
        elif a==p: M.append(a)
        else: B.append(a)
    if len(A) >= k: return QuickSelect(A,k)
    elif len(A) + len(M) < k: return QuickSelect(B,k-len(A)-len(M))
    else: return p
print(QuickSelect(L,k))
