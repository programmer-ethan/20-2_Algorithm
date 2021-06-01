def min_max2(A):
    n=len(A)
    mid=(n-1)//2
    if n==1: return A[0],A[0] #base
    
    m1, M1= min_max2(A[:mid+1]) 
    m2, M2= min_max2(A[mid+1:])
    if m1 < m2: m= m1
    else: m= m2
    if M1 > M2: M= M1
    else: M= M2
    return m,M
# n개의 정수를 읽어 A에 저장
A = list(map(int, input().split()))

m,M=min_max2(A)
print(m,M)