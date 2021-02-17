#include <stdio.h>
 
int main() {
 
    int x,i;
    scanf("%d",&x);
    for(i=1; i<=x; i++)
    {
        if(i%2 != 0)
            printf("%d\n",i);
    }
 
    return 0;
}

//https://urisolutions.blogspot.com/2020/04/uri-problem-1067-solution-odd-numbers.html