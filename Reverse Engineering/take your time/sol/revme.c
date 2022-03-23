
#include <stdio.h> 
#include <stdlib.h> 
#include<time.h> 
int a[]={149,142,160,146,128,86,148,204,157,158,161,172,121};
int b[13]={0};
void itachi(){
    b[12] = a[12];
    for(int i = 12; i>=0; i--) {
        a[i-1] = a[i-1] - a[i];
        b[i-1] = b[i-1] + a[i-1];
    }
    for (int i=0; i<13; i++) {
        printf("%c", b[i]);
    }
    printf("\n");
}
int main(void)
{ 


    


	char str[80];

	int T = time(0);

    srand(T); 
  
    int num1 = rand();
    uint num2 = (num1 - 3) * 3;
  
    if(num2 & 1 != 0)
    {
    	num2 = num2 - 1;
    }

    int num3 = (int) num2 /2 + 7;

    
     int a,b,c;
     printf("Guess The numbers that i am thinking...\n");
    printf("Enter first number: ");
    scanf("%d", &a);
    
    printf("Enter second number: ");
    scanf("%d", &b);
    
    printf("Enter third number: ");
    scanf("%d", &c);

    if(a==num1 && b==num2 && c==num3)
    {
        itachi();
    }
    else{
        printf("wrong guess \n");
        sprintf(str,"%d %d %d %d",T,num1,num2,num3);
        puts(str);
    }
  
    return 0; 
} 

