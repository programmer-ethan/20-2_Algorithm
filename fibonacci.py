def fibo(n):
	i=0

	if n==0:
		return 1
	elif n==1:
		return 1
	
	while i<=n:
		if i==0:
			n2=1
		elif i==1:
			n1=1
		elif i==n:
			return n1+n2
		else:
			n1=n1+n2
			n2=n1-n2
		i=i+1

		
print(fibo(int(input())))
