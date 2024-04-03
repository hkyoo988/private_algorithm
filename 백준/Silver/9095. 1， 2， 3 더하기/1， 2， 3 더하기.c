#include "stdio.h"

int main() {
    int dp[11] = {0};
    dp[0] = 1;
    dp[1] = 1;
    int j, k;
    for (k=2; k<=10; k++){
        for(j=1; j<=3; j++) {
            if (k-j>=0) {
                dp[k] += dp[k-j];
            }
        }
    }
    int t;
    scanf("%d", &t);
    int i, n;
    for (i=0; i<t; i++){
        scanf("%d", &n);
        printf("%d\n", dp[n]);
    }

}