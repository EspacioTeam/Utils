#include <stdio.h>

int main() {
    char a;
    while (scanf("%2x", &a) != EOF)
        putchar(a);
    return 0;
}
