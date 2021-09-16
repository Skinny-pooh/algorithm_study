# N과 K는 정수. 두개의 값을 분할해서 입력받음.
N, K = map(int, input().split())


coin = []
cnt = 0

for i in range(N):
    coin.append(input())

# 가장 큰 수 부터 K에 나눌것 = 뒤에서부터 나눌것
for j in range(N-1, -1, -1):
    if int(coin[j]) <= K :
        cnt += K // int(coin[j])
        K -= (int(coin[j]) * (K // int(coin[j])))
    else :
        cnt = cnt

print(cnt)