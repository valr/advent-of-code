
/* cc -O2 puzzle14.c && ./a.out */

#include <stdio.h>
#include <stdlib.h>

/* for answer 1: 306281 */
/* for answer 2: 30628100 (random, just high enough to get a result) */
#define RECIPE 306281

typedef struct _recipe {
  struct _recipe *prev;
  struct _recipe *next;
  unsigned long long value;
} recipe;

static recipe *list, *current1, *current2;
static int count = 0;

static recipe *new_recipe(unsigned long long value) {
  recipe *new = malloc(sizeof(recipe));

  list->prev = list->next = list = new;
  list->value = value;

  count++;
  return new;
}

static recipe *add_at_end_recipe(unsigned long long value) {
  recipe *new = malloc(sizeof(recipe));

  new->prev = list->prev;
  new->next = list;
  list->prev->next = new;
  list->prev = new;
  new->value = value;

  count++;
  return new;
}

/* noooo, it's not a too long function name */
static void
how_many_recipes_appear_on_the_scoreboard_to_the_left_of_the_first_recipes_whose_score_are_the_digits_from_the_input(
    void) {
  unsigned long long value =
      list->prev->prev->prev->prev->prev->prev->value * 100000ULL +
      list->prev->prev->prev->prev->prev->value * 10000ULL +
      list->prev->prev->prev->prev->value * 1000ULL +
      list->prev->prev->prev->value * 100ULL + list->prev->prev->value * 10ULL +
      list->prev->value;

  if (value == 306281)
    printf("answer 2 (only take the first result): %llu\n",
           count - 6); /* 6 = number of digits in the value */
}

int main(int argc, char **argv) {
  current1 = new_recipe(3);
  current2 = add_at_end_recipe(7);

  while (count < RECIPE + 12) {
    unsigned long long value = current1->value + current2->value;

    if (value < 10) {
      add_at_end_recipe(value);
      how_many_recipes_appear_on_the_scoreboard_to_the_left_of_the_first_recipes_whose_score_are_the_digits_from_the_input();
    } else {
      add_at_end_recipe(1);
      how_many_recipes_appear_on_the_scoreboard_to_the_left_of_the_first_recipes_whose_score_are_the_digits_from_the_input();

      add_at_end_recipe(value - 10);
      how_many_recipes_appear_on_the_scoreboard_to_the_left_of_the_first_recipes_whose_score_are_the_digits_from_the_input();
    }

    for (int j = current1->value; j >= 0; j--)
      current1 = current1->next;

    for (int j = current2->value; j >= 0; j--)
      current2 = current2->next;
  }

  recipe *r = list->prev->prev->prev->prev->prev->prev->prev->prev->prev->prev
                  ->prev->prev;
  printf("answer 1: ");
  for (int i = 0; i < 10; i++) {
    printf("%d", r->value);
    r = r->next;
  }
  printf("\n");
  return 0;
}
