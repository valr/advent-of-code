
/* cc -O2 puzzle9.c && time ./a.out */

#include <stdio.h>
#include <stdlib.h>

#define PLAYER 404
#define LAST 7185200

typedef struct _marble {
    struct _marble *prev;
    struct _marble *next;
    unsigned long long value;
} marble;

int main (int argc, char **argv)
{
    marble *circle, *current;
    int player = 0;
    unsigned long long score[PLAYER] = {}, winning_score = 0;

    circle = malloc(sizeof(marble));
    circle->prev = circle->next = circle;
    circle->value = 0;
    current = circle;

    for (unsigned long long counter = 1; counter <= LAST; counter++)
    {
        if ((counter % 23) == 0)
        {
            marble *die = current->prev->prev->prev->prev->prev->prev->prev;
            die->prev->next = die->next;
            die->next->prev = die->prev;
            current = die->next;

            score[player] += counter + die->value;
            free(die);
        }
        else
        {
            marble *new = malloc(sizeof(marble));
            new->prev = current->next;
            new->next = current->next->next;
            new->prev->next = new;
            new->next->prev = new;
            new->value = counter;
            current = new;
        }

        player = (player + 1) % PLAYER;
    }

    for (player = 0; player < PLAYER; player++)
    {
        if (winning_score < score[player])
            winning_score = score[player];
    }

    printf("winning score: %llu", winning_score);
    return 0;
}
