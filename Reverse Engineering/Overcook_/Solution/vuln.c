
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

void getMessage();
int printmsg();

int main(int argc, char* argv[]) {
    getMessage();
    exit(EXIT_SUCCESS);
}

void getMessage() {
    char buffer[50];
    
    gets(buffer);
    printf("\n");
    printf(buffer);
    printf("\n");
}
#define FLAGSIZE 64
int printflag() {
    printf("\n114 \n");
    
    printf("051 \n");
    printf("118 \n");
    printf("101 \n");
    printf("114 \n");
    printf("115 \n");
    printf("049\n");
    printf("110\n");
    printf("103\n");
    printf("095\n");
    printf("100\n");
    printf("117\n");
    printf("100\n");
    printf("051\n");
 
  return 0;
}
