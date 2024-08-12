
/* cc -O2 puzzle13.c && time ./a.out */

#include <stdio.h>
#include <stdlib.h>

char grid[200][200] = {};
int cart[200][6] = {};
int nline = 0, ncart = 0;

void display_grid (void)
{
    for (int y = 0; y < nline; y++) {
        for (int x = 0; x < 200; x++) {
            char newchar = ' '; int added = 0;
            for (int c = 0; c < ncart; c++) {
                if (cart[c][0] == y && cart[c][1] == x) {
                    if (cart[c][2] == 1)  { newchar = 'v'; added++; }
                    if (cart[c][2] == -1) { newchar = '^'; added++; }
                    if (cart[c][3] == 1)  { newchar = '>'; added++; }
                    if (cart[c][3] == -1) { newchar = '<'; added++; }
                }
            }
            switch (added) {
                case 0: putchar(grid[y][x]); break;
                case 1: putchar(newchar); break;
                default: putchar('X'); break;
            }
        }
        putchar('\n');
    }
}

int find_crash_cart (void)
{
    for (int y = 0; y < nline; y++) {
        for (int x = 0; x < 200; x++) {
            int added = 0;
            for (int c = 0; c < ncart; c++) {
                if (cart[c][0] == y && cart[c][1] == x) {
                    added++;
                    if (added > 1) {
                        printf("location of the crash: %d,%d\n", x, y);
                        return 1;
                    }
                }
            }
        }
    }
    return 0;
}

int find_and_remove_crash_cart (void)
{
    for (int y = 0; y < nline; y++) {
        for (int x = 0; x < 200; x++) {
            for (int c1 = 0; c1 < ncart - 1; c1++) {
                int crash = 0;
                for (int c2 = c1 + 1; c2 < ncart; c2++) {
                    if (cart[c1][0] == y && cart[c2][0] == y &&
                        cart[c1][1] == x && cart[c2][1] == x &&
                        cart[c1][5] == 0 && cart[c2][5] == 0) {
                        cart[c2][5] = crash = 1;
                    }
                }
                if (crash == 1)
                    cart[c1][5] = 1;
            }
        }
    }

    int count = 0, found = 0;
    for (int c = 0; c < ncart; c++) {
        if (cart[c][5] == 0) {
            count++;
            found = c;
        }
    }

    if (count <= 1) {
        printf("location of the last cart: %d,%d\n", cart[found][1], cart[found][0]);
        return 1;
    }

    return 0;
}

int compare (const void *s1, const void *s2)
{
    int *c1 = (int*)s1, *c2 = (int*)s2;
    if (c1[0] < c2[0]) return -1;
    if (c1[0] > c2[0]) return  1;
    if (c1[1] < c2[1]) return -1;
    if (c1[1] > c2[1]) return  1;
    return 0;
}

int main (int argc, char **argv)
{
    FILE *file;
    int x, y, c;
    int end = 0;

    file = fopen("puzzle13.txt", "r");
    while (fgets(&grid[nline++][0], 200, file) != NULL);
    fclose(file);

    for (y = 0; y < nline; y++) {
        for (x = 0; x < 200; x++) {
            cart[ncart][0] = y;
            cart[ncart][1] = x;
            switch (grid[y][x]) {
                case '/': case '\\': case '-': case '|': case '+': break;
                case '>': cart[ncart++][3] =  1; grid[y][x] = '-'; break;
                case '<': cart[ncart++][3] = -1; grid[y][x] = '-'; break;
                case 'v': cart[ncart++][2] =  1; grid[y][x] = '|'; break;
                case '^': cart[ncart++][2] = -1; grid[y][x] = '|'; break;
                default: grid[y][x] = ' '; break;
            }
        }
    }

    while (!end) {
//      display_grid();
        qsort(cart, ncart, sizeof(cart[0]), compare);
        for (c = 0; c < ncart; c++) {
            if (cart[c][5] == 1)
                continue;

            cart[c][0] += cart[c][2];
            cart[c][1] += cart[c][3];
            switch (grid[cart[c][0]][cart[c][1]]) {
                case '-': case '|':
                    break;
                case '/':
                    if (cart[c][2] ==  1) { cart[c][2] = 0; cart[c][3] = -1; } else
                    if (cart[c][2] == -1) { cart[c][2] = 0; cart[c][3] =  1; } else
                    if (cart[c][3] ==  1) { cart[c][2] = -1; cart[c][3] = 0; } else
                    if (cart[c][3] == -1) { cart[c][2] =  1; cart[c][3] = 0; }
                    break;
                case '\\':
                    if (cart[c][2] ==  1) { cart[c][2] = 0; cart[c][3] =  1; } else
                    if (cart[c][2] == -1) { cart[c][2] = 0; cart[c][3] = -1; } else
                    if (cart[c][3] ==  1) { cart[c][2] =  1; cart[c][3] = 0; } else
                    if (cart[c][3] == -1) { cart[c][2] = -1; cart[c][3] = 0; }
                    break;
                case '+':
                    switch (cart[c][4]) {
                        case 0:
                            if (cart[c][2] ==  1) { cart[c][2] = 0; cart[c][3] =  1; } else
                            if (cart[c][2] == -1) { cart[c][2] = 0; cart[c][3] = -1; } else
                            if (cart[c][3] ==  1) { cart[c][2] = -1; cart[c][3] = 0; } else
                            if (cart[c][3] == -1) { cart[c][2] =  1; cart[c][3] = 0; }
                            break;
                        case 2:
                            if (cart[c][2] ==  1) { cart[c][2] = 0; cart[c][3] = -1; } else
                            if (cart[c][2] == -1) { cart[c][2] = 0; cart[c][3] =  1; } else
                            if (cart[c][3] ==  1) { cart[c][2] =  1; cart[c][3] = 0; } else
                            if (cart[c][3] == -1) { cart[c][2] = -1; cart[c][3] = 0; }
                            break;
                    }
                    cart[c][4] = (cart[c][4] + 1) % 3;
                    break;
            }
//          end += find_crash_cart(); // part 1
            end += find_and_remove_crash_cart(); // part 2
        }
    }
//  display_grid();
    return 0;
}
