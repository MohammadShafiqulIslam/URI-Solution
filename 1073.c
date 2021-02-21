#include <stdio.h>
int main() {
    int num,i;
    scanf("%d",&num);
    for(i=1; i<=num; i++)
    {
        if(i%2 ==0 )
        {
            printf("%d^2 = %d\n",i,i*i);
        }
    }
    return 0;
}

//https://urisolutions.blogspot.com/2020/04/uri-problem-1073-solution-even-square.html