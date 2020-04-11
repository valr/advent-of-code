
/* cc -O2 puzzle10.c && ./a.out */

#include <signal.h>
#include <stdio.h>
#include <unistd.h>

volatile sig_atomic_t flag = 1;
void handler (int sig)
{
    flag = 1;
}

int main (int argc, char **argv)
{
    FILE *file, *gnuplot;
    int point[350][4] = {}, counter = 0, second = 10000;

    /* read the points and velocity */
    file = fopen("puzzle10.txt", "r");
    while (fscanf(file, "position=<%d,%d> velocity=<%d,%d>\n",
                        &point[counter][0], &point[counter][1],
                        &point[counter][2], &point[counter][3]) != EOF) {
        counter++;
    }
    fclose(file);

    /* fast forward */
    for (int j = 0; j < second; j++) {
        for (int i = 0; i < counter; i++) {
            point[i][0] += point[i][2];
            point[i][1] += point[i][3];
        }
    }

    /* plot the graph */
    gnuplot = popen("gnuplot", "w");
    fprintf(gnuplot, "reset\n");
    fprintf(gnuplot, "unset key\n");
    fprintf(gnuplot, "unset tics\n");
    fprintf(gnuplot, "unset border\n");
    fprintf(gnuplot, "set yrange [*:*] reverse\n");
    fprintf(gnuplot, "plot \"puzzle10.dat\" with points pointtype 5 lc rgb \"black\"\n");
    fflush(gnuplot);

    /* ctrl+c to increment the points by their velocity */
    signal(SIGINT, handler);

    while (1) {
        if (flag == 1) {
            flag = 0;

            /* increment the simulated time */
            printf("number of seconds: %d\n", second++);

            /* rewrite the gnuplot data file */
            file = fopen("puzzle10.dat", "w");
            for (int i = 0; i < counter; i++) {
                fprintf(file, "%d %d\n", point[i][0], point[i][1]);

                /* increment the points by their velocity */
                point[i][0] += point[i][2];
                point[i][1] += point[i][3];
            }
            fclose(file);

            /* replot the graph */
            fprintf(gnuplot, "replot\n");
            fflush(gnuplot);
        }
        usleep(100000);
    }

    pclose(gnuplot);
    return 0;
}
