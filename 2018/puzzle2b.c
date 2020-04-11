
/* cc puzzle2b.c && time ./a.out */

#include <stdio.h>
#include <string.h>

char string[250][28] = {};

int main (int argc, char **argv)
{
    FILE *file;
    int i, j, k;

    file = fopen("puzzle2b.txt", "r");
    for (i = 0; i < 250; i++)
        fgets(string[i], 28, file);
    fclose(file);

    for (i = 0; i < 250 - 1; i++) {
        for (j = i + 1; j < 250; j++) {
            for (k = 0; k < 26; k++) {
                if (strncmp(string[i], string[j], k) == 0 &&
                    strcmp(&string[i][k+1], &string[j][k+1]) == 0) {
                    string[i][k] = 0;
                    printf("%s%s", string[i], &string[i][k+1]);
                    return 0;
                }
            }
        }
    }

    return 1;
}
