
/* cc puzzle3b.c && time ./a.out */

#include <stdio.h>

int fabric[1024][1024] = {};

int main(int argc, char **argv) {
  FILE *file;
  char id[16];
  int left, top, width, height;
  int i, j, k, l;
  int count;

  file = fopen("puzzle3a.txt", "r");

  while (fscanf(file, "%s @ %d,%d: %dx%d", id, &left, &top, &width, &height) !=
         EOF) {
    for (i = left, j = left + width; i < j; i++) {
      for (k = top, l = top + height; k < l; k++) {
        fabric[i][k] = fabric[i][k] + 1;
      }
    }
  }

  fseek(file, 0, SEEK_SET);
  while (fscanf(file, "%s @ %d,%d: %dx%d", id, &left, &top, &width, &height) !=
         EOF) {
    count = 0;
    for (i = left, j = left + width; i < j; i++) {
      for (k = top, l = top + height; k < l; k++) {
        count += fabric[i][k];
      }
    }
    if (count == (width * height))
      printf("%s\n", &id[1]); /* I could return when I'm here */
  }

  fclose(file);
  return 0;
}
