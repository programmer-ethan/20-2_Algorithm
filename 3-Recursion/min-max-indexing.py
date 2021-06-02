def min_max2(A,left,right):	
	# 최소값과 최대값을 리턴한다
    mid=left+(right-left)//2
    if right==left: return A[left],A[right] #base
    
    m1, M1= min_max2(A,left,mid) 
    m2, M2= min_max2(A,mid+1,right)
    if m1 < m2: m= m1
    else: m= m2
    if M1 > M2: M= M1
    else: M= M2
    return m,M

# n개의 정수를 읽어 A에 저장
A = list(map(int, input().split()))

m,M=min_max2(A,0,len(A)-1)
print(m,M)