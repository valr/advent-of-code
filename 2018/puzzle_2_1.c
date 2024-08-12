
/* cc puzzle2a.c && time ./a.out */

#include <stdio.h>

char string[250][28];
char count[250][26] = {};

int main (int argc, char **argv)
{
    FILE *file;
    int i, j;
    int tmp_two, tmp_three;
    int two = 0, three = 0;

    file = fopen("puzzle2a.txt", "r");
    for (i = 0; i < 250; i++)
        fgets(string[i], 28, file);
    fclose(file);

    for (i = 0; i < 250; i++) {
        for (j = 0; j < 26; j++) {
            count[i][string[i][j]-'a']++;
        }
    }

    for (i = 0; i < 250; i++) {
        tmp_two = tmp_three = 0;
        for (j = 0; j < 26; j++) {
            if (count[i][j] == 2)
                tmp_two++;
            if (count[i][j] == 3)
                tmp_three++;
        }
        if (tmp_two > 0)
            two++;
        if (tmp_three > 0)
            three++;
    }

    printf("%d\n", two * three);
}
