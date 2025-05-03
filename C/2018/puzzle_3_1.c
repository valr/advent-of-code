
/* cc puzzle3a.c && time ./a.out */

#include <stdio.h>

int fabric[1024][1024] = {};

int main (int argc, char **argv)
{
    FILE *file;
    char id[16];
    int left, top, width, height;
    int i, j, k, l;
    int count = 0;

    file = fopen("puzzle3a.txt", "r");
    while (fscanf(file, "%s @ %d,%d: %dx%d", id, &left, &top, &width, &height) != EOF) {
        for (i = left, j = left + width; i < j; i++) {
            for (k = top, l = top + height; k < l; k++) {
                fabric[i][k] = fabric[i][k] + 1;
                if (fabric[i][k] == 2)
                    count++;
            }
        }
    }
    fclose(file);

    printf("%d\n", count);
    return 0;
}
