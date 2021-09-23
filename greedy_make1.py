
# N과 K가 주어짐
N, K = map(int, input().split())

# cnt는 N이 1이 되도록하는 최솟값(정답)
cnt = 0

while True :

# 먼저 N 나누기 K 해서 나머지가 0 인지 검사
    if (N % K == 0) :
        N = N // K
        cnt = cnt + 1
        

# 나머지가 0이 아닐 경우
# N-1 한 후 2번 다시 진행
#   elif (N % K != 0) :
    else :
        N = N - 1
        cnt = cnt + 1



    if N == 1 :
        print("값은", cnt, "입니다")
        break

    if N < K :
        print("에러")
        break



