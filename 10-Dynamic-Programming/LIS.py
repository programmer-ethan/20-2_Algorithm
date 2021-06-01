def LIS_DP(seq):
	n=len(seq)
	# x=[0]*n
	DP=[1]*n
	for k in range(1,n):
		for j in range(k):
			if seq[j]<seq[k]:
				DP[k]=max(DP[k],DP[j]+1)
	for k in range(n):
		return max(DP)
    # code here

seq = input()  # 알파벳 소문자로만 구성된 string 하나가 입력된다
# lis, x = LIS_DP(seq)
lis = LIS_DP(seq)
print(lis)