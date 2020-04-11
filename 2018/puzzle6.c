
/* cc puzzle6.c && time ./a.out */

#include <stdio.h>
#include <stdlib.h>

typedef struct _point {
    int x;
    int y;
} point;

point list[50] = {};

int grid[1000][1000];
int gridx = 0, gridy = 0;

int manhattan_distance (point a, point b)
{
    return (abs(b.x - a.x) + abs(b.y - a.y));
}

int main (int argc, char **argv)
{
    FILE *file;
    int count = 0;
    int safe_size = 0, dangerous_size = 0;
    int x, y, i;

    /* read the list of coordinates and determine the grid size */
    file = fopen("puzzle6.txt", "r");

    while (fscanf(file, "%d, %d", &list[count].x, &list[count].y) != EOF) {
        if (list[count].x > gridx)
            gridx = list[count].x;
        if (list[count].y > gridy)
            gridy = list[count].y;

        count++;
    }
    gridx += 2;
    gridy += 1;

    fclose(file);

    /* determine the locations closest to coordinates */
    for (y = 0; y < gridy; y++) {
        for (x = 0; x < gridx; x++) {
            grid[y][x] = -1;

            point p = { .x = x, .y = y };
            int min_dist = x * y;
            int min_i = -1;

            for (i = 0; i < count; i++) {
                int dist = manhattan_distance(p, list[i]);

                /* distance is equally far from two or more coordinates */
                if (dist == min_dist)
                    min_i = -1;

                if (dist < min_dist) {
                    min_dist = dist;
                    min_i = i;
                }
            }

            grid[y][x] = min_i;
        }
    }

    /* process the limits */
    for (i = 0; i < gridx; i++)
        grid[0][i] = grid[1][i];

    for (i = 0; i < gridy; i++)
        grid[i][0] = grid[i][1];

    /* determine the largest area, excluding infinites */
    for (i = 0; i < count; i++) {
        int size = 0;
        int infinite = 0;

        for (y = 0; y < gridy; y++) {
            for (x = 0; x < gridx; x++) {
                if (grid[y][x] == i) {
                    if (x == 0 || y == 0 || x == gridx - 1 || y == gridy - 1)
                        infinite = 1;
                    else
                        size++;
                }
            }
        }

        if (infinite == 0 && size > dangerous_size)
            dangerous_size = size;
    }

    printf("part1, size of the dangerous area: %d\n", dangerous_size);

    /* determine the size of the region containing all locations which have */
    /* a total distance to all given coordinates of less than 10000 */
    for (y = 0; y < gridy; y++) {
        for (x = 0; x < gridx; x++) {

            point p = { .x = x, .y = y };
            int dist = 0;

            for (i = 0; i < count; i++)
                dist += manhattan_distance(p, list[i]);

            if (dist < 10000)
                safe_size++;
        }
    }

    printf("part2, size of the safe area: %d\n", safe_size);
    return 0;
}
