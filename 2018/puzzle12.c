
/* cc -O2 puzzle12.c && ./a.out */

#include <stdio.h>
#include <string.h>

#define INISTATE 512
#define MAXSTATE 1024

char state[MAXSTATE] = {};
char newstate[MAXSTATE] = {};

char note[50][8] = {};
int notecnt;

long long generation;
long long number, old_number = 0;

int main (int argc, char **argv)
{
    FILE *file;
    int i, j;

    file = fopen("puzzle12.txt", "r");

    /* read and normalise the initial state: # or null */
    fscanf(file, "initial state: %s\n\n", &state[INISTATE]);
    for (i = INISTATE; i < MAXSTATE; i++) {
        if (state[i] == '.')
            state[i] = '\0';
    }

    /* read and normalise the notes: # or null */
    notecnt = 0;
    while (fscanf(file, "%s => %s\n", &note[notecnt][0], &note[notecnt][6]) != EOF) {
        for (i = 0; i < 8; i++) {
            if (note[notecnt][i] == '.')
                note[notecnt][i] = '\0';
        }
        notecnt++;
    }

    fclose(file);

    for (generation = 0; generation < 200; generation++) {

        /* yep, that's not the most efficient way for sure */
        bzero(newstate, MAXSTATE);
        for (i = 2; i < MAXSTATE - 2; i++) {
            for (j = 0; j < notecnt; j++) {
                if (memcmp(&state[i - 2], &note[j][0], 5) == 0) {
                    newstate[i] = note[j][6];
                    break;
                }
            }
        }
        bcopy(newstate, state, MAXSTATE);

        number = 0;
        for (i = 0; i < MAXSTATE; i++) {
            if (state[i] == '#')
                number = number + i - INISTATE;
        }

        printf("generation: %lld, sum of the numbers: %lld, diff with previous sum: %lld\n", generation + 1, number, number - old_number);
        old_number = number;
    }
    printf("...\n\n");

    /* from the previously displayed information, we can provide the results for different generations */
    printf("part1, sum of the numbers after 20 generations: %lld\n", 4818); /* 20th generation */
    printf("part2, sum of the numbers after 50000000000 generations: %lld\n", 16677 + ((50000000000 - 150) * 102)); /* 150th generation + 5bi - 150 * diff between generations */

    return 0;
}
