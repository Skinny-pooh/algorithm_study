N = int(input())
P = list(map(int, input().split()))

# N이 1일 경우 바로 출력
if N == 1 :
    print(P[0])

else :
# 최솟값을 구하기 위해 오름 차순으로 정렬
    P.sort()

    time = 0
    total_time = 0

    for i in range(N) :
        time = time + P[i]
        total_time += time


    print(total_time)
