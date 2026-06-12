#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int add (int* a , int* b)
{
    return *a + *b;
}


int main(int argc, char** argv)
{


    int (*fptr)(int*, int*) = add;


    char name[10] = {0, }; // 12345678901
    int login = 1;

    // if (strlen(argv[1] > 10)) {
    //     printf("Invalid input received \n");
    //     return -1;
    // }

    strcpy(name, argv[1]);

    if (strcmp(name, "dilip") == 0) {
        login = 1;
    }

    if (login == 1) {
        printf("logged in!\n");
    } else {
        printf("Invalid user\n");
    }

    return 0;
}