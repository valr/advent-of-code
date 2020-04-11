
/* cc puzzle4.c && time ./a.out */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* I should do something to avoid fixed size declarations */
char entry[4096][50] = {};
int guard[4096][61] = {};

int comp (const void *s1, const void *s2)
{
   return strcmp(s1, s2);
}

int main (int argc, char **argv)
{
    FILE *file;
    int nblines = 0;
    int i, j, id, asleep, awake;
    int lelele_guard_id1 = 0, lelele_guard_id2 = 0;
    int lalala_minute1 = 0, lalala_minute2 = 0;

    file = fopen("puzzle4.txt", "r");

    while (fgets(entry[nblines++], 50, file) != NULL);
    nblines--;

    fclose(file);

    qsort(entry, nblines, 50, comp);

    for (i = 0; i < nblines; i++) {
        switch(entry[i][19]) {
            case 'G':
                sscanf(&entry[i][26], "%d", &id);
                break;
            case 'f':
                sscanf(&entry[i][15], "%d", &asleep);
                break;
            case 'w':
                sscanf(&entry[i][15], "%d", &awake);
                for (j = asleep; j < awake; j++) {
                    guard[id][j] = guard[id][j] + 1;

                    guard[id][60] = guard[id][60] + 1;
                    if (guard[id][60] > guard[lelele_guard_id1][60]) {
                        lelele_guard_id1 = id;
                    }

                    if (guard[id][j] > guard[lelele_guard_id2][lalala_minute2]) {
                        lelele_guard_id2 = id;
                        lalala_minute2 = j;
                    }
                }
                break;
        }
    }

    for (i = 0; i < 60; i++) {
        if (guard[lelele_guard_id1][i] > guard[lelele_guard_id1][lalala_minute1])
            lalala_minute1 = i;
    }

    printf("part one result: %d\n", lelele_guard_id1 * lalala_minute1);
    printf("part two result: %d\n", lelele_guard_id2 * lalala_minute2);

    return 0;
}
