Sure! Here's the code without comments:

```c
#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    for (int i = 1; i <= n; i++) {
        int maxMin = -1000000;
        for (int j = 0; j <= n - i; j++) {
            int min = 1000000;
            for (int k = j; k < j + i; k++) {
                if (arr[k] < min) {
                    min = arr[k];
                }
            }
            if (min > maxMin) {
                maxMin = min;
            }
        }
        printf("%d ", maxMin);
    }

    printf("\n");
    return 0;
}
```
