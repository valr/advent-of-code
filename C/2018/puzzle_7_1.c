
/* cc puzzle7a.c && time ./a.out */

#include <stdio.h>

int predecessor[26][26 + 1] = {};

void show_steps(void) {
  for (int i = 0; i < 26; i++) {
    if (predecessor[i][26] != 0)
      printf("%c has predecessor:", i + 'A');

    for (int j = 0; j < 26; j++) {
      if (predecessor[i][j])
        printf(" %c", j + 'A');
    }

    if (predecessor[i][26] != 0)
      printf("\n");
  }
}

int main(int argc, char **argv) {
  FILE *file;
  char string[50];

  file = fopen("puzzle7.txt", "r");
  while (fgets(string, 50, file) != NULL) {
    predecessor[string[36] - 'A'][string[5] - 'A'] = 1;
    predecessor[string[36] - 'A'][26] = 1;
  }
  fclose(file);

  //  show_steps();

  printf("part1, order to complete the steps: ");

  int last = -1;
  int found = -1;
  while (found) {
    found = 0;
    for (int j = 0; j < 26 && found == 0; j++) {
      for (int i = 0; i < 26 && found == 0; i++) {
        if (predecessor[i][26] != 0 && /* there are predecessors */
            predecessor[i][j] != 0 &&  /* and it's one of them */
            predecessor[j][26] == 0) { /* and it's ready */

          /* the step is the first one ready */
          found = 1;
          printf("%c", 'A' + j);

          /* the step is now processed */
          for (int k = 0; k < 26; k++)
            predecessor[k][j] = 0;

          /* is there a new step ready? */
          for (int k = 0; k < 26; k++) {
            if (predecessor[k][26] != 0) {
              int count = 0;

              for (int l = 0; l < 26; l++) {
                if (predecessor[k][l] != 0)
                  count++;
              }

              if (count == 0) {
                predecessor[k][26] = 0;
                last = k;
              }
            }
          }
        }
      }
    }
  }
  printf("%c\n", 'A' + last);

  return 0;
}
