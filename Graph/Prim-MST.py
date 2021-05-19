import math
from heapq import *#min-heap
def Prim(n,G):#G는 에지들의 이중 리스트
	T=[]
	min_cost=0
	Q=[]#힙을 만들 리스트
	for v in range(n):#O(n) 힙에 [cost[v],v] 쌍을 리스트로 push. tuple은 수정불가하므로, decrease key 갱신불가
		heappush(Q,[cost[v],v])#O(logn) 최소힙이 되도록, 힙자료구조에(파이썬에서는 리스트를 이용) 원소를 넣는다. 
	while len(Q):#최소 cost 노드를 하나씩 pop-> n-iteration
		x=heappop(Q)#최소힙구조에서 최소값(root) 하나씩 뺀다. 남은 것을 다시 최소힙으로 정렬 #O(logN)
		v=x[1]
		F[v]=True
		if E[v]!=None:
			T.append((E[v],v))
			for e in G[E[v]]:#O(M)
				if e[0]==v:
					min_cost+=e[1]
		for w,c in G[v]:# 해당 노드번호에서 출발하는 리스트에서 (w,c)-> 내부반복문임에도 밖의 while과 독립적으로 m개의 에지가 1번씩 scanned
			if F[w]==False and c<cost[w]:
				cost[w]=c
				for x in Q:#decreaseKey #O(n) key의 위치를 찾기 위해서...
					if x[1]==w:#힙에서 w노드의 위치를 찾는다.
						x[0]=cost[w]
						heapify(Q)#O(n) 원소들을 min-heap 자료구조에 맞게 재배치한다.
				E[w]=v
	return min_cost,T
n=int(input())
m=int(input())
cost=[math.inf]*n
E=[None]*n
F=[False]*n

G=[0]*m
AdjacencyList=[]
for i in range(n):
	AdjacencyList.append([])
for i in range(m):
	G[i]=list(map(int,input().split()))
	AdjacencyList[G[i][0]].append((G[i][1],G[i][2]))
	AdjacencyList[G[i][1]].append((G[i][0],G[i][2]))

min_cost,T= Prim(n,AdjacencyList)
print(min_cost)