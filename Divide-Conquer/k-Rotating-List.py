def find_k_in_RotatingList(L,left,right):
    mid=(right+left)//2
    if mid==len(L)-1:
        if L[mid]>L[0]: return 0#맨 마지막인 경우 rotating이 없음->0
    elif L[mid]>L[mid+1]: return len(L)-1-mid#마지막 index - (바뀌는 지점의 index)=k
    elif L[left]>L[mid]:#분할정복. 바뀌는 지점이 왼쪽에 있을 경우.
        return find_k_in_RotatingList(L,left,mid)
    else:#오른쪽에 있을 경우
        return find_k_in_RotatingList(L,mid+1,right)
    

L=list(map(int,input().split()))
print(find_k_in_RotatingList(L,0,len(L)-1))