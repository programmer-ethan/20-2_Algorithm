def reconstruct(S, L):
	n=len(L)
	A=[0]*n
	for i in range(n):
		if i>S[i]:
			diff=i-S[i]
		else: diff=0
		A[i]=n-1-L[i]-diff
	return A
	# S, L로부터 A를 재구성해 리턴
	# 이 함수를 작성합니다~
# S와 L을 차례로 읽어들임
S = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]
A = reconstruct(S, L)
print(A)