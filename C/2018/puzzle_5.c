
/* cc puzzle5.c && time ./a.out */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int react (char *polymer, int size)
{
    int units, i, j;

    units = size-1;
    for (i=1; i<size; i++) {
        for (j=i-1; j>=0 && polymer[j]==0; j--);
        if (j>=0 && polymer[i]==(polymer[j]^' ')) {
            polymer[i] = polymer[j] = 0;
            units -=2;
        }
    }

    return units;
}

int reduce (char *polymer, int size)
{
    char *reduced;
    int units, i, j, k, l;

    units = size-1;
    for (i='a'; i<='z'; i++) {
        reduced = memset(malloc(size),0,size);
        for (j=0, k=0; j<size; j++) {
            if (polymer[j]!=i && (polymer[j]^' ')!=i) {
                reduced[k++] = polymer[j];
            }
        }
        if ((l = react(reduced, k))<units)
            units = l;
        free(reduced);
    }

    return units;
}

int main (int argc, char **argv)
{
    FILE *file;
    int size;
    char *polymer;

    file = fopen("puzzle5.txt", "r");

    fseek(file, 0L, SEEK_END);
    size = ftell(file); rewind(file);

    polymer = malloc(size);
    fgets(polymer, size, file);

    fclose(file);

    printf("part2, remaining units: %d\n", reduce(polymer, size));
    printf("part1, remaining units: %d\n", react(polymer, size));

    return 0;
}
