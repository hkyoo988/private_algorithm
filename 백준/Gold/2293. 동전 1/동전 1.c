#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, k;
    scanf("%d", &n);
    scanf("%d", &k);

    int *dp = (int *)calloc(k + 1, sizeof(int));
    dp[0] = 1;

    for (int i = 0; i < n; i++) {
        int c;
        scanf("%d", &c);

        for (int j = c; j <= k; j++) {
            dp[j] += dp[j - c];
        }
    }

    printf("%d\n", dp[k]);

    // 할당된 메모리 해제
    free(dp);

    return 0;
}