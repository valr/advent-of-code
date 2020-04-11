
/* cc -O2 puzzle11.c && time ./a.out */

#include <stdio.h>

void largest_total_power (int serial, int start_size, int end_size,
                          int *total_power, int *total_size, int *total_x, int *total_y)
{
    int x, y;
    int grid[301][301] = {};
    int rack, power;
    int size, size_x, size_y;

    /* compute the power by cell */
    for (y = 1; y <= 300; y++) {
        for (x = 1; x <= 300; x++) {
            rack = x + 10;
            power = (rack * y + serial) * rack;
            grid[y][x] = (power / 100) % 10 - 5;
        }
    }

    /* compute the total power */
    *total_power = *total_size = 0;
    for (size = start_size; size <= end_size; size++) {
        for (y = 1; y <= 300 - size + 1; y++) {
            for (x = 1; x <= 300 - size + 1; x++) {
                power = 0;
                for (size_y = 0; size_y < size; size_y++) {
                    for (size_x = 0; size_x < size; size_x++) {
                        power += grid[y + size_y][x + size_x];
                    }
                }
                if (*total_power < power) {
                    *total_power = power;
                    *total_size = size;
                    *total_x = x;
                    *total_y = y;
                }
            }
        }
    }
}

int main (int argc, char **argv)
{
    int total_power, total_size, total_x, total_y;

    largest_total_power(5177, 3, 3, &total_power, &total_size, &total_x, &total_y);
    printf("3x3 square with the largest total power: %d X,Y: %d,%d\n",
           total_power, total_x, total_y);

    largest_total_power(5177, 1, 300, &total_power, &total_size, &total_x, &total_y);
    printf("square with the largest total power: %d X,Y,size: %d,%d,%d\n",
            total_power, total_x, total_y, total_size);

    return 0;
}
