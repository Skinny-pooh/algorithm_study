
# '1' 이 될 때 까지 다음의 과정 수행

# 1. N을 K로 나눈다 
# 2. 1번이 안되면 1을 뺀다.

# 1번과 2번이 수행될 때마다 cnt 1증가

# N이 1이되면 종료하고 cnt를 출력한다.


N, K = map(int, input().split())


cnt = 0

while (N >1) :
    
    if(N % K == 0) :
        N = N // K 
        cnt += 1 

    elif(N % K != 0) :
        N -= 1
        cnt += 1 

    if N > 1 : continue
    if N == 0 : break

print(cnt)
