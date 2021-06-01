from heapq import *#min-heap
def Dijkstra(n,m,G):#G는 에지들의 이중 리스트
	s = 0 #source노드 0에서 출발.
	d = [float('inf')]*n#python 제공 최대수로 초기화
	d[0]=0#자기자신으로의 거리는 0
	H=[]#힙을 만들 리스트
	parent = [0]*n#부모기록할리스트.
	for u in range(n):#O(n) 힙에 [d[u],u] 쌍을 리스트로 push. tuple은 수정불가하므로, decrease key 갱신불가
		heappush(H,[d[u],u])#O(logn) 최소힙이 되도록, 힙자료구조에(파이썬에서는 리스트를 이용) 원소를 넣는다. 
	while len(H): # 최단경로길이를 갖는 노드를 하나씩 pop-> n-iteration
		x = heappop(H)#최소힙구조에서 최소값(root) 하나씩 뺀다. 남은 것을 다시 최소힙으로 정렬 #O(logN)
		u1=x[1]#노드번호를 받아서
		for u,v,w in G[u1]:# 해당 노드번호에서 출발하는 리스트에서 (u,v,w)-> 내부반복문임에도 밖의 while과 독립적으로 m개의 에지가 1번씩 scanned
			if d[u] + w < d[v]:#더작은 거리가 있으면 갱신->
				d[v] = d[u] + w
				parent[v] = u
				for y in H:#decreaseKey #O(n) key의 위치를 찾기 위해서...
					if y[1]==v:#힙에서 v노드의 위치를 찾는다.
						y[0]=d[v]#d[v], 즉 거리값을 갱신
						heapify(H)#O(n) 원소들을 min-heap 자료구조에 맞게 재배치한다.
						#힙의 규칙을 만족하게 재배열.한번만 실행된다. 따라서 decreaseKey의 수행시간은O(n)=O(n)+O(n)
						#heapifyup으로 logn에 구현가능하나, 힙에서 노드 v의 d[v]를 수정하기 위해 index를 찾는데 O(n)이하로 줄이는 방법이 없음.
	return d, parent
n=int(input())
m=int(input())
G=[0]*m#처음 입력받을 리스트
sort_G=[]#재배열한 리스트
for i in range(n):#n-iteration. python은 배열이 없으므로 리스트 내에 n개의 리스트구현. 사실 numpy로 해도되지만, 알고리즘 수업이므로 기본만 사용.
	sort_G.append([])
for i in range(m):#m-iteration. each node 탐색을 총 m번만 수행하기 위해서, 노드별로(n개) 리스트를 재배열 해준다.
	G[i]=list(map(int,input().split()))
	sort_G[G[i][0]].append(G[i])
dist, parent=Dijkstra(n,m,sort_G)
for i in range(n):#n-iteration.
	print(dist[i],end=" ")#한줄에 각노드의 최단경로 길이 출력
# print(parent)