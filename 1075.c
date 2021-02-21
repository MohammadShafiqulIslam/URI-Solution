#include <stdio.h>
int main() {
    int num,i;
    scanf("%d",&num);
    for(i=1; i<=10000; i++)
    {
        if(i%num == 2)
            printf("%d\n",i);
    }
    return 0;
}

//https://urisolutions.blogspot.com/2020/04/uri-problem-1075-solution-remaining-2.html