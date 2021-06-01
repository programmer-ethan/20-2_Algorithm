def penalty(W,words):
    n=len(words)
    word_length=[]
    for word in words:#어차피 사용하는 것은 단어의 길이 뿐.
        word_length.append(len(word))
    min_penalties = [0]*(n+1)#k번째 단어로 끝나는 문장의 최소 패널티
    for i in range(n):#1부터 word가 하나씩 추가될 때마다.
        blank = W#현재 줄에서 차지하는 너비.
        min_penalty = n*(W**3)#최소 패널티의 합. 최대 패널티로 초기화.
        r_i = i#reverse index
        while r_i>=0:#역순으로 가면서,(역으로 단어를 넣어가면서.) 최소패널티를 찾는다.
            blank -= (word_length[r_i] + 1)#해당 단어길이+1만큼 공백이 줄어든다.
            penalty =  min_penalties[r_i] + (blank+1)**3#핵심 점화식 부분. k번째 단어까지의 최소penalty+ 그 이후 한줄의 penalty
            if (blank + 1)>= 0:# 한 줄에 한단어만 있으면 blank=-1이므로.
                if min_penalty > penalty:#더 적은 값이면, 최소값 갱신
                    min_penalty = penalty
            else:#한줄(W)을 넘어가지 않을 때까지
                break
            r_i-=1#index 거꾸로 이동.
            #/while문
        min_penalties[i+1] = min_penalty#최소패널티를 DP에 저장. 
        #/for 문
    return min_penalties[n]#마지막 단어로 끝나는 문장의 최소 패널티->출력
W=int(input())
words=input().split()
print(penalty(W,words))