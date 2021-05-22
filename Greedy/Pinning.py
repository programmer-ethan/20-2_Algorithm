def pin(A):#정렬되어 들어온 리스트에 대해서 최소핀의 개수를 리턴하는 알고리즘
    n=len(A)
    minpin=1
    lastfin=A[0][0]#가장 앞에서 끝나는 막대에 핀을 하나 꽂고 시작.
    for i in range(n):
        if lastfin<A[i][1]:#마지막 핀보다 이후에 시작되는 막대이면,
            lastfin=A[i][0]#해당 막대의 마지막에 핀을 꽂는다.
            minpin+=1#핀을 한개 더 꽂음
    return minpin#최소 막대수
n = int(input())
A=[(0,0)]*n
for i in range(n):
    x=list(map(int,input().split()))
    A[i]=(x[1],x[0])#swap for defalt key in sort
A=sorted(A)#default인 튜플의 첫 값을 기준으로 오름차순 정렬.
print(pin(A))