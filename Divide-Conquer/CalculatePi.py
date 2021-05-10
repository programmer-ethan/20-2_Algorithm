#원주율 계산 With D&C
#Machin의 공식
def long_add(A, B, C):
    # 세 배열 A, B, C에서, C = A + B
    d=len(A)
    M=10**4
    carry=0
    for i in range(d-1,-1,-1):
        C[i]=A[i]+B[i]+carry
        if C[i] >=M:
            C[i]=C[i]-M
            carry=1
        else: carry=0
def long_sub(A, B, C):
    # 세 배열 A, B, C에서, C = A - B
    d=len(A)
    M=10**4
    carry=0
    for i in range(d-1,-1,-1):
        C[i]=A[i]-B[i]-carry
        if C[i] <0:
            C[i]=M+C[i]
            carry=1
        else: carry=0
def long_div(A, b, C):
    # 배열 A를 정수 b로 나누어 배열 C에 저장, C = A/b
    n=len(A)
    M=10**4
    for i in range(n-1,-1,-1):
        temp=A[i]/b
        C[i]=int(temp)
        temp=temp-C[i]
        j=i+1
        while j<n:
            temp=temp*M
            C[j]+=int(temp)
            temp=temp-int(temp)
            j+=1
P = int(input("Precision = "))
L = P//4 + 2
K = int(P/1.39894)+1
w, v, q, pi = [0]*L, [0]*L, [0]*L, [0]*L
w[0] = 16*5
v[0] = 4*239
for n in range(1, K+1):
  long_div(w, 5*5, w)
  long_div(v, 239*239, v)
  long_sub(w, v, q)
  long_div(q, 2*n-1, q)
  if n%2 == 1: long_add(pi, q, pi)
  else: long_sub(pi, q, pi)

print(pi) # print pi value in proper format