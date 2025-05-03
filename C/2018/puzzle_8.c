
/* cc puzzle8.c && time ./a.out */

#include <stdio.h>

int sum_nodes_1 (FILE *file)
{
    int child, metadata, entry;
    int entries = 0;

    fscanf(file, "%d %d", &child, &metadata);

    /* read child nodes */
    for (int i = 0; i < child; i++)
        entries += sum_nodes_1(file);

    /* read metadata entries */
    for (int i = 0; i < metadata; i++) {
        fscanf(file, "%d", &entry);
        entries += entry;
    }

    return entries;
}

int sum_nodes_2 (FILE *file)
{
    int child, metadata, entry;
    int child_entry[100] = {};
    int entries = 0;

    fscanf(file, "%d %d", &child, &metadata);

    /* read child nodes */
    for (int i = 0; i < child; i++)
        child_entry[i] = sum_nodes_2(file);

    /* read metadata entries */
    for (int i = 0; i < metadata; i++) {
        fscanf(file, "%d", &entry);
        entries += child == 0 ? entry : (--entry >= 0 ? child_entry[entry] : 0);
    }

    return entries;
}

int main (int argc, char **argv)
{
    FILE *file;

    file = fopen("puzzle8.txt", "r");
    printf("part1, sum of all metadata entries: %d\n", sum_nodes_1(file));
    rewind(file);
    printf("part2, value of the root node: %d\n", sum_nodes_2(file));
    fclose(file);

    return 0;
}
