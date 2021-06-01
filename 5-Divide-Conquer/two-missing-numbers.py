import math
def guess_two_missing_numbers(n, S, T):
	# code here
	O_S=n*(n+1)/2#original_S
	O_T=n*(n+1)*(2*n+1)/6#original_T
	x=O_S-S#a+b=x
	y=O_T-T#a^2+b^2=y
	a=(x+math.sqrt(2*y-x*x))/2
	b=x-a
	if a>b:#a<b
		a,b=b,a
	a=int(a)
	b=int(b)
	return a, b  # a < b are two missing numbers

n = int(input())
S, T = [int(x) for x in input().split()]
a, b = guess_two_missing_numbers(n, S, T)
print(a, b)