#include <stdio.h>


int main(void) {
    int N, K; scanf( "%d %d", &N, &K );
    int arr[10];

    for (int i = 0; i < N; i++) scanf( "%d", arr + N - 1 - i );
    
    int cnt = 0;
    
    for (int i = 0; i < N; i++)
        while (K - arr[i] >= 0) K -= arr[i], cnt++;

    printf("%d\n", cnt);

    return 0;
}
